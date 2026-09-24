# Changelog

All notable changes to this starter workflow should be documented here.

## [Unreleased]

### Added
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
- Bootstrap now refines an existing canonical AGENTS policy instead of generating project rules from scratch.
- Real-world bootstrap test patterns were incorporated into the default AGENTS workflow and documentation structure.
- Removed the duplicate `templates/AGENTS.template.md` source to avoid ambiguity; `project-starter/AGENTS.md` is canonical.
- Renamed the old AGENTS refresh concept to the lifecycle-oriented `90-agents-maintenance-and-sync.md`.

### Notes
- This repository is intentionally site-agnostic.
- Runtime credentials and site-specific audit output must not be committed here.
