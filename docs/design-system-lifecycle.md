# Design-System Lifecycle

## Purpose

This document defines how Codex should treat design systems across established, partial, and greenfield Bricks projects.

## Site maturity

### ESTABLISHED

A meaningful site and visual language already exist.

Codex should learn from:

- live Bricks structure;
- live plugin/framework state;
- rendered public frontend;
- documented recurring patterns.

Visual auditing is required for design/layout work.

### PARTIAL / IN PROGRESS

Some design decisions exist, but the system is incomplete.

Codex may document observed patterns, but it must distinguish:

- established rules;
- provisional patterns;
- experiments;
- unknowns.

Do not promote isolated examples to site-wide rules.

### GREENFIELD

No meaningful established site design exists yet.

The bootstrap audit should:

- map the technical environment;
- detect existing framework/providers;
- document any existing tokens/classes/settings;
- mark visual design evidence as insufficient when appropriate;
- avoid inventing a complete design language.

A separate approved design-system creation/seed task should come before broad page design.

## Design-system authority

Every project should classify its design-system authority as one of:

- BRICKS NATIVE
- EXTERNAL FRAMEWORK
- HYBRID
- CUSTOM CODE DRIVEN
- UNKNOWN / UNDEFINED

Document ownership for major resources:

- colors;
- typography;
- spacing;
- breakpoints;
- global classes;
- variables/tokens;
- components/patterns;
- theme-level rules.

## External CSS / design frameworks

If a plugin or integration such as Core Framework or another equivalent system provides classes, variables, or tokens:

- treat those resources as provider-owned;
- document where they are configured;
- document how they appear in Bricks;
- do not create redundant Bricks-native copies;
- do not edit provider-owned resources through the wrong layer;
- preserve provenance even when resources are mirrored into Bricks.

## Updating Theme Styles or other global resources

A global design-system change has a larger blast radius than a page-local change.

Before changing:

1. identify the authoritative owner;
2. read the current live state;
3. identify representative affected pages/templates;
4. capture the relevant pre-change state where practical;
5. understand whether the change is additive, compatible, or breaking.

After changing:

1. re-read persisted global state;
2. verify representative frontend pages;
3. verify relevant responsive widths;
4. inspect for regressions;
5. update local documentation and snapshots;
6. record intentional breaking changes and any migration requirement.

## Documentation freshness

When a design-system source changes, update the corresponding project documentation.

Typical affected files may include:

- design-system documentation;
- theme-style documentation;
- class/variable inventories;
- breakpoint documentation;
- visual-pattern documentation;
- site rules;
- framework/plugin-specific documentation.

Do not rerun the entire bootstrap audit unless the change is broad enough to invalidate the site's overall architectural model.
