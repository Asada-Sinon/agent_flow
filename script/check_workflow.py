#!/usr/bin/env python3
"""Check flow's Markdown conventions and README examples using only stdlib.

Supports inline Markdown links and ATX headings used by this repository;
this is not a general Markdown parser. README creation examples run in a
throwaway directory, so review changes to those commands before running.
"""

from datetime import date
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def prose(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", text, flags=re.M | re.S)


def heading_anchors(text):
    anchors = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.M):
        slug = "".join(
            char for char in heading.lower()
            if char in " -_" or unicodedata.category(char)[0] in "LNM"
        ).replace(" ", "-")
        candidate = slug
        suffix = 0
        while candidate in anchors:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        anchors.add(candidate)
    return anchors


def check_documents():
    files = sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").rglob("*.md"))
    links = anchors = 0
    for file in files:
        for destination in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", prose(file.read_text(encoding="utf-8"))):
            url = urlsplit(destination.strip().strip("<>"))
            if url.scheme or url.netloc:
                continue
            target = (file.parent / unquote(url.path)).resolve() if url.path else file
            label = f"{file.relative_to(ROOT)}: {destination}"
            require(target.exists(), f"Missing local target: {label}")
            if url.fragment:
                require(target.is_file(), f"Anchor target is not a file: {label}")
                require(unquote(url.fragment) in heading_anchors(target.read_text(encoding="utf-8")),
                        f"Missing heading anchor: {label}")
                anchors += 1
            links += 1
    print(f"Documents: PASS ({len(files)} files, {links} local links, {anchors} anchors)")


