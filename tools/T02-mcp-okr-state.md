# T02 · `mcp__okr__state`

**Server:** `okr` · **Tool:** `state` · **Surface:** `mcp__okr__state:always-load@1`

The single write surface for direction, progress and proof.

---

## Description (verbatim)

> Single write surface for OKR facts. Objective = direction, Key Result = observable progress,
> Task = owned action; Check-ins carry proof and learning.
>
> Always pass the top-level `action` field. For new work use `action="task.upsert"` with
> `task.title`; omit `task.taskId` so OKR generates one.
>
> For time wakes such as 14:30, create the Task first, then call `mcp__cron__state`
> `action="create"` with the returned `taskId` and `schedule="30 14 * * *"`.
>
> Tasks bound to a Key Result land as `task.upsert` with both ids; ad hoc Tasks omit both.
> **Terminal Task states (blocked / completed / failed / cancelled) are only written by
> `task.check_in`.**
>
> Progress is stored as 0..1; percent inputs like 50 or 100 are accepted and normalized. Do not
> create local Tasks from `msg_` department-message ids; reply to department messages with
> `mcp__matrix__department` `message.reply`.
>
> See `action.description` for per-action field requirements.

## Actions

```
DEPARTMENT_ACTIONS   state.get · key_result.create · key_result.update · key_result.state_patch
                     task.upsert · task.check_in
PRIMARY_ACTIONS      DEPARTMENT_ACTIONS + objective.create · objective.update · objective.state_patch

aliases              state|get|read → state.get
                     task.create|task.update|okr_task.upsert → task.upsert
                     okr_task.check_in → task.check_in
                     objective.patch → objective.state_patch
                     key_result.patch → key_result.state_patch
```

## Per-action field guide (shipped in `action.description`)

```
state.get              → reads OKR + tasks for `department`.
objective.create       → `objective` with title+ownerDepartmentId+summary+status+timeHorizon.
objective.update       → `objectiveId` + `objective` patch.
objective.state_patch  → `objectiveId` + `objectiveStatePatch` (health/riskSummary/lastProofAt only).
key_result.create      → `keyResult` with objectiveId+ownerDepartmentId+title+targetState+status+priority.
key_result.update      → `keyResultId` + `keyResult` patch.
key_result.state_patch → `keyResultId` + `keyResultPatch` (progress accepts 0..1 or 0..100 percent).
task.upsert            → `task.title` (+ objectiveId & keyResultId together, or neither for inbox;
                          omit taskId for new work).
task.check_in          → `taskId` + `checkIn`.
```

## Schema

