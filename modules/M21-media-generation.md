# M21 · Media Generation

**Source modules:** `media_mcp`, `client2`, `character_assets`, `image_processing`, `store7`,
`media-generation` managed skill (155 lines) + reference (181 lines)

---

## Purpose

First-class image, video and audio generation with consistent characters, workspace-native
output paths, and async completion through hooks.

## Why it is a tool, not a curl call

> "Use this instead of Bash/curl; it handles auth, hook creation, output paths, and artifact
> metadata."

Four things the tool does that an agent would get wrong: credential handling, hook registration
for async completion, department-relative output paths, and artifact metadata for provenance.

## Tools (7)

| Tool | Purpose |
|---|---|
| `character_asset_register` | register a reusable person/character so `@name` stays consistent |
| `character_asset_list` | list registered characters (call when the user writes `@name`) |
| `image_generate` | text → image |
| `image_edit` | restyle / remove / recolor / cleanup / masked edit |
| `video_create` | text/frame/reference → video |
| `audio_generate` | music, speech, voice cloning, ambience, Foley, SFX |
| `video_status` | poll / download a video task |

Full schemas in [tools/T05](../tools/T05-mcp-media.md).

## Output convention

```
outputPath: absolute path, OR a filename relative to
            departments/<id>/artifacts/media-generation/
            (omit for a generated path)
```

Generated media lands inside the owning department's artifacts, so it is automatically
provenance-tracked, visible in Files, and usable as a proof ref.

## Sizing philosophy

```
size: "Prefer aspect/tier tokens such as 16:9, 16:9@2K, 1:1, or 9:16.
       Omit for default 16:9 4K. Avoid arbitrary pixels like 1920x1080."
```

Aspect tokens instead of pixel dimensions — fewer invalid combinations, better defaults, and it
matches how creatives actually talk.

## Masking without temp files

`image_edit` takes a **normalized selection rectangle** (`x,y,width,height` in 0..1) and the
media client synthesizes the provider mask **in memory**:

> "Do not create intermediate mask files in the workspace; use selection for rectangular
> annotations."

This connects directly to the UI's visual annotation feature
(`ComposerVisualAnnotationTarget`) — you draw a box on an image in chat and it becomes an edit
region. Excellent design; copy it.

## Video modes (mutually exclusive)

```
1. prompt only
2. one first_frame
3. first_frame + last_frame
4. reference_image | reference_video | character_asset  (+ optional reference_audio)
```

Constraints enforced in the description: never mix first/last frames with reference mode;
`reference_audio` can never be the only reference; for editing an existing video use
`reference_video` with `aspectRatio: "adaptive"` and describe changes **semantically** because
selection rectangles are agent context, not provider masks.

Defaults: `durationSec` 15 (or `-1` for model-selected, else 4–15), `aspectRatio` 16:9,
`resolution` 1080p, `audio` true.

## Audio

Seed Audio 1.0. Up to **3** reference clips total across `audioUrls` + `audioReferences`,
referenced in the prompt as `@Audio1..@Audio3`. `voice` (preset) and cloning are mutually
exclusive. Image references drive ambience/Foley/mood and cannot combine with audio references.
`outputFormat` wav|mp3|pcm|ogg_opus (default mp3), `sampleRate` 8k–48k (default 24000),
`speed`/`volume` 0.5–2, `pitch` −12..+12.

## Character assets

```
character_asset_register { name:"小海", imagePath|imageUrl|assetUri, description?, thumbnailPath? }
→ user can then write @小海 in a video request
```

Backed by BytePlus `asset://` URIs (Seedance). `character_asset_list` is called whenever the
user mentions an `@name`. UI: `Character*` types, `OfficeVRM` avatars reuse the same idea in 3D.

## Async + hooks

Both `image_*` and `video_create` take `workRun` and `async` schemas **[V]**
(`neo-agent.fmt.js:128662`):

```ts
workRun?: { id: string,            // REQUIRED — not `taskId`
            title?: string, itemId?: string, totalItems?: number }

async?:   { mode?: "async" | "sync",   // "Default async: create a Matrix hook and return immediately."
            timeoutSec?: number, pollIntervalSec?: number }
```

Note `async` is an **object**, not a boolean, and `workRun.id` is required with no
`keyResultId` field. In async mode the tool returns immediately with a task id, registers a
hook, and the completion arrives as a wake with `resultRefs` — which the agent then files as
proof. See [M12](M12-hooks-workruns.md).

## Reuse in shotgun-next

**This is the core toolset for a creative studio** — promote it from a peripheral capability to
the centre.

Copy as-is: output path convention, aspect tokens, in-memory selection masks, mutually exclusive
video modes, character assets, async-by-default with hooks.

Add for a studio:
- **variant sets** — `n` generations grouped as v1..vN of one deliverable, with a chosen variant
- **style locks** — a named reference bundle applied to every generation in a production
- **cost preview** — estimated spend before a batch runs
