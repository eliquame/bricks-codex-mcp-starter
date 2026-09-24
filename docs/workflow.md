# Generic Bricks + Codex MCP Workflow

## 1. Connect the site

Configure Bricks AI abilities and the WordPress MCP Adapter on the target site. Create a dedicated WordPress user and Application Password, then add that site's MCP server block to the local Codex configuration.

Each site should use a unique MCP server name.

## 2. Create one Codex project per website

A website should normally map to one local Codex project.

Example:

```text
my-site-bricks/
├── AGENTS.md
└── docs/
    └── bricks/
```

Use separate Codex threads for separate pages, features, or workstreams.

## 3. Run the bootstrap audit

Run `prompts/00-full-site-bootstrap-audit.md` in a fresh thread.

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
- rendered frontend and responsive visual patterns;
- site-wide conventions and known exceptions.

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

## 6. Re-audit when needed

Do not rerun the entire bootstrap audit after every change.

Use targeted re-audits when:

- a major plugin is added/removed;
- the design system changes;
- template routing changes;
- CPT/field/query architecture changes;
- WooCommerce architecture changes;
- a large redesign is completed.
