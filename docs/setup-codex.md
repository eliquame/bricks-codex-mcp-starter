# Codex Project Setup

## Global setup

Bricks skills are installed globally for Codex and do not need to be copied into every site project.

The MCP connection is also configured globally in the local Codex `config.toml`, with one server block per connected site.

## Per-site project

Create one local project folder per website.

Recommended minimal structure:

```text
site-name-bricks/
├── AGENTS.md
└── docs/
    └── bricks/
```

The bootstrap audit will expand `docs/bricks/` with site-specific knowledge.

## Threads

Use separate Codex threads for focused work:

- bootstrap audit;
- homepage;
- header/navigation;
- template work;
- responsive fixes;
- WooCommerce;
- design-system cleanup;
- plugin/data architecture changes.

The project files provide persistent context across threads.

## Important

The local project documentation is a cached architectural reference, not a replacement for live MCP reads.

Before any write, Codex should re-read the affected live resource.
