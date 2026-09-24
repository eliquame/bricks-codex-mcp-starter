# Full Site Bootstrap Audit Prompt

Use this prompt as the first major Codex task after a new Bricks site has been connected through MCP and the Bricks skills are available.

```text
We are bootstrapping the long-term Codex project repository for the currently connected WordPress / Bricks website.

This task is SITE READ-ONLY.

You may create and update files inside the current local Codex project folder,
but you MUST NOT modify anything on the WordPress / Bricks site.

Use the installed Bricks skills where relevant, especially:

- bricks-start-here
- bricks-agent-repository
- bricks-site-audit
- bricks-audit-design-system
- bricks-design-systems
- bricks-naming-conventions
- bricks-breakpoints
- bricks-templates-conditions
- bricks-components
- bricks-dynamic-data
- bricks-global-queries
- bricks-custom-code
- bricks-headers-footers
- bricks-woocommerce
- bricks-browser-verify
- bricks-quality-gate

Treat runtime data returned by the connected Bricks MCP site as authoritative
for current Bricks structure and configuration.

Treat the rendered public frontend in the browser as authoritative for actual
visual appearance.

Treat the current WordPress plugin/theme environment as authoritative for
site integrations and available functionality.

Do not make assumptions from generic Bricks or WordPress knowledge where the
actual site state can be inspected.

==================================================
PRIMARY GOAL
==================================================

Build a durable local documentation repository that future Codex threads can
use to understand this website before making changes.

The resulting project knowledge base must cover:

A. the actual Bricks architecture and design system
B. the actual rendered visual language of the public website
C. the relevant WordPress plugin/integration ecosystem
D. the site's content/data architecture
E. WooCommerce architecture whenever WooCommerce is active

The objective is that future Codex tasks can:

- understand how this site is built
- understand how this site actually looks
- understand where its dynamic data comes from
- understand which plugins own which functionality
- reuse its established design system
- reuse existing custom fields, CPTs, taxonomies and relationships
- reuse established query/data patterns
- reproduce its established visual language
- avoid unnecessary duplicate plugins, fields, queries, classes or variables
- avoid breaking integrations by treating Bricks in isolation

This is not only a technical Bricks audit.

It is a:

- Bricks architecture audit
- WordPress integration audit
- data-model audit
- plugin ecosystem audit
- frontend visual audit
- design-language audit

==================================================
DOCUMENTATION STRUCTURE
==================================================

Use the starter repository's `templates/documentation-structure.md` as the current structural reference, and use the following structure where appropriate:

docs/bricks/
    00-bootstrap-status.md
    00-audit-progress.md
    00-site-overview.md
    00-site-state.md
    site-inventory.md

    01-plugin-ecosystem.md
    02-data-architecture.md

    03-design-system.md
    design-system-authority.md
    04-theme-styles.md
    05-global-classes.md
    06-global-variables.md
    07-colors-typography.md
    08-breakpoints.md

    09-templates.md
    pages-index.md
    site-settings.md
    10-components.md
    11-dynamic-data.md
    12-queries.md
    13-custom-code.md

    14-woocommerce.md

    15-frontend-visual-audit.md
    16-visual-patterns.md

    17-site-rules.md
    18-known-patterns.md
    19-audit-findings.md

    pages/
        <page-slug>.md

    templates/
        <template-name>.md

    plugins/
        <plugin-or-integration-name>.md

    snapshots/
        site-inventory.json
        plugin-inventory.json
        data-architecture.json
        design-context.json
        design-system-authority.json
        design-system.json
        site-settings.json
        template-architecture.json
        page-architecture.json
        dynamic-dependencies.json
        audit-findings.json
        templates.json
        other useful machine-readable snapshots

    visual-references/
        screenshots or browser captures where useful and supported

Do not create empty documents merely to satisfy the structure.

==================================================
PHASE 0 — AUDIT PROGRESS AND RESUMABILITY
==================================================

Before performing the full audit, create/update:

docs/bricks/00-audit-progress.md

Use the starter repository's `templates/audit-progress.template.md` as the baseline structure, then extend it when the target site requires additional audit categories.

Do not overwrite or confuse the separate `docs/bricks/00-bootstrap-status.md`, which tracks setup/orchestration rather than site-discovery coverage.

`00-audit-progress.md` must act as the persistent checklist for the entire site audit.

Track discovered resources using statuses such as:

- DISCOVERED
- INSPECTED
- DOCUMENTED
- VISUALLY VERIFIED
- VERIFIED
- ACCESS BLOCKED
- NOT ACTIVE
- NOT INSTALLED
- NOT APPLICABLE
- INSUFFICIENT EVIDENCE

Track at minimum:

- site maturity classification
- design-system state
- design-system authority/providers
- pages
- templates
- template-rendered frontend examples
- plugins
- plugin integrations
- CPTs
- taxonomies
- custom field systems
- relationships
- queries
- global classes
- global variables
- theme styles
- breakpoints
- components
- WooCommerce
- other relevant resources

The audit must be resumable if interrupted.

Do not declare the audit complete if discovered resources remain unprocessed
without an explicit documented reason.

==================================================
PHASE 1 — SITE INVENTORY
==================================================

Enumerate all relevant WordPress and Bricks resources available to the
connected user.

Inspect and inventory where available:

- Bricks-enabled pages
- landing pages
- Bricks templates
- template types
- template conditions
- headers
- footers
- custom post types
- taxonomies
- WooCommerce templates
- components
- global queries
- global classes
- global variables
- color palettes
- theme styles
- breakpoints
- relevant global settings
- custom fonts
- dynamic-data usage
- reusable structural patterns
- page-level custom CSS or code where readable
- important post types rendered through Bricks
- relevant plugin-generated resources

Create/update:

docs/bricks/site-inventory.md
docs/bricks/site-settings.md
docs/bricks/snapshots/site-inventory.json
docs/bricks/snapshots/site-settings.json
docs/bricks/00-site-overview.md

Include identifiers such as:

- post ID
- title
- slug
- URL
- resource type
- template type
- publication status

where available.

Use pagination/batching where required.

--------------------------------------------------
1.1 — SITE MATURITY CLASSIFICATION
--------------------------------------------------

Classify the current project before deriving visual or design-system rules.

Create/update:

docs/bricks/00-site-state.md

Classify SITE_MATURITY as one of:

- ESTABLISHED
- PARTIAL / IN PROGRESS
- GREENFIELD

Use evidence, not assumptions.

ESTABLISHED means there is enough real site content and rendered frontend
evidence to derive recurring structural and visual conventions.

PARTIAL / IN PROGRESS means some real pages, templates, styles or visual
patterns exist, but there is not enough evidence to treat every observed
pattern as a mature site-wide rule.

GREENFIELD means the project is blank or effectively blank for design-learning
purposes: no meaningful established frontend system exists yet.

Also classify DESIGN_SYSTEM_STATE as:

- ESTABLISHED
- PARTIAL
- UNDEFINED

Do not equate "Bricks is installed" with "a design system exists".

If the site is GREENFIELD or the design system is UNDEFINED:

- do not invent visual conventions from absent evidence;
- do not promote generic Bricks defaults to project rules;
- mark visual-pattern discovery as NOT APPLICABLE or INSUFFICIENT EVIDENCE
  where appropriate;
- document that a separate design-system creation/seed workflow is required
  before design-heavy page construction;
- keep this bootstrap task read-only.

==================================================
PHASE 2 — PLUGIN AND INTEGRATION ECOSYSTEM
==================================================

Inspect the WordPress plugin environment.

This is READ-ONLY.

Do NOT:

- install plugins
- delete plugins
- activate plugins
- deactivate plugins
- update plugins
- change plugin settings
- change licenses
- modify plugin files

Create:

docs/bricks/01-plugin-ecosystem.md
docs/bricks/snapshots/plugin-inventory.json

The goal is NOT merely to dump the plugin list.

The goal is to understand which plugins materially affect:

- site structure
- Bricks editing
- dynamic data
- custom fields
- CPTs
- taxonomies
- relationships
- queries
- forms
- WooCommerce
- multilingual content
- SEO output
- frontend rendering
- performance/caching relevant to development
- custom code
- templates
- reusable content systems
- CSS frameworks
- design-system providers
- token/class/variable providers

--------------------------------------------------
2.1 — PLUGIN INVENTORY
--------------------------------------------------

Inventory installed plugins where access permits.

For every relevant plugin document where available:

- plugin name
- plugin slug
- version
- active/inactive state
- apparent purpose
- whether it materially affects Bricks/content/frontend architecture
- important dependencies
- known integration points with Bricks
- resources owned or generated by that plugin
- discovery source/provenance (standard plugin list, runtime-detected, MU-plugin, theme/child-theme bundled, custom/Composer loaded, or unknown loader)
- inventory confidence/coverage

Do NOT produce deep documentation for plugins that have no meaningful
relationship to page architecture or editing.

Classify plugins as:

- CORE SITE ARCHITECTURE
- DATA / DYNAMIC CONTENT
- ECOMMERCE
- FORMS
- SEO
- MULTILINGUAL
- PERFORMANCE
- MEDIA
- SECURITY
- EDITOR / BUILDER EXTENSION
- UTILITY
- OTHER
- IRRELEVANT TO BRICKS WORKFLOW

--------------------------------------------------
2.2 — IMPORTANT OPTIONAL INTEGRATIONS
--------------------------------------------------

Detect whether important data/content plugins exist.

Examples include, but are not limited to:

- Advanced Custom Fields / ACF Pro
- JetEngine
- ACPT / ACPT Pro
- Meta Box
- Pods
- Toolset
- Carbon Fields
- Bricks-related dynamic data extensions
- custom CPT/field plugins

These integrations are OPTIONAL.

Do NOT assume they are installed.

A runtime integration can exist even when it is absent from the standard active-plugin list. If runtime evidence proves the provider exists, record it as RUNTIME DETECTED and investigate/mark its loader provenance separately. Do not downgrade runtime evidence merely because the normal plugin list omits it.

For each one:

IF absence is proven by a sufficiently complete inventory:
    mark NOT INSTALLED

IF the provider is simply not found but inventory coverage is incomplete:
    mark NOT DETECTED / INVENTORY INCOMPLETE

IF INSTALLED BUT INACTIVE:
    mark INSTALLED / INACTIVE

IF ACTIVE:
    perform the relevant read-only integration audit.

--------------------------------------------------
2.3 — CUSTOM POST TYPES AND TAXONOMIES
--------------------------------------------------

Identify custom post types and taxonomies.

Where possible determine:

- post type slug
- label
- public/non-public status
- source/owner
- plugin or custom-code origin
- associated taxonomies
- Bricks usage
- templates rendering the post type
- custom fields
- archive behaviour
- frontend examples

Do not assume every CPT comes from the same plugin.

--------------------------------------------------
2.4 — CUSTOM FIELD SYSTEMS
--------------------------------------------------

If ACF, JetEngine, ACPT, Meta Box or another custom-field system is active,
inspect its relevant data model where current permissions allow.

Document:

- field groups
- field sets
- associated post types
- taxonomy fields
- options/settings fields
- user fields where relevant
- repeating structures
- groups
- relationships
- media fields
- dynamic-data usage in Bricks

Do NOT copy sensitive field values unnecessarily.

Focus on:

- schema
- architecture
- usage
- dependencies

rather than private content.

Create plugin-specific files where useful:

docs/bricks/plugins/acf.md
docs/bricks/plugins/jetengine.md
docs/bricks/plugins/acpt.md

or equivalent.

--------------------------------------------------
2.5 — JETENGINE / RELATIONSHIP / QUERY SYSTEMS
--------------------------------------------------

If JetEngine or a similar plugin is active, inspect where accessible:

- CPTs
- meta fields
- taxonomies
- relations
- listings
- Query Builder queries
- option pages
- dynamic visibility logic
- dynamic data used in Bricks
- relationships between entities

Map these to Bricks usage.

Do NOT assume a JetEngine resource is unused simply because it does not appear
on the homepage.

--------------------------------------------------
2.6 — ACF
--------------------------------------------------

If ACF or ACF Pro is active, inspect where accessible:

- field groups
- locations
- field names
- field types
- repeaters
- flexible content
- groups
- relationships
- options pages
- relevant dynamic tags/use in Bricks

Document how ACF participates in the site's data architecture.

Do NOT modify field groups.

--------------------------------------------------
2.6.1 — ADVANCED THEMER / BUNDLED ACF HEURISTIC
--------------------------------------------------

Advanced Themer can bundle ACF Pro for its own Theme Settings functionality.

If:
- Advanced Themer is active;
- ACF runtime APIs/data sources are demonstrably available and working;
- standalone ACF / ACF Pro is absent from the standard plugin list;

then do NOT mark ACF as absent.

Investigate loader provenance.

Classify as:

- VERIFIED: ADVANCED THEMER BUNDLED
  when runtime/file-path/version evidence confirms the ACF copy is loaded from Advanced Themer.

- STRONG EVIDENCE / LIKELY ADVANCED THEMER BUNDLED
  when Advanced Themer is active + ACF runtime works + standalone ACF is absent,
  but the loader path cannot be verified.

- UNKNOWN LOADER
  when ACF runtime exists but evidence does not identify the loader.

Do not treat this as universal.
ACF may instead come from:
- standalone ACF / ACF Pro;
- another plugin bundle;
- MU-plugin;
- Composer/custom loader;
- theme/child-theme code.

Also treat Advanced Themer itself as architecture-relevant when it owns or influences:
- Theme Settings;
- classes/variables;
- Core Framework integration;
- custom CSS/design-system behavior;
- Bricks builder authoring behavior.

Official evidence:
https://advancedthemer.com/changelogs/

--------------------------------------------------
2.7 — ACPT
--------------------------------------------------

If ACPT / ACPT Pro is active, inspect where accessible:

- post types
- taxonomies
- meta boxes
- fields
- relationships
- option pages
- dynamic data integration
- Bricks usage

Document its role separately from ACF/JetEngine.

--------------------------------------------------
2.8 — CSS FRAMEWORK / DESIGN-SYSTEM PROVIDERS
--------------------------------------------------

Detect whether an active plugin, theme layer, or custom integration provides
a site-wide CSS/design framework.

Examples may include Core Framework or another comparable system.

Do NOT assume any specific framework is installed.

If a design-system provider is detected, inspect where current permissions allow:

- framework/provider name and version
- active/inactive state
- integration with Bricks
- framework-owned classes
- framework-owned variables/tokens
- spacing/typography/color systems
- breakpoint strategy where relevant
- generated/synced Bricks resources
- naming conventions
- source-of-truth location
- whether resources are edited in the provider, in Bricks, or both
- dependencies and synchronization behaviour observable from the current site

Classify every major design-system resource by ownership/provenance where possible:

- BRICKS OWNED
- FRAMEWORK / PLUGIN OWNED
- THEME / CHILD-THEME OWNED
- CUSTOM-CODE OWNED
- PAGE-LOCAL
- UNKNOWN

Also record ownership confidence where useful:
- VERIFIED
- STRONG EVIDENCE
- TENTATIVE
- UNKNOWN

Do not duplicate framework-owned classes or variables as Bricks-native resources
merely because they appear in the Bricks UI.

If provider-owned resources are mirrored or synchronized into Bricks, preserve
their provider ownership in the documentation.

Create plugin-specific documentation under:

docs/bricks/plugins/

when the provider materially affects page building.

--------------------------------------------------
2.9 — MUST-USE / CUSTOM SITE CODE
--------------------------------------------------

Where visible and permitted, identify:

- must-use plugins
- site-specific plugins
- child-theme functionality
- custom integration plugins

Only inspect them deeply when relevant to:

- content model
- Bricks behaviour
- dynamic data
- frontend output
- templates
- forms
- WooCommerce
- site-wide functionality

Do NOT modify source files.

==================================================
PHASE 3 — DATA ARCHITECTURE
==================================================

Create:

docs/bricks/02-data-architecture.md
docs/bricks/snapshots/data-architecture.json

Build a high-level map of the site's content/data model.

Document relationships between:

WORDPRESS CONTENT TYPE
    ↓
CUSTOM FIELDS
    ↓
TAXONOMIES
    ↓
RELATIONSHIPS
    ↓
QUERIES
    ↓
BRICKS TEMPLATE
    ↓
BRICKS ELEMENT
    ↓
PUBLIC FRONTEND

Where relevant identify:

- Pages
- Posts
- CPTs
- taxonomies
- WooCommerce products/categories
- custom fields
- relationships
- global options
- dynamic data
- queries
- listing systems
- template relationships

The purpose is that future Codex threads understand where data already exists
before creating new structures.

==================================================
PHASE 4 — DESIGN SYSTEM
==================================================

Inspect the complete current Bricks design system.

Document:

- theme styles
- theme-style conditions
- global classes
- class naming conventions
- global variables
- variable naming conventions
- color palettes
- typography
- spacing
- content widths
- container widths
- breakpoints
- responsive cascade strategy
- borders
- radii
- shadows
- gradients
- pseudo states/selectors
- recurring grid/flex structures
- common section structures
- button systems
- heading patterns
- card systems
- reusable layout conventions

Create/update:

docs/bricks/03-design-system.md
docs/bricks/design-system-authority.md
docs/bricks/04-theme-styles.md
docs/bricks/05-global-classes.md
docs/bricks/06-global-variables.md
docs/bricks/07-colors-typography.md
docs/bricks/08-breakpoints.md

Also save useful machine-readable snapshots, including where useful:

docs/bricks/snapshots/design-system-authority.json

Before documenting the design system, determine its authority model.

Classify DESIGN_SYSTEM_AUTHORITY as one of:

- BRICKS NATIVE
- EXTERNAL FRAMEWORK
- HYBRID
- CUSTOM CODE DRIVEN
- UNKNOWN / UNDEFINED

Document which layer owns:

- colors
- typography
- spacing
- breakpoints
- global classes
- variables/tokens
- components/patterns
- theme-level visual rules

If Theme Styles are empty, minimal, or clearly not authoritative, do not treat
that as a failure. Determine whether another provider owns the system.

If no authoritative design system exists:

- record DESIGN_SYSTEM_STATE: UNDEFINED or PARTIAL;
- do not invent a complete system during this read-only bootstrap;
- document what does exist;
- add a future-project rule that design-system creation/approval should happen
  before broad page design work.

Do NOT invent a design rule because a value occurs once.

Classify observations as:

- EXPLICIT GLOBAL RULE
- STRONG RECURRING CONVENTION
- LOCAL IMPLEMENTATION
- ONE-OFF
- POSSIBLE INCONSISTENCY

==================================================
PHASE 5 — TEMPLATES
==================================================

Inspect every Bricks template accessible through MCP.

For each template record where relevant:

- ID
- name
- type
- status
- conditions
- purpose
- element hierarchy
- major classes used
- global variables used
- components used
- custom/plugin data used
- query loops
- dynamic data
- interactions
- element conditions
- responsive behaviour
- custom CSS/code
- frontend contexts where rendered

Create/update:

docs/bricks/09-templates.md

and where useful:

docs/bricks/templates/<descriptive-template-name>.md

Document routing for:

- headers
- footers
- single templates
- archives
- CPT templates
- WooCommerce templates
- conditional templates

==================================================
PHASE 6 — ALL BRICKS PAGES
==================================================

Enumerate and inspect every accessible Bricks-built page.

Do NOT stop after the homepage.

For every relevant page record:

- post ID
- title
- slug
- public URL
- purpose
- page/template relationship
- top-level element hierarchy
- major sections
- global classes
- variables
- components
- plugin-provided dynamic data
- custom fields used
- theme styles
- queries
- query loops
- conditions
- interactions
- responsive behaviour
- local styles
- recurring patterns
- important exceptions

Create/update:

docs/bricks/pages-index.md

Create one detail file per relevant page:

docs/bricks/pages/<slug>.md

Do not dump thousands of raw settings.

Document architecture and dependencies.

==================================================
PHASE 7 — COMPONENTS, DYNAMIC DATA, QUERIES & CODE
==================================================

Create/update:

docs/bricks/10-components.md
docs/bricks/11-dynamic-data.md
docs/bricks/12-queries.md
docs/bricks/13-custom-code.md

Inspect where relevant:

- components
- component instances
- global queries
- query loops
- dynamic tags
- ACF dynamic data
- JetEngine dynamic data
- ACPT dynamic data
- WooCommerce dynamic data
- custom dynamic data providers
- reusable query patterns
- relevant CSS/JS
- custom Bricks code structures

Do NOT execute PHP.

Do NOT modify code.

==================================================
PHASE 8 — WOOCOMMERCE
==================================================

WooCommerce MUST ALWAYS be checked during the bootstrap audit.

Do NOT assume WooCommerce exists.

FIRST determine its status.

IF a sufficiently complete inventory proves WooCommerce is absent:
    record:
    WOOCOMMERCE: NOT INSTALLED

IF WooCommerce is not detected but plugin inventory is incomplete:
    record:
    WOOCOMMERCE: NOT DETECTED / INVENTORY INCOMPLETE

IF installed but inactive:
    record:
    WOOCOMMERCE: INSTALLED / INACTIVE

IF active:
    WooCommerce becomes a REQUIRED audit area.

Create/update:

docs/bricks/14-woocommerce.md

If active, inspect where relevant and accessible:

- products
- product categories
- product tags
- attributes
- variations
- product data architecture
- product custom fields
- Bricks WooCommerce templates
- shop/archive templates
- category templates
- single product templates
- cart
- checkout
- account pages
- WooCommerce components/elements
- dynamic product data
- query loops
- related/up-sell/cross-sell patterns
- frontend shop design
- responsive shop behaviour

Map WooCommerce frontend rendering back to:

- template
- Bricks structure
- classes
- variables
- dynamic data
- plugin integrations

Do NOT change:

- products
- prices
- stock
- orders
- customers
- checkout settings
- payment settings
- shipping settings
- tax settings
- coupons
- WooCommerce configuration

Never expose private customer/order data in documentation.

==================================================
PHASE 9 — FRONTEND VISUAL AUDIT AND DESIGN LANGUAGE
==================================================

The Bricks/MCP structure alone is NOT sufficient for understanding a site's
visual design language when a meaningful public design already exists.

Frontend visual auditing is CONDITIONAL on site maturity.

IF SITE_MATURITY = ESTABLISHED:
    perform the full frontend visual audit below.

IF SITE_MATURITY = PARTIAL / IN PROGRESS:
    inspect all meaningful available public references, but clearly mark
    conclusions as limited by incomplete evidence. Do not promote isolated
    experiments to site-wide rules.

IF SITE_MATURITY = GREENFIELD:
    verify whether any meaningful public visual reference exists.
    If none exists, mark the deep visual audit and visual pattern library as
    NOT APPLICABLE / INSUFFICIENT EVIDENCE.
    Do not invent a visual language from default WordPress/Bricks output.

This remains READ-ONLY.

--------------------------------------------------
9.1 — GOAL
--------------------------------------------------

Build a visual understanding of how:

- Bricks
- plugin-driven data
- templates
- classes
- variables
- layouts

actually render together in the browser.

The purpose is to learn enough about the site's visual language that future
Codex tasks can design pages that feel native to the site.

Use:

- Bricks MCP as authority for Bricks structure/configuration
- plugin/runtime data as authority for integration architecture
- rendered frontend as authority for actual appearance

--------------------------------------------------
9.2 — PUBLIC PAGE INVENTORY
--------------------------------------------------

Open every relevant publicly accessible page where practical.

Include representative examples of:

- homepage
- landing pages
- main navigation destinations
- service pages
- CPT pages
- category/archive pages
- brand pages
- articles
- forms/contact pages
- pages rendered by templates
- plugin-driven frontend pages
- WooCommerce pages when active
- other visually distinct page types

Do NOT stop after the homepage.

For template-only resources, identify real frontend URLs where they render.

Create/update:

docs/bricks/15-frontend-visual-audit.md

--------------------------------------------------
9.3 — RESPONSIVE VISUAL INSPECTION
--------------------------------------------------

Inspect important page types at:

- large desktop
- normal desktop/laptop
- tablet/narrow desktop
- mobile

Prefer actual Bricks breakpoints where practical.

Observe:

- content widths
- section spacing
- grid collapse
- flex direction
- visual ordering
- typography scaling
- image cropping
- heroes
- buttons
- navigation
- cards
- gaps
- margins
- padding
- alignment
- overlaps
- decorative elements
- overflow
- hidden elements
- responsive simplification

--------------------------------------------------
9.4 — VISUAL DESIGN LANGUAGE
--------------------------------------------------

Study recurring visual patterns.

Document:

### Composition
- whitespace
- hierarchy
- density
- pacing
- alignment
- column proportions
- section sequencing

### Layout
- heroes
- containers
- grids
- cards
- split layouts
- CTA sections
- image/text patterns
- overlaps
- backgrounds

### Typography
- hierarchy
- line length
- wrapping
- paragraph width
- labels
- emphasis

### Colour
- backgrounds
- accents
- contrast
- light/dark sequencing
- overlays

### Imagery
- crop
- aspect ratios
- placement
- contained/full-width
- photography/graphics

### UI
- buttons
- cards
- navigation
- forms
- icons
- badges
- interactive patterns

Describe visual personality using observable evidence.

==================================================
PHASE 10 — VISUAL PATTERN LIBRARY
==================================================

Create/update:

docs/bricks/16-visual-patterns.md

If SITE_MATURITY = GREENFIELD and no meaningful frontend patterns exist,
do not fabricate this library. Record that the pattern library requires future
design-system/page development.

Otherwise identify reusable patterns such as:

- homepage hero
- standard hero
- media/text section
- card grid
- feature section
- CTA
- article layout
- form section
- product layout when WooCommerce is active
- archive/card pattern
- navigation
- footer
- mobile adaptations

For each pattern document:

- frontend example
- URL
- Bricks page/template
- classes
- variables
- plugin/data dependencies
- structural implementation
- visual purpose
- responsive behaviour
- reuse guidance

Classify:

- SITE-WIDE VISUAL RULE
- STRONG RECURRING PATTERN
- PAGE-TYPE PATTERN
- ONE-OFF DESIGN
- POSSIBLE INCONSISTENCY

==================================================
PHASE 11 — PAGE-TO-IMPLEMENTATION CORRELATION
==================================================

For important patterns correlate:

VISIBLE FRONTEND
    ↓
WORDPRESS CONTENT TYPE
    ↓
PLUGIN / DATA SOURCE
    ↓
BRICKS TEMPLATE
    ↓
ELEMENT STRUCTURE
    ↓
GLOBAL CLASSES
    ↓
GLOBAL VARIABLES
    ↓
QUERY / DYNAMIC DATA
    ↓
RESPONSIVE SETTINGS

The purpose is to understand BOTH what the design looks like and how it is
implemented.

==================================================
PHASE 12 — SITE-WIDE RULES
==================================================

Create/update:

docs/bricks/17-site-rules.md
docs/bricks/18-known-patterns.md

Derive rules using ALL relevant evidence that actually exists:

A. Bricks architecture
B. WordPress/plugin/data architecture
C. browser-rendered frontend when meaningful visual references exist
D. external framework/design-system providers when present

For GREENFIELD or visually immature sites, do not manufacture visual rules.
Record explicit unknowns and future design-system requirements instead.

Separate:

1. Explicit global rules
2. Strong recurring structural conventions
3. Strong recurring visual conventions
4. Data-model conventions
5. Plugin integration conventions
6. Page-type-specific patterns
7. Exceptions
8. Inconsistencies
9. Things future agents must verify

Examples:

- container structure
- section hierarchy
- classes
- variables
- field/data usage
- query patterns
- CPT/template relationships
- responsive patterns
- spacing
- typography
- buttons
- cards
- heroes
- imagery
- WooCommerce patterns

==================================================
PHASE 13 — AUDIT FINDINGS
==================================================

Create/update:

docs/bricks/19-audit-findings.md

Do NOT fix anything.

Document potential issues such as:

- duplicate classes
- duplicate variables
- naming inconsistencies
- duplicate field structures
- overlapping CPT/data systems
- ACF/JetEngine/ACPT duplication
- unused-looking fields
- unused-looking queries
- design-system drift
- plugin dependency concerns
- local styles repeating global patterns
- template overlap
- visual inconsistency
- responsive inconsistency
- architecture requiring review

Classify:

- CONFIRMED FACT
- LIKELY ISSUE
- POSSIBLE ISSUE
- RECOMMENDATION
- NEEDS HUMAN REVIEW

==================================================
PHASE 14 — AGENTS.md
==================================================

Finally refine the project-root:

AGENTS.md

The automated `START-HERE.md` flow should already have initialized the project-root AGENTS.md from the starter repository's `project-starter/AGENTS.md` before this full audit begins.

Read the existing file first.

Preserve its general safety, source-of-truth, permission-aware, plugin-aware,
visual-verification, design-system ownership, documentation-lifecycle, skill-routing,
and write-verification rules.

Do NOT replace it with a shorter ad-hoc file.

Populate/refine its PROJECT PROFILE and add only useful site-specific routing/reference
guidance derived from this verified audit.

If project-root AGENTS.md is missing, treat that as incomplete bootstrap initialization. If the starter repository source is still available, create AGENTS.md from `project-starter/AGENTS.md` yourself, then continue. If the starter source is unavailable, stop and report the missing initialization rather than inventing a different policy.

Keep site-specific additions concise and operational.

It must record verified project-profile values where available:

- Site name
- Site URL
- Allowed MCP server
- Bootstrap status
- SITE_MATURITY
- DESIGN_SYSTEM_STATE
- DESIGN_SYSTEM_AUTHORITY
- WooCommerce status
- Primary data/content providers
- Primary CSS/design-system provider

It must also preserve or strengthen:

--------------------------------------------------
SITE IDENTITY
--------------------------------------------------

This project belongs exclusively to the currently connected target website.

Use only the MCP server assigned to this project unless explicitly instructed otherwise.

--------------------------------------------------
SOURCE OF TRUTH
--------------------------------------------------

For current Bricks structure:
LIVE BRICKS MCP wins.

For current plugin/integration architecture:
LIVE WORDPRESS/PLUGIN STATE wins.

For actual appearance:
CURRENT RENDERED FRONTEND wins.

Local docs are cached architectural references, not guaranteed current state.

--------------------------------------------------
PLUGIN-AWARE WORKFLOW
--------------------------------------------------

Before creating new:

- custom fields
- CPTs
- taxonomies
- relationships
- queries
- forms
- WooCommerce structures
- dynamic-data architecture

inspect the existing plugin/data ecosystem first.

Do not recreate functionality already provided by:

- ACF
- JetEngine
- ACPT
- WooCommerce
- another existing active plugin
- existing custom site code

Prefer the established site architecture unless the user explicitly requests
a redesign/rearchitecture.

--------------------------------------------------
DESIGN-SYSTEM AUTHORITY AND LIFECYCLE
--------------------------------------------------

The project documentation must state which system owns global design resources.

Possible authority models include:

- BRICKS NATIVE
- EXTERNAL FRAMEWORK
- HYBRID
- CUSTOM CODE DRIVEN
- UNDEFINED / PARTIAL

Future agents must not create duplicate Bricks classes/variables when an
external framework/provider already owns equivalent resources.

If the design system is UNDEFINED or materially incomplete, future design-heavy
work must first establish or explicitly approve a design-system direction
rather than silently inventing one page-by-page.

Changes to any global design-system source — including Bricks Theme Styles,
global classes, global variables, external framework tokens/classes, or
theme/custom-code design tokens — must be treated as global-impact changes.

For such changes future agents must:

1. verify resource ownership and current live state;
2. identify affected/representative pages and templates;
3. preserve or snapshot the relevant pre-change state where practical;
4. apply only the approved global change;
5. re-read persisted state;
6. browser-verify representative affected frontend pages at relevant viewports;
7. update design-system documentation and snapshots;
8. document any intentional breaking change or migration requirement.

--------------------------------------------------
BEFORE EVERY WRITE
--------------------------------------------------

1. Read AGENTS.md.
2. Read relevant documentation.
3. Inspect current live Bricks state.
4. Inspect current plugin/data dependencies.
5. Inspect relevant frontend references for visual work.
6. Reuse existing structures where appropriate.
7. Avoid unrelated changes.
8. Preview/plan where possible.
9. Commit only agreed scope.
10. Re-read persisted state.
11. Browser verify.
12. Run quality-gate checks.
13. Update documentation if architecture materially changed.

--------------------------------------------------
PERMISSION-AWARE BEHAVIOUR
--------------------------------------------------

The bootstrap audit may have used elevated admin permissions.

Future work may use a restricted user.

Never interpret inaccessible data as nonexistent.

Use statuses:

- VERIFIED LIVE
- CACHED / PREVIOUSLY AUDITED
- LIVE ACCESS BLOCKED
- NOT VERIFIED

Do not attempt privilege escalation automatically.

--------------------------------------------------
VISUAL DESIGN VERIFICATION
--------------------------------------------------

Bricks data alone is not sufficient for design/layout work.

Use both:

- architecture
- browser-rendered visual references

Always visually verify significant design work after implementation.

--------------------------------------------------
WOOCOMMERCE
--------------------------------------------------

Always determine WooCommerce status.

If inactive/not installed:
do not assume WooCommerce functionality exists.

If active:
inspect existing WooCommerce architecture before creating/changing e-commerce
layouts or data structures.

Never expose order/customer/private commerce data in project documentation.

--------------------------------------------------
SAFETY
--------------------------------------------------

Never:

- execute PHP without explicit authorization
- modify plugins
- modify plugin files
- activate/deactivate plugins without explicit authorization
- install/delete/update plugins without explicit authorization
- delete fields/CPTs/taxonomies/relationships without explicit authorization
- delete Bricks global resources without explicit authorization
- make unrelated site-wide changes

==================================================
GLOBAL SAFETY RULES FOR THIS BOOTSTRAP TASK
==================================================

SITE IS READ-ONLY.

Local project documentation MAY be created or updated.

Do NOT:

- modify posts
- modify pages
- modify Bricks elements
- modify templates
- modify theme styles
- modify classes
- modify variables
- modify components
- modify queries
- modify plugin settings
- modify field groups
- modify CPTs
- modify taxonomies
- modify relationships
- modify WooCommerce
- modify products
- modify orders
- modify customers
- install/update/delete plugins
- activate/deactivate plugins
- execute PHP
- modify themes
- modify server files

==================================================
COMPLETION REPORT
==================================================

At completion report:

- SITE_MATURITY classification
- DESIGN_SYSTEM_STATE
- DESIGN_SYSTEM_AUTHORITY
- detected design-system/CSS framework providers
- whether full frontend visual auditing was applicable
- pages discovered
- pages MCP-inspected
- public pages browser-inspected
- templates discovered
- templates inspected
- template frontend examples inspected
- installed plugins count where discoverable
- active plugins count where discoverable
- architecture-relevant plugins identified
- custom field systems detected
- CPT systems detected
- CPT count
- taxonomy count
- relationship systems detected
- ACF status
- JetEngine status
- ACPT status
- other major data plugins detected
- WooCommerce status
- WooCommerce resources inspected if active
- global class count
- global variable count
- theme style count
- component count
- query count
- major responsive visual references inspected
- strongest visual design references
- reusable visual patterns
- inaccessible resources and reasons
- plugin/provider inventory coverage and unresolved loader provenance
- design ownership confidence where unresolved
- meaningful snapshot deltas discovered versus previous cached state

State whether audit is:

COMPLETE

or

PARTIAL

Do not report COMPLETE unless every discovered relevant resource has either:

- been inspected/documented/verified

OR

- has an explicit documented reason why it could not be inspected.

Finally:

1. Summarize all local documentation created or updated.
2. Summarize the plugin/integration architecture.
3. Summarize the content/data architecture.
4. Summarize the Bricks architecture.
5. Summarize the visual-design conclusions.
6. Summarize important inconsistencies/audit findings.
7. Confirm that no WordPress / Bricks / plugin changes were made.
```
