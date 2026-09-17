# T05 · `mcp__media__*`

**Server:** `media` · **7 tools** · **Surface:**
`mcp__media__character_asset_register+character_asset_list+image_generate+image_edit+audio_generate+video_create+video_status:always-load@1`

The generation toolset. For a creative studio this is the centre of gravity.

---

## 1 · `character_asset_register`

> Register a reusable real-person or character asset for Seedance. Use before `video_create` when
> a named `@person` should stay consistent across videos.

```ts
{ name: string          // "Human-readable handle, e.g. 小海. Users can reference it as @小海."
  imagePath?: string    // absolute local face/character image
  imageUrl?: string     // public URL
  assetUri?: string     // existing BytePlus asset:// URI to persist in Matrix
  description?: string
  thumbnailPath?: string }
```

## 2 · `character_asset_list`

> List reusable Matrix character assets. Use when the user mentions `@name` in a video request.

No arguments. The description doubles as the trigger condition — that is why the agent calls it
at the right time without being told.

## 3 · `image_generate`

> Generate an image through Matrix media generation. **Use this instead of Bash/curl**; it handles
> auth, hook creation, output paths, and artifact metadata.

```ts
{ prompt: string
  outputPath?: string
      // "Absolute path, or filename relative to this department's
      //  artifacts/media-generation directory. Omit for a generated path."
  size?: string
      // "Prefer aspect/tier tokens such as 16:9, 16:9@2K, 1:1, or 9:16.
      //  Omit for default 16:9 4K. Avoid arbitrary pixels like 1920x1080."
  quality?: "low"|"medium"|"high"        // default high
  n?: int 1..10
  background?: string
  workRun?: WorkRun                      // execution grouping; not an OKR task link
  async?: Async }                        // async mode → returns immediately, completes via hook
```

## 4 · `image_edit`

> Edit an existing image through Matrix media generation. Use for restyle, remove, recolor,
> cleanup, or masked edits.

```ts
{ prompt: string
  imagePath: string
  maskPath?: string
      // "Optional user-supplied mask. Do not create intermediate mask files in the workspace;
      //  use selection for rectangular annotations."
  selection?: { x: 0..1, y: 0..1, width: (0,1], height: (0,1] }
      // "Normalized rectangular edit region from an image annotation. The media client creates
      //  the provider mask IN MEMORY, so no workspace mask file is needed."
  size?: string
      // "Omit to preserve the source image aspect ratio automatically; pass an aspect/tier token
      //  only when the user explicitly requests a different canvas."
  outputPath?, workRun?, async? }
```

The normalized `selection` rectangle is the bridge to the UI's visual annotation feature — the
user draws a box on an image in chat and it becomes an edit region, with no temp files anywhere.
**Copy this exactly.**

## 5 · `video_create`

> Create or edit a video through Matrix media generation. Choose one mode: prompt-only; one
> `first_frame`; `first_frame` plus `last_frame`; or
> `reference_image`/`reference_video`/`character_asset` with optional `reference_audio`. Use
> `reference_video` for an original video being edited, set `aspectRatio` to `adaptive`, and
> describe changes **semantically** because selection rectangles are Agent context rather than
> Seedance masks. Never mix first/last frames with reference mode, and never send
> `reference_audio` alone. Use character assets for real or photoreal people.

```ts
{ prompt?: string
  outputPath?: string
  references?: Array<{ role: "first_frame"|"last_frame"|"reference_image"
                             |"reference_video"|"reference_audio"|"character_asset",
                       source: { type: "path"|"url"|"asset_uri", value: string } }>
      // "Native JSON array; do not stringify it."
      // example: [{"role":"reference_video","source":{"type":"path","value":"/abs/source.mp4"}}]
  characterAssets?: Array<{ name?: string, assetUri?: string }>
      // "Native JSON array; do not stringify it."
      // selects reference mode; cannot combine with first_frame / last_frame
  durationSec?: -1 | int 4..15          // default 15; -1 = model-selected
  aspectRatio?: "16:9"|"9:16"|"1:1"|"adaptive"   // default 16:9
  resolution?: "480p"|"720p"|"1080p"             // default 1080p
  audio?: boolean                                 // default true
  workRun?, async? }
```

Mode matrix:

