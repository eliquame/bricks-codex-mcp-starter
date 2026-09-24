# START HERE — One-prompt Codex bootstrap

This file is meant to be executed by Codex inside the **target site's Codex project**.

The user should not manually create `AGENTS.md`, `docs/bricks/`, or copy starter files. Codex must initialize and maintain those files itself from this repository.

---

## Prompt for Codex

```text
Bootstrap the CURRENT Codex project for a WordPress + Bricks Builder site using this starter repository:

https://github.com/eliquame/bricks-codex-mcp-starter

GOAL

From this point onward, do the setup yourself as far as your available tools allow.

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
- restarting/reopening Codex;
- granting a missing permission.

SECURITY

- Never ask me to paste a WordPress Application Password, normal WordPress password, API key, PAT, token, or other credential into chat.
- Never echo credentials from local files.
- If you inspect config.toml, redact secret values in anything you display.
- Prefer Bricks "Paste config" over Bricks "Copy a prompt" because the latter may include credentials.
- Do not enable PHP abilities.
- Do not modify the WordPress / Bricks site during bootstrap discovery.
- Local project files may be created and edited.

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
- continue automatically once access exists.

Read at minimum:

- project-starter/AGENTS.md
- prompts/00-full-site-bootstrap-audit.md
- prompts/02-design-system-change-workflow.md
- prompts/90-agents-maintenance-and-sync.md
- docs/setup-bricks-mcp.md
- docs/setup-codex.md
- docs/security.md
- docs/workflow.md
- docs/design-system-lifecycle.md
- templates/documentation-structure.md

PHASE B — INITIALIZE THE CURRENT SITE PROJECT

Treat the CURRENT working directory as the site-specific Codex project.

1. If project-root AGENTS.md does not exist:
   - create it from project-starter/AGENTS.md.

2. If AGENTS.md already exists:
   - read it first;
   - merge the starter rules into it;
   - preserve useful existing site-specific instructions;
   - do not blindly overwrite it.

3. Ensure:
   docs/bricks/
   exists.

4. If docs/bricks/README.md does not exist, initialize it from:
   project-starter/docs/bricks/README.md

5. Do not create empty audit documents yet merely to satisfy a template.
   The bootstrap audit will create only the documents supported by real site evidence.

6. Do not copy any site-specific documentation from another project.

PHASE C — CHECK BRICKS MCP CONNECTION

First inspect the currently loaded Codex MCP servers/tools.

If the correct Bricks site MCP is already connected:
- identify it;
- perform read-only diagnostic discovery;
- continue.

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

If you can open/edit the file locally:
- preserve all existing configuration;
- add the Bricks-generated MCP block as a new unique [mcp_servers.<site-name>] section;
- let me paste the secret-bearing block directly into the local file if user interaction is required;
- do not display the secret.

If you cannot edit it safely:
- open/show me the exact file path;
- tell me exactly where to paste the Bricks-generated block;
- do not ask me to paste it into chat.

Never:
- overwrite unrelated config;
- nest the new MCP block inside another server section;
- define the same MCP server name twice.

After saving:
- start a fresh Codex chat if MCP reload requires it;
- if needed, fully restart Codex;
- continue verification afterward.

PHASE D — VERIFY MCP READ-ONLY

Use read-only Bricks diagnostics available in the current host, including the equivalents of:

- bricks-start-here
- bricks/get-mcp-version
- bricks/list-ability-status

Verify:
- server connected;
- Bricks abilities visible;
- current WordPress permissions are sufficient for discovery.

Do not modify the site.

If access is restricted:
- distinguish "resource absent" from "permission blocked";
- report the missing access;
- do not automatically request privilege escalation.

PHASE E — INSTALL OR VERIFY BRICKS SKILLS

Check whether client-side skills beginning with `bricks-` are already loaded.

If loaded:
- list/verify them;
- continue.

If not loaded:
- use the current official Bricks Skills install workflow;
- read the Bricks Skills source/readme:
  https://github.com/codeerhq/bricks-skills
- install them using the Codex-compatible method described by that repository;
- prefer the latest appropriate public release/install method;
- start a fresh Codex chat or restart only if required;
- verify the loaded `bricks-` skills.

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
4. enforce project isolation: this project may use only that site's MCP server unless explicitly instructed otherwise.

Do not guess site identity.

PHASE G — RUN THE FULL BOOTSTRAP AUDIT

Now read and execute:

prompts/00-full-site-bootstrap-audit.md

Run it against the connected target site.

Important:
- remote site remains READ-ONLY for this bootstrap;
- local project files are writable;
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

Do not report or expose secrets.

If the bootstrap required temporarily elevated WordPress permissions, remind me that routine work should use the minimum permissions needed after the audit.

Do not make any site write after the audit unless I explicitly request a new task.
```
