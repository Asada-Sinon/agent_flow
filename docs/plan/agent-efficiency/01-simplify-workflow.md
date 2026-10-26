# Simplify and verify the workflow

> Task record: goals, authorization, repository addresses, and environment details apply only to this task. When copied to another project, this is an example, not authorization or requirements for that project.
>
> Historical translation: the evidence below describes the original run, not a new verification run.

**status**: done
**Source**: [Agent efficiency workflow](../../spec/agent-efficiency/spec.md#acceptance-criteria), AC-01 through AC-05.

## Goal and acceptance

Implement the six approved suggestions while preserving real verification and continuity. Accept through rule-scenario review, local-link checks, README example execution, and ignore-rule checks.

## Steps

- [x] Simplify AGENTS, README, and both templates; mark historical examples.
- [x] Check links, README examples, ignore rules, and representative workflows.
- [x] Record results and pass deliverables to publication.

## Verification results

- The one-off local `python3 temp/check_workflow.py` passed: 10 Markdown files, 22 local links, 4 anchors, and no trailing whitespace. The diagnostic script was not versioned at that time.
- Executed 3 README shell blocks in a separate temporary directory; work directories were created and 2 copied templates exactly matched their sources.
- In a temporary Git repository, 11 local-data/environment/cache paths were ignored and 18 document/fixture/script/lockfile/environment-example paths were eligible for version control.
- Scenario review passed: direct verification for local configuration fixes; plans for multi-step tasks; spec + plan for significant interfaces; impact-based classification of rule edits; direct diagnostics in temp; no per-attempt debugging logs; milestone handoffs; no done status before acceptance.
- README links AGENTS rather than repeating complete workflow/status definitions. Templates omit mandatory empty sections; historical examples preserve evidence and identify superseded rules.
- No business application or tests existed. No business tests or comparative efficiency benchmark were claimed.

## Important adjustments

The user corrected the repository name to `agent_flow`; the verified address was `https://github.com/Asada-Sinon/agent_flow`. Publication is recorded in the [publication plan](02-publish-repository.md).
