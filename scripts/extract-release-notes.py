#!/usr/bin/env python3
import pathlib
import re
import sys

if len(sys.argv) != 2:
    print("Usage: extract-release-notes.py <version>", file=sys.stderr)
    raise SystemExit(2)

version = sys.argv[1].lstrip("v")
root = pathlib.Path(__file__).resolve().parents[1]
text = (root / "CHANGELOG.md").read_text(encoding="utf-8")

pattern = re.compile(
    rf"^## \[{re.escape(version)}\] - \d{{4}}-\d{{2}}-\d{{2}}\s*$",
    re.MULTILINE,
)
match = pattern.search(text)
if not match:
    print(f"Release section not found for {version}", file=sys.stderr)
    raise SystemExit(1)

start = match.end()
next_header = re.search(r"^## \[", text[start:], flags=re.MULTILINE)
end = start + next_header.start() if next_header else len(text)
body = text[start:end].strip()

if not body:
    print(f"Release section for {version} is empty", file=sys.stderr)
    raise SystemExit(1)

print(body)
