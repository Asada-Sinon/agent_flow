# English workflow and recovery fixes

> Task record: goals, authorization, repository addresses, and environment details apply only to this task. When copied to another project, this is an example, not authorization or requirements for that project.

## Goal

Fix template creation recovery and retained TODO behavior, then convert all version-controlled project text to English without losing historical evidence.

## Scope

- Reject missing or unreadable template sources before creating plan/spec targets; preserve existing-file protection and test recovery.
- Skip retained cancelled/replaced tasks and user-checked items until explicitly reactivated.
- Translate instructions, README, templates, inbox, changelog, historical records, ignore comments, and checker expectations; update links and document README/checker coupling.
- Validate and publish the changes to the existing main branch.

## Non-goals

- No background agent, task-creation framework, new dependency, Git history rewrite, or GitHub Release.
- Do not translate ignored local data, logs, or temporary scripts.
- Do not claim measured agent speed or token savings from translation.

## Constraints and assumptions

- The user authorized both fixes and repository-wide English text. The inbox is currently empty; no user task content needs migration.
- Preserve original dates, commit IDs, acceptance IDs, measured counts, and historical outcomes. Mark old records as translations, not new verification.
- Under the existing version rule, replacing template fields and TODO section names is an incompatible document convention change: release 1.0.0. Paths, status values, and the checker command remain unchanged.
- Missing/unreadable source and wrong-directory recovery are in scope. Mid-write storage failures are reported without automatically deleting a possibly user-modified target.

## Acceptance criteria

- **AC-01**: Both creation examples reject missing/unreadable/non-file sources and wrong working directories without leaving a target; restoring the source allows retry. Existing empty and populated targets remain unchanged.
- **AC-02**: Retained cancelled/replaced items use `Do not execute: cancelled`, are skipped until explicitly reactivated, and are removed only on explicit request. User-checked `[x]`/`[X]` items are skipped without claiming agent verification.
- **AC-03**: All version-controlled project text is English; internal links, anchors, template fields, and TODO section checks agree. Historical evidence and task boundaries are preserved.
- **AC-04**: README and checker explain their coupled example structure; automated checks include source-failure recovery and still detect representative document/template/version failures.
- **AC-05**: VERSION and CHANGELOG agree on 1.0.0 and explain the heading/field migration. Publish and verify local/remote main agreement.
