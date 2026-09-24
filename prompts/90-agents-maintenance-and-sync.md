# AGENTS.md Maintenance & Synchronization Prompt

Use this later in an existing site project when the active project-root `AGENTS.md` needs to be synchronized after a targeted re-audit, permission-model change, plugin/data architecture change, design-system change, or other material project evolution.

This is **not** the initial AGENTS.md. New projects should start from `project-starter/AGENTS.md`.

```text
Synchronize the project-root AGENTS.md with the verified current project state.

First read:
- the existing project-root AGENTS.md;
- the task-relevant docs/bricks documentation;
- current site rules and audit findings;
- the current live MCP state required to verify any facts you plan to change.

Preserve the general safety, source-of-truth, permission-aware, visual-verification,
plugin-aware, design-system ownership, and write-verification rules unless the user
explicitly changes them.

Update site-specific facts only from verified evidence.

Check and refresh where relevant:

1. Site identity and allowed MCP server.
2. Bootstrap/audit status.
3. SITE_MATURITY.
4. DESIGN_SYSTEM_STATE.
5. DESIGN_SYSTEM_AUTHORITY.
6. Primary CSS/design-system provider.
7. Primary data/content providers.
8. WooCommerce status.
9. Site-specific documentation routing and important references.
10. Permission-model notes.
11. Framework/provider ownership rules.
12. Any site-specific workflow rule that became stale after a material architecture change.

Do not turn AGENTS.md into a full site dump.
Detailed architecture belongs under docs/bricks/.

If documentation and accessible live state disagree, use the relevant live source
and explicitly identify the stale cached reference.

Do not modify the WordPress / Bricks site as part of this AGENTS.md synchronization task.

After updating AGENTS.md:
- summarize exactly what changed;
- identify any previous instruction that conflicted with verified current state;
- list any facts that remain unverified because of permissions or missing evidence.
```
