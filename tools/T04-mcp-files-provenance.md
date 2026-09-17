# T04 · `mcp__files__provenance`

**Server:** `files` · **Tool:** `provenance` · **Surface:**
`mcp__files__provenance:always-load:department-scope:lineage:import-origin:access-rollups@5`

Answer "where did this file come from, who touched it, and what changed".

---

## Description (verbatim)

> Inspect and explain local workspace file provenance through the same File Service used by
> Files(New).
>
> Use `metadata.get` for identity/current revision, `history.list` for actor/causal mutation
> history, `access.list` for bounded read/preview/download events and rollups, `lineage.get` for
> actual copy source/Revision ancestry, and `revision.diff` to explain content changes.
>
> Department Space and Department Message participation bound which files and causal fields are
> visible; **redacted history must not be guessed or reconstructed**.
>
> `revision.restore` is mutating: first read the latest `currentRevisionID`, then ask the exact
> confirmation question returned by the tool. **Never invent actor or causal fields.**

## Actions

```
metadata.get · history.list · access.list · lineage.get · revision.diff · revision.restore
```

## Schema

```ts
{
  action: enum(FILE_PROVENANCE_ACTIONS)
  path?: string(≤2048)        // workspace-relative, for metadata/history/access/lineage
  fileID?: string(≤128)
  cursor?: string(≤2048)      // opaque nextCursor from history.list
  limit?: int 1..40           // MAX_AGENT_HISTORY_PAGE
  beforeRevisionID?: string(≤128)
  afterRevisionID?:  string(≤128)
  revisionID?: string(≤128)                // the revision to restore
  expectedCurrentRevisionID?: string(≤128) // REQUIRED optimistic guard for restore;
                                           // read currentRevisionID immediately before restoring
  operationID?: string(≤128)               // stable idempotency key for a restore retry
}
```

Limits: `MAX_AGENT_DIFF_TEXT_CHARS = 48 000`, `MAX_AGENT_DIFF_LINE_CHARS = 2 000`.

## The three anti-hallucination clauses

This tool description is unusually defensive, and correctly so — provenance is precisely the
domain where a plausible invention is worst:

1. *"redacted history must not be guessed or reconstructed"*
2. *"Never invent actor or causal fields"*
3. restore requires reading the current revision **and** asking the exact confirmation question
   the tool returns — the model does not compose its own confirmation prompt

Plus structural guards: `expectedCurrentRevisionID` (optimistic concurrency) and `operationID`
(idempotent retry).

## Visibility model

```
primary department          → canReadAllDepartments = true
non-primary department      → own files fully;
                              peer files only where it participated
                              (Department Space / Department Message participation)
```

Redacted fields are returned as redacted, not omitted — so the agent knows something exists and
must not speculate.

## shotgun-next mapping

Keep as-is and extend for creative work:

```
mcp__studio__provenance
  metadata.get · history.list · access.list · lineage.get · revision.diff · revision.restore
  + variant.list        v1..vN of one deliverable, with the chosen variant marked
  + approval.list       who approved what, when, with what note
  + source.list         which references / inputs fed a generated asset
```

`source.list` matters a lot for generated media: "which reference image and which prompt produced
this frame" is the studio's version of provenance, and it should be captured by the media tool
automatically rather than reported by the agent.
