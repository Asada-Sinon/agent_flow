# Simplify and complete the workflow template

> Task record: goals, authorization, repository addresses, and environment details apply only to this task. When copied to another project, this is an example, not authorization or requirements for that project.
>
> Historical translation: this preserves the original requirements and evidence, not a new verification run. Small-change planning and recording rules have since been superseded by [AGENTS.md](../../../AGENTS.md) and the [efficiency spec](../../spec/agent-efficiency/spec.md).

## Goal

Let flow choose a workflow by task size and support future development with resumable plans and real verification evidence.

## Background

Earlier rules required a full spec and plan for every code change, with confirmation for each plan adjustment. Model signatures and log snapshots added maintenance cost. A spec template existed, but plan templates, handoff guidance, and complete examples were missing.

## Scope

- Centralize rules in AGENTS.md, with CLAUDE.md importing them.
- Separate investigation, small changes, and complete features; allow implementation adjustments within approved goals.
- Complete spec/plan templates, acceptance IDs, verification evidence, and handoff guidance.
- Write results directly into plans; remove mandatory model signatures, log snapshots, and duplicate document indexes.
- Update directories, ignore rules, and adoption instructions.
- Use this actual task's spec and plan as the full example.

## Non-goals

- No business code, framework, dependency, or automation script.
- No Git initialization or commits in the working directory for this task.
- No pre-created application sources, fixtures, or deliverables; only define their locations.

## Constraints and assumptions

- Initially there were only instructions, one spec template, ignore rules, and an empty log placeholder.
- Small changes still required a short saved plan; documentation-only changes did not require a separate plan under these historical rules.
- data, log, output, and temp were local directories; versioned fixtures and deliverables used separate locations.
- The user accepted the review suggestions and explicitly requested the full implementation.

## Acceptance criteria

- **AC-01**: Maintain one set of shared rules; CLAUDE.md reads AGENTS.md, and README links rules, templates, and real examples.
- **AC-02**: Define investigation, small changes, full features, plan adjustments, and interruption recovery without unrelated repeated confirmation.
- **AC-03**: Specs retain non-goals and numbered criteria; plans support source, steps, verification methods, actual results, changes, blockers, and next steps. Unverified work cannot be done.
- **AC-04**: Store evidence in plans; remove mandatory signatures, log snapshots, duplicate indexes, placeholders, and stale references.
- **AC-05**: Ignore local data, outputs, logs, temporary files, environment configuration, dependencies, and caches while permitting rules, templates, environment examples, fixtures, and deliverables.
- **AC-06**: README covers local directory creation and environment/install/run/check/source setup; records contain only checks actually performed and their results.

## Open questions

None. Record new issues affecting goals, scope, or acceptance in the plan and handle them under the shared rules.

## Decisions

- The user accepted the review, requested changes, then requested implementation of the resulting plan.
- Small changes would save a short plan by default; results would stay in plans. The example would document this real task, without fabricated implementation or verification.
