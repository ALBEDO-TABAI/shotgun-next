# shotgun-next · Decisions & Tradeoffs

Proposals from the previous author, corrected against the bundle. They are not user-approved platform, scope or visual-fidelity decisions. The user's core-to-exterior recreation goal is broader than the reduced creative-studio MVP described here.

---

## D1 · Local daemon, not in-process

**Matrix:** separate Bun-compiled daemon, supervised child of the app.
**Us:** same.

Rationale: separate UI and execution lifecycles. In Matrix's `swift_child` mode, loss of the owner triggers daemon shutdown; it does not keep running through a client crash. Recover durable session state after restart. Independent headless execution requires a separate supervisor mode and explicit acceptance tests.

---

## D2 · Client platform

| Option | Pros | Cons |
|---|---|---|
| **Native Swift** (Matrix's choice) | best terminal, best 3D, system polish | macOS only; 259 `Hub*` symbols with no shared schema in evidence (hand-written Codable by every available indicator — see M27); slower iteration |
| **Tauri + React** | one codebase, generated types, fast iteration, web-capable | terminal is xterm.js; 3D is R3F; less system integration |
| Electron | ubiquitous | heavy, and this app already ships a browser |

**Proposal: Tauri + React**, with generated types. Native Swift remains an option if reference fidelity and OS integration outweigh portability.

Cross-platform delivery and iteration speed need prototypes and measurements. There is no evidence for the earlier “3x faster” claim.

Revisit if the terminal or the floor becomes the differentiator.

---

## D3 · Schema-first

**Matrix:** separate daemon contracts and native Hub symbols; no codegen marker in the binary, function-local `Ack` DTOs and a hand-written `HubChannelValue.init(from:)` — hand-authored on both sides.
**Us:** one zod schema → daemon validators + client types + docs.

Non-negotiable. This is the single clearest lesson from reading their client.

---

## D4 · Work Items as Markdown packets

**Matrix:** Markdown + YAML frontmatter under `tasks/`.
**Us:** same.

Rationale: readable, diffable projections. Canonical records remain in a daemon-owned store; repair uses validated recovery tooling. Do not bypass state guards by editing exported packets when an MCP call fails.

---

## D5 · Tool-owned state must be unwritable by file tools

**Matrix:** tool-specific path/authority checks plus prompt rules, without a proven universal process write boundary.
**Us:** require an enforced daemon-state/agent-workdir boundary, covering shells and workers. `deniedWrites` is not a supported field found in the inspected SDK and is not an implementation. See [contracts](10-implementation-contracts.md).

---

## D6 · The Critic is structural, not advisory

**Matrix:** conditional verifier text remains in the bundle, but `verificationNudgeNeeded` has exactly two producers in `neo-intelligence.fmt.js` (TodoWrite `:337411`, TaskUpdate `:396757`) and both assign a literal `false`; there is no other write site. The "3+ tasks" verifier is dead code in this build **[V]**.
**Us:** assigned quality reviewer by stable ID and daemon-authenticated actor, followed by separate human final acceptance of the exact reviewed revision.

Rationale: in creative work the temptation to self-accept is stronger, because quality is
subjective. Matrix's own line — *"You cannot self-assign PARTIAL by listing caveats in your
summary — only the verifier issues a verdict"* — should be an invariant, not a nudge.

---

## D7 · Style locks as a first-class entity

**Matrix:** no equivalent (character assets are the closest).
**Us:** typed records, authored by a review, applied by generations, visible in the UI and
in-world.

This is the studio's version of "learning changes future behavior". Without it, the director
repeats themselves and the product feels stupid on day three.

---

## D8 · Variants, not revisions

**Matrix:** files have revisions.
**Us:** deliverables have **variants** (v1..vN) with a chosen one, *plus* revisions on each.

Choosing between alternatives is the creative act. Modelling it as version history destroys the
comparison affordance.

---

## D9 · Buy the 3D renderer

**Matrix:** custom Metal renderer, custom VRM parser, OSM city — 264 `Office*` types, 32 shader entry-point names.
**Us:** React Three Fiber + three-vrm, one stylised room.

We keep what is actually the product: entity mapping, behaviour state machine, signature gate,
live content as texture, overlay projection. We skip what is commodity.

---

## D10 · Drop revenue, marketplace, and extra channels

Payments, payouts, disputes, the Agent Space store, WeChat and Telegram bridges: out of scope.

**But build the role-template package format immediately** — duplication, sharing and versioning
of seats are day-one needs even without a store.

---

## D11 · Autonomy default

**Matrix:** `proactive` is off by default; primary gets all three lanes, others post-turn only.
**Us:** respect the master autonomy switch for every role. A user-authorized submission may enqueue one bounded review as continuation of that work; do not implement an always-on Critic nudge that bypasses pause or recursively reviews its own reviews.

---

## D12 · Model routing

**Matrix:** host-managed provider selection via env; agents pick a *runtime*, never a model.
**Us:** same, with a cleaner `ProviderAdapter` interface instead of the env-var matrix.

Keep the routing argument verbatim: default native; escalate only when you can **name a concrete
benefit for this specific task**; refuse category-based routing.

---

## D13 · Credentials in Keychain

**Matrix:** multiple stores and write paths; per-file permissions and encryption differ. WeChat state is JSON and media encryption is a separate mechanism.
**Us:** OS keychain, with the JSON path as an explicit fallback for headless use.

---

## D14 · Imported knowledge is untrusted

**Matrix:** imported departments ship welcome memory cards that load into prompts; SHA-256 on the
handoff document is recorded as provenance only. Import validation is **structural only [V]**
(path shape, counts, sizes, duplicate/kind conflicts — M15 §Import validation): no frontmatter,
`allowed-tools`, signature or injection check exists on either side.
**Us:** any skill or memory arriving from outside the machine gets a **diff review and explicit
acceptance** before it can enter a prompt.

---

## D15 · What we keep verbatim

Because it is already right:

- the three-plane separation (topology / knowledge / execution)
- `dispatch | note | reply(+outcome)` and its CHECK constraints
- the ordered next-step reason list, shared between board and autonomy
- the static-prefix / volatile-tail split and the five hot keys
- wake reasons, coalescing, per-host mutex, lane policy, backoff, activity gate
- placeholders-are-blockers
- the learning decision enum
- crystallize: demotion over deletion, 90-day decay test, planned-orphan grace,
  "no changes needed is a valid outcome"
- host-side provenance capture
- two-phase trash and four-phase upload
- disable the unconstrained built-in, ship a constrained MCP replacement
- `next` hints on every tool result
- the Receivable description voice
- "brief the agent like a smart colleague who just walked into the room"
- don't peek / don't race on background workers
- persona for display, never for prompt

---

## Open questions

1. **How many seats before it gets noisy?** Matrix's live install had 12 departments and a
   dashboard reporting *"0 open tasks"* — i.e. an org chart with no work in it. Cap the default
   ensemble and make the Director justify each new seat.
2. **Who owns the Brief when the client changes their mind mid-production?** Probably: a Brief
   revision is a first-class event with its own review, not an edit.
3. **How is generation budget expressed?** Per production, per milestone, or per batch? Leaning
   per milestone with a batch-level `cost_estimate` gate.
4. **Does the floor earn its cost for a solo user?** Matrix bet yes. Validate with the rail
   preview before building the full room.
