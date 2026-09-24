# Greenfield Design-System Seed Workflow

Use this prompt when the bootstrap classified the project as GREENFIELD and the design system is UNDEFINED or materially incomplete.

```text
We are defining the first approved design-system foundation for the CURRENT Bricks project.

This is NOT a generic styling exercise. Build a deliberate, documented foundation that future pages can reuse.

Before any write:

1. Read project-root AGENTS.md.
2. Read docs/bricks/00-site-state.md if present.
3. Read docs/bricks/design-system-authority.md and docs/bricks/03-design-system.md if present.
4. Inspect live Bricks Theme Styles, global classes, variables, breakpoints, components and site settings.
5. Inspect active CSS/design-system providers or frameworks.
6. Determine DESIGN_SYSTEM_AUTHORITY and ownership before creating resources.
7. Inspect any user-provided brief, brand guide, Figma, screenshots, existing assets or visual references.

If the visual direction is not sufficiently specified, STOP before building a broad design system and ask for the missing design input.

Do not invent a brand identity from generic defaults.

DEFINE THE FOUNDATION

Propose a compact V1 covering only the system needed for upcoming page work:

- color tokens
- typography roles
- spacing scale
- content/container widths
- breakpoints strategy
- radii
- borders
- shadows where needed
- buttons
- common section spacing
- basic grid/flex conventions
- class naming convention
- variable/token naming convention

When an external framework already owns any of these:
- configure/use the provider-owned layer;
- do not duplicate equivalent Bricks-native resources.

Before writing, show:
- proposed token/class structure;
- ownership for each layer;
- what will be created vs. reused;
- any assumptions requiring approval.

APPLY

After approval:

1. create only the agreed global resources;
2. keep names systematic and reusable;
3. avoid page-specific styling in the global foundation;
4. do not build unrelated pages/templates.

VERIFY

After writing:

1. re-read persisted design-system state;
2. confirm no duplicate resources were introduced;
3. create or use the smallest safe representative test context if needed and explicitly approved;
4. visually verify at relevant viewport widths;
5. document the resulting system.

UPDATE DOCUMENTATION

Update where relevant:

- docs/bricks/design-system-authority.md
- docs/bricks/03-design-system.md
- docs/bricks/04-theme-styles.md
- docs/bricks/05-global-classes.md
- docs/bricks/06-global-variables.md
- docs/bricks/07-colors-typography.md
- docs/bricks/08-breakpoints.md
- docs/bricks/17-site-rules.md
- project-root AGENTS.md project profile

FINAL REPORT

Report:
- authority/provider used;
- global resources created;
- resources reused;
- naming conventions established;
- responsive strategy;
- visual verification performed;
- documentation updated;
- remaining design decisions not yet defined.
```
