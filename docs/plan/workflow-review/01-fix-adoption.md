# Fix template adoption and verification

> Task record: goals, authorization, repository addresses, and environment details apply only to this task. When copied to another project, this is an example, not authorization or requirements for that project.
>
> Historical translation: the evidence below describes the original run, not a new verification run.

**status**: done
**Source**: The user requested implementation of the review suggestions and upload to the existing repository.

## Goal and acceptance

- README creation examples succeed initially, reject repeated execution with a recovery message, and preserve existing contents.
- `python3 script/check_workflow.py` uses the standard library to check local links, anchors, template fields, and README creation examples; failures exit nonzero.
- README provides adoption/check instructions; task records scope historical goals and authorization to their original task and preserve evidence.
- Rules and the plan template support cancelled with a reason and replacement task if any. Independent review remains optional.
- Commit and push main, then compare local and remote commits.

## Steps

- [x] Update creation examples, adoption guidance, task notices, and statuses.
- [x] Retain the checker and verify normal behavior plus fault detection.
- [x] Record evidence, commit, push, and verify the remote.

## Verification results

- `python3 script/check_workflow.py` passed: 11 Markdown files, 24 local links, 4 anchors, required template fields, and 5 statuses.
- All 3 README examples passed. Initial plan/spec copies matched their templates; existing populated and empty targets caused nonzero exits, recovery messages, and unchanged contents.
- Temporary copies with a broken link, broken anchor, missing template field, or removed overwrite protection each exited 1 with the corresponding diagnostic.
- Running by absolute path from `/tmp` passed; invocation did not depend on the caller's working directory.
- All 6 task records included authorization-scope notices. Comparing against Git showed the 5 previous records were unchanged apart from those notices.
- Review confirmed adoption guidance removes template task records and fixes links, cancelled differs from done, and independent review is optional.
- `git diff --check` passed; a pre-push fetch showed no local/remote divergence.

## Publication result

Published to main of `Asada-Sinon/agent_flow`. The implementation commit was `8149a51f535fe728f97c128427fadf5377eaac59`; after pushing, local HEAD matched remote main and the worktree was clean. This completion record followed in a separate documentation commit.
