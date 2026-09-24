# Existing Page Edit Workflow

Use this prompt for scoped changes to an existing Bricks page.

```text
Modify the requested existing Bricks page in the CURRENT project.

SCOPE FIRST

1. Read AGENTS.md.
2. Read the page's local documentation and relevant site/design-system docs.
3. Re-read the CURRENT live page structure through MCP.
4. Re-read all shared resources directly involved in the requested change.
5. Inspect the rendered frontend before writing when the task affects appearance, responsive behavior or interaction.
6. Identify plugin/data/framework dependencies.
7. Distinguish page-local settings from global resources.
8. Before proposing implementation, check whether the requested result can be achieved with:
   - a more appropriate native Bricks element;
   - native element/inherited style controls;
   - existing global classes/variables;
   - a justified new shared class/variable;
   before custom CSS or class-like CSS IDs.

Before writing, summarize:
- current relevant structure;
- exact requested scope;
- proposed smallest safe change;
- whether any global resource would be affected;
- visual references to preserve.

WRITE

- Modify only the requested scope.
- Reuse existing classes/variables/tokens/components where appropriate.
- Do not opportunistically clean up unrelated code/classes.
- Do not convert ownership layers without explicit approval.
- Use preview/dry-run where available for non-trivial changes.
- Preserve or improve Bricks-native authoring quality inside the requested scope.
- Do not add a custom CSS ID merely to create a styling selector.
- Do not add custom CSS for properties that the target element exposes natively.

VERIFY

After writing:
1. re-read persisted state;
2. compare before/after scope;
3. verify rendered frontend;
4. verify relevant responsive widths;
5. verify interactions/conditions if affected;
6. run the relevant Bricks quality gate;
7. inspect for unrelated regressions;
8. run a native-authoring review on the changed scope.

DOCUMENT

Update only the affected page documentation and any site-wide docs that became materially stale.

FINAL REPORT

Report:
- exact changes;
- global resources touched, if any;
- verification performed;
- regressions found/fixed;
- documentation updated;
- native-authoring issues introduced/removed;
- any remaining custom CSS and its justification.
```
