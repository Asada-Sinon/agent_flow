# flow

A reusable workflow template for agent-assisted development. Optimize the total cost of completing and verifying work: act directly on simple tasks, keep plans and acceptance criteria for complex work, and leave useful handoff notes for long tasks.

Shared rules live in [AGENTS.md](AGENTS.md); Claude Code imports them through [CLAUDE.md](CLAUDE.md). Read only what the current task needs.

See [VERSION](VERSION) for the current `MAJOR.MINOR.PATCH` version, [CHANGELOG.md](CHANGELOG.md) for changes, and [Versioning](AGENTS.md#versioning) for increment rules.

## Write requests for an agent

Add requests or ideas to `Pending` in [docs/TODO.md](docs/TODO.md), using plain text or checkboxes. You need not repeat them in chat. The agent reads them when starting work; you can also say "process the inbox." Saving the file alone does not start background work.

Completed, verified entries are removed, leaving a short receipt. Failed, unclear, or user-edited entries stay. Mark notes `Do not execute`; retained cancelled/replaced entries use `Do not execute: cancelled` and remain inactive until explicitly reactivated. User-checked `[x]`/`[X]` entries are skipped as user-marked records, not agent-verified results. Current chat instructions can limit which tasks are handled. Requests may be written in your preferred language.

## Getting started

When adopting this template:

1. Fill in the project goal, environment, run commands, and verification commands below; update ignore rules for the chosen stack.
2. Remove the template's task directories under `docs/spec/` and `docs/plan/` while keeping `_template.md`, and remove their README example links. Alternatively, move retained records into an explicit examples directory and fix relative links. Their goals, authorization, repository addresses, and environment details belong only to the original tasks.
3. Reset VERSION, CHANGELOG, and the template's TODO receipt for the new project, preserving the version rules and inbox structure. Do not inherit template releases as project releases.
4. Start the project's first real task through TODO or chat; create a spec or plan only when needed.

Create local work directories as needed:

```bash
mkdir -p data log output temp script
```

Choose a workflow using [task classification](AGENTS.md#starting-a-task). Clear local changes need no file plan. When a persistent plan is needed, run this example from the repository root. Replace the example slug `refactor-import` and step name with your actual task. An existing target causes a failure: resume that task or choose a new slug.

```bash
(
set -eu
task_slug=refactor-import
source_template=docs/plan/_template.md
target="docs/plan/$task_slug/01-refactor-import.md"
if [ ! -f "$source_template" ] || [ ! -r "$source_template" ]; then
  printf 'Template is not a readable file: %s. Run from the repository root.\n' "$source_template" >&2
  exit 1
fi
mkdir -p "docs/plan/$task_slug"
if ! (set -C; cat < "$source_template" > "$target"); then
  printf 'Cannot create %s. If it exists, resume the existing task or choose a new slug.\n' "$target" >&2
  exit 1
fi
)
```

For a task requiring a spec, create it under the same slug:

```bash
(
set -eu
task_slug=refactor-import
source_template=docs/spec/_template.md
target="docs/spec/$task_slug/spec.md"
if [ ! -f "$source_template" ] || [ ! -r "$source_template" ]; then
  printf 'Template is not a readable file: %s. Run from the repository root.\n' "$source_template" >&2
  exit 1
fi
mkdir -p "docs/spec/$task_slug"
if ! (set -C; cat < "$source_template" > "$target"); then
  printf 'Cannot create %s. If it exists, resume the existing task or choose a new slug.\n' "$target" >&2
  exit 1
fi
)
```

The examples check the source before creating directories or targets and open it before redirecting output. Missing/unreadable sources and a wrong working directory leave no target behind. Existing files are never overwritten. A storage failure during writing may leave a partial new file: inspect it before explicitly removing it and retrying; the examples do not automatically delete files.

Fill applicable fields and omit empty optional sections. A plan linked to the spec above uses `../../spec/refactor-import/spec.md#acceptance-criteria` as its source. Name steps for the actual work; do not pre-create unused documents or directories.

Maintenance: `script/check_workflow.py` expects these three Bash blocks, the example slug, target paths, and recovery messages. Update the checker together with changes to these examples. A shared creation command can be introduced later if repeated use justifies it.

## Project entry points and verification

Fill this in early to avoid rediscovering the environment each session. This repository contains workflow documents and a standard-library checker, with no application runtime or business tests. Run from the repository root:

```bash
python3 script/check_workflow.py
```

The checker validates inline local Markdown links, heading anchors, template fields, version/changelog consistency, and inbox sections. It runs the README examples in temporary directories to test creation, existing-file protection, source failures, and recovery. It does not contact the network, modify project files, execute user tasks, or clear the inbox. Workflow semantics still require human or agent review.

| Item | Current value / replace when adopting |
|---|---|
| Project goal | Currently a workflow template; replace with the business goal |
| Environment and installation | Python 3.8+ and Bash for checks, no third-party packages; add application requirements |
| Run entry point | No application yet; add the start command and working directory |
| Minimum verification | `python3 script/check_workflow.py`; add focused application checks |
| Full verification and triggers | For workflow, template, or checker changes, run the command and review affected rule scenarios; add application test/build commands and triggers |
| External dependencies and duration | Local document checks need no service; publishing requires GitHub access and Git write permission. Document slow checks, services, and expected duration |
| Source and test locations | Choose for the stack; small versioned fixtures go in `tests/fixtures/` |
| Configuration | Local environment files are ignored; provide credential-free `.env.example` or `.env.<environment>.example` |

Migration from 0.1.0: document headings and fields are now English, including `Pending`, `Latest result`, and `Source`. Update customized templates, section-based tooling, and heading links together with the checker. File paths, task statuses, and the check command are unchanged. Historical records are translated for readability; their measurements describe the original runs.

## Templates and examples

Task records below describe this template's own history. They do not grant authorization or define requirements for a new project.

- [Spec template](docs/spec/_template.md): requirements, boundaries, and verifiable acceptance criteria.
- [Plan template](docs/plan/_template.md): goals, progress, verification, and useful handoff information.
- Efficiency work: [spec](docs/spec/agent-efficiency/spec.md), [implementation plan](docs/plan/agent-efficiency/01-simplify-workflow.md), and [publication record](docs/plan/agent-efficiency/02-publish-repository.md).
- Earlier template work: [spec](docs/spec/workflow-template/spec.md) and [plan](docs/plan/workflow-template/01-update-workflow.md), whose rules are partly superseded.
- [Adoption and verification fixes](docs/plan/workflow-review/01-fix-adoption.md): creation protection, reusable checks, and adoption guidance.

## Layout

| Path | Purpose |
|---|---|
| `VERSION`, `CHANGELOG.md` | Current version and delivered changes |
| `docs/TODO.md` | User requests and the latest processing receipt |
| `docs/spec/`, `docs/plan/` | Specs, plans, and templates |
| `data/`, `log/`, `output/`, `temp/` | Local work data, created as needed and ignored by default |
| `script/` | Retained helper scripts |
| `tests/fixtures/`, `docs/deliverables/` | Small versioned fixtures and deliverable documents |

Choose application source/test layouts for the stack and update the table above. Version source, dependency lockfiles, and necessary records; keep reproducible data and outputs in local work directories.
