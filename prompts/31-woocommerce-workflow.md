# WooCommerce + Bricks Workflow

Use this for WooCommerce layout/template/data work after WooCommerce has been verified ACTIVE.

```text
Perform the requested WooCommerce + Bricks task in the CURRENT project.

SAFETY

Do not expose or document private customer/order data.
Do not change prices, stock, orders, customers, taxes, shipping, payments, coupons, or checkout configuration unless the user explicitly requested that operational change.

DISCOVERY

1. Read AGENTS.md and docs/bricks/14-woocommerce.md.
2. Confirm WooCommerce is ACTIVE.
3. Re-read relevant WooCommerce + Bricks templates/resources.
4. Identify product/taxonomy/attribute/custom-field/query dependencies.
5. Identify representative frontend contexts:
   - shop/archive
   - product category
   - single product
   - cart
   - checkout
   - account
   - other requested state.
6. Inspect browser output before visual/template changes.

PLAN

Before writing, report:
- target Woo context;
- template/data owner;
- existing dependencies;
- proposed scope;
- representative test URLs/states;
- whether any operational commerce data is in scope.

WRITE

- Keep layout/template work separate from operational store-data changes.
- Reuse existing design system and Woo patterns.
- Preserve Woo data/query semantics.
- Do not access private orders/customers unless strictly necessary and explicitly authorized.

VERIFY

After writing:
1. re-read persisted template/page state;
2. verify representative frontend states;
3. verify responsive behavior;
4. verify dynamic product data;
5. verify cart/checkout/account behavior only when relevant and safely testable;
6. run quality-gate checks.

DOCUMENT

Update WooCommerce architecture docs and affected template/page docs only.

FINAL REPORT

Report:
- contexts changed;
- data dependencies checked;
- frontend states verified;
- operational data touched (normally none);
- documentation updated.
```
