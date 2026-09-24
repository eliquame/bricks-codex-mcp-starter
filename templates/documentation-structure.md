# Documentation Structure

The starter repository itself is site-agnostic.

A new site-specific Codex project starts from:

```text
site-project/
├── AGENTS.md
└── docs/
    └── bricks/
        └── README.md
```

The automated START-HERE flow first creates `00-bootstrap-status.md` to persist setup/resume state. The full bootstrap audit then creates `00-audit-progress.md` and expands `docs/bricks/` according to the resources that actually exist on the target site.

Recommended generated structure:

```text
site-project/
├── AGENTS.md
└── docs/
    └── bricks/
        ├── 00-bootstrap-status.md
        ├── 00-audit-progress.md
        ├── 00-site-overview.md
        ├── 00-site-state.md
        ├── site-inventory.md
        ├── site-settings.md
        │
        ├── 01-plugin-ecosystem.md
        ├── 02-data-architecture.md
        │
        ├── 03-design-system.md
        ├── design-system-authority.md
        ├── 04-theme-styles.md
        ├── 05-global-classes.md
        ├── 06-global-variables.md
        ├── 07-colors-typography.md
        ├── 08-breakpoints.md
        │
        ├── 09-templates.md
        ├── pages-index.md
        ├── 10-components.md
        ├── 11-dynamic-data.md
        ├── 12-queries.md
        ├── 13-custom-code.md
        ├── 14-woocommerce.md
        │
        ├── 15-frontend-visual-audit.md
        ├── 16-visual-patterns.md
        ├── 17-site-rules.md
        ├── 18-known-patterns.md
        ├── 19-audit-findings.md
        │
        ├── pages/
        │   └── <page-slug>.md
        ├── templates/
        │   └── <template-name>.md
        ├── plugins/
        │   └── <plugin-or-provider>.md
        ├── snapshots/
        │   ├── site-inventory.json
        │   ├── design-system.json
        │   ├── design-system-authority.json
        │   ├── site-settings.json
        │   ├── template-architecture.json
        │   ├── page-architecture.json
        │   ├── dynamic-dependencies.json
        │   ├── audit-findings.json
        │   └── other useful machine-readable snapshots
        └── visual-references/
            └── browser captures where useful
```

## Conditional files

The structure is intentionally conditional.

Examples:

- `01-plugin-ecosystem.md` is useful on every non-trivial site, but plugin-specific detail files are created only for architecture-relevant plugins/providers.
- `02-data-architecture.md` becomes deeper when ACF, JetEngine, ACPT, Meta Box, custom CPTs/fields, relationships, or other data systems are present.
- `14-woocommerce.md` is required only when WooCommerce is installed/active; otherwise status can be recorded without inventing content.
- deep frontend visual references are required for ESTABLISHED sites, limited for PARTIAL sites, and may be NOT APPLICABLE / INSUFFICIENT EVIDENCE on GREENFIELD sites.
- empty files should not be created merely to satisfy a template.

## Setup status vs. audit progress

- `00-bootstrap-status.md` tracks orchestration: MCP setup, skills loading, project initialization, restart/resume state.
- `00-audit-progress.md` tracks actual site-discovery coverage.

They are intentionally separate.

## Why both Markdown and JSON?

Markdown files are the durable human/agent-facing architectural reference.

JSON snapshots are useful for:

- compact machine-readable inventories;
- change comparison;
- dependency mapping;
- resuming interrupted audits;
- verifying whether cached architecture has materially changed.

Snapshots are still cached data. They never replace current live MCP verification before writes.

## Proven useful audit outputs

Real bootstrap testing showed that the following artifacts are especially useful across later Codex threads:

- a page index plus individual page detail files;
- a template index plus individual template detail files;
- a dedicated site-settings reference;
- design-system/class/variable/breakpoint references;
- frontend visual audit;
- site rules and known-pattern documents;
- machine-readable page/template architecture and dependency snapshots.

The generic starter keeps these concepts while allowing additional plugin/data/framework documentation when the target site requires it.
