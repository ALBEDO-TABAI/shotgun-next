# D09 · Delegation Decision

## The one-line rule

> A **worker** parallelizes work that is already yours;
> a **department message** moves work that belongs to someone else.

## Primary department routing

```mermaid
flowchart TD
    START["Request that names work to do"] --> OWN{"Ownership resolved?"}
    OWN -->|unclear| LIST["department.list — settle ownership first"]
    LIST --> OWN
    OWN -->|"peer owns it"| R1

    subgraph R1["Route 1 · Dispatch"]
        D1["mcp__matrix__department message.send"]
        D2["include: task · owner · context refs ·<br/>expected output · proof expectation · stop condition"]
        D3["you remain the user's single point of contact"]
        D1 --> D2 --> D3
    end

    OWN -->|"genuinely yours"| R2
    subgraph R2["Route 2 · Handle it"]
        H1["intake · cross-dept synthesis · triage ·<br/>direction-setting · user-facing continuity"]
        H2["optionally: Agent worker for speed/isolation/parallel slices"]
        H1 --> H2
    end

    OWN -->|"no owner exists"| R3
    subgraph R3["Route 3 · Create the owner"]
        C1["department.create — one clear signal is enough"]
        C2["send first brief"]
        C3["tell the user about the new lane"]
        C4["write routing-*.md memory card"]
        C5["dispatch the slice"]
        C1 --> C2 --> C3 --> C4 --> C5
    end

    R3 -.->|"❌ worst outcome"| BAD["create owners, then do their work<br/>with your own workers →<br/>empty shells, company map is a lie"]
```

## Non-primary department

```mermaid
flowchart TD
    W["Owned work arrives"] --> Q1{"Can the lead finish it directly?"}
    Q1 -->|yes| SELF["do it — default posture"]
    Q1 -->|"real leverage available"| Q2{"what kind?"}
    Q2 -->|"parallel slices"| PAR["N workers, independent proof slices"]
    Q2 -->|"isolation needed"| ISO["worker with isolation"]
    Q2 -->|"specialist judgment"| SPEC["worker with a specialist runtime"]
    Q2 -->|"correctness critical"| ADV["adversarial pattern:<br/>independent attempts to compare ·<br/>builder + skeptic ·<br/>parallel reviewers cross-checking"]
    ADV --> SYN["lead synthesizes the disagreement"]
    W --> Q3{"crosses domains / conflicts with a peer /<br/>lacks authority / needs a workspace ruling?"}
    Q3 -->|yes| ESC["message.send → primary"]
    Q3 -->|no| Q1
```

## Runtime escalation test

```mermaid
flowchart TD
    A["Need a worker"] --> B["Default: Neo — omit `runtime`"]
    B --> C{"Can you NAME a concrete benefit<br/>from an external specialist<br/>for THIS task?"}
    C -->|no| B
    C -->|yes| D{"which?"}
    D -->|"Claude-family strengths:<br/>design taste from mockups,<br/>open-ended product/narrative shaping"| E["runtime: claude_code"]
    D -->|"GPT-family execution:<br/>large terminal-heavy refactor/migration"| F["runtime: codex"]
    E & F --> G{"self-contained enough to<br/>leave Matrix context behind?"}
    G -->|no| B
    G -->|yes| H["escalate — one slice only;<br/>ownership, threading, synthesis stay on Neo"]
    M["@neo / @codex / @claude_code mention"] -.->|"hard assignment"| H
    NOTE["❌ do NOT route by task category<br/>Neo handles coding, design and research fine"]
```

## Worker context modes

```mermaid
flowchart LR
    T["context: task (default)<br/>prompt only"] --> U1["most work · polling · nudges ·<br/>media checks · follow-ups"]
    R["context: recent<br/>prompt + recent excerpt"] --> U2["needs nearby state,<br/>not full parent context"]
    F["context: fork — Neo only<br/>parent turn/context"] --> U3["parallel workers in one parent turn<br/>sharing a hot prefix"]
    NOTE2["Codex / Claude Code: no fork"]
```
