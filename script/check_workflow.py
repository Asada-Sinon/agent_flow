#!/usr/bin/env python3
"""Check flow's Markdown conventions and README examples using only stdlib.

Supports inline Markdown links and ATX headings used by this repository;
this is not a general Markdown parser. README creation examples run in a
throwaway directory, so review changes to those commands before running.
"""

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
        "docs/spec/_template.md": ["## 一句话目标", "## 范围", "## 非目标", "## 验收标准", "**AC-01**"],
        "docs/plan/_template.md": ["**status**: pending", "**来源**:", "## 目标与验收", "## 步骤", "- [ ]", "## 验证结果"],
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


def run_example(block, workspace):
    return subprocess.run(
        ["bash", "-eu", "-c", block], cwd=workspace,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15,
    )


def check_examples():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    section = re.search(r"^## 开始使用\s*\n(.*?)(?=^## |\Z)", readme, re.M | re.S)
    require(section is not None, "README is missing the 开始使用 section")
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
            require(target.is_file(), f"README example {number} did not create {relative}")
            require(target.read_bytes() == (ROOT / source).read_bytes(), f"Template copy differs: {relative}")
            for original in (b"Saved task progress\n", b""):
                target.write_bytes(original)
                result = run_example(block, workspace)
                require(result.returncode != 0, f"Repeated example must fail: {relative}")
                require(target.read_bytes() == original, f"Existing file overwritten: {relative}")
                require("继续已有任务" in result.stderr and "slug" in result.stderr,
                        f"Missing recovery instructions for existing file: {relative}")
    print("README examples: PASS (3 examples; plan/spec reject existing populated and empty files)")


def main():
    try:
        check_documents()
        check_templates()
        check_examples()
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