| Mode | References |
|---|---|
| prompt-only | none |
| single frame | one `first_frame` |
| frame pair | `first_frame` + `last_frame` |
| reference | `reference_image` \| `reference_video` \| `character_asset` (+ optional `reference_audio`) |

Never: mix frames with reference mode; send `reference_audio` alone.

## 6 · `audio_generate`

> Generate standalone audio through Matrix media generation using Seed Audio 1.0. Supports music,
> speech, voice cloning from `@Audio` references, ambience, Foley, sound effects, preset voices,
> image-guided ambience, `output_format`, `sample_rate`, `speed`, `volume`, and `pitch`.

```ts
{ prompt: string
  outputPath?: string
  voice?: string                 // Seed Audio preset voice; omit when cloning
  audioUrls?: string[]           // ≤3 public URLs
  audioReferences?: FileSource[] // ≤3 local paths or URLs; staged through Matrix uploads
      // combined limit is 3 clips; reference them in the prompt as @Audio1, @Audio2, @Audio3
      // omit `voice` when cloning a speaker
  imageUrl?: string              // ambience/Foley/mood/environment; backend field image_url
  imageSource?: FileSource       // local or URL variant
      // NOT for voice cloning or speech; cannot combine with audio references
  outputFormat?: "wav"|"mp3"|"pcm"|"ogg_opus"     // default mp3
  sampleRate?: 8000|16000|24000|32000|44100|48000 // default 24000
  speed?: 0.5..2    // default 1
  volume?: 0.5..2   // default 1
  pitch?: int -12..12 // default 0
  workRun?, async? }
```

The `@Audio1..@Audio3` prompt-reference convention is a neat solution to "which of these clips do
you mean" without inventing a nested schema.

## 7 · `video_status`

> Check or download a Matrix media video task. Use `taskId` from `video_create`; `generationId`
> is optional recovery metadata.

```ts
{ taskId: string, generationId?: string, outputPath?: string, download?: boolean /*default true*/ }
```

---

## Shared Input Contracts

The shipped Zod definitions at `neo-agent.fmt.js:128662` are:

```ts
type WorkRun = { id: string; title?: string; itemId?: string; totalItems?: number };
// id is nonempty; totalItems is a positive integer.
type Async = { mode?: "async" | "sync"; timeoutSec?: number; pollIntervalSec?: number };
// Positive integer time values. Default mode is async. async:true is INVALID.
type FileSource = { type: "path" | "url"; value: string };
// `videoReferenceSchema.source` is the wider `mediaSourceSchema`: type: "path" | "url" | "asset_uri"
// (asset_uri points at a registered character asset). audioReferences / imageSource use the
// two-value FileSource above. See ERRATA E3.
```

`workRun.id` groups an execution; `itemId` is an item within that grouping. Neither is an automatic durable OKR `taskId` or `keyResultId` link. Media provider task IDs, hook IDs and OKR Task IDs must be tracked separately. See [exact expressions](../_analysis/audit/mcp-reference.md) for validators and handler locations.

## Cross-cutting patterns

| Pattern | Why it matters |
|---|---|
| "Use this instead of Bash/curl" | states *why*: auth, hooks, paths, artifact metadata |
| Output relative to `artifacts/media-generation/` | automatic provenance + proof-ref usability |
| Aspect tokens, not pixels | fewer invalid combos, matches how creatives talk |
| In-memory masks from normalized selections | no temp files, direct UI bridge |
| Mutually exclusive modes stated in prose | a design can encode them using unions/refinements; inspect client normalization in addition to the published schema |
| "Native JSON array; do not stringify it" | pre-empts a very common model error |
| `workRun` + `async` on every long op | everything becomes a hook, nothing blocks a turn |
| Defaults stated in every description | the model stops inventing values |

## shotgun-next mapping

Promote to the core toolset and add:

```
image_generate / image_edit / video_create / audio_generate / video_status   (as-is)
character_asset_register / list                                              (as-is)
+ variant_set_create      group n generations as v1..vN of one deliverable
+ variant_select          mark the chosen variant; others stay as history
+ style_lock_apply        apply a named reference bundle to a generation
+ cost_estimate           predicted spend for a batch, before it runs
```

`style_lock_apply` is the studio's answer to consistency: a named bundle of references, palette,
lens/lighting notes and negative prompts that every generation in a production inherits — the
same idea as `character_asset` generalised from a person to a look.
