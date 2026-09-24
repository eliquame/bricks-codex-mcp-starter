# Bricks-Native Authoring Standard

This document defines the generic authoring standard for pages, templates, and components created or edited through Codex + Bricks MCP.

It complements the official Bricks skills. It does not replace runtime schemas or site-specific conventions.

## Core principle

Prefer this order:

1. **Correct native Bricks element**
2. **Native Bricks control**
3. **Existing global class / variable / component**
4. **New reusable global class / variable when justified**
5. **Element-local Bricks control for truly one-off styling**
6. **Custom selector / custom CSS only when native controls cannot express the requirement**
7. **Custom JS/PHP only when Bricks-native behavior is insufficient and the user explicitly authorizes the required code path**

Do not use custom CSS merely because it is faster to type.

Do not use generic Div + Basic Text structures when Bricks already has a better native element for the content pattern.

---

## 1. Choose the right Bricks element before styling

Translate the semantic/content pattern into the most appropriate Bricks primitive.

| Content / behavior | Prefer |
|---|---|
| Headline | Heading |
| Paragraph / short text | Text / Basic Text as appropriate |
| Repeated bullet/features list | List or Icon List |
| Button/CTA | Button |
| Standalone image | Image |
| Custom SVG graphic/icon | SVG or supported icon control / custom icon set |
| Accordion content | Accordion / Accordion Nested |
| Tabs | Tabs / Tabs Nested |
| Form | Form |
| Navigation | Nav Nested or the site's established navigation pattern |
| Download/file | File |
| Repeated data cards | Query loop on appropriate layout element / component |
| Reusable structured block | Component when genuine reuse exists |

A source document is not a literal element map. A Word/Google document that contains bullets, headings, callouts, grouped content, or repeated features must be interpreted semantically before building.

### List rule

Do not represent a real list as a stack of unrelated Basic Text elements inside a Div when a native List/Icon List is suitable.

Bricks' List element supports list-item repeaters, optional icons, titles, metadata, descriptions, highlighting, item spacing, borders, and other list-specific controls.

The Icon List element supports icon + label/link rows with direction, alignment, and spacing controls.

Before choosing generic text nodes for repeated items, explicitly check whether List, Icon List, or another native repeater element is the better fit.

---

## 2. Native controls before custom CSS

For every visual/style requirement, check the target element's runtime schema and Bricks controls first.

Examples:

- Image fit → use Image **Object fit**
- Image focal alignment → use **Object position**
- Aspect ratio → use the native aspect-ratio control
- Width/height/min/max → use inherited layout controls
- Margin/padding/gap → use native spacing/layout controls
- Grid tracks → use native grid controls
- Typography → use native typography controls
- Background/border/radius/shadow/transform/filter → use the corresponding Bricks controls
- Hover/focus/state → use Bricks pseudo/selectors and class styles where appropriate

Custom CSS is justified only when:
- the installed Bricks element has no equivalent control;
- the requirement needs a selector relationship the native controls cannot model cleanly;
- an external framework/provider requires a code-level declaration;
- the user explicitly requests custom CSS.

If custom CSS is used, record the reason in the task report.

### Example: Image object-fit

Do not write custom CSS for object-fit: cover when the Image element's native **Object fit: Cover** control can express the same result.

Bricks exposes fill, contain, cover, none, and scale-down natively.

---

## 3. IDs are not classes

Bricks already gives each element an internal builder ID and default frontend selector.

A custom CSS/HTML ID is only for a genuinely unique identity such as:

- URL anchor / fragment target;
- ARIA relationship;
- JavaScript or third-party integration target;
- a user-requested stable unique selector;
- another explicit unique semantic/integration requirement.

Do not put class-like names such as ps-expertise-image, ps-hull-grid, service-card, or hero-wrapper into the CSS ID field merely to name/style elements.

For reusable styling, use a global class.

For a one-off style, leave the custom CSS ID empty and style the Bricks element locally through its native controls.

For human readability inside the builder, use the element's custom label/name where supported instead of abusing CSS ID.

The official bricks-element-schemas skill explicitly distinguishes Bricks internal element IDs from settings._cssId and says to set a custom CSS ID only when an intentional custom HTML id is needed.

---

## 4. Global classes and BEM

Before creating a class:

1. inspect existing global classes;
2. reuse an existing class when it already expresses the pattern;
3. follow the site's existing naming convention;
4. respect external framework ownership.

For reusable component-level patterns, BEM is a good default when the site has no conflicting convention:

- .service-card
- .service-card__icon
- .service-card__title
- .service-card__text
- .service-card--featured

Use BEM where it improves component clarity. Do not force BEM onto utility classes or framework-owned naming systems.

Bricks' own wireframe templates use a BEM-style convention for reusable block/element/modifier classes.

### Class vs. element-local styling

- Shared/repeated decision → global class
- Single unique exception → element-local Bricks style
- Repeated scalar/design token → global variable
- Repeated structure → component when appropriate

Do not create a global class merely to avoid using an element-local style once.

Do not leave a reusable design decision trapped on an element ID.

---

## 5. Global variables and fluid values

Inspect existing variables and variable categories before hardcoding a value.

Reuse existing variables for spacing, typography, colors, widths, radii, reusable layout dimensions, and other repeated design tokens.

Create a new global variable when:
- the value represents a reusable design/system concept;
- the existing variable library has no suitable equivalent;
- the new name follows the site's naming convention and ownership model.

