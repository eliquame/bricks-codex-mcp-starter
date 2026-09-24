# Prompt Catalog

These prompts are reusable workflow entry points. They are not site-specific.

| Prompt | Purpose |
|---|---|
| `00-full-site-bootstrap-audit.md` | First full read-only discovery of a connected site; builds the project knowledge base and refines AGENTS project facts. |
| `10-design-system-change-workflow.md` | Controlled change to an existing global design system, Theme Styles, classes, variables/tokens, breakpoints, or framework-owned resources. |
| `11-greenfield-design-system-seed.md` | Creates the first approved design-system foundation for a GREENFIELD site with an undefined/incomplete design system. |
| `20-new-page-build-workflow.md` | Builds a new Bricks page using the bootstrapped site architecture and visual references. |
| `21-existing-page-edit-workflow.md` | Makes a scoped change to an existing Bricks page with live readback and frontend verification. |
| `22-template-change-workflow.md` | Safely changes Bricks templates/conditions with multi-context verification. |
| `30-plugin-data-architecture-change-workflow.md` | Changes CPTs, fields, taxonomies, relationships, queries, or other provider-owned data architecture. |
| `31-woocommerce-workflow.md` | WooCommerce + Bricks layout/template/data workflow with commerce-specific safety rules. |
| `80-targeted-reaudit.md` | Read-only re-audit of a limited area after material project changes. |
| `81-existing-project-upgrade.md` | Reconciles an older site project against the current starter without losing site-specific knowledge. |
| `90-agents-maintenance-and-sync.md` | Synchronizes the site-specific AGENTS profile/routing after material evolution. |

## Numbering convention

- `00` — initial bootstrap/discovery
- `10–19` — design-system lifecycle
- `20–29` — Bricks page/template work
- `30–39` — plugin/data/commerce architecture
- `80–89` — re-audit/verification
- `90–99` — project-policy maintenance

The project-root `AGENTS.md` remains the always-on policy. These prompts are task workflows used when their scope applies.
