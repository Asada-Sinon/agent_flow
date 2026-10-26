# Changelog

[VERSION](VERSION) is the version source; see [Versioning](AGENTS.md#versioning) for increment rules. Record delivered changes here and task details in plans. Releases before versioning was introduced are not backfilled.

## 1.0.0 — 2026-10-26

- Translate maintained documents, templates, historical records, comments, and checker expectations into English.
- Breaking document convention change: template fields, inbox sections, and heading links now use English. Update customized templates and heading-based tooling; paths, status values, and the check command remain unchanged.
- Check template sources before creating targets; missing/unreadable sources and wrong-directory attempts leave no target, and corrected attempts can be retried.
- Keep retained cancelled/replaced tasks inactive until explicitly reactivated; skip user-checked items without treating them as agent-verified.
- Expand source-failure regression checks and document the README/checker coupling.

## 0.1.0 — 2026-10-26

- Establish major/minor/patch rules and a single version file.
- Add the [user inbox](docs/TODO.md) for requests processed during sessions, verified completion cleanup, and a latest-result receipt.
- Define priority between inbox requests and the current conversation, preserving unfinished and edited items.
- Add version/changelog consistency and inbox-section checks.
