# Generic Bricks + Codex MCP Workflow

## 1. Connect the site

Configure Bricks AI abilities and the WordPress MCP Adapter on the target site. Create a dedicated WordPress user and Application Password, then add that site's MCP server block to the local Codex configuration.

Each site should use a unique MCP server name.

## 2. Create one Codex project per website

A website should normally map to one local Codex project.

Before the first thread, copy the contents of `project-starter/` from this repository into the new project root.

Initial structure:

```text
my-site-bricks/
├── AGENTS.md
└── docs/
    └── bricks/
        └── README.md
```

The project-root `AGENTS.md` is the canonical baseline policy and must be active from the first task. It is not generated from scratch by the bootstrap audit.

Use separate Codex threads for separate pages, features, or workstreams.

## 3. Run the bootstrap audit

Run `prompts/00-full-site-bootstrap-audit.md` in a fresh thread.

The audit refines the existing AGENTS project profile with verified site-specific facts and expands `docs/bricks/` into the durable site knowledge base.

The audit first classifies site maturity (ESTABLISHED, PARTIAL / IN PROGRESS, or GREENFIELD) and design-system authority (Bricks-native, external framework, hybrid, custom-code-driven, or undefined).

The audit should build a persistent site-specific knowledge base covering:

- plugin and integration ecosystem;
- data architecture;
- Bricks design system;
- templates;
- pages;
- components;
- dynamic data;
- queries;
- WooCommerce when active;
- rendered frontend and responsive visual patterns when meaningful public references exist;
- design-system ownership/provenance, including external CSS frameworks when present;
- site-wide conventions and known exceptions.

For GREENFIELD projects, the audit must not invent a visual language from missing evidence. A separate design-system creation/seed workflow should precede broad page design.

## 4. Reduce permissions

After the initial full audit, reduce the MCP user's WordPress and Bricks permissions to the minimum needed for normal editing.

The generated project documentation remains useful, but it is cached knowledge. Future writes must re-read the affected live resources.

## 5. Work in scoped threads

For a specific task:

1. read the project `AGENTS.md`;
2. read only the relevant documentation;
3. re-read the affected live MCP resources;
4. inspect relevant browser references for visual work;
5. plan the smallest safe change;
6. write only the agreed scope;
7. re-read persisted state;
8. verify the rendered frontend;
9. update local documentation when the architecture or design rules materially changed.

## 6. Handle global design-system changes

Treat Theme Styles, global classes, global variables, and external framework tokens/classes as global-impact resources.

For global changes:

1. verify which system owns the resource;
2. identify representative affected pages/templates;
3. capture relevant pre-change state where practical;
4. make the scoped change;
5. re-read persisted state;
6. browser-verify representative pages at relevant viewport widths;
7. refresh affected documentation and snapshots.

Use `prompts/02-design-system-change-workflow.md` for this class of task.

## 7. Re-audit when needed

Do not rerun the entire bootstrap audit after every change.

Use targeted re-audits when:

- a major plugin is added/removed;
- the design system changes;
- template routing changes;
- CPT/field/query architecture changes;
- WooCommerce architecture changes;
- a large redesign is completed.


## 8. Maintain AGENTS.md

Do not recreate AGENTS.md for routine tasks.

Use `prompts/90-agents-maintenance-and-sync.md` only after a material project change, re-audit, permission-model change, or other event that makes the site-specific project profile/routing stale.
