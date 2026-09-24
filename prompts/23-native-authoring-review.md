# Bricks-Native Authoring Review

Use this as a read-only authoring-quality review after a new page, substantial page edit, or template build, or before approving an existing implementation.

~~~text
Review the requested Bricks page/template for native-authoring quality.

This review is READ-ONLY unless the user explicitly asks to fix the findings.

Read:
- project-root AGENTS.md;
- relevant docs/bricks site/design-system docs;
- the live current element tree;
- current global classes/variables;
- relevant element schemas;
- the rendered frontend when visual/responsive quality is in scope.

Review these categories:

1. NATIVE ELEMENT CHOICE
- Find repeated Basic Text/Div constructions that should use List, Icon List, Accordion, Tabs, Form, Nav, File, query loop, component, or another appropriate Bricks element.
- Distinguish legitimate generic layout containers from div soup.
- Do not recommend a special element merely because it exists; it must fit the semantic/functional pattern.

2. NATIVE CONTROL USAGE
- Identify custom CSS that duplicates an available Bricks control.
- Examples: object-fit/object-position, aspect ratio, dimensions, spacing, grid/flex, typography, background, border, radius, shadow, transform, filters.
- For each custom CSS finding, name the preferred Bricks control when known.

3. CSS ID HYGIENE
- Flag custom CSS/HTML IDs used as class-like styling names.
- A custom ID should have an explicit unique purpose: anchor, ARIA, JS/integration target, etc.
- BEM/component names belong in global classes, not CSS ID.

4. GLOBAL CLASS REUSE
- Check whether existing global classes should have been reused.
- Flag reusable styles trapped on one element.
- Flag duplicate/near-duplicate new classes.
- Respect external framework-owned classes.

5. GLOBAL VARIABLES / TOKENS
- Identify repeated hardcoded values that should reuse an existing variable.
- Identify strong candidates for a new variable only when the value is a reusable design concept.
- Avoid variable proliferation.

6. RESPONSIVE / FLUID LAYOUT
- Flag brittle magic values and chains of breakpoint patches.
- Consider native grid/flex controls and fluid/intrinsic values such as clamp(), min(), max(), minmax(), repeat(), auto-fit/auto-fill, fr, wrapping, and existing fluid scales.
- Do not demand fluid CSS when a deliberate breakpoint layout switch is clearer.

7. MEDIA / ICON REUSE
- Check whether existing media/custom icons were considered.
- Flag unnecessary uploads/recreated SVGs when a suitable shared asset already exists.
- Check image size, loading, alt text, and native image controls.

8. CUSTOM CODE JUSTIFICATION
- List every custom CSS/JS/PHP usage in scope.
- Classify each as:
  - JUSTIFIED
  - REPLACE WITH NATIVE CONTROL
  - REPLACE WITH GLOBAL CLASS/VARIABLE
  - NEEDS HUMAN REVIEW

9. NAMING
- Follow the site's existing convention.
- Where no convention exists, BEM is preferred for reusable component classes, not for utilities or provider-owned classes.

OUTPUT

Return a concise table:

| Severity | Element/resource | Finding | Preferred Bricks-native solution | Action |

Severity:
- HIGH: structurally wrong, brittle, or global design-system conflict
- MEDIUM: maintainability/reuse/responsive issue
- LOW: cleanup/consistency improvement

Also report:
- number of unnecessary custom CSS declarations;
- number of class-like custom CSS IDs;
- likely missed native elements;
- global class reuse opportunities;
- variable/token opportunities;
- responsive-fluidity opportunities.

Do not modify the site unless explicitly asked to apply the review.
~~~
