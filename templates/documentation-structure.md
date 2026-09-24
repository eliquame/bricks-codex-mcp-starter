# Documentation Structure

The starter repository itself is site-agnostic.

The bootstrap prompt generates site-specific documentation inside the target Codex project.

Recommended target project structure:

```text
site-project/
├── AGENTS.md
└── docs/
    └── bricks/
        ├── 00-audit-progress.md
        ├── 00-site-overview.md
        ├── site-inventory.md
        ├── 01-plugin-ecosystem.md
        ├── 02-data-architecture.md
        ├── 03-design-system.md
        ├── 04-theme-styles.md
        ├── 05-global-classes.md
        ├── 06-global-variables.md
        ├── 07-colors-typography.md
        ├── 08-breakpoints.md
        ├── 09-templates.md
        ├── 10-components.md
        ├── 11-dynamic-data.md
        ├── 12-queries.md
        ├── 13-custom-code.md
        ├── 14-woocommerce.md
        ├── 15-frontend-visual-audit.md
        ├── 16-visual-patterns.md
        ├── 17-site-rules.md
        ├── 18-known-patterns.md
        ├── 19-audit-findings.md
        ├── pages/
        ├── templates/
        ├── plugins/
        ├── snapshots/
        └── visual-references/
```

The generated documentation is a durable cache/reference. It must never replace live verification before writes.
