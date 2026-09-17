# M25 · Marketplace (Agent Space)

**Source modules:** `acquisition_handover`, `acquisition_handover2`, `department_import_welcome`,
`marketplace_integration_routes`, `onboarding`, `manager`, plus 88 top-level `AgentSpace*` Swift names

---

## Purpose

Package, sell, buy and install departments — and whole companies.

## Two package kinds

| Kind | Effect | Opening wake |
|---|---|---|
| `department` | adds one owner to an existing workspace | `department_import_welcome` |
| `workspace` | you take over a running company | `acquisition_handover` |

Sources: `marketplace` or `zip_import`.

## Import payload

From a live `marketplaceDepartmentImports` entry:

```ts
{ id, source:"marketplace", packageKind:"department",
  listingSlug, listingTitle, tagline, summary, descriptionMarkdown, releaseNotesMarkdown,
  releaseId, preparedAt, importedAt,
  targetWorkspaceId/Title, targetDepartmentId/Name,
  primaryDepartmentId/Name, sourceWorkspaceId, sourceDepartmentId/Name,
  departmentHandoffDocumentPath, departmentHandoffGeneratedAt, departmentHandoffSha256,
  handoffDocumentPath, departmentManualDocumentPath,
  integrationReferences: [{provider:"composio", slug, name, scope, requirementKind:"optional"|"required"}],
  departmentWelcomeSkillRefs:  [{title, path}],
  departmentWelcomeMemoryRefs: [{title, path}],
  departmentManualSummary: { type:"department_manual_summary", departmentName, title, subtitle,
                             manualDocumentPath, manualDocumentTitle,
                             sections:[{id:"capabilities"|"use_cases"|"what_it_brings"|"boundaries",
                                        title, summary, details:[…]}] },
  acquiringUserLocale, acquiringUserPreferredLanguages }
```

Note what ships with a department: **skills, memory cards, an integration manifest, a manual, and
a handoff letter with a SHA-256.** A department is a portable operating unit, not a config blob.

## Manual summary — the "department letter"

Four fixed sections, rendered as a card in the UI and injected into the primary's prompt:

| id | Localised title |
|---|---|
| `capabilities` | 这个部门能做什么 / What this department can do |
| `use_cases` | 什么时候适合叫它 / When to call it |
| `what_it_brings` | 它带来了什么 / What it brings |
| `boundaries` | 使用边界 / Usage boundaries |

## Containment rules

The import context injected into the prompt is explicit that an import must not hijack direction:

> "Treat this as a newly registered capability available to route or coordinate when the user's
> ask matches it." (primary's role guidance)

> "Treat the Marketplace listing as the imported department's capability description, not as the
> Workspace's new purpose, target, or strategic direction. … Preserve existing OKRs, scheduled
> work, and Workspace direction unless the user explicitly asks to change them."

For a company handover instead:

> "Treat the user as the new owner taking over a running company, not as someone starting from a
> blank workspace. … Use Workspace as the whole company, departments as operating units with
> ownership boundaries, and <primary> as the primary entrypoint that coordinates the company map,
> OKRs, scheduled work, and first-day operating priorities."

## Publish flow

`AgentSpace*` types cover: catalog sections/cards, detail sheets with cover images,
**evidence** (links, images, attachments — each with Draft/DTO/Upload variants),
`AgentSpaceCompositionMetrics` (skills vs memory vs tasks composition), checkout sessions,
downloads, and `CompletePublishRequest/Response`.

Endpoints on the Swift side; the daemon handles preparation:
`HubPrepareMarketplaceDepartmentHandoffResponse`, `HubPrepareAcquisitionHandoverResponse`.

## Skill marketplace

A parallel, lighter-weight catalogue for individual skills
(`SkillMarketplaceView`, `SkillMarketplaceImportController`, `SkillMarketplaceGrouping`).

## Security note

Imported **memory cards** are injected into a department's knowledge. That is a prompt-injection
supply chain. A handoff SHA-256 alone does not establish validation of every imported file. Native importer bodies were not recovered, so absence of content verification cannot be concluded from this dossier.

**For shotgun-next:** if you ship this, show a diff of every imported skill and memory card and
require explicit acceptance before the first prompt build includes them.

## Reuse in shotgun-next

Defer the marketplace, but **build the package format now**: a role (department) that exports as
`{config, profile, skills/, memory/, integration manifest, manual}` is exactly what you need for
templates, team sharing, and duplication across productions — which you want on day one even
without a store.
