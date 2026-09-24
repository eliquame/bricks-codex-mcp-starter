# Codex Project Setup

## Global setup

Bricks skills are installed globally for Codex and do not need to be copied into every site project.

The MCP connection is also configured globally in the local Codex `config.toml`, with one server block per connected site.

## Per-site project

Create one local project folder per website.

Before the first Codex thread, copy the contents of `project-starter/` from this repository into the new site project.

Recommended initial structure:

```text
site-name-bricks/
├── AGENTS.md
└── docs/
    └── bricks/
```

The copied `AGENTS.md` is the active baseline project policy from the first task. The bootstrap audit will refine its verified project profile and expand `docs/bricks/` with site-specific knowledge.

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


## AGENTS lifecycle

- Initial baseline: `project-starter/AGENTS.md`
- First site discovery: `prompts/00-full-site-bootstrap-audit.md`
- Later synchronization after material changes: `prompts/90-agents-maintenance-and-sync.md`

The `templates/` folder is for documentation templates; it is not the active project instruction location.
