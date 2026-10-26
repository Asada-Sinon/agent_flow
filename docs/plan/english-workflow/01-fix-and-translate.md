# Fix recovery and translate the repository

> Task record: goals, authorization, repository addresses, and environment details apply only to this task. When copied to another project, this is an example, not authorization or requirements for that project.

**status**: done
**Source**: [English workflow and recovery fixes](../../spec/english-workflow/spec.md#acceptance-criteria), AC-01 through AC-05.

## Goal and acceptance

Implement the approved fixes and English migration. Verify creation recovery, existing-file protection, links, fields, version consistency, historical evidence, and retained-task rules.

## Steps

- [x] Translate current instructions and templates; fix creation and TODO rules.
- [x] Translate historical records without changing evidence; update checker expectations and recovery cases.
- [x] Verify, record results, commit, push, and compare main with the remote.

## Verification results

- `python3 script/check_workflow.py` passed: 17 Markdown files, 36 local links, 9 anchors, English template fields, 5 statuses, version 1.0.0/changelog agreement, and inbox sections.
- Both plan/spec examples passed initial creation, missing/unreadable/non-file source rejection with no target, retry after source repair, wrong-directory rejection, and unchanged existing populated/empty targets. Unreadable cases ran as UID 1000; none were skipped.
- Temporary-copy fault injection detected 8 regressions with exit code 1: broken link, broken anchor, missing template field, invalid version, version mismatch, missing inbox section, removed overwrite protection, and the old output-before-source creation bug.
- A temporary inbox containing retained cancelled, `[x]`, `[X]`, and active entries remained byte-for-byte unchanged by the checker, invoked from `/tmp`. This checks read-only validation, not autonomous agent behavior.
- Rule review confirmed retained cancelled/replaced entries and checked records are skipped; cancellation updates both a plan and its associated inbox entry; reactivation and removal require explicit user intent. User-checked records do not become agent verification evidence.
- An audit of 20 tracked/candidate files found no remaining Chinese text. All 8 historical task records retained their commit IDs, dates, acceptance IDs, and numeric evidence; their English text identifies the records as translations of earlier work. Ignore patterns were unchanged apart from translated comments.
- README and checker both document their example coupling. Migration instructions identify the English headings/fields and unchanged paths/statuses/command. The 1.0.0 increment follows the existing rule for incompatible document conventions; no performance gain is claimed.
- `git diff --check` passed. Fetching origin/main showed no divergence before publication.

## Delivery result

Published version 1.0.0 to main of `Asada-Sinon/agent_flow`. Implementation commit `21d6df75fd3167d213d950b1029076db9ee687cf` matched remote main after pushing, with a clean worktree. This completion record follows in a documentation-only commit without a version increment.
