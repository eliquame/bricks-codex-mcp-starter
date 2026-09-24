# Changelog

All notable changes to this starter workflow should be documented here.

## [Unreleased]

### Added
- Task workflow prompt suite for greenfield design-system seeding, new/existing pages, templates, plugin/data architecture, WooCommerce, and targeted re-audits.
- Prompt catalog with lifecycle-based numbering convention.
- One-prompt `START-HERE.md` orchestration: Codex initializes AGENTS/docs, guides MCP setup securely, verifies skills, and runs the bootstrap audit itself.
- Site maturity handling for ESTABLISHED, PARTIAL / IN PROGRESS, and GREENFIELD projects.
- Design-system authority/provenance handling for Bricks-native, external framework, hybrid, custom-code-driven, and undefined systems.
- External CSS/design-framework detection and ownership rules, including provider-owned classes/variables/tokens.
- Controlled global design-system change workflow and lifecycle documentation.
- Initial repository structure.
- Bilingual README (Hungarian first, English second).
- Generic full-site Bricks + Codex MCP bootstrap audit prompt.
- Canonical `project-starter/AGENTS.md` loaded before the first site-specific Codex task.
- AGENTS maintenance/synchronization prompt for later project lifecycle changes.
- Audit-progress and documentation-structure templates.
- Setup, workflow, and security documentation.

### Changed
- Default AGENTS policy now automatically routes natural-language tasks to the appropriate specialist workflow; users do not need to know prompt filenames.
- Repository audit aligned every setup document with the one-prompt automation model; removed remaining manual starter-copy instructions.
- `START-HERE.md` now persists bootstrap state across new-chat/restart boundaries via `docs/bricks/00-bootstrap-status.md`.
- Renumbered the global design-system workflow to `prompts/10-design-system-change-workflow.md` for clearer lifecycle grouping.
- Audit-progress and documentation-structure templates now match the bootstrap maturity/ownership/status model.
- Removed redundant `project-starter/README.md`; the internal starter source now contains only files Codex actually consumes.
- README simplified around a single copy-to-Codex bootstrap prompt; users no longer manually create starter project files.
- `project-starter/` is now an internal source consumed by Codex rather than a manual user copy step.
- Removed the superseded `prompts/COPY-TO-CODEX-SETUP-WIZARD.md`; root `START-HERE.md` is canonical.
- Bootstrap now refines an existing canonical AGENTS policy instead of generating project rules from scratch.
- Real-world bootstrap test patterns were incorporated into the default AGENTS workflow and documentation structure.
- Removed the duplicate `templates/AGENTS.template.md` source to avoid ambiguity; `project-starter/AGENTS.md` is canonical.
- Renamed the old AGENTS refresh concept to the lifecycle-oriented `90-agents-maintenance-and-sync.md`.

### Notes
- This repository is intentionally site-agnostic.
- Runtime credentials and site-specific audit output must not be committed here.
