# Bricks + Codex MCP Project Rules

This is the default operating policy for one site-specific WordPress / Bricks Codex project.

It is loaded before the first project task. The bootstrap audit must refine the PROJECT PROFILE and site-specific routing below with verified facts, while preserving the general safety, verification, ownership, and workflow rules unless the user explicitly changes them.

## Project profile

Until verified by the bootstrap audit, use these states:

- Site name: UNKNOWN
- Site URL: UNKNOWN
- Allowed MCP server: UNKNOWN
- Bootstrap status: NOT RUN
- Site maturity: UNKNOWN
- Design-system state: UNKNOWN
- Design-system authority: UNKNOWN
- WooCommerce status: UNKNOWN
- Primary data/content providers: UNKNOWN
- Primary CSS/design-system provider: UNKNOWN

Do not guess these values. Populate them from live evidence.

## Project isolation

- This project belongs to exactly one WordPress / Bricks site.
- After the MCP server is verified, use only that site's MCP server unless the user explicitly requests cross-site work.
- Never carry site-specific classes, variables, templates, plugin assumptions, visual rules, or cached documentation from another project into this one.
- If several WordPress MCP servers are configured and the correct target is ambiguous, stop before any site write.

## Sources of truth

- **Live Bricks MCP state** is authoritative for current Bricks structure and configuration.
- **Live WordPress/plugin state** is authoritative for current integration, data-model, and provider architecture.
- **Rendered frontend in the browser** is authoritative for actual visual appearance and responsive behavior.
- **Local files under `docs/bricks/`** are durable cached references, not guaranteed-current runtime state.

If local documentation disagrees with accessible live state, follow the relevant live source and update stale documentation after a verified change. Never silently rewrite documentation from assumptions.

## Bricks workflow

- Use Bricks MCP abilities for inspecting or modifying Bricks-managed site resources.
- Read only the task-relevant Bricks skill(s); do not load the entire skill catalog without need.
- Use the current MCP ability schema as the operation contract.
- Inspect the existing target resource and relevant design/data dependencies before proposing changes.
- Reuse existing global classes, variables, components, queries, fields, templates, and naming conventions wherever appropriate.
- Do not create duplicate classes, variables, tokens, fields, CPTs, taxonomies, relationships, or queries when a suitable existing resource already exists.
- Prefer Bricks-native controls and structures when the site is Bricks-native, but respect external framework/provider ownership where present.
- Prefer the smallest scoped change that satisfies the request.

## Bricks-native authoring standard

For page, template, and component authoring, use this priority order:

1. correct native Bricks element;
2. native Bricks control;
3. existing global class / variable / component;
4. new reusable global class / variable only when justified;
5. element-local Bricks control for a truly one-off style;
6. custom selector / custom CSS only when native controls cannot cleanly express the requirement;
7. custom JS/PHP only when Bricks-native behavior is insufficient and the required code path is explicitly authorized.

### Element choice

- Interpret source content semantically; do not map a Word/Google document literally to generic containers/text nodes.
- Do not build a real list as a Div containing many Basic Text elements when List or Icon List fits the content.
- Before using generic Div/Block + repeated text for a structured pattern, check the runtime element catalog and relevant schema.
- Prefer purpose-built Bricks elements for headings, buttons, images, SVGs/icons, lists, accordions, tabs, forms, navigation, files, query-driven content, and other supported patterns.
- Use a Component when genuine structural reuse exists; do not create speculative components for one-off structures.

### Native controls before custom CSS

- Before writing custom CSS, fetch/check the target element's native controls.
- Use native controls for object-fit/object-position, aspect ratio, dimensions, spacing, grid/flex, typography, backgrounds, borders, radii, shadows, transforms, filters, responsive values, and other supported properties.
- Example: Image object-fit must use the Image element's Object fit control when that control satisfies the requirement; do not write custom CSS for it.
- If custom CSS remains necessary, record why the native controls/classes/variables were insufficient.

### CSS ID discipline

