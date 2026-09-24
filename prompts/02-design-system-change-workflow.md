# Design-System Change Workflow Prompt

Use this prompt for changes to Bricks Theme Styles, global classes, global variables, external CSS-framework tokens/classes, or other site-wide design-system resources.

```text
We are performing a controlled global design-system change on the currently connected Bricks project.

This task MAY modify the live site, but only within the explicitly approved design-system scope.

Before any write:

1. Read AGENTS.md.
2. Read the relevant docs/bricks design-system documentation.
3. Determine SITE_MATURITY.
4. Determine DESIGN_SYSTEM_STATE.
5. Determine DESIGN_SYSTEM_AUTHORITY.
6. Identify the exact owner/provider of the resource being changed.

Possible ownership includes:

- BRICKS OWNED
- FRAMEWORK / PLUGIN OWNED
- THEME / CHILD-THEME OWNED
- CUSTOM-CODE OWNED
- UNKNOWN

If ownership is unclear, STOP before writing and report what must be resolved.

If an external framework owns the resource, do not create a duplicate Bricks-native replacement unless explicitly requested.

If the project is GREENFIELD or the design system is UNDEFINED, distinguish between:

A. creating/seeding the design system
B. modifying an existing design system

Do not silently invent a full design system while performing what was requested as a small update.

PRE-CHANGE IMPACT CHECK

Inspect:

- current live value/state
- relevant classes/variables/theme styles/tokens
- affected or representative templates
- affected or representative pages
- relevant visual references
- responsive implications
- plugin/framework dependencies

Where practical, preserve a machine-readable or documented pre-change snapshot in the local project.

Before applying the change, summarize:

- what will change
- which layer owns it
- why this layer is the correct place to change it
- likely blast radius
- representative pages/templates that will be verified afterward

Do not make unrelated cleanup changes.

APPLY

Apply only the approved design-system change.

POST-WRITE VERIFICATION

After the change:

1. re-read the persisted source-of-truth state;
2. verify that no duplicate class/variable/token was introduced;
3. inspect representative frontend pages in the browser;
4. verify relevant responsive viewport widths;
5. compare against the expected visual result;
6. identify regressions or unexpected cascade effects;
7. correct only regressions caused by this approved change, unless further approval is required.

DOCUMENTATION

Update only the project documentation made stale by this change.

This may include:

- design-system authority
- theme styles
- global classes
- global variables
- typography/colors
- breakpoints
- provider/plugin documentation
- visual patterns
- site rules

Do not regenerate unrelated audit documents.

FINAL REPORT

Report:

- exact resource changed
- owner/provider
- old state
- new state
- affected references checked
- viewport checks performed
- any regressions found
- documentation updated
- any follow-up migration or cleanup that still requires approval
```
