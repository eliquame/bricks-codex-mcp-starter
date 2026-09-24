# Release & Versioning Policy

This repository uses **Semantic Versioning** and a **Keep a Changelog-style** changelog.

## Version model

While the project is still evolving privately, versions remain below 1.0:

- **PATCH** — fixes, documentation corrections, and small non-breaking behavior corrections.
  - Example: `0.1.0 → 0.1.1`
- **MINOR** — new workflows/features, material authoring-policy improvements, or breaking workflow changes during the pre-1.0 phase.
  - Example: `0.1.x → 0.2.0`
- **MAJOR** — reserved for the stable public contract starting at `1.0.0`.

GitHub Releases may be marked **Pre-release** while the repository is still private/developmental, even when the tag itself is a normal SemVer such as `v0.1.0`.

## Changelog categories

Use these headings under `[Unreleased]` and each version:

- **Added** — new features/workflows/capabilities
- **Changed** — improvements or behavior changes
- **Fixed** — bug fixes and corrected workflow behavior
- **Security** — security or credential-handling changes
- **Deprecated** — still available but planned for removal
- **Removed** — removed features/files/behavior

Do not copy every commit into the changelog. Record user-meaningful changes.

## Release files

Release metadata is intentionally redundant so ZIP distributions remain traceable:

- `VERSION` — current release version
- `STARTER-MANIFEST.json` — package identity, release version, content revision
- `CHANGELOG.md` — human-readable release history
- Git tag — `vX.Y.Z`
- GitHub Release — release notes extracted from the matching changelog section

## Development workflow

During normal development:

1. Put notable changes under `## [Unreleased]`.
2. Use the appropriate category: Added / Changed / Fixed / Security / Deprecated / Removed.
3. Keep commit messages focused; commits are implementation history, not release notes.
4. Bump `content_revision` when starter semantics, layout, or canonical workflow behavior materially changes.

## Preparing a release

1. Choose the new SemVer version.
2. Update `VERSION`.
3. Update `STARTER-MANIFEST.json`:
   - `version`
   - `content_revision` if needed
4. Move the relevant entries from `[Unreleased]` into:
   - `## [X.Y.Z] - YYYY-MM-DD`
5. Leave a fresh `## [Unreleased]` section at the top.
6. Run:
   - `python scripts/validate_release_metadata.py`
7. Commit the preparation as:
   - `release: prepare vX.Y.Z`

## Publishing on GitHub

Use:

**Actions → Publish Release → Run workflow**

Inputs:

- `version`: version without the `v` prefix, e.g. `0.1.0`
- `prerelease`: keep enabled while the project is still experimental/private

The workflow:

1. validates release metadata;
2. extracts notes from `CHANGELOG.md`;
3. creates annotated tag `vX.Y.Z`;
4. pushes the tag;
5. creates the GitHub Release.

The workflow fails rather than overwrite an existing tag/release.

## After release

New development goes back under `[Unreleased]`.

Do not rewrite old release sections unless correcting a factual error. If a released behavior changes, document it in the next version.
