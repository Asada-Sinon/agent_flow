# flow — Working conventions

Optimize the total cost of completing and verifying work. Avoid repeated investigation, unnecessary reading, and user interruptions while preserving acceptance evidence and useful handoff context. Project entry points and commands are in [README.md](README.md).

## Starting a task

Read the [user inbox](docs/TODO.md), then locate relevant code, entry points, and unfinished plans. Read related specs, history, and templates only when needed; do not scan every document by default. When resuming, compare recorded progress with the actual files.

Choose the lightest suitable workflow based on uncertainty, impact, and continuity needs, rather than file count or whether a feature is new:

| Situation | Workflow |
|---|---|
| Investigation, or a clear local change with limited impact | Act → verify → report; no file plan required |
| Multiple steps, persistent context, or work likely to span sessions | Short plan → implement → verify and record |
| Important unresolved requirements or significant interface/behavior changes | Resolve key questions → spec + plan → implement → accept |

Apply this classification to code, scripts, configuration, and documentation. Upgrade the workflow if complexity or impact grows; do not add paperwork to simple changes.

Ask only about unresolved decisions that affect goals, scope, or acceptance and cannot be determined from context. Do not reconfirm existing authorization. Decide routine implementation details independently; record consequential assumptions in an existing plan or final response. While awaiting a decision, continue independent work.

One-off diagnostic or reproduction scripts may be written and run in `temp/` without a separate plan, provided they do not modify deliverables or cause effects requiring additional authorization. If retained as project tools, treat them as normal project changes.

## Task inbox

- The `Pending` section of `docs/TODO.md` contains user requests; users need not repeat them in chat. Read it when starting work or asked to process the inbox. Editing the file does not start a background agent.
- Handle the current chat request first, then pending requests in the user's priority order or file order. If the user limits work to investigation, named items, or a pause, do not expand into other tasks. Current user instructions take precedence over conflicting inbox text; retain unresolved questions when needed.
- Ignore examples, comments, `Latest result`, and items marked `Do not execute`. Apply task classification to clear requests. Retain ideas with unresolved goals or acceptance conditions, record the question, and continue independent items. Users may write requests in their preferred language.
- When a task is cancelled or replaced but retained, mark its inbox entry `Do not execute: cancelled`, with the reason and replacement link if available. Skip it until the user explicitly reactivates it. A cancelled plan must not leave its associated inbox entry looking runnable; update both records.
- Skip user-checked `[x]` or `[X]` entries as user-marked completed records. This is not evidence that the agent verified them. Do not execute or remove these records unless the user explicitly requests that action.
- Remember the selected entries' original text and boundaries. In a plan, record their source and enough context to resume. Check records and actual outputs before repeating work after an interruption.
- After completing and verifying an item, record the result, reread TODO, and remove only that item's uniquely identifiable, unchanged text and subordinate notes. Do not replace the entire file. Retain failed, blocked, partially completed, newly added, or user-edited entries. Do not restore entries the user deleted. When uncertain, keep the entry and explain.
- Replace `Latest result` with the date, completion summary, verification, and remaining issues; link an existing plan when available. Keep only the latest receipt. Add brief status/questions beside unfinished entries as needed. Leave an empty inbox unchanged and never turn examples into tasks. Remove cancelled records only on explicit user request.

## Versioning

- Root `VERSION` is the single version source: `MAJOR.MINOR.PATCH`, without a `v` prefix. Versioning began at `0.1.0`; [CHANGELOG.md](CHANGELOG.md) records each version, date, and delivered changes.
- Incompatible interface, directory, or workflow conventions increment MAJOR and reset the other numbers. Compatible features or entry points increment MINOR and reset PATCH. Fixes, compatible improvements, and corrections affecting usage increment PATCH. For example: `0.1.0 → 1.0.0 / 0.2.0 / 0.1.1`.
- Increment once per delivery batch using its highest-impact change, not once per file, commit, or inbox item. Progress notes, inbox receipts, publication evidence, and formatting that does not change usage do not increment the version.
- Update VERSION and CHANGELOG together at delivery and verify consistency. Commit IDs identify revisions; versions describe deliveries. If a release tag is requested, use `v<version>`. Do not create tags or GitHub Releases automatically.

## Planning and execution

- Specs: `docs/spec/<slug>/spec.md`, using the [spec template](docs/spec/_template.md). Keep the goal, scope, non-goals, and numbered acceptance criteria. Record relevant constraints, assumptions, and open questions as needed.
- Plans: `docs/plan/<slug>/NN-<step>.md`, using the [plan template](docs/plan/_template.md). Use hyphenated slugs and numbering from 01; related specs and plans share a slug.
- One plan should produce an independently verifiable result; do not split artificially. Without a spec, record the user request and a verifiable goal. With a spec, link it and reference IDs such as `AC-01` instead of copying requirements.
- Default plan content: goal and acceptance, status, steps, and verification results. Add blockers, decisions, or handoff information only when useful; omit empty optional sections.

Adjust implementation independently within authorized goals and constraints. Do not log every debugging attempt. Record changes that affect later steps or handoff at milestones, task switches, or session end. Before unauthorized changes to scope, compatibility, cost, or data handling, explain the impact and obtain the required decision, then update the relevant spec and plan.

Save progress and the next action after useful milestones, not only before interruption. For handoff, prioritize file entry points, rejected approaches and reasons, and the next executable command over a chronological activity log.

Statuses: `pending` means not started; `in-progress` means underway, including ordinary interruptions; `blocked` requires an external dependency or unresolved question, with the cause, unblock condition, and next step; `done` requires all relevant acceptance criteria to pass with real evidence; `cancelled` means cancelled or superseded, with a reason and replacement task if any, not successful acceptance. On resumption, check the files and return unblocked work to `in-progress`.

## Verification and evidence

- Significant interface, compatibility, or data migration changes may warrant an independent review of the diff and acceptance evidence. This is not a mandatory stage for every task.
- Start with the smallest relevant verification. Expand to full tests or builds according to impact and project requirements; do not mechanically add tests for low-impact edits.
- Do not rerun passing checks without new changes, failures, or concerns. Commands, full-check triggers, and external dependencies are documented in README.
- Record key commands or reproducible observations, actual results, and remaining issues. Disclose failed or unrun verification; do not mark unmet acceptance as done.
- Write results into an existing plan, or report changes, verification, and remaining issues in the final response when no plan is needed. Do not copy log snapshots, record every action, or add model signatures.

## Directories

- `data/`, `log/`, `output/`, and `temp/` contain local data, logs, generated outputs, and temporary files. Create them as needed; they are ignored by default.
- Small versioned fixtures belong in `tests/fixtures/`; deliverable documents belong in `docs/deliverables/`.
- Retained helper scripts belong in `script/`, named `<verb>_<object>.*`. Document other source/test layouts and project commands in README.