- Do not use the CSS ID field as a class/name field.
- Leave custom CSS ID empty unless a genuinely unique HTML id is required for an anchor, ARIA relation, JS/third-party integration, or another explicit unique target.
- Human-readable reusable names belong in global classes.
- Human-readable builder organization belongs in element labels/names where supported.
- BEM-like names such as service-card__title or hero-wrapper must not be placed in CSS ID merely for styling.

### Global classes and naming

- Reuse existing global classes before creating new ones.
- Follow the site's existing naming convention and external framework ownership.
- If no conflicting convention exists, prefer BEM for reusable component classes:
  - block
  - block__element
  - block--modifier
- Do not force BEM onto utility classes or provider-owned framework classes.
- Shared/repeated style → global class.
- Unique exception → element-local Bricks controls.

### Global variables and fluid layout

- Reuse existing variables/tokens before hardcoding values.
- Create a new variable only when the value is a reusable design/system concept and no suitable variable exists.
- Do not create a variable for every one-off number.
- Before adding chains of breakpoint overrides, consider a more robust native/fluid solution using clamp(), min(), max(), minmax(), repeat(), auto-fit/auto-fill, fr units, intrinsic sizing, wrapping, and existing fluid scales.
- Breakpoint overrides are appropriate when the layout mode genuinely changes, not merely to patch brittle magic values.
- When a Bricks spacing/typography scale already exists, extend/use that system instead of inventing a parallel token family.

### Media and icons

- Before uploading/recreating media or icons, inspect existing WordPress media, Bricks custom icon sets, and the site's established icon language.
- Reuse an existing SVG/icon/media asset when it is appropriate.
- For lists/features, consider native list/icon controls and existing site icons instead of manually assembling repeated text/icon markup.

### Required authoring review

For every new page, substantial page edit, or template change, perform a native-authoring review before declaring the task complete.

Check:
- missed native elements;
- custom CSS that duplicates native controls;
- class-like custom CSS IDs;
- reusable styles trapped locally;
- duplicate/near-duplicate classes;
- repeated hardcoded values that should reuse tokens;
- brittle breakpoint patch chains;
- missed media/icon reuse;
- unjustified custom code.

When the starter repository is accessible, use prompts/23-native-authoring-review.md as the canonical detailed review workflow.

## Site maturity

Classify the site as:

- **ESTABLISHED** — meaningful live content and a recurring visual language exist.
- **PARTIAL / IN PROGRESS** — some real patterns exist, but the system is incomplete.
- **GREENFIELD** — no meaningful established visual language exists yet.

For ESTABLISHED sites, use the public frontend as a major design reference.

For PARTIAL sites, distinguish strong recurring patterns from experiments and one-offs.

For GREENFIELD sites:

- do not invent site-wide rules from generic Bricks or WordPress defaults;
- inspect whether Theme Styles, a CSS framework, tokens, classes, variables, a visual brief, or other approved foundation already exists;
- if the design system is undefined, establish or explicitly approve a design-system direction before broad page design.

## Design-system authority and ownership

Classify the design-system authority as one of:

- **BRICKS NATIVE**
- **EXTERNAL FRAMEWORK**
- **HYBRID**
- **CUSTOM CODE DRIVEN**
- **UNKNOWN / UNDEFINED**

Classify design-system state as:

- **ESTABLISHED**
- **PARTIAL**
- **UNDEFINED**

Track ownership/provenance for global design resources where possible:

- BRICKS OWNED
- FRAMEWORK / PLUGIN OWNED
- THEME / CHILD-THEME OWNED
- CUSTOM-CODE OWNED
- PAGE-LOCAL
- UNKNOWN

Never assume a class, variable, or token is Bricks-owned merely because it is visible inside Bricks.

For important ownership claims, track confidence where useful: VERIFIED, STRONG EVIDENCE, TENTATIVE, or UNKNOWN.

If an external CSS/design framework such as Core Framework or another equivalent provider owns classes, variables, tokens, spacing, typography, colors, or breakpoints:

