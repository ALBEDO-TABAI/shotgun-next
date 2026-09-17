# D11 · Office Scene Synchronization

## App state → 3D scene

```mermaid
flowchart TB
    subgraph events["Daemon events"]
        E1["department.status / activity"]
        E2["task.tool.start / update / end"]
        E3["chat.delta"]
        E4["hook.work.changed (progress)"]
        E5["workers list / runtime state"]
        E6["department message delivery"]
    end

    subgraph model["OfficeSceneModel"]
        SIG["OfficeSceneUpdateSignature"]
        WS["OfficeWorkerSceneState<br/>+ SceneAction / ResolvedWorkerActionKind"]
        NAV["OfficeWorkerNavigation<br/>waypoints · travel mode · seat mode"]
        ANC["OfficeWorkerAnchor → ResolvedAnchor"]
        CONV["OfficeWorkerConversation / BoardroomMeetingState"]
        MIND["AgentMindService<br/>mood · energy · traits (display only)"]
    end

    subgraph gate["Signature gate"]
        G1["scene signature changed?"]
        G2["worker screen texture signature?"]
        G3["presentation panel signature?"]
        G4["department sign cache key?"]
        G5["vacant workstation cache key?"]
    end

    subgraph render["OfficeMetalRenderer"]
        P1["pipeline bundles: mesh · VRM · primitive · depth · sampler"]
        P2["passes present (order constrained by texture flow, see below):<br/>shadow · opaque/mesh · VRM · SSAO ·<br/>TAA · bloom · blur · exposure ·<br/>reflection resolve · composite"]
        P3["MetalFX upscale (disabled · temporal · spatialFallback)<br/>dynamic resolution · adaptive load level"]
        CACHE["signature-keyed caches"]
        LOOP["demand-driven render loop:<br/>wake singleFrame / continuous(duration) · idlePause"]
    end

    subgraph overlay["SwiftUI overlays"]
        O1["OfficeProjectedPoint / OverlayProjection"]
        O2["InteractionPrompt · DetailOverlay"]
        O3["DepartmentArtifactsSpatialOverlay"]
    end

    events --> model --> gate
    gate -->|unchanged| NOOP["skip placement / texture rebuild<br/>(loop idle-pauses unless camera/animation<br/>request a continuous wake)"]
    gate -->|changed| render --> overlay
    MIND -.->|"idle behaviour, reactions"| WS
```

## Entity mapping

```mermaid
flowchart LR
    D["Department"] --> R["room · carpet material · corner sign · folder cluster"]
    W["Worker / running session"] --> A["VRM character at an allocated workstation"]
    O["Worker output"] --> S["live texture on its monitor"]
    AR["Department artifact"] --> F["folder object (folder-single.glb)"]
    SK["Skill"] --> B["book on skill-shelf.glb"]
    MSG["Department message"] --> FL["flight pulse between rooms"]
    LV["Live session / voice"] --> HUD["HUD · participant rows · visitor banner"]
    OBJ["Objective / dashboard"] --> PP["presentation panel in the boardroom"]
```

## Render passes — **[I] order constrained, not read**

The shader entry points below are **verified** present in `default.metallib`. Their *sequence*
was never read from the renderer's draw code; but the fourth pass recovered the renderer's
stored-property metadata (`docs/08` §2.1), which fixes the **texture data-flow**:
`shadowDepthTexture` → geometry (`sceneColor/Depth/Normal/Velocity`) → `aoTexture` →
`aoBlurTexture` → composite → `taaHistory/taaResolved` → `bloomTextureA…D` → `exposureTexture` →
MetalFX (`reactiveMaskTexture`, `metalFXUpscaledTexture`) → drawable. The arrows therefore mean
"this stage consumes the previous one's output"; only bloom-vs-TAA placement and the exposure
sample point remain open. The dotted `V1 → … → CO` chain is that dependency chain.

```mermaid
flowchart LR
    V1["office_mesh_shadow_vertex<br/>office_vrm_shadow_vertex<br/>office_shadow_vertex"]
    OP["office_mesh_fragment · office_vrm_vertex<br/>city_terrain_* · farm_grass_*"]
    AO["office_ssao_fragment"]
    TA["office_taa_fragment<br/>office_reactive_mask_kernel"]
    BL["office_bloom_extract_* · office_blur_*"]
    EX["office_exposure_kernel"]
    RF["office_reflection_resolve_kernel"]
    CO["office_composite_fragment"]
    BG["office_environment_background_fragment<br/>office_baked_sky_fragment"]
    V1 -.- OP -.- AO -.- TA -.- BL -.- EX -.- RF -.- CO
    BG -.- CO
```


## Adaptive degradation

```mermaid
flowchart TD
    M["frame timings + OfficeMetalRendererGPUPressure"] --> E["RuntimePressureEvaluation"]
    E --> Q{"pressure"}
    Q -->|low| F["full quality tier · full city · MetalFX off/spatial"]
    Q -->|medium| G["reduce adaptiveLoadLevel<br/>fewer city buildings/trees<br/>MetalFX temporal"]
    Q -->|high| H["static environment cache only<br/>drop marine traffic, grass instancing<br/>lower sky quality"]
    F & G & H --> R["rebuild only the affected signature-keyed caches"]
```
