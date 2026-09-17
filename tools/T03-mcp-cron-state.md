# T03 · `mcp__cron__state`

**Server:** `cron` · **Tool:** `state` · **Surface:** `mcp__cron__state:always-load@1`

Deterministic time triggers — for Tasks that already exist.

---

## Description (verbatim)

> Manage deterministic time triggers for existing Tasks. Always pass
> `action=create/update/delete/list`.
>
> **Time wakes must attach to a Task and never be free-floating reminders.**
>
> Typical flow: create the Task with `mcp__okr__state` `action="task.upsert"`, then schedule it
> with `action="create"`, `taskId` from that result, `schedule="30 14 * * *"` for 14:30 local
> time, and `recurring=false` for one-shot.

## Schema

```ts
{
  action?: enum("create","update","delete","list")
      // "Required. create schedules an existing Task; update edits or pauses a trigger;
      //  delete removes one; list shows department triggers. Do not omit action."

  id?: string             // required for update / delete

  schedule?: string
      // required for create, optional for update.
      // 5-field cron expression in LOCAL time, or a compact relative interval such as "5m" / "1h".
      // For 14:30 local: "30 14 * * *". Set recurring=false for a one-shot wake.

  prompt?: string         // "Optional execution nuance. The Task packet remains the source of truth."

  recurring?: boolean     // for compact intervals: false = one-shot, true = recurring interval

  activeHours?: { start: "HH:MM", end: "HH:MM" } | null
      // 24-hour window; if end < start the window crosses midnight.
      // pass null on update to clear

  enabled?: boolean       // false pauses without deleting; true resumes

  taskId?: string
      // required for create. Create the OKR Task first with mcp__okr__state action="task.upsert",
      // then pass the returned taskId. Optional replacement Task id for update.
      // "Delete/pause instead of clearing linkage."

  keyResultId?: string | null      // preserve OKR linkage; null clears
  purpose?: "follow_up" | "monitor" | "deadline" | "review" | null
      // "Why this trigger exists in the Task loop"
  sourceRefs?: string[] | null     // sources that justify this scheduled Task
}
```

## Design notes worth copying

1. **`prompt` is explicitly demoted.** *"The Task packet remains the source of truth."* Without
   this, agents stuff the whole instruction into the cron prompt and the Task becomes a shell.
2. **`activeHours` with midnight wrap** — a scheduled check shouldn't fire at 03:00.
3. **`enabled: false` instead of delete** — pausing preserves history and intent.
4. **`purpose` is a closed enum** — four reasons cover the real cases and make the UI groupable.
5. **Linkage cannot be cleared** — *"Delete/pause instead of clearing linkage."* A trigger without
   a Task is exactly the thing this tool exists to prevent.

## Enforcement

Built-in `CronCreate` / `CronDelete` / `CronList` are in `disallowedTools`, so there is no
unconstrained scheduling path. See [M11](../modules/M11-cron-scheduler.md).

## shotgun-next mapping

Identical, bound to Work Items:

```
mcp__studio__schedule
  action: create|update|delete|list
  itemId (required for create)
  schedule, recurring, activeHours, enabled
  purpose: follow_up | monitor | deadline | review
```

Studio-specific `purpose` additions worth considering: `render_check` (poll a long render) and
`publish_window` (a scheduled release).
