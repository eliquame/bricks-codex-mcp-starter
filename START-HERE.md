# START HERE — One-prompt Codex bootstrap

This file is meant to be executed by Codex inside the **target site's Codex project**.

The user should not manually create `AGENTS.md`, `docs/bricks/`, audit files, or copy starter files. Codex initializes and maintains them from this repository.

---

## Prompt for Codex

```text
Bootstrap the CURRENT Codex project for a WordPress + Bricks Builder site using this starter repository:

https://github.com/eliquame/bricks-codex-mcp-starter

GOAL

Do the setup yourself as far as your available tools allow.

Do NOT ask me to manually create:
- AGENTS.md
- docs/bricks/
- starter files
- audit files
- documentation folders

Create, merge, and maintain those local project files yourself from this repository.

Only stop for user action when one of these is genuinely required:
- a WordPress admin UI action;
- entering or pasting a secret locally;
- authorizing GitHub access;
- starting a new Codex chat or restarting Codex;
- granting a missing permission.

SECURITY

- Never ask me to paste a WordPress Application Password, normal WordPress password, API key, PAT, token, or other credential into chat.
- Never echo credentials from local files.
- If you inspect config.toml, redact secret values from anything you display.
- Prefer Bricks "Paste config" over Bricks "Copy a prompt" because the latter may include credentials.
- Do not enable PHP abilities.
- Do not modify the WordPress / Bricks site during bootstrap discovery.
- Local project files may be created and edited.

PERSISTENT BOOTSTRAP STATE

Create and maintain:

docs/bricks/00-bootstrap-status.md

before any step that may require a new Codex chat or restart.

At minimum record:
- bootstrap status: IN PROGRESS / COMPLETE / BLOCKED
- current phase
- target site if known
- assigned MCP server if known
- MCP connection status
- Bricks skills status
- AGENTS.md status
- last completed action
- exact next action
- blockers, without secrets

Update this file after every completed phase.

If a new chat/restart is required, save progress first and tell me to open a new Codex chat and say:

Continue the Bricks/Codex bootstrap from docs/bricks/00-bootstrap-status.md

In a resumed chat, read AGENTS.md and docs/bricks/00-bootstrap-status.md first, then continue from the recorded phase instead of restarting from the beginning.

PHASE A — LOAD THIS STARTER REPOSITORY

Use an authorized method already available in this Codex environment.

Preferred order:
1. GitHub connector/MCP if available;
2. authenticated `gh` CLI if available;
3. authenticated `git` clone into a temporary directory outside the target project.

Do not clone the starter repository into the target site project itself.

If this private repository is not accessible:
- do not ask for a GitHub token in chat;
- ask me to authorize/connect GitHub access;
- continue once access exists.

Read at minimum from the STARTER REPOSITORY, not from the target project:

- project-starter/AGENTS.md
- project-starter/docs/bricks/README.md
- prompts/00-full-site-bootstrap-audit.md
- prompts/10-design-system-change-workflow.md
- prompts/90-agents-maintenance-and-sync.md
- docs/setup-bricks-mcp.md
- docs/setup-codex.md
- docs/security.md
- docs/workflow.md
- docs/design-system-lifecycle.md
- templates/audit-progress.template.md
- templates/documentation-structure.md

Keep the starter repository source location/reference available for later phases.
Do not assume these starter files exist inside the target project.

PHASE B — INITIALIZE THE CURRENT SITE PROJECT

Treat the CURRENT working directory as the site-specific Codex project.

1. If project-root AGENTS.md does not exist:
   - create it from the starter repository's project-starter/AGENTS.md.

2. If AGENTS.md already exists:
   - read it first;
   - merge the starter rules into it;
   - preserve useful existing site-specific instructions;
   - do not blindly overwrite it.

3. Ensure:
   docs/bricks/
   exists.

4. If docs/bricks/README.md does not exist:
   - initialize it from the starter repository's project-starter/docs/bricks/README.md.

5. Create/update:
   docs/bricks/00-bootstrap-status.md

6. Do not create empty audit documents merely to satisfy a template.
   The full bootstrap audit will create only documentation supported by real site evidence.

7. Do not copy site-specific documentation from another project.

PHASE C — CHECK BRICKS MCP CONNECTION

Inspect the currently loaded Codex MCP servers/tools.

If exactly one suitable Bricks site MCP is already connected:
- identify it;
- perform read-only diagnostic discovery;
- continue.

If multiple Bricks site MCP servers are available and the intended target is ambiguous:
- stop before any site operation;
- ask me which site this project belongs to.

If no Bricks MCP server is connected, guide me interactively through the minimum required WordPress setup.

WordPress steps:
1. Bricks > AI > Configuration
2. Enable Bricks abilities
3. Install/activate WordPress MCP Adapter if required
4. Confirm MCP server connected
5. Select/create a dedicated WordPress user for Codex where practical
6. Generate a WordPress Application Password
7. Select Codex client
8. Use "Paste config"

IMPORTANT:
Do not ask me to paste the credential-bearing config block into chat.

Locate the global Codex config:

Windows:
%USERPROFILE%\.codex\config.toml

macOS/Linux:
~/.codex/config.toml

If you can safely open/edit the file locally:
- preserve all existing configuration;
- add the Bricks-generated MCP block as a new unique [mcp_servers.<site-name>] section;
- let me paste the secret-bearing block directly into the local file if user interaction is required;
- do not display the secret.

If you cannot safely edit it:
- show me the exact file path;
- tell me exactly where to paste the Bricks-generated block;
- do not ask me to paste it into chat.

Never:
- overwrite unrelated config;
- nest the new MCP block inside another server section;
- define the same MCP server name twice;
- move WP_API_PASSWORD into the endpoint URL, command arguments, or global shell config.

If Bricks generated NODE_TLS_REJECT_UNAUTHORIZED=0 for a local/self-signed development site, keep it scoped only to that MCP server.

Before asking for a new chat/restart, update docs/bricks/00-bootstrap-status.md.

After saving:
- start a fresh Codex chat so MCP configuration reloads;
- if the MCP server still does not appear, fully restart Codex;
- resume from docs/bricks/00-bootstrap-status.md.

PHASE D — VERIFY MCP READ-ONLY

Use read-only Bricks diagnostics available in the current host, including the equivalents of:

- bricks-start-here
- bricks/get-mcp-version
- bricks/list-ability-status

If a diagnostic ability is not exposed as a direct tool, use the MCP Adapter dispatcher when available.

Verify:
- server connected;
- Bricks version/abilities visible;
- current WordPress permissions are sufficient for the intended discovery.

Do not modify the site.

If access is restricted:
- distinguish "resource absent" from "permission blocked";
- record the limitation;
- do not automatically request privilege escalation.

PHASE E — INSTALL OR VERIFY BRICKS SKILLS

Check whether client-side skills beginning with `bricks-` are already loaded.

If loaded:
- list/verify them;
- record success;
- continue.

If not loaded:
- use the current official Bricks Skills install workflow;
- read the Bricks Skills repository/readme:
  https://github.com/codeerhq/bricks-skills
- install them using the current Codex-compatible method described by that repository;
- prefer the latest appropriate public release/install method;
- verify the installed skill names.

If skill loading requires a new Codex chat or restart:
- update docs/bricks/00-bootstrap-status.md first;
- tell me to open a new chat and say:
  Continue the Bricks/Codex bootstrap from docs/bricks/00-bootstrap-status.md
- then verify loaded `bricks-` skills in the resumed chat.

Do not confuse:
- MCP site abilities
with
- client-side Bricks skills.

Skills add workflow guidance, not WordPress permissions.

PHASE F — DETERMINE TARGET SITE IDENTITY

Before the full audit:

1. identify the connected site;
2. identify the exact MCP server name assigned to this project;
3. update the PROJECT PROFILE in project-root AGENTS.md with verified values only;
4. enforce project isolation: this project may use only that site's MCP server unless explicitly instructed otherwise;
5. update docs/bricks/00-bootstrap-status.md.

Do not guess site identity.

PHASE G — RUN THE FULL BOOTSTRAP AUDIT

Read and execute the content of this file FROM THE STARTER REPOSITORY:

prompts/00-full-site-bootstrap-audit.md

Do not assume that prompt file exists inside the target project.

Run it against the connected target site.

Important:
- remote site remains READ-ONLY for this bootstrap;
- local project files are writable;
- use templates/audit-progress.template.md from the starter repository as the baseline for the audit progress document;
- inspect the plugin/data ecosystem;
- determine site maturity;
- determine design-system state and ownership;
- inspect WooCommerce status every time;
- inspect ACF / JetEngine / ACPT / Meta Box / other systems only when present;
- inspect external CSS/design-system frameworks when present;
- inspect Bricks pages/templates/resources;
- for established or partially established sites, inspect the real public frontend in the browser and derive visual/layout rules from actual rendered evidence;
- for greenfield sites, do not invent a visual language from missing evidence.

Populate docs/bricks/ with the site-specific knowledge base.

Refine project-root AGENTS.md using verified project facts while preserving the general starter policy.

Keep docs/bricks/00-bootstrap-status.md separate from docs/bricks/00-audit-progress.md:
- bootstrap status tracks setup/orchestration;
- audit progress tracks site discovery coverage.

PHASE H — FINAL CHECK

At the end report:

- target site
- allowed MCP server
- MCP connection status
- Bricks skills status
- AGENTS.md status
- docs/bricks knowledge-base status
- SITE_MATURITY
- DESIGN_SYSTEM_STATE
- DESIGN_SYSTEM_AUTHORITY
- primary data/content providers
- primary CSS/design-system provider
- WooCommerce status
- bootstrap audit COMPLETE / PARTIAL
- any permissions that limited the audit

Update docs/bricks/00-bootstrap-status.md to:
- COMPLETE if setup/orchestration finished, even if the site audit is PARTIAL for documented reasons;
- BLOCKED if a setup requirement still prevents continuation.

Do not report or expose secrets.

If the bootstrap required temporarily elevated WordPress permissions, remind me that routine work should use the minimum permissions needed after the audit.

Do not make any site write after the audit unless I explicitly request a new task.
```
