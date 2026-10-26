# Add versioning and a user inbox

> Task record: goals, authorization, repository addresses, and environment details apply only to this task. When copied to another project, this is an example, not authorization or requirements for that project.
>
> Historical translation: the evidence below describes the original run, not a new verification run.

**status**: done
**Source**: [Versioning and task inbox](../../spec/version-and-inbox/spec.md#acceptance-criteria), AC-01 through AC-05.

## Goal and acceptance

Establish lightweight version rules and docs/TODO.md. Verify through the checker, fault injection, and inbox-scenario review, without a background process.

## Steps

- [x] Add VERSION, CHANGELOG, and TODO; update shared rules and README.
- [x] Extend the checker and verify version, inbox, and existing behavior.
- [x] Review execution/cleanup scenarios, record evidence, commit, and push.

## Verification results

- `python3 script/check_workflow.py` passed: 15 Markdown files, 35 local links, 8 anchors, template fields, and 5 statuses. Version 0.1.0 matched the changelog, inbox sections existed, and the 3 existing README examples and repeated-execution protection passed.
- 5 temporary-copy faults exited nonzero with relevant diagnostics: a leading-zero version, VERSION/changelog mismatch, invalid date, missing pending section, and missing result section.
- A temporary inbox containing an actionable request, a do-not-execute note, and a clarification-needed entry passed checks invoked from `/tmp`; its bytes stayed unchanged. The checker does not execute or clear requests for the agent.
- Rule review, not a background runtime test: clear tasks follow classification; ambiguities stay with questions; investigation-only requests do not expand scope; only completed unchanged entries are cleared; failures and partial work remain; new/edited/ambiguous entries stay; empty inboxes do not activate examples; resumption checks actual outputs before repeating work.
- Version review: incompatible changes increment major, compatible features minor, fixes patch; one increment per batch at the highest level, none for receipts/publication evidence alone. This first release used 0.1.0 without backfilled releases or automatic tags.
- `git diff --check` passed; fetching showed no divergence from origin/main.

## Delivery result

Version 0.1.0 was pushed to main of `Asada-Sinon/agent_flow`. Implementation commit `6a40b3e2646534bbef3542cafb52c2590608f99c` matched remote main and the worktree was clean. The completion record followed in a documentation commit without a version increment.
