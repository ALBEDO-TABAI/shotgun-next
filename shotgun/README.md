# shotgun-next · The Build

The previous author's proposed creative-production adaptation. Platform, feature removals and visual simplification are not user-approved decisions. [Implementation contracts](10-implementation-contracts.md) resolve state, review, recovery and fidelity gaps before development.

| # | Document | What it settles |
|---|---|---|
| 00 | [Brief](00-brief.md) | what the product is, what changes from Matrix, the default ensemble |
| 01 | [Target architecture](01-target-architecture.md) | processes, filesystem, transport, layer rules |
| 02 | [Role system](02-role-system.md) | seats, profiles, ownership policy, emergent roles |
| 03 | [Data model](03-data-model.md) | every entity, every enum, the message schema |
| 04 | [Tool surface](04-tool-surface.md) | every MCP tool and built-in a role gets |
| 05 | [Prompt system](05-prompt-system.md) | context layers, the cache contract, maintenance prompts |
| 06 | [UI spec](06-ui-spec.md) | shell, surfaces, the review queue |
| 07 | [Studio floor](07-studio-floor.md) | the 3D layer — what to build, what to buy |
| 08 | [Build plan](08-build-plan.md) | provisional effort estimates, phase exits, risks and tests |
| 09 | [Decisions](09-decisions.md) | 15 explicit calls and the open questions |
| 10 | [Implementation contracts](10-implementation-contracts.md) | authenticated reviews, isolated state, restart recovery, cost and fidelity acceptance |

Diagram: [D15 · shotgun-next target](../diagrams/D15-shotgun-target.md)

---

## The three ideas that carry the product

**1 · Ownership is a data structure, not a personality.**
Every seat carries `collaborationBoundary: { keepLocal, handoffToRole, createChildRole }`.
The Director is structurally pushed to route rather than to make. Matrix spends hundreds of
prompt words on this because it is the difference between a team and a costume party.

**2 · Nothing is done without a verdict.**
Acceptance criteria are the gate; deliverable refs satisfy them; only a Review writes terminal
states; and a maker cannot accept its own work. Placeholders are blockers, never deliverables.

**3 · Your taste becomes durable state.**
Every review must decide what the studio learns. A correction becomes a **style lock** in the
same turn, and every later generation inherits it. This is why the studio feels like it learns
instead of resetting.

---

## What to build first

```
Phase 0   5 engineer-days      schema package — one source of truth for both sides
Phase 1  22 engineer-days      daemon + state engines — provable with no LLM in the loop
Phase 2  22 engineer-days      sessions + prompt + the two core tools  ← the risky phase
Phase 3  28 engineer-days      autonomy + generation + client
Phase 4  56–61 engineer-days   maintenance, board, integrations, the floor (36–41 of these)
Phase 5  ongoing               polish
```

Effort figures are provisional engineer-days from [08-build-plan](08-build-plan.md) (133–138 in
total before polish and contingency), not calendar weeks; staffing and the runtime/fidelity
prototypes decide the calendar.

The exit test at the end of Phase 2 is the whole bet:

> You brief a launch film in one sentence. The Director shapes it, creates a seat that didn't
> exist, dispatches, receives a delivery, and the Critic files a verdict — end to end, once.
