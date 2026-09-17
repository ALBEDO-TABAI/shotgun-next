# D15 · shotgun-next Target

## System

```mermaid
flowchart TB
    U(("Director<br/>(you)"))
    subgraph client["shotgun-next · Tauri + React"]
        RAIL["Rail<br/>Needs your eye · Roles · Modules · Floor preview"]
        S1["Chat"]; S2["Review queue"]; S3["Board"]; S4["Library"]
        S5["Memory &amp; Skills"]; S6["Studio floor"]; S7["Settings"]
        SC["StudioClient · generated types"]
        RAIL --- S1 & S2 & S3 & S4 & S5 & S6 & S7 --- SC
    end
    U --> client
    SC <==>|"ws · loopback"| API
    subgraph d["studiod"]
        API["API · schema-generated"]
        ST["Brief · Milestone · Work Item · Review<br/>Role registry · Message bus · Library ledger<br/>Memory · Skills · Board projection"]
        OR["Session manager · Prompt assembly<br/>Wake engine · Lanes · Schedule · Hooks · Maintenance"]
        SV["Model gateway · Generation · Integrations · Browser"]
        API --> ST & OR & SV
    end
    subgraph roles["Role sessions"]
        D["Director"]; RS["Researcher"]; ST2["Strategist"]; W["Writer"]
        AD["Art Director"]; P["Producer"]; C["Critic"]
    end
    OR ==> roles
    subgraph tools["MCP"]
        T1["studio · role"]; T2["studio · state"]; T3["studio · schedule"]
        T4["studio · provenance"]; T5["studio · generate"]; T6["studio · browser"]
        T7["provider packs<br/>Figma · Drive · Notion · Frame.io"]
    end
    roles === tools
    FS["~/.shotgun/productions/&lt;id&gt;/"]
    d === FS
    roles === FS
```

## The studio loop

```mermaid
flowchart LR
    B["<b>Brief</b><br/>audience · message · success signal"]
    M["<b>Milestone</b><br/>doneState"]
    I["<b>Work Item</b><br/>owned by one seat"]
    A["<b>Acceptance</b><br/>the gate"]
    DV["<b>Deliverable</b><br/>v1..vN"]
    R["<b>Review</b><br/>Critic verdict"]
    L["<b>Learning</b><br/>style lock · taste card · skill edit"]
    B --> M --> I --> A --> DV --> R
    R -->|milestoneDecision| M
    R -->|learningDecision| L
    L -.->|"constrains future generations"| DV
    R -->|"needs your eye"| YOU(("You"))
    YOU -->|"verdict + note"| L
```

## Role routing

```mermaid
flowchart TD
    REQ["Director receives a request"] --> Q{"which seat's craft?"}
    Q -->|"Researcher"| R1["references · scans · facts · rights"]
    Q -->|"Strategist"| R2["positioning · audience · the one line"]
    Q -->|"Writer"| R3["scripts · copy · names"]
    Q -->|"Art Director"| R4["look · palette · style locks"]
    Q -->|"Producer"| R5["schedule · assets · publish package"]
    Q -->|"Critic"| R6["verdict · required fixes"]
    Q -->|"no seat fits"| NEW["role.create → brief → routing memory → dispatch"]
    Q -->|"intake / synthesis / continuity"| SELF["Director handles it"]
    R1 & R2 & R3 & R4 & R5 --> DEL["delivery + outcome"]
    DEL --> R6
    R6 -->|"accept"| WALL["review wall → your eye"]
    R6 -->|"revise"| BACK["back to the maker with required fixes"]
```

## Taste becomes state

```mermaid
sequenceDiagram
    participant Y as You
    participant C as Critic
    participant G as generate
    participant AD as Art Director
    Y->>C: "direction 2, but warmer and less symmetrical"
    C->>C: item.review verdict=revise<br/>requiredFixes + learningDecision="style-lock"
    C->>G: style_lock_create {name, palette, grade,<br/>positive/negativePrompt, refs, authoredIn: reviewId}
    G-->>C: lockId
    C->>AD: message.send assignment (lock attached)
    AD->>G: image {prompt, styleLockIds:[lockId], n:4}
    G-->>AD: variant set — each variant records the applied lock
    Note over Y,AD: your one sentence now constrains every future generation
```

## Phased build

```mermaid
flowchart LR
    P0["<b>0 · Schema</b><br/>5 engineer-days<br/>one source of truth"]
    P1["<b>1 · Daemon + state</b><br/>22 engineer-days<br/>no LLM required"]
    P2["<b>2 · Sessions + tools</b><br/>22 engineer-days<br/>ownership model holds"]
    P3["<b>3 · Autonomy + generation + client</b><br/>28 engineer-days<br/>the product"]
    P4["<b>4 · Depth</b><br/>56–61 engineer-days<br/>maintenance · board · integrations · floor (36–41)"]
    P5["<b>5 · Polish</b><br/>ongoing"]
    P0 --> P1 --> P2 --> P3 --> P4 --> P5
```

Figures are the provisional engineer-day rows from [shotgun/08](../shotgun/08-build-plan.md)
(133–138 total before polish and contingency), not calendar weeks; the earlier "15 weeks" total
was inconsistent with the floor's own breakdown and has been withdrawn.
