# Targeted Re-Audit Workflow

Use this after a material change when the full bootstrap audit does not need to be rerun.

```text
Run a READ-ONLY targeted re-audit of the requested project area.

1. Read AGENTS.md.
2. Read existing docs for the requested scope.
3. Re-read the current live resources.
4. Inspect rendered frontend where visual behavior is part of the scope.
5. Compare cached docs with current live state.
6. Update only stale documentation inside the requested scope.
7. Do not modify the WordPress / Bricks site.

Possible scopes include:
- design system;
- plugin ecosystem;
- ACF / JetEngine / ACPT data model;
- template routing;
- components;
- queries/dynamic data;
- WooCommerce architecture;
- a page family;
- responsive/visual patterns.

For each checked item classify:
- VERIFIED LIVE
- UPDATED
- ACCESS BLOCKED
- NOT APPLICABLE
- INSUFFICIENT EVIDENCE

Do not mark the targeted re-audit complete while discovered in-scope resources remain unchecked without a documented reason.

At the end report:
- scope;
- live resources checked;
- stale docs corrected;
- unresolved permission/evidence gaps;
- whether AGENTS.md now requires synchronization.
```