- treat that provider as the source of truth for those resources;
- document where they are configured and how they are exposed/synchronized into Bricks;
- do not create redundant Bricks-native copies;
- do not edit provider-owned resources through the wrong layer.

## Plugin-aware architecture

Before creating or restructuring any of the following, inspect the existing plugin/data architecture:

- CPTs
- taxonomies
- custom fields
- repeaters
- option pages
- relationships
- queries
- listings
- forms
- dynamic visibility
- commerce structures
- design-system providers

Potential systems include ACF / ACF Pro, JetEngine, ACPT / ACPT Pro, Meta Box, Pods, Toolset, Carbon Fields, WooCommerce, Bricks extensions, custom plugins, child-theme code, and other site-specific systems.

Do not recreate functionality already provided by an active system unless the user explicitly requests rearchitecture or migration.

### Advanced Themer / bundled ACF provenance heuristic

Advanced Themer can bundle ACF Pro for its own Theme Settings functionality.

Therefore, if:
- Advanced Themer is active;
- ACF runtime APIs/data sources are demonstrably working;
- standalone ACF/ACF Pro is absent from the normal plugin list;

do not conclude that ACF is absent.

Instead investigate provenance:
- if runtime/file-path evidence points into Advanced Themer, mark ACF loader provenance as VERIFIED: ADVANCED THEMER BUNDLED;
- if only the combination above is known, mark it as STRONG EVIDENCE / LIKELY ADVANCED THEMER BUNDLED;
- otherwise keep loader provenance UNKNOWN.

This is a heuristic, not a universal assumption. ACF may also be loaded by another plugin, MU-plugin, Composer/custom code, theme/child-theme, or standalone installation.

## WooCommerce

Always determine WooCommerce evidence/status. Prefer:

- ACTIVE
- INSTALLED / INACTIVE
- NOT DETECTED
- UNKNOWN / INVENTORY INCOMPLETE

Use NOT INSTALLED only when the available plugin inventory is complete enough to prove absence.

If ACTIVE:

- inspect the existing WooCommerce + Bricks architecture before commerce-related layout or data changes;
- inspect relevant templates, attributes, taxonomies, custom fields, and dynamic data where permitted;
- never expose private customer/order data in project documentation;
- never modify operational commerce data or configuration unless explicitly requested.

## Task workflow routing

For normal site work, infer the workflow from the user's request. The user should not need to know prompt filenames.

When the starter repository is accessible, use the matching canonical workflow as additional task guidance:

- global design-system change → `prompts/10-design-system-change-workflow.md`
- GREENFIELD design-system creation/seed → `prompts/11-greenfield-design-system-seed.md`
- new page → `prompts/20-new-page-build-workflow.md`
- existing page edit → `prompts/21-existing-page-edit-workflow.md`
- Bricks template/header/footer/archive/single change → `prompts/22-template-change-workflow.md`
- CPT/field/taxonomy/relationship/query/plugin-owned data architecture change → `prompts/30-plugin-data-architecture-change-workflow.md`
- WooCommerce + Bricks work → `prompts/31-woocommerce-workflow.md`
- Bricks-native authoring quality review → `prompts/23-native-authoring-review.md`
- limited read-only re-audit → `prompts/80-targeted-reaudit.md`
- reconcile an older bootstrapped project with a newer starter → `prompts/81-existing-project-upgrade.md`
- AGENTS/project-profile synchronization → `prompts/90-agents-maintenance-and-sync.md`

If the starter repository is not currently accessible, follow the equivalent rules embedded in this AGENTS.md and the local `docs/bricks/` knowledge base rather than blocking ordinary work.

Do not make the user manually select a workflow when their intent is already clear.

## New page workflow in a fresh task

When asked to create a page:

