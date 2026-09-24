#!/usr/bin/env python3
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
manifest = json.loads((ROOT / "STARTER-MANIFEST.json").read_text(encoding="utf-8"))
changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

semver = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
errors = []

if not semver.fullmatch(version):
    errors.append(f"VERSION is not valid SemVer: {version!r}")

if manifest.get("version") != version:
    errors.append(
        "STARTER-MANIFEST.json version does not match VERSION: "
        f"{manifest.get('version')!r} != {version!r}"
    )

if "## [Unreleased]" not in changelog:
    errors.append("CHANGELOG.md is missing '## [Unreleased]'")

release_header = re.compile(
    rf"^## \[{re.escape(version)}\] - \d{{4}}-\d{{2}}-\d{{2}}$",
    re.MULTILINE,
)
if not release_header.search(changelog):
    errors.append(
        f"CHANGELOG.md is missing a dated release section for [{version}]"
    )

if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)

print(f"Release metadata OK: {version}")
