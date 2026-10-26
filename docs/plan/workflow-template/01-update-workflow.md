# Simplify conventions and complete workflow templates

> Task record: goals, authorization, repository addresses, and environment details apply only to this task. When copied to another project, this is an example, not authorization or requirements for that project.
>
> Historical translation: this preserves the original requirements and evidence, not a new verification run. Small-change planning and recording rules have since been superseded by [AGENTS.md](../../../AGENTS.md) and the [efficiency spec](../../spec/agent-efficiency/spec.md).

**status**: done
**Source**: [Workflow template changes](../../spec/workflow-template/spec.md#acceptance-criteria).

## Goal and acceptance

Implement the approved template changes, covering AC-01 through AC-06. This file is also a complete execution-record example.

## Steps

- [x] Save this task's spec and plan.
- [x] Centralize conventions and clarify task classification, questions, and plan adjustment boundaries.
- [x] Update the spec template and add a plan template with acceptance, results, and handoff fields.
- [x] Simplify README, remove duplicate indexes and log placeholders, and update ignore rules.
- [x] Verify document links, workflow scenarios, and ignore behavior; record actual results here.

## Verification methods

| Criteria | Method | Passing condition |
|---|---|---|
| AC-01, AC-04 | Check local Markdown links and search references to old rules/deleted files | Valid local files/anchors, shared entry point, no obsolete references |
| AC-02 | Review investigation, small-change, feature, adjustment, and recovery scenarios | Rules support progress and identify decisions requiring confirmation |
| AC-03 | Check template/example fields and acceptance mappings | Complete fields, traceable criteria, no completion before verification |
| AC-05 | Copy ignore rules into a temporary Git repository; use git check-ignore and git ls-files | Local artifacts ignored, intended versioned files visible |
| AC-06 | Check README preparation/setup/examples against actual outputs | Complete reuse instructions with evidence matching executed checks |

## Verification results

All criteria passed in the original task. These were actual checks; no nonexistent business tests or application were run.

### Documents, templates, and entry points (AC-01, AC-03, AC-04)

A one-off Python check read all Markdown, checked local links and anchors, required fields in both templates, mappings for 6 criteria, and absence of deleted-file/obsolete-rule references:

```text
Markdown links: PASS (7 files, 11 local links, 1 anchor)
Entry point and removed-rule references: PASS
Template fields and acceptance mapping: PASS (6 acceptance items)
```

CLAUDE.md imports shared rules through `@AGENTS.md`. At the time, this syntax was checked against the [official Claude Code import documentation](https://code.claude.com/docs/en/memory#import-additional-files). The entry file and target were inspected; no Claude Code session was started to test loading.

### Workflow review (AC-02)

Manually reviewed AGENTS.md, README, and both templates:

| Scenario | Observed historical rule |
|---|---|
| Read or investigate existing implementation | Investigate and run local checks directly; add a plan before changing code/scripts/configuration |
| Clear small change | Save a short plan with request, steps, acceptance, and results; spec optional |
| New feature or cross-module change | Resolve key questions, write a spec with numbered criteria, then implement through one or more plans |
| Change implementation approach | With goals/scope/acceptance unchanged, update the plan before continuing; confirm unauthorized scope/compatibility/cost/data changes |
| Session interruption or external blocker | Ordinary interruptions remain in-progress with a next step; external blockers name the unblock condition; resumption checks actual files |

All five scenarios had rules. Documentation-only exemptions and the prohibition on done after failed verification were consistent.

### Ignore behavior (AC-05)

Initialized Git in an automatically cleaned temporary directory, copied .gitignore, and created nonsensitive representative files. Used `git check-ignore --no-index -q -- <path>`, then checked the complete eligible set using `git ls-files --others --exclude-standard`:

```text
Git ignore rules: PASS (28 ignored, 20 eligible for version control)
```

Coverage included root data/log/old-snapshot/output/temp paths and local environment/dependency/cache paths in root and nested directories. Rules, templates, environment examples, fixtures, deliverable documents, and lockfiles remained eligible; root data rules did not affect `tests/fixtures/data/sample.csv`.

### Usage instructions (AC-06)

Copied both templates into another automatically cleaned temporary directory and ran README's three shell examples using `bash -eu -c`. Checked created directories, copied contents, the complete task's source path, and project setup fields:

```text
README quick start: PASS (3 shell blocks, 5 local directories, 3 copied templates)
Workspace Git initialization: unchanged (temporary repositories only)
```

At that point the working directory was not a Git repository; only temporary repositories were created. No business dependencies or automation scripts were added.

## Changes during execution

- Initial plan: implement the approved proposal using this actual task as the example, without invented business examples.
- Document review: limit pre-execution plan review to tasks needing a plan, avoiding conflict with investigation/documentation exemptions. Use a repository-root reference in the spec template so copying into task directories does not break the guidance. Goals and acceptance stayed unchanged.

## Blockers and next step

- Blockers: none.
- Next step: none; the plan was completed.