def check_templates():
    required = {
        "docs/spec/_template.md": ["## Goal", "## Scope", "## Non-goals", "## Acceptance criteria", "**AC-01**"],
        "docs/plan/_template.md": ["**status**: pending", "**Source**:", "## Goal and acceptance", "## Steps", "- [ ]", "## Verification results"],
    }
    for name, fields in required.items():
        text = prose((ROOT / name).read_text(encoding="utf-8"))
        for field in fields:
            require(field in text, f"Missing template field in {name}: {field}")
    for name in ("AGENTS.md", "docs/plan/_template.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        for status in ("pending", "in-progress", "blocked", "done", "cancelled"):
            require(re.search(r"(?<![\w-])" + re.escape(status) + r"(?![\w-])", text),
                    f"Missing status in {name}: {status}")
    print("Templates: PASS (required fields and 5 statuses)")


def check_version_and_inbox():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    version_pattern = r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
    require(re.fullmatch(version_pattern, version), "VERSION must use major.minor.patch without leading zeros")
    changelog = prose((ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))
    headings = re.findall(r"^## (.+)$", changelog, re.M)
    require(headings, "CHANGELOG.md must contain a version and date heading")
    releases = []
    for heading in headings:
        release = re.fullmatch(r"(" + version_pattern + r") — ([0-9]{4}-[0-9]{2}-[0-9]{2})", heading)
        require(release, f"Invalid CHANGELOG release heading: {heading}")
        date.fromisoformat(release.group(2))
        releases.append(release.group(1))
    require(releases[0] == version, "VERSION must match the latest CHANGELOG entry")
    require(len(releases) == len(set(releases)), "Duplicate version in CHANGELOG.md")
    inbox = prose((ROOT / "docs/TODO.md").read_text(encoding="utf-8"))
    sections = re.findall(r"^## (.+)$", inbox, re.M)
    for section in ("Pending", "Latest result"):
        require(sections.count(section) == 1, f"docs/TODO.md must contain one {section} section")
    require(sections.index("Pending") < sections.index("Latest result"), "TODO results must follow pending tasks")
    print(f"Version and inbox: PASS ({version}; changelog aligned; TODO sections present)")


def run_example(block, workspace):
    return subprocess.run(
        ["bash", "-eu", "-c", block], cwd=workspace,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15,
    )


def check_examples():
    # Coupled to README's three Getting started blocks, sample slug/paths,
    # and recovery messages. Update both files when changing those examples.
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    section = re.search(r"^## Getting started\s*\n(.*?)(?=^## |\Z)", readme, re.M | re.S)
    require(section is not None, "README is missing the Getting started section")
    blocks = re.findall(r"^```bash\n(.*?)^```", section.group(1), re.M | re.S)
    require(len(blocks) == 3, "Expected directory, plan and spec creation examples in README")
    expected = [
        (None, None),
        ("docs/plan/refactor-import/01-refactor-import.md", "docs/plan/_template.md"),
        ("docs/spec/refactor-import/spec.md", "docs/spec/_template.md"),
    ]
    with tempfile.TemporaryDirectory(prefix="flow-examples-") as temporary:
        workspace = Path(temporary)
        for kind in ("plan", "spec"):
            destination = workspace / "docs" / kind
            destination.mkdir(parents=True)
            shutil.copyfile(ROOT / "docs" / kind / "_template.md", destination / "_template.md")
        for number, (block, (relative, source)) in enumerate(zip(blocks, expected), 1):
            result = run_example(block, workspace)
            require(result.returncode == 0, f"README example {number} failed: {result.stderr}")
            if relative is None:
                require(all((workspace / name).is_dir() for name in ("data", "log", "output", "temp", "script")),
                        "Directory example did not create the expected directories")
                continue
            target = workspace / relative
            source_file = workspace / source
            source_bytes = source_file.read_bytes()
            source_mode = source_file.stat().st_mode
            target.unlink()
            for failure in ("missing", "not-a-file", "unreadable"):
                if failure == "missing":
                    source_file.unlink()
                elif failure == "not-a-file":
                    source_file.unlink()
                    source_file.mkdir()
                else:
                    source_file.chmod(0)
                try:
                    if failure == "unreadable" and os.access(source_file, os.R_OK):
                        print(f"SKIP: unreadable-source case for {relative} (process can read mode-000 files)")
                        continue
                    result = run_example(block, workspace)
                    require(result.returncode != 0, f"Invalid source must fail ({failure}): {relative}")
                    require(not target.exists(), f"Failed creation left a target ({failure}): {relative}")
                    require("Template is not a readable file" in result.stderr,
                            f"Missing source diagnostic ({failure}): {relative}")
                finally:
                    if failure == "not-a-file":
                        source_file.rmdir()
                    elif failure == "unreadable":
                        source_file.chmod(source_mode)
                    source_file.write_bytes(source_bytes)
                    source_file.chmod(source_mode)
                result = run_example(block, workspace)
                require(result.returncode == 0 and target.read_bytes() == source_bytes,
                        f"Cannot retry after source recovery ({failure}): {relative}")
                target.unlink()
            with tempfile.TemporaryDirectory(prefix="flow-wrong-cwd-") as wrong_directory:
                result = run_example(block, wrong_directory)
                require(result.returncode != 0, f"Wrong working directory must fail: {relative}")
                require(not (Path(wrong_directory) / relative).exists(),
                        f"Wrong working directory left a target: {relative}")
            result = run_example(block, workspace)
            require(result.returncode == 0, f"Final creation failed: {relative}")
            require(target.is_file(), f"README example {number} did not create {relative}")
            require(target.read_bytes() == (ROOT / source).read_bytes(), f"Template copy differs: {relative}")
            for original in (b"Saved task progress\n", b""):
                target.write_bytes(original)
                result = run_example(block, workspace)
                require(result.returncode != 0, f"Repeated example must fail: {relative}")
                require(target.read_bytes() == original, f"Existing file overwritten: {relative}")
                require("resume the existing task" in result.stderr and "slug" in result.stderr,
                        f"Missing recovery instructions for existing file: {relative}")
    print("README examples: PASS (3 examples; source failure/recovery, wrong directory, existing populated/empty targets)")


def main():
    try:
        check_documents()
        check_templates()
        check_version_and_inbox()
        check_examples()
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
