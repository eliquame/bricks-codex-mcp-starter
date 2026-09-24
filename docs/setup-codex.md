# Codex Project Setup

This guide is the manual/reference version of the automated `START-HERE.md` flow.

For normal use, create/open the target site's Codex project and paste the one-prompt bootstrap from the root README. Codex should initialize the project files itself.

## Global setup

Bricks skills are installed globally for Codex and do not need to be copied into every site project.

MCP connections are configured in the local Codex `config.toml`, with one uniquely named server block per connected site.

Typical paths:

Windows:

```text
%USERPROFILE%\.codex\config.toml
```

macOS / Linux:

```text
~/.codex/config.toml
```

## Per-site project

Use one local Codex project folder per website.

You do not need to manually create the starter files in the normal workflow.

`START-HERE.md` instructs Codex to create/merge:

```text
site-name-bricks/
├── AGENTS.md
└── docs/
    └── bricks/
        ├── README.md
        └── 00-bootstrap-status.md
```

The source for the baseline project policy is:

```text
project-starter/AGENTS.md
```

The full bootstrap audit then expands `docs/bricks/` with verified site-specific knowledge.

## Threads

Use separate Codex threads for focused work after bootstrap, for example:

- homepage;
- header/navigation;
- template work;
- responsive fixes;
- WooCommerce;
- design-system changes;
- plugin/data architecture changes.

The project files provide persistent context across threads.

## Bootstrap resume

MCP config changes or Bricks skill installation may require a new Codex chat or restart.

Before that happens, the setup flow stores progress in:

```text
docs/bricks/00-bootstrap-status.md
```

In the new chat, continue with:

```text
Continue the Bricks/Codex bootstrap from docs/bricks/00-bootstrap-status.md
```

## AGENTS lifecycle

- Baseline source: `project-starter/AGENTS.md`
- Automated setup/orchestration: `START-HERE.md`
- First full site discovery: `prompts/00-full-site-bootstrap-audit.md`
- Later synchronization after material changes: `prompts/90-agents-maintenance-and-sync.md`

The `templates/` folder contains audit/documentation templates. It is not the active project instruction location.

## Important

Local project documentation is a cached architectural reference, not a replacement for live MCP reads.

Before any site write, Codex should re-read the affected live resource and relevant dependencies.
