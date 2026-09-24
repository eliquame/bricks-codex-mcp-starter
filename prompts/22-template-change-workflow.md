# Bricks Template Change Workflow

Use this for headers, footers, single/archive templates, WooCommerce templates, conditional templates, or other Bricks template changes.

```text
Modify the requested Bricks template in the CURRENT project.

Because templates can affect many URLs, treat this as a potentially broad-impact change.

BEFORE WRITE

1. Read AGENTS.md.
2. Read template index/detail docs and relevant site rules.
3. Re-read the CURRENT live template and its conditions.
4. Identify every major frontend context where the template is rendered.
5. Identify global classes/variables/components/queries/plugin dependencies used by the template.
6. Inspect representative live frontend URLs before changing visual/layout behavior.
7. Determine blast radius.

Before writing, report:
- template ID/type;
- current conditions/routing;
- representative affected URLs;
- requested scope;
- expected blast radius;
- verification plan.

WRITE

- Change only the agreed template scope.
- Preserve routing/conditions unless the task explicitly changes them.
- Reuse established design-system resources.
- Do not alter unrelated templates.
- Use preview/planning where available.

VERIFY

After writing:
1. re-read persisted template structure and conditions;
2. verify multiple representative frontend URLs;
3. verify relevant viewport widths;
4. verify query/dynamic-data contexts;
5. verify logged-in/logged-out or state-dependent contexts when relevant and safely testable;
6. run the relevant quality gate.

DOCUMENT

Update:
- template index/detail docs;
- routing/conditions docs;
- visual/site rules only if materially changed.

FINAL REPORT

Report:
- template changed;
- routing/conditions changed or preserved;
- representative contexts checked;
- regressions found/fixed;
- documentation updated.
```