Do not create variables for every one-off number.

### Prefer fluid/intrinsic layout before breakpoint patches

Before adding multiple breakpoint overrides, test whether the layout can be expressed with:

- clamp()
- min()
- max()
- minmax()
- repeat()
- auto-fit
- auto-fill
- fr
- intrinsic/content sizing
- flex wrapping
- existing fluid spacing/typography scales
- reusable CSS variables

A responsive override is appropriate when the **layout mode actually changes**, not merely to patch a brittle fixed value.

A recurring two-column system may use a class or variable-backed track definition instead of repeating arbitrary magic values and then correcting them independently at several breakpoints.

### Bricks variable system

Bricks Global Variables are site-level CSS custom properties and can contain complex CSS values such as clamp(), minmax(), and calc() where the target CSS property accepts them.

If the site already uses a configured Bricks spacing/typography scale, extend that scale through the appropriate Bricks design-system workflow instead of hand-authoring a parallel token family.

---

## 6. Responsive authoring

Use the actual site's breakpoint model.

Do not assume Bricks defaults if custom breakpoints are configured.

Prefer:
1. robust base/intrinsic layout;
2. fluid values;
3. targeted breakpoint overrides only where necessary.

After a visual/layout write:
- inspect the persisted responsive settings;
- check intermediate widths, not only breakpoint presets;
- browser-verify representative wide/tablet/mobile views.

Avoid breakpoint-by-breakpoint patch chains caused by an inflexible base layout.

---

## 7. Media and icons

Before uploading or inventing a new asset:

1. inspect existing WordPress media;
2. inspect existing Bricks custom icon sets/icons;
3. inspect the site's established icon style;
4. reuse a suitable existing asset when appropriate.

For a list or feature block that benefits from icons:
- search existing media/custom icons first;
- prefer an existing site SVG/icon when visually appropriate;
- otherwise use a suitable Bricks-native icon source.

Do not add decorative icons merely because an element supports them; preserve the site's visual language.

For images, choose the appropriate WordPress image size and loading behavior. Keep hero/LCP and below-fold loading behavior intentional.

---

## 8. Custom code budget

Treat custom CSS/JS/PHP as an escalation path.

Before custom CSS, answer:

1. Is there a native element control?
2. Is there an inherited Bricks style control?
3. Can the style live on an existing/new global class using native controls?
4. Is a variable more appropriate for the value?
5. Is a pseudo/custom selector sufficient?
6. Does an external framework own the declaration?

Only then use custom CSS.

Custom JavaScript/PHP requires an even stronger justification and the relevant permissions/safety workflow.

---

## 9. Required authoring preflight for broad page/template work

For a broad build from a brief/document:

1. Use bricks-plan-from-brief.
2. Inspect the site design context.
3. Map content semantics to Bricks element types.
4. Use bricks-element-schemas to inspect unfamiliar/complex elements and controls.
5. Use bricks-naming-conventions before new shared names.
6. Use bricks-design-systems before creating global classes/variables.
7. Use bricks-media-assets before uploading/recreating media/icons.
8. Use bricks-components when real structural reuse exists.
9. Use bricks-custom-code only after native options are exhausted and custom code remains justified.

The official element schema skill can list runtime element types and fetch exact schemas. Use that instead of assuming the small common-element set is always the best choice.

---

## 10. Native-authoring review before finalizing

For new pages, substantial page edits, or template changes, review:

### Element choice
- Any Div/Block + repeated Basic Text that should be List/Icon List/another native element?
- Any hand-built behavior that should use Accordion/Tabs/Form/Nav/etc.?
- Any reused structure that should be a component?

### Styling
- Any custom CSS declaration that has an equivalent Bricks control?
- Any style applied locally that should be a global class?
- Any repeated scalar value that should use an existing/new variable?

### ID/class hygiene
- Any custom CSS ID used as if it were a class?
- Any BEM-like name incorrectly stored in CSS ID?
- Any duplicate or near-duplicate class?

### Responsive quality
- Any magic fixed value causing multiple breakpoint patches?
- Could a fluid/intrinsic CSS value solve it more cleanly?
- Were intermediate widths tested?

### Media
- Was existing media/icon inventory checked before adding assets?
- Are image size/loading/alt settings intentional?

If violations are found, fix them before declaring the visual task complete unless preserving the existing implementation is explicitly required.

---

## Official references

- Bricks Adding & Editing Elements: https://academy.bricksbuilder.io/builder/interface/editing-elements/
- Global CSS Classes: https://academy.bricksbuilder.io/builder/styling/global-css-classes/
- Global Variables Manager: https://academy.bricksbuilder.io/builder/styling/global-variables-manager/
- Style Manager: https://academy.bricksbuilder.io/builder/features/style-manager/
- Responsive Editing: https://academy.bricksbuilder.io/builder/interface/responsive-editing/
- List element: https://academy.bricksbuilder.io/builder/elements/layout/list/
- Icon List: https://academy.bricksbuilder.io/builder/elements/general/icon-list/
- Image element: https://academy.bricksbuilder.io/builder/elements/basic/image/
- Custom Code: https://academy.bricksbuilder.io/builder/features/custom-code/
- Bricks element/data schemas: https://academy.bricksbuilder.io/developer/schema/
- Bricks Wireframe Templates / BEM: https://academy.bricksbuilder.io/builder/features/wireframe-templates/
- Bricks skills: https://github.com/codeerhq/bricks-skills
