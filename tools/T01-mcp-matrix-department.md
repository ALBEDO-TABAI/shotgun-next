# T01 · `mcp__matrix__department`

**Server:** `matrix` · **Tool:** `department` · **Surface:**
`mcp__matrix__department:always-load:thread-digest@1`

One tool, 13 canonical actions (10 collaboration + 3 management), permission-scoped. The cross-owner coordination surface.

---

## Actions

```ts
COLLAB (all departments)
  message.send · message.reply · message.queue · message.thread
  chat.read_recent · chat.search
  user_profile.get · user_profile.update
  department.list · department.get

MANAGEMENT (primary only — canManageDepartments)
  department.create · department.update · department.delete
```

## Description (verbatim, as the model sees it)

> Departments are owners. Each owns a domain with its own memory, skills, Tasks, operating style,
> and coordination history.
>
> Primary entrypoint has two scopes: workspace operator for the map, user entrypoint, department
> topology, routing, and shared resources; department owner for its own Key Results, Tasks, proof,
> memory, skills, and artifacts. Non-primary departments own bounded domain execution.
>
> Agents/subagents are same-owner execution seats inside one department, useful when owned work
> benefits from speed, parallelism, or isolation. Cross-owner work routes through department
> messages.
>
> Department messages are the primary cross-department channel: `message.send` opens dispatch work
> and carries the message body and attachments. Received wakes carry `messageId`; the matching
> `message.reply` answers that exact message. Outcome lives on `message.reply` `kind="reply"`.
>
> Keep department tool calls minimal: omit optional fields instead of sending empty strings, empty
> arrays, or placeholders. `message.reply` infers the recipient from `messageId`, so the body and
> outcome are usually all it needs.
>
> Message kind expresses intent: `dispatch` opens work, `note` adds silent context to an existing
> thread, `reply`+`outcome` closes work.
>
> Department message bodies are stored losslessly. Substantial deliverables land in a Markdown file
> in the shared workspace, with a concise summary in the message body and the file path in
> attachments.
>
> `message.queue` lists pending work; `message.thread` gives compact context, with `includeBodyFor`
> for one exact body when needed. A business result lands once `message.reply` `kind="reply"` with
> outcome closes the thread.
>
> `user_profile.get/update` read and write the global User Profile **only** for stable
> cross-workspace user preferences, work style, identity facts, and public handles the user wants
> remembered. Do not write project facts, workspace facts, credentials, or transient observations
> there.
>
> The Agent tool spawns an Agent inside this department's context and memory; reach for it when the
> work is owned by this department.
>
> `department.list` returns each peer's charter and domains — use it to see whose domain a piece of
> work falls under.
>
> *(primary only)* `department.create` forms a new owner when the work falls outside every existing
> department's responsibility — **one clear signal is enough, do not wait for repetition**. Use
> `action="department.create"` with `name="<display name>"`; the create field is `name`, not
> `department`. If an existing department already owns the domain, route via `message.send` instead.
> After creating a department, send it an initial brief and preserve routing memory for future
> similar work. Use `department.update` lifecycle retired/merged for ordinary department evolution;
> `department.delete` is hard deletion only.

## Minimal contracts (shipped in the description)

```
message.send   : action, message, toDepartment, topic?, attachments?
                 never send kind, outcome, messageId, department, query, sessionId, includeBodyFor
message.reply  : action, messageId, message, outcome, attachments?
                 recipient inferred; omit department, toDepartment, query, sessionId,
                 includeBodyFor, limit, topic unless truly needed
message.reply(note): action, messageId, kind="note", message      (no outcome)
message.queue  : department?
message.thread : messageId, includeBodyFor?
chat.read_recent: department, limit?
chat.search    : department, query, limit?
user_profile.get
user_profile.update: profileContent, expectedVersion?
department.list
department.get : department?
department.create: name, description?, parentDepartmentId?, profile?
department.update: department, name?/description?/parentDepartmentId?/proactive?/profile?/lifecycle?
department.delete: department, confirmDepartmentId
```

## Schema

```ts
{
  action: enum(COLLAB | COLLAB+MANAGEMENT)              // by permission
  department?:        string   // target for queue/thread/chat/get. Omit on message.reply.
  toDepartment?:      string   // message.send only
  messageId?:         string   // message.reply / message.thread
  includeBodyFor?:    string   // message.thread: reveal one exact body
  sessionId?:         string   // chat reads, when a specific session is needed
  query?:             string   // chat.search
  limit?:             int 1..50
  topic?:             string   // message.send only
  message?:           string   // body; large deliverables → file + summary
  profileContent?:    string   // user_profile.update; empty clears
  expectedVersion?:   string   // optimistic concurrency
  attachments?:       Array<{ uri, name?, mime?, size?, sha256? }>
  kind?:              enum("dispatch","reply","note")   // default "reply" on message.reply
  outcome?:           enum("completed","failed","cancelled")  // only kind="reply"

  // primary only
  name?, description?, parentDepartmentId?: string
  proactive?:  boolean            // workspace proactive mode; primary department only
  model?:      Record<string,unknown>
  profile?:    Record<string,unknown>
  lifecycle?:  { status: "active"|"retired"|"merged",
                 successorDepartmentId?, reason?, updatedAt? }
  confirmDepartmentId?: string    // must equal the target id for delete
}
```

Every optional string description ends with *"Omit this field instead of using an empty string or
placeholder."*

## Result

```ts
{ ok: true,  action, …payload, next }
{ ok: false, action, error, next }
```

`next` hints per action — see [tools/README §5](README.md#5-department-results-carry-a-next-hint).

## Guards

- Action enum narrows by `canManageDepartments`.
- `validateKnownMatrixWorkspaceArgs` rejects unknown fields with a teaching message.
- `normalizeMatrixWorkspaceArgs` strips empty strings, placeholders, empty arrays, and every field
  not relevant to the action.
- `department.delete` requires `confirmDepartmentId === department`.
- Catalog-change notification is best-effort: if `notifyDepartmentCatalogChanged` throws, it is
  logged and the mutation still succeeds.

## shotgun-next mapping

```
mcp__studio__role
  message.send / reply / queue / thread        → same
  chat.read_recent / search                     → same
  user_profile.get / update                     → same (creative preferences, taste)
  role.list / get                               → same
  role.create / update / delete                 → director only
```

Keep the `dispatch | note | reply(+outcome)` vocabulary exactly. It is the minimum viable protocol
for delegated work and it maps perfectly onto a studio's assignment → comment → delivery flow.
