# Versioning and a file-based task inbox

> Task record: goals, authorization, repository addresses, and environment details apply only to this task. When copied to another project, this is an example, not authorization or requirements for that project.
>
> Historical translation: dates, acceptance IDs, decisions, and evidence describe the original task, not new verification.

## Goal

Introduce an explicit template version and let users write Markdown requests for an agent to execute, verify, and clear during a session.

## Scope

- Store the version in root VERSION, delivered changes in CHANGELOG.md, and increment rules in the shared conventions.
- Use docs/TODO.md for requests, with rules for reading, priority, clarification, completion cleanup, and receipts.
- Update README and the checker for version format, changelog consistency, and inbox structure.

## Non-goals

- No background watcher, scheduled task, automatic model invocation, or new dependency.
- No script-based natural-language executor or mechanical deletion of arbitrary Markdown.
- No inheritance of historical template authorization and no automatic GitHub Release.

## Constraints and assumptions

- This task first introduced versions, starting at 0.1.0 without backfilling old commits.
- Continue the established delivery process: verify, commit, and push main; no automatic version tags.
- Read the inbox when an agent starts work or is asked to process it; editing the file alone does not start a session.
- Retain one short latest-result receipt rather than completed request bodies. Reuse existing plans for detailed evidence; small tasks still need no extra plan.

## Acceptance criteria

- **AC-01**: VERSION is 0.1.0 for this delivery, with a corresponding dated changelog entry and clear major/minor/patch and no-increment cases.
- **AC-02**: Users can write plain text or checkbox requests in docs/TODO.md without repeating them in chat; explain session triggering and link the entry from README and AGENTS.
- **AC-03**: Execute clear requests; retain incomplete ideas or key ambiguities with questions. Do not execute unrelated inbox items when the current user limits scope.
- **AC-04**: Remove only completed, verified entries unchanged by the user. Retain failed, blocked, partial, new, or edited entries; reread before cleanup and leave a receipt.
- **AC-05**: The checker detects invalid versions, changelog mismatches, and missing inbox sections; existing document and creation-protection checks pass.