1. Read this `AGENTS.md`.
2. Read the task-relevant site rules, design-system documentation, visual references/patterns, site inventory, and audit findings under `docs/bricks/`.
3. Identify the closest existing page/template/pattern when the site is ESTABLISHED or PARTIAL; inspect the relevant individual page/template docs.
4. Inspect the exact shared resources the new page may use: Theme Styles, classes, variables/tokens, components, plugin/data bindings, queries, and relevant settings.
5. Re-check the comparable public frontend and every affected live resource through the assigned MCP server. Confirm that cached documentation, routing, ownership, and permissions still match.
6. For a significant page, explain the proposed structure, reuse choices, and any new global resources before writing.
7. Build only the requested page. Use preview/dry-run/planning abilities for non-trivial work where available.
8. Read back persisted state and visually verify wide, tablet, and mobile behavior where relevant.
9. Update only documentation whose architectural or design facts materially changed.

For GREENFIELD sites with no established visual language, do not pretend an existing site style can be copied. Follow the approved design-system/brief direction instead.

## Existing page / template workflow

When modifying an existing resource:

1. Read the relevant cached documentation.
2. Re-read the current live target, conditions, dependencies, classes, variables/tokens, components, queries, and provider-owned resources.
3. Inspect the rendered frontend when the task affects appearance or responsive behavior.
4. Keep the change to the requested scope.
5. Avoid opportunistic cleanup of unrelated architecture.
6. Verify persisted state and relevant frontend behavior after writing.
7. Update only documentation made stale by the change.

## Skill routing

- Use `bricks-start-here` for broad or unclear Bricks tasks.
- Use `bricks-plan-from-brief` for broad page/site builds from a document, content brief, or ambiguous design request before writing.
- Use `bricks-element-schemas` to list/fetch runtime element/control schemas before choosing generic structures or writing unfamiliar/complex controls.
- Use `bricks-naming-conventions` before creating new shared class/variable/component names.
- Use `bricks-media-assets` before uploading/recreating images, SVGs, icon sets, or other shared media.
- Use `bricks-custom-code` only after native Bricks controls/selectors/classes/variables are insufficient and custom code remains justified.
- For a known focused target, prefer the narrow live MCP abilities that match the task.
- Use `bricks-agent-repository` only when focused abilities cannot express a complex existing-site change and the host advertises that route.
- Use `bricks-design-systems` for Theme Styles, global classes, variables, palettes, and related design-system work.
- Use `bricks-components` for component definitions or instances.
- Use `bricks-templates-conditions` for template placement/routing.
- Use `bricks-element-conditions` for element visibility.
- Use `bricks-forms` for Bricks forms.
- Use `bricks-dynamic-data` for dynamic bindings; add `bricks-query-loops` when repeater, relationship, post, term, or other loop context is involved.
- Read `bricks-element-schemas` when writing unfamiliar or complex controls.
- Use `bricks-site-audit` or `bricks-audit-design-system` only when an audit of that scope is actually needed.
- Use `bricks-quality-gate` for broad, destructive, multi-resource, global, or uncertain writes.
- Use `bricks-browser-verify` for affected frontend, responsive, or interactive behavior.
- Keep verification proportional to the change.

## Global design-system changes

Treat changes to these resources as **global-impact changes**:

- Bricks Theme Styles
- global classes
- global variables
- global breakpoints
- external framework classes/tokens/variables
- global typography/color/spacing systems
- design-system custom code

Before changing them:

1. verify the authoritative owner/provider;
2. re-read current live state;
3. identify dependent or representative pages/templates;
4. estimate blast radius;
5. preserve a useful pre-change snapshot/reference where practical.

After changing them:

1. re-read persisted global state;
2. verify representative affected pages/templates;
3. verify relevant viewport widths;
4. inspect cascade/regression effects;
5. update affected design-system documentation and snapshots;
6. record intentional breaking changes or required migration work.

Do not perform opportunistic global cleanup during a scoped change.

## Permission-aware access

