# A workflow that prioritizes agent efficiency

> Task record: goals, authorization, repository addresses, and environment details apply only to this task. When copied to another project, this is an example, not authorization or requirements for that project.
>
> Historical translation: dates, acceptance IDs, decisions, and evidence describe the original task, not new verification.

## Goal

Reduce process overhead, repeated reading, and repeated investigation while retaining acceptance and handoff records, then publish the template to the user's `Asada-Sinon/agent_flow` repository.

## Scope

- Choose workflows by uncertainty, impact, and continuity needs; do not require file plans for clear local changes.
- Read on demand, record important changes at milestones, simplify templates, and allow one-off diagnostic scripts.
- Put adoption guidance, environment information, and layered verification entry points in README; mark old examples as historical.
- Initialize Git and commit verified files to the empty `Asada-Sinon/agent_flow` repository.

## Non-goals

- No application runtime, automation framework, extra tooling dependency, or mandatory multi-agent workflow.
- No rewriting historical verification results or committing local data, logs, temporary files, or credentials.
- No overwriting remote history.

## Constraints and assumptions

- The user approved the six review suggestions and Git initialization/upload.
- No comparative task benchmark was performed; do not claim quantified efficiency gains.
- Initial Git write/network restrictions blocked publication, and the GitHub connector returned 403 on writes. On 2026-10-26 the user switched to an environment allowing filesystem writes and networking; publication continued through local Git and existing HTTPS authentication.

## Acceptance criteria

- **AC-01**: Clear local changes run directly; multi-step or cross-session tasks use a plan; significant interface/behavior changes or complex requirements needing clarification use spec + plan. Classify code, scripts, configuration, and documents by impact.
- **AC-02**: Read only current-task context; routine debugging needs no per-attempt update; save important progress at milestones and check files when resuming.
- **AC-03**: Default plan content is goal, status, steps, and results; omit empty optional content. Support entry points, rejected approaches, and next commands. Unaccepted work cannot be done.
- **AC-04**: README links the shared rules, templates, and examples, and provides environment, focused verification, full-check triggers, and external-dependency fields. Permit one-off diagnostics without extra side effects and avoid unjustified repeated checks.
- **AC-05**: Local links, usage examples, and relevant ignore checks pass; historical examples are clearly not current policy.
- **AC-06**: The remote branch contains all deliverables with matching content, and local Git is initialized. Restricted portions remain unfinished with blockers and recovery steps recorded.
