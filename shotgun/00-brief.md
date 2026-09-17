# shotgun-next · Product Brief

> **A studio, not a company.** Matrix built an agent *corporation* — departments, OKRs, revenue,
> a marketplace. shotgun-next takes the same machine and points it at creative production: a small
> ensemble of agents in professional roles, collaborating on work that gets made, critiqued and
> shipped.

---

## 1. The one-sentence product

**shotgun-next is a desktop studio where you brief a team of AI specialists, watch them work,
critique what they make, and ship it — with every deliverable traceable to the decision that
produced it.**

## 2. What changes from Matrix

| Matrix | shotgun-next | Why |
|---|---|---|
| Workspace = company | **Studio** (persistent) + **Production** (a body of work) | creatives think in projects, not companies |
| Department = owner | **Role** = a studio seat with a craft | "Design Dept" → "Art Director" |
| Objective / Key Result / Task | **Brief / Milestone / Work Item** | the language a client and a producer already use |
| Criteria / Proof / Check-in | **Acceptance / Deliverable / Review** | review is the native creative ritual |
| Dashboard (business metrics) | **Production board + review queue** | "what needs my eye" beats "how are we doing" |
| Receivable, payouts, marketplace | *dropped* | not a payments product |
| Office tower, San Francisco | **Studio floor** | a room, not a city |
| Media generation (peripheral) | **Media generation (core)** | this is the work |

Everything else — the daemon, the message bus, the wake engine, provenance, memory,
skills, the prompt architecture — carries over almost unchanged, because it is genuinely good.

## 3. The four roles (unchanged from Matrix, correctly)

```
YOU            direction · references · taste calls · approvals · final say
DIRECTOR       the primary role: intake, shaping, routing, synthesis, your single contact
SPECIALISTS    own a craft; produce deliverables; critique each other
SYSTEM         wakes the studio on deadlines, blocked work, finished renders, pending reviews
```

Matrix's framing — *"You do founder work"* — becomes *"You do director work"*. The user's job is
to **set direction, supply references, and judge**, not to prompt.

## 4. The default ensemble

Seven seats, created on demand, not all at once:

| Role | Owns | Escalates to |
|---|---|---|
| **Director** *(primary)* | intake, the Brief, routing, synthesis, continuity with you | you |
| **Researcher** | references, competitive scans, facts, rights/clearance notes | Director |
| **Strategist** | positioning, audience, message, the argument a piece must make | Director |
| **Writer** | copy, scripts, narration, naming | Strategist |
| **Art Director** | look, palette, typography, style locks, image direction | Director |
| **Producer** | schedule, dependencies, asset wrangling, publish packaging | Director |
| **Critic** | structured critique rounds, the verdict, the "not yet" | Director |

The **Critic is not optional**. Matrix *ships the text* of a forced verification nudge but never
fires it (the flag is hard-wired `false` in both producers — T09, ERRATA E16); a model still
cannot grade itself, so a studio needs the structural check Matrix only gestures at, and in
creative work it is the single highest-value seat.

## 5. The core loop

```
Brief ──► Milestone ──► Work Item ──► Acceptance ──► Deliverable ──► Review ──► Learning
                                                          │                        │
                                                          └──► variants v1..vN     └──► style lock
                                                                                      or skill edit
```

Rules carried over verbatim in spirit:

- **Only a Review writes terminal states.** No self-marking "done".
- **Placeholders are blockers, never deliverables.** ("TBD", an empty frame, a lorem headline.)
- **Every Review must decide what the studio learns** — nothing, a note, a style lock, a skill
  edit, or a follow-up item.
- **A dispatch is complete when the owner replies with an outcome**, not when files appear.

## 6. What "good" looks like on day one

A first session that works:

```
You:      "Launch film for a botanical skincare line. 30s, moody, Chinese market, two weeks."
Director: reads it, creates the Brief + first Milestone, tells you the shape in plain words,
          asks ONE precise question (the vague part), and dispatches:
            → Researcher: competitor scan + reference board
            → Strategist: positioning + the one line the film must land
Later:    Strategist replies with outcome. Director creates the Art Director seat (no owner
          existed), briefs it, writes routing memory, and tells you a new lane exists.
You:      open the Review queue, see three style directions, pick one, say why.
Director: turns your "why" into a style lock. Every later generation inherits it.
```

Two things had to be true for that to work, and both come straight from Matrix:

1. The Director is **structurally prevented** from hoarding the work.
2. Your one sentence of taste becomes **durable state**, not a message that scrolls away.

## 7. Non-goals

- Not a chat wrapper with personas.
- Not a payments or marketplace product.
- Not a general coding agent (it can code, but that is not the pitch).
- Not a city simulator — the 3D floor is one room, in service of legibility.

## 8. The five things we are actually copying

1. **Ownership as a data structure** (`collaborationBoundary`: keepLocal / handoff / create).
2. **Proof-gated completion** with an explicit learning decision.
3. **The static-prefix / volatile-tail prompt split** (the whole cost model).
4. **The message bus** — `dispatch | note | reply(+outcome)` with CHECK constraints.
5. **Multi-lane autonomy with a cost gate** and a logged decision for every skip.

## 9. Read next

- [01-target-architecture.md](01-target-architecture.md) — the system
- [02-role-system.md](02-role-system.md) — seats, boundaries, ownership
- [03-data-model.md](03-data-model.md) — every entity
- [04-tool-surface.md](04-tool-surface.md) — every tool
- [05-prompt-system.md](05-prompt-system.md) — context assembly
- [06-ui-spec.md](06-ui-spec.md) — the client
- [07-studio-floor.md](07-studio-floor.md) — the 3D layer
- [08-build-plan.md](08-build-plan.md) — phased plan with effort
- [09-decisions.md](09-decisions.md) — tech choices and tradeoffs