```ts
{
  action?: enum(actions + aliases) // optional in Zod; omission handled by the action handler
  department?: string            // defaults to this department
  objectiveId?: string           // required for objective.update / state_patch
  keyResultId?: string           // required for key_result.update / state_patch
  taskId?: string                // required for task.check_in
  acknowledgePending?: string    // primary only: one-line reason for closing an Objective
                                 //   whose Key Results are still open

  objective?: {
    title?, ownerDepartmentId?, summary?
    status?: draft|active|blocked|completed|cancelled
    timeHorizon?: string   // "Optional free-text horizon for genuinely long-running direction
                           //  (e.g. 'this cycle'). Omit it for ordinary or short work — do not
                           //  invent a duration, and never inflate a quick job into a
                           //  multi-week one."
    setAsFocus?: boolean
    health?: on_track|at_risk|blocked|done|null
    riskSummary?: string|null
    lastProofAt?: string|null
  }

  keyResult?: {
    objectiveId?, ownerDepartmentId?, title?, targetState?
    status?:   draft|active|at_risk|blocked|completed|cancelled
    priority?: low|normal|high
    deadline?: string|null
    effortSize?: "quick"|"deep"|null
        // quick = one focused session; deep = must decompose into Tasks before executing
    dependsOn?: string[]
    progress?: number|null        // stored 0..1; 0..100 accepted and normalized
    health?, blockers?, confidence?, nextAction?, proofRefs?, learningRefs?
  }

  keyResultPatch?: {  // for key_result.state_patch
    status?, progress?, health?, blockers?, confidence?, nextAction?,
    proofRefs?, learningRefs?,
    appendProofRefs?: string[], appendLearningRefs?: string[]   // merge, don't replace
  }

  objectiveStatePatch?: { health?, riskSummary?, lastProofAt? }   // only these three

  task?: {
    taskId?: string      // "Omit for new local Tasks so OKR generates a task-* id.
                         //  Never use a msg_ department-message id to create a local shadow Task."
    title?, ownerDepartmentId?
    objectiveId?: string|null
    keyResultId?: string|null      // pass both together, or neither
    status?: TaskStatus  // Zod accepts all nine states; store guard rejects terminal upsert transitions
    priority?: low|normal|high|null
    nextAction?: string|null
    trigger?: { type: manual|time|department_message,
                scheduleId?, dueAt?, recurrence?, reason?, sourceRefs? } | null
    criteria?: Array<{ id, text, status: open|satisfied|blocked|not_applicable,
                       proofRefs: string[],   // required (≥1) when status=satisfied
                       notes? }>
    contextRefs?: string[]
    proofRefs?: string[]
    learningRefs?: string[]        // prefer memory/knowledge/name.md or skills/name.md
  }

  checkIn?: {
    status?: TaskStatus
    authorDepartmentId?: string
    judgment?: string              // "Human reason for the state change."
    nextAction?: string|null
    blockerCategory?: user_input_missing | department_waiting | external_system_failure
                    | permission_or_credential | business_blocker | null
                                   // required when status = blocked | failed
    criteria?: Array<{id,text,status,proofRefs,notes?}>
        // "merged by id: items you list update the matching criterion, items you omit are left
        //  unchanged. A check-in cannot drop a criterion — use task.upsert to add, remove, or
        //  fully restate criteria."
    proofRefs?: string[]
    learningRefs?: string[]
    keyResultDecision?: accept|modify|reject
        // required for KR-linked Tasks.
        // accept = apply auto KR patch; modify = override via keyResultState; reject = leave KR untouched
    learningDecision?: ignore|proof-only|memory-card|skill-update|next-task
        // required whenever learningRefs are written.
        // memory-card / skill-update refs must already exist on disk
    keyResultState?: KeyResultPatch    // used with keyResultDecision="modify"
  }
}
```

### Proof ref guidance (appears on every proof field)

> "For local artifacts, prefer existing department/workspace-relative paths like
> `artifacts/name.md`; use `file://` only for absolute local file URLs."

## Invariants enforced

| Invariant | Enforcement |
|---|---|
| Only the primary writes Objectives | `requirePrimary(deps)` |
| A department cannot mutate a peer's state | `resolveTargetDepartment()` |
| KR lives in its owner's store | write-path validation |
| Terminal task transitions only via check-in | both payloads share the full enum; `assertUpsertDoesNotBypassCheckIn` in the store enforces transitions |
| `satisfied` criteria carry proof | `proofRefs` required when `status="satisfied"` |
| KR-linked check-ins decide the KR | `keyResultDecision` required |
| Materialized learning | memory-card / skill-update decisions check destination files; other decisions have different requirements |
| Destructive data ops need confirmation | `checkDestructiveWorkspaceDataWrite()` |
| Check-ins can't silently drop criteria | merge-by-id semantics |

## Error shape

```json
{ "ok": false,
  "error": "unsupported OKR action \"foo\"",
  "allowedActions": ["state.get","key_result.create", …],
  "next": "Use the top-level action field. Allowed actions here: … For a new Task call
           mcp__okr__state with action=\"task.upsert\" and a task payload; omit task.taskId so
           OKR generates one. For a time wake, create the Task first, then call mcp__cron__state
           with action=\"create\", taskId from the Task result, and a schedule such as
           \"30 14 * * *\" for 14:30 local time." }
```

## shotgun-next mapping

```
mcp__studio__state
  brief.create / update / state_patch          (director only)
  milestone.create / update / state_patch
  item.upsert
  item.review           ← check_in, renamed
    verdict:          accept | revise | reject            (was reviewDecision)
    learningDecision: ignore | deliverable-only | style-lock | memory-card | skill-update | next-item
    blockerCategory:  input_missing | role_waiting | tool_failure | rights_or_access
                    | creative_blocker | budget
    -- enums are canonical in shotgun/03-data-model.md §4; D15 and shotgun/04 use the same values
```

Keep every guard. In a creative studio the "mark it done without evidence" failure is *more*
tempting, not less, because the evidence is subjective — which is exactly why the criteria +
proof-ref mechanism matters.
