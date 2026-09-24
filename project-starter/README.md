# Site Project Starter

This folder contains the files that should exist in a new local Codex project **before the first site-specific thread is started**.

Copy the contents of this folder into the root of the new site's Codex project.

Expected initial structure:

```text
your-site-project/
├── AGENTS.md
└── docs/
    └── bricks/
        └── README.md
```

Then:

1. connect the intended WordPress / Bricks site through MCP;
2. open this folder as the Codex project;
3. start a new Codex thread;
4. run `prompts/00-full-site-bootstrap-audit.md` from the starter repository;
5. allow the bootstrap audit to populate `docs/bricks/` and refine the PROJECT PROFILE in `AGENTS.md` with verified site-specific facts.

The default `AGENTS.md` is deliberately site-agnostic. It already contains the baseline Bricks/MCP workflow, safety, source-of-truth, visual verification, plugin/data, WooCommerce, permission, and design-system ownership rules.

Do not place MCP credentials, WordPress Application Passwords, or Codex `config.toml` inside the site project.
