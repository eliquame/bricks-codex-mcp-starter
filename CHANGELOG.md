# Changelog

All notable user-meaningful changes to this starter workflow are documented here.

This project follows [Semantic Versioning](https://semver.org/) and a Keep a Changelog-style structure.

## [Unreleased]

New work goes here until the next release.

## [0.1.0] - 2026-09-24

First versioned development baseline for the Bricks + Codex MCP starter.

### Added
- One-prompt `START-HERE.md` orchestration for project initialization, MCP setup guidance, Bricks skills verification, and bootstrap audit execution.
- Persistent bootstrap resume state via `docs/bricks/00-bootstrap-status.md`.
- Canonical `project-starter/AGENTS.md` with site isolation, source-of-truth, permission-aware, safety, documentation, and workflow rules.
- Full read-only site bootstrap audit covering Bricks architecture, plugin/data architecture, design systems, templates, pages, WooCommerce, and frontend visual references.
- Site maturity model: ESTABLISHED / PARTIAL / GREENFIELD.
- Design-system authority/provenance model for Bricks-native, external framework, hybrid, custom-code-driven, and undefined systems.
- External CSS/design-framework ownership handling.
- Existing-project upgrade/reconciliation workflow.
- Greenfield design-system seed workflow.
- New page, existing page, template, plugin/data architecture, WooCommerce, targeted re-audit, and AGENTS synchronization workflows.
- Bricks-native authoring standard and read-only native-authoring quality review.
- Advanced Themer bundled-ACF provenance heuristic.
- ZIP/package lineage support through `STARTER-MANIFEST.json`.
- Audit-progress and documentation-structure templates.
- Bilingual README with secure setup guidance and Bricks Skills screenshot.
- Release/versioning infrastructure: `VERSION`, release policy, metadata validation, changelog note extraction, and GitHub Actions release workflow.

### Changed
- Default AGENTS policy automatically routes natural-language tasks to specialist workflows.
- New-page, existing-page, and template workflows now require Bricks-native preflight and post-write authoring review.
- Skill routing explicitly uses `bricks-plan-from-brief`, `bricks-element-schemas`, `bricks-naming-conventions`, `bricks-media-assets`, and `bricks-custom-code` only when appropriate.
- Plugin/provider detection distinguishes runtime evidence from standard plugin-list visibility and records unresolved loader provenance.
- WooCommerce absence/status is evidence-aware when plugin inventory is incomplete.
- Design-system ownership can carry confidence: VERIFIED / STRONG EVIDENCE / TENTATIVE / UNKNOWN.
- Bootstrap completion reports expose meaningful snapshot deltas and unresolved provenance/ownership gaps.
- Setup/documentation flow was simplified around a single copy-to-Codex bootstrap prompt.
- `project-starter/` became an internal source consumed by Codex rather than a manual copy step.
- Global design-system workflow was renumbered into the lifecycle-based prompt catalog.

### Fixed
- Removed duplicate/conflicting AGENTS template sources.
- Removed the superseded AGENTS refresh prompt and replaced it with lifecycle-oriented maintenance/synchronization.
- Removed the superseded standalone setup wizard in favor of root `START-HERE.md`.
- Removed stale manual starter-copy instructions from setup documentation.
- Added restart/new-chat resume handling so MCP/skills reloads do not lose bootstrap progress.
- Aligned WooCommerce documentation behavior with mandatory status detection.
- Aligned audit/documentation templates with the actual bootstrap maturity, ownership, and evidence model.

### Security
- Added secret-safe `.gitignore` rules for Codex config, credentials, keys, and local secret files.
- Standardized the secure connection path around Bricks **Paste config** so Application Passwords do not need to be pasted into chat.
- Added least-privilege guidance and explicit no-PHP/no-destructive-write bootstrap rules.
- Added credential redaction and local-only handling requirements for `config.toml`.

[Unreleased]: https://github.com/eliquame/bricks-codex-mcp-starter/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/eliquame/bricks-codex-mcp-starter/releases/tag/v0.1.0
