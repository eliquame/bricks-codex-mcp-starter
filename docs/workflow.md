# Generic Bricks + Codex MCP Workflow

## 1. Open one Codex project per website

A website should normally map to one local Codex project.

The normal user flow does **not** require manually creating AGENTS/docs files.

Paste the root README bootstrap prompt into a new Codex chat. Codex reads `START-HERE.md` and initializes the current project itself.

## 2. Establish the Bricks MCP connection

The automated setup checks whether the intended Bricks MCP server is already loaded.

If not, it guides the required WordPress admin actions:

- enable Bricks abilities;
- install/activate the WordPress MCP Adapter;
- create/select a dedicated WordPress user;
- generate an Application Password;
- use the Bricks Codex **Paste config** block;
- merge that block into the existing Codex `config.toml`.

Credential-bearing config stays local and should not be pasted into chat.

Each site should use a unique MCP server name.

## 3. Initialize the project policy

Codex creates or merges project-root `AGENTS.md` from:

```text
project-starter/AGENTS.md
```

It also initializes `docs/bricks/` and a persistent bootstrap status file.

If MCP or skill loading requires a new chat/restart, resume from:

```text
docs/bricks/00-bootstrap-status.md
```

## 4. Install or verify Bricks skills

Get the MCP connection working first.

Then verify that client-side `bricks-` skills are loaded.

If not, follow the current Codex-compatible installation method from:

https://github.com/codeerhq/bricks-skills

Skills provide workflow guidance; they do not grant WordPress permissions.

## 5. Run the full bootstrap audit

Execute the starter repository's:

```text
prompts/00-full-site-bootstrap-audit.md
```

The audit first classifies:

- SITE_MATURITY: ESTABLISHED / PARTIAL / GREENFIELD;
- DESIGN_SYSTEM_STATE;
- DESIGN_SYSTEM_AUTHORITY.

It then builds the site-specific knowledge base covering, where relevant:

- plugin and integration ecosystem;
- data architecture;
- Bricks design system;
- templates;
- pages;
- components;
- dynamic data;
- queries;
- WooCommerce;
- rendered frontend and responsive visual patterns;
- external CSS/design-system providers;
- site-wide conventions and known exceptions.

For GREENFIELD projects, the audit must not invent a visual language from missing evidence. If the design system remains UNDEFINED or materially incomplete, run `prompts/11-greenfield-design-system-seed.md` before broad page construction.

## 6. Reduce permissions after bootstrap

A full read-only audit may need broader access than routine editing.

After the initial audit, reduce the MCP user's WordPress and Bricks permissions to the minimum needed for normal work.

The generated documentation remains useful, but it is cached knowledge. Future writes must re-read affected live resources.

## 7. Work in scoped threads

For a specific task:

1. read project `AGENTS.md`;
2. read only relevant documentation;
3. re-read affected live MCP resources;
4. inspect plugin/data/design-system ownership where relevant;
5. inspect browser references for visual work;
6. plan the smallest safe change;
7. write only the agreed scope;
8. re-read persisted state;
9. verify rendered frontend where appropriate;
10. update only documentation made stale by the change.

## 8. Handle global design-system changes

Theme Styles, global classes, global variables, breakpoints, and external framework tokens/classes are global-impact resources.

Use:

```text
prompts/10-design-system-change-workflow.md
```

The workflow verifies ownership, blast radius, persisted state, representative frontend output, and documentation updates.

## 9. Re-audit when needed

Do not rerun the entire bootstrap audit after every change.

Use targeted re-audits when:

- a major plugin is added/removed;
- design-system ownership or global resources materially change;
- template routing changes;
- CPT/field/query architecture changes;
- WooCommerce architecture changes;
- a large redesign is completed.

## 10. Maintain AGENTS.md

Do not recreate AGENTS.md for routine tasks.

Use:

```text
prompts/90-agents-maintenance-and-sync.md
```

only after material project evolution makes the site-specific project profile or routing stale.


## 11. Use task-specific workflows

After bootstrap, prefer the reusable workflow prompt that matches the task:

- new page: `prompts/20-new-page-build-workflow.md`
- existing page edit: `prompts/21-existing-page-edit-workflow.md`
- template change: `prompts/22-template-change-workflow.md`
- native-authoring quality review: `prompts/23-native-authoring-review.md`
- plugin/data architecture change: `prompts/30-plugin-data-architecture-change-workflow.md`
- WooCommerce: `prompts/31-woocommerce-workflow.md`
- targeted re-audit: `prompts/80-targeted-reaudit.md`

See `prompts/README.md` for the complete catalog.
