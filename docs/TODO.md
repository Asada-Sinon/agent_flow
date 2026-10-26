# User inbox

Write requests or ideas in `Pending` below, as plain text or a `- [ ]` list, one goal per entry. Use your preferred language; there is no need to repeat requests in chat.

The agent reads this file when starting work, or when asked to "process the inbox." Editing it does not start an agent or background job. Clear requests follow the project workflow. Questions affecting goals or acceptance are recorded beside the entry for clarification. Mark reference-only notes `Do not execute`.

Retained cancelled or replaced tasks are marked `Do not execute: cancelled` and skipped until you explicitly reactivate them. Manually checked `[x]` or `[X]` entries are treated as your completed records and skipped, not counted as agent-verified work. Cancelled and checked records are removed only if you explicitly request removal.

After completion and verification, the agent removes only processed entries whose original text has not changed, then updates `Latest result`. Unfinished, newly added, or edited entries remain. See the [inbox rules](../AGENTS.md#task-inbox).

Examples only; these are not actual requests:

```markdown
- [ ] Add CSV export with a date in the filename.
- [ ] Fix the settings page notification that remains after saving.
- Do not execute: consider a dark theme.
- Do not execute: cancelled — replace the old export task with the CSV request.
- [x] A task I completed myself; no agent verification is claimed.
```

## Pending

<!-- Add requests here. Preserve this heading and note when clearing completed entries. -->

## Latest result

No inbox tasks have been processed.

<!-- Replace after each processing batch: date, completed work, verification, remaining issues, and an existing plan link if applicable. Keep only the latest receipt. -->
