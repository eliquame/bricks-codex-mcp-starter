# New Page Build Workflow

Use this prompt for creating a new Bricks page inside an already bootstrapped site project.

```text
Create a new Bricks page for the CURRENT project.

Do not start writing immediately.

DISCOVERY

1. Read AGENTS.md.
2. Read only the task-relevant docs/bricks references.
3. Re-read live design-system resources and relevant plugin/data dependencies.
4. Determine SITE_MATURITY and DESIGN_SYSTEM_AUTHORITY.
5. If ESTABLISHED or PARTIAL:
   - identify the closest existing pages/templates/patterns;
   - inspect their live Bricks structure;
   - inspect their rendered frontend at relevant widths.
6. If GREENFIELD:
   - verify that an approved design-system direction exists;
   - if not, stop and recommend/use the greenfield design-system seed workflow first.
7. Identify any dynamic-data, CPT, taxonomy, query, form, WooCommerce or framework dependencies.
8. Run an authoring preflight:
   - use bricks-plan-from-brief for broad/document-driven builds;
   - map semantic content patterns to the most appropriate Bricks elements;
   - use bricks-element-schemas for unfamiliar/complex elements and controls;
   - inspect existing media/custom icons before inventing/uploading assets;
   - inspect existing global classes/variables before new shared resources;
   - identify whether any requested styling can be expressed with native Bricks controls instead of custom CSS.

PLAN

Before writing, present a concise implementation plan covering:
- page purpose;
- element hierarchy;
- reusable existing patterns;
- classes/variables/tokens/components to reuse;
- new global resources, if any;
- dynamic-data/query dependencies;
- responsive behavior;
- visual references used;
- native element choices for structured content (lists, accordions, tabs, forms, media, etc.);
- any custom CSS/code that may be required and why native controls are insufficient;
- responsive strategy, including whether fluid/intrinsic values can avoid unnecessary breakpoint patches.

Avoid introducing new global resources unless existing ones are insufficient.

WRITE

After approval:
- create only the requested page;
- use the assigned project MCP server only;
- preserve provider ownership;
- use preview/dry-run/planning abilities where available;
- keep the implementation Bricks-native unless the project architecture requires another owner/provider layer;
- do not modify unrelated templates/settings/resources;
- do not use class-like names in CSS ID fields;
- use custom CSS only when no suitable Bricks control/class/variable/selector path exists;
- prefer existing/native List/Icon List/etc. over generic repeated Basic Text structures when semantically appropriate.

VERIFY

After writing:
1. re-read persisted page structure;
2. verify frontend rendering;
3. verify relevant desktop/tablet/mobile widths;
4. verify important interactions/conditions;
5. run the relevant Bricks quality gate;
6. check for unexpected global/cascade effects;
7. run the Bricks-native authoring review:
   - missed native elements;
   - unnecessary custom CSS;
   - CSS ID misuse;
   - missed global class/variable reuse;
   - brittle magic values/breakpoint patch chains;
   - missed media/icon reuse.

DOCUMENT

Create/update the page detail file and any indexes or pattern docs made stale by the new page.

Do not rewrite unrelated audit documentation.

FINAL REPORT

Report:
- page ID/slug;
- structure created;
- reused resources;
- new resources introduced;
- responsive verification;
- frontend verification;
- documentation updated;
- unresolved issues;
- custom CSS/code used and justification;
- native-authoring review findings/fixes.
```
