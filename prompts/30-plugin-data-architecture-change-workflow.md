# Plugin / Data Architecture Change Workflow

Use this when changing CPTs, taxonomies, custom fields, option pages, relationships, queries, listings, forms, dynamic visibility, or plugin-owned data structures.

```text
Perform the requested data/plugin architecture change in the CURRENT project.

This workflow may affect Bricks templates/pages indirectly, so map dependencies before writing.

DISCOVERY

1. Read AGENTS.md.
2. Read plugin ecosystem and data architecture docs.
3. Detect the owning provider for the requested resource:
   - WordPress core
   - ACF
   - JetEngine
   - ACPT
   - Meta Box
   - WooCommerce
   - another plugin
   - custom code
4. Re-read the current live provider state through authorized tools.
5. Map consumers:
   - Bricks templates/pages
   - queries
   - dynamic tags
   - relationships
   - frontend forms
   - WooCommerce integration
   - APIs/feeds where relevant.
6. Do not treat unavailable provider admin access as proof that the resource is absent.

PLAN

Before writing, report:
- owner/provider;
- existing schema;
- requested schema change;
- affected consumers;
- migration/backfill need;
- rollback considerations;
- permissions required.

If a provider-native admin/write path is unavailable, stop rather than writing raw database/plugin internals.

WRITE

After approval:
- modify the resource through its authoritative provider layer;
- preserve existing identifiers when compatibility matters;
- do not create duplicate fields/CPTs/relationships;
- do not delete/migrate existing data without explicit approval.

VERIFY

After writing:
1. re-read provider state;
2. verify Bricks dynamic bindings/query consumers;
3. verify representative frontend output;
4. verify no unrelated schema changed.

DOCUMENT

Update plugin/data architecture docs, dynamic-data/query docs, affected page/template docs, and AGENTS profile only when materially required.

FINAL REPORT

Report:
- provider;
- schema change;
- consumers verified;
- migration performed/not performed;
- frontend verification;
- documentation updated.
```
