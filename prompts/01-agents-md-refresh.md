# AGENTS.md Refresh Prompt

Use this after a bootstrap audit or a material architecture change.

```text
Update the project-root AGENTS.md for the long-term Bricks + Codex MCP workflow.

First read:
- the existing AGENTS.md;
- the current docs/bricks site documentation;
- the current audit findings and site rules.

Preserve useful existing instructions.
Do not blindly replace the file.
Keep AGENTS.md concise and operational.
Detailed site knowledge belongs under docs/bricks/.

Ensure AGENTS.md clearly defines:

1. Site identity and the single allowed MCP server for this project.
2. Live Bricks MCP as the source of truth for current Bricks structure.
3. Live plugin/runtime state as the source of truth for integrations.
4. Rendered frontend as the source of truth for actual visual appearance.
5. Local docs as cached reference rather than guaranteed current state.
6. Mandatory live re-read before writes.
7. Plugin/data architecture checks before creating CPTs, taxonomies, fields, relationships, queries, forms, or commerce structures.
8. Browser inspection before and after substantial visual work.
9. Permission-aware behavior: inaccessible does not mean nonexistent.
10. WooCommerce status checks and safe handling when active.
11. Documentation refresh rules after material changes.
12. No automatic privilege escalation.
13. No PHP execution, plugin modification, or destructive global changes without explicit authorization.
14. No unrelated changes.

If a previous full audit used elevated permissions but routine work now uses a restricted account, explicitly document that distinction.

After updating AGENTS.md:
- summarize what changed;
- identify any conflicting old instruction;
- do not modify the WordPress / Bricks site as part of this task.
```
