# Existing Project Upgrade & Reconciliation Workflow

Use this when a site-specific Bricks + Codex project was bootstrapped with an older starter revision and must be aligned with the current starter without losing useful site-specific knowledge.

```text
Reconcile the CURRENT existing Bricks + Codex project against the CURRENT starter package/repository.

This is NOT a fresh bootstrap.

Assume:
- MCP may already work;
- Bricks skills may already be installed;
- AGENTS.md already contains site-specific rules;
- docs/bricks/ already contains a substantial knowledge base.

The remote WordPress / Bricks site is READ-ONLY for this reconciliation.
Local project files MAY be renamed, merged, normalized, created, or removed when safe.

GOAL

Align the project with the current generic starter while preserving verified site-specific knowledge.

Use:
- the current starter as the GENERIC policy/workflow source;
- the existing local project as the SITE-SPECIFIC knowledge source;
- live MCP/browser checks only where needed to resolve gaps, drift, or conflicts.

Do not blindly regenerate the full project.

PHASE 1 — IDENTIFY STARTER REVISION

Read the starter package manifest when present:

STARTER-MANIFEST.json

Record:
- starter package identity;
- content revision;
- source type (GitHub / ZIP / local copy);
- Git commit if actually available.

If the package came from a ZIP and no Git commit is available, do not pretend a commit was verified. Record the manifest revision instead.

PHASE 2 — INVENTORY THE EXISTING PROJECT

Inspect:
- project-root AGENTS.md;
- full docs/bricks/ tree;
- page/template detail files;
- JSON snapshots;
- existing internal links.

Classify each existing artifact as:
- KEEP
- RENAME
- MERGE
- CREATE REPLACEMENT
- REMOVE AFTER MERGE
- SITE-SPECIFIC / DO NOT REPLACE

Do not delete useful information.

PHASE 3 — RECONCILE AGENTS.md

Merge the current generic starter policy into the existing AGENTS.md.

Preserve valuable site-specific content, including:
- site identity;
- assigned MCP server;
- proven documentation routing;
- site-specific workflow rules;
- permission notes;
- visual/design references;
- plugin/data/provider notes.

Add missing newer generic rules where applicable.

Do not replace a mature site-specific AGENTS.md with a shorter generic file.

PHASE 4 — NORMALIZE DOCUMENTATION STRUCTURE

Compare docs/bricks/ against the current templates/documentation-structure.md.

Prefer rename/merge over regeneration.

After renames:
- update internal links;
- keep page/template detail files;
- keep useful snapshots;
- avoid duplicate documents for the same concept.

Do not create empty files only for naming conformity.

PHASE 5 — GAP ANALYSIS

Compare the previous audit coverage with the current prompts/00-full-site-bootstrap-audit.md.

Check for newly required concepts such as:
- SITE_MATURITY;
- DESIGN_SYSTEM_STATE;
- DESIGN_SYSTEM_AUTHORITY;
- plugin/provider provenance;
- runtime-detected integrations not visible in standard plugin lists;
- external CSS/design-system providers;
- WooCommerce evidence state;
- frontend visual references;
- page-to-implementation correlation;
- permission/evidence gaps.

Do NOT rerun the entire audit if existing evidence is still sufficient.

PHASE 6 — TARGETED LIVE VERIFICATION

Use read-only MCP/browser checks only where needed to:
- verify drift;
- resolve conflicts;
- fill a missing concept;
- confirm current counts/routing;
- establish ownership/provenance.

If cached and live counts differ, record the delta instead of silently overwriting history.

If a resource is documented but inaccessible now, mark:
LIVE ACCESS BLOCKED

Do not treat it as absent.

PHASE 7 — PLUGIN / PROVIDER PROVENANCE

A runtime provider may exist even when it is absent from a normal active-plugin list.

For each important provider/integration, distinguish:
- PLUGIN LIST VERIFIED
- RUNTIME DETECTED
- MU-PLUGIN
- THEME / CHILD-THEME BUNDLED
- CUSTOM / COMPOSER LOADED
- LOADER UNKNOWN
- NOT DETECTED
- ACCESS BLOCKED

If runtime evidence proves ACF/CMB2/etc. exists but the loader is unknown, preserve the runtime fact and mark provenance unresolved.

Do not claim NOT INSTALLED unless inventory coverage is sufficient to prove it.

PHASE 8 — DESIGN OWNERSHIP CONFIDENCE

For important design resources/providers, record both:
- owner/provenance;
- confidence.

Use:
- VERIFIED
- STRONG EVIDENCE
- TENTATIVE
- UNKNOWN

Do not force ownership when Advanced Themer, child-theme code, external frameworks, or other layers could share responsibility.

PHASE 9 — FRONTEND RE-VERIFICATION

Reuse existing visual evidence when still valid.

Only re-check representative pages/viewports needed to:
- validate current design conclusions;
- cover missing page types;
- resolve drift;
- refresh stale evidence.

Track viewport verification independently where practical (desktop/tablet/mobile).

PHASE 10 — VALIDATE

Before finishing verify:
- AGENTS links resolve;
- Markdown internal links resolve;
- JSON snapshots parse;
- no useful site-specific docs were lost;
- no stale old filenames remain;
- no duplicate concept files remain unintentionally;
- current starter revision is recorded;
- unresolved provenance/permission gaps are documented;
- remote site was not modified.

FINAL REPORT

Report:
- starter revision used;
- files renamed;
- files merged;
- files created;
- files removed;
- AGENTS changes;
- live checks performed;
- snapshot deltas found;
- plugin/provider provenance gaps;
- design ownership confidence;
- WooCommerce evidence/status;
- frontend checks performed;
- permission limitations;
- remaining unresolved items.

Return:
PROJECT STATUS: ALIGNED WITH CURRENT STARTER
or
PROJECT STATUS: PARTIALLY ALIGNED
```