- The bootstrap audit may temporarily use higher privileges than routine work.
- An inaccessible resource is not evidence that it is absent.
- If a documented resource cannot currently be read, treat its docs as historical reference and state that live status is unverified.
- When relevant, label evidence as **VERIFIED LIVE**, **CACHED / PREVIOUSLY AUDITED**, **LIVE ACCESS BLOCKED**, **NOT VERIFIED**, **NOT APPLICABLE**, or **INSUFFICIENT EVIDENCE**.
- Do not request or attempt privilege escalation automatically.
- Do not use elevated access merely for convenience.
- If the task requires inaccessible live resources, stop before the blocked write and explain what access is missing and why it is required.

## Site write checklist

Before writing:

1. Read this file and task-relevant `docs/bricks/` references.
2. Re-read every affected live resource and dependency through the assigned MCP server.
3. Verify plugin/data/design-system ownership where relevant.
4. Compare cached documentation with live state.
5. Reuse existing resources and patterns where appropriate.
6. Inspect relevant frontend references for visual work.
7. Use preview, dry-run, or planning abilities where available for non-trivial work.
8. Confirm scope before destructive or global-impact operations.

After writing:

1. confirm authoritative mutation readback or re-read persisted state;
2. verify that unrelated resources did not change;
3. apply the relevant Bricks quality gate;
4. visually verify frontend/responsive behavior where appropriate;
5. update only local documentation made stale by the change.

## Documentation lifecycle

Keep the bootstrap audit as a durable reference; do not regenerate it for routine tasks.

Use targeted re-audits when a material change affects:

- plugin/integration architecture
- data model
- Theme Styles
- global classes/variables/tokens
- design-system provider/framework
- breakpoints
- templates/routing
- components
- queries
- WooCommerce architecture
- reusable visual patterns

Major audit/reference documents should include, where practical:

- Last audited
- Last live-verified
- Resource ID / post ID where applicable
- Verification status

Record only supported dates, IDs, and status.

## Bootstrap orchestration and resume

The one-prompt starter may require a new Codex chat or full Codex restart while MCP or skills are being loaded.

When `docs/bricks/00-bootstrap-status.md` exists and its status is `IN PROGRESS` or `BLOCKED`:

- read it before starting normal site work;
- if the user asks to continue/setup/resume, continue from its recorded phase instead of restarting the whole bootstrap;
- do not delete or overwrite bootstrap progress from assumptions;
- never record secrets in the status file.

The bootstrap status file tracks setup/orchestration. The separate `docs/bricks/00-audit-progress.md` tracks site-audit coverage.

## Bootstrap-audit mode

During the initial full-site bootstrap audit:

- the remote WordPress / Bricks site is READ-ONLY;
- local project files may be created and updated;
- browser/frontend inspection is allowed;
- no WordPress, Bricks, plugin, theme, WooCommerce, media, or server resource may be modified;
- no PHP may be executed;
- the audit may update this file's PROJECT PROFILE and add verified site-specific routing/reference guidance;
- preserve these general safety and workflow rules unless the user explicitly changes them.

Do not declare the bootstrap audit COMPLETE while relevant discovered resources remain unprocessed without a documented reason.

## Safety

Unless explicitly authorized for the specific task:

- do not execute PHP;
- do not modify plugin, theme, child-theme, or server source files;
- do not install, delete, update, activate, or deactivate plugins;
- do not alter licenses;
- do not delete pages, posts, templates, global classes, variables, components, CPTs, taxonomies, field groups, relationships, or media;
- do not modify WooCommerce operational data/configuration;
- do not change global templates, headers, footers, or site-wide settings outside the requested scope;
- do not make unrelated changes.

Prefer reversible, scoped changes.

## Communication

- Clearly distinguish read-only analysis, proposed changes, committed changes, cached facts, verified live facts, inference, recommendations, and unresolved uncertainty.
- Do not present inferred design conventions as established rules without evidence.
- If ambiguity could materially affect architecture, global design rules, data structures, permissions, or destructive operations, ask before writing.
- For ordinary scoped work, proceed with the safest interpretation supported by verified project state.
