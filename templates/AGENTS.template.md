# Project Instructions

## Site identity

This project belongs to exactly one WordPress / Bricks website.

Use only the MCP server assigned to this project unless the user explicitly instructs otherwise.

## Sources of truth

- Live Bricks MCP state is authoritative for current Bricks structure and configuration.
- Live plugin/runtime state is authoritative for current integration architecture.
- The rendered frontend is authoritative for actual visual appearance.
- Local documentation under `docs/bricks/` is a durable cached reference, not guaranteed current state.

If sources disagree, document the discrepancy and prefer the relevant live source.

## Site maturity and design-system authority

Record and respect the project's current maturity:

- ESTABLISHED
- PARTIAL / IN PROGRESS
- GREENFIELD

Also record the current design-system authority:

- BRICKS NATIVE
- EXTERNAL FRAMEWORK
- HYBRID
- CUSTOM CODE DRIVEN
- UNDEFINED / PARTIAL

If the project is GREENFIELD or the design system is undefined, do not invent site-wide visual rules from generic defaults. Establish or explicitly approve a design-system direction before broad design work.

When an external CSS/design framework owns classes, variables, or tokens, treat those resources as provider-owned even if they are visible or mirrored in Bricks. Do not create redundant Bricks-native duplicates.

## Global design-system changes

Changes to Theme Styles, global classes, global variables, framework tokens/classes, or other site-wide design sources are global-impact changes.

Before such a change:

1. verify ownership and current live state;
2. identify representative affected pages/templates;
3. capture relevant pre-change state where practical.

After the change:

1. re-read persisted state;
2. browser-verify representative affected frontend pages at relevant viewport widths;
3. refresh affected design-system documentation and snapshots;
4. document intentional breaking changes or migration requirements.

## Before every write

1. Read this file.
2. Read the relevant project documentation.
3. Re-read the affected live MCP resources.
4. Inspect current plugin/data dependencies where relevant.
5. Inspect relevant browser references for visual work.
6. Reuse existing classes, variables, components, fields, queries, templates, and patterns where appropriate.
7. Avoid unrelated changes.
8. Use preview/planning capabilities when available.
9. Commit only the agreed scope.
10. Re-read persisted state.
11. Verify the rendered frontend where appropriate.
12. Update project documentation when architecture or design rules materially changed.

## Permission-aware behavior

The current MCP user may have fewer permissions than the user that created the bootstrap audit.

Never interpret inaccessible data as nonexistent.

Use these states when relevant:

- VERIFIED LIVE
- CACHED / PREVIOUSLY AUDITED
- LIVE ACCESS BLOCKED
- NOT VERIFIED

Do not attempt privilege escalation automatically.

## Plugin-aware workflow

Before creating new CPTs, taxonomies, fields, relationships, queries, forms, or commerce structures, inspect the existing plugin/data architecture first.

Do not recreate functionality already provided by an active integration unless the user explicitly requests a rearchitecture.

## Visual design verification

Bricks configuration alone is not sufficient for visual design work.

For substantial visual work:

- inspect relevant existing frontend references;
- inspect the target resource through MCP;
- reuse established site patterns;
- render and visually verify the result at relevant responsive widths.

Do not claim visual consistency based only on Bricks settings or JSON.

## WooCommerce

Always determine WooCommerce status before commerce-related work.

If active, inspect the existing WooCommerce and Bricks architecture before changing commerce layouts or dynamic data.

Never expose private customer/order data in documentation.

## Safety

Never execute PHP, modify plugins, alter plugin files, activate/deactivate plugins, or perform destructive global changes without explicit authorization.

Never make unrelated changes.
