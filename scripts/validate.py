#!/usr/bin/env python3
"""Validate the distributable skill package using only Python's standard library."""

from pathlib import Path
import re
import struct
import sys
import zlib

ROOT = Path(__file__).resolve().parents[1]
NAME = "cai-preserve-plan-color-render"
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


required = [
    "SKILL.md", "README.md", "LICENSE", "ASSET_NOTICE.md",
    "agents/openai.yaml", "references/style-cards.md",
    "references/style-card-gallery.md", "references/quality-check.md",
]
for relative in required:
    check((ROOT / relative).is_file(), f"Missing file: {relative}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
check(frontmatter is not None, "SKILL.md needs YAML frontmatter")
if frontmatter:
    check(f"name: {NAME}" in frontmatter.group(1), "Incorrect skill name")
    check(re.search(r"^description:\s*\S", frontmatter.group(1), re.M),
          "Missing description")
adapter = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
check(f"${NAME}" in adapter, "Invocation name differs in openai.yaml")

cards = (ROOT / "references/style-cards.md").read_text(encoding="utf-8")
numbers = re.findall(r"^## (\d{2}) ", cards, re.M)
check(numbers == [f"{n:02}" for n in range(1, 16)],
      "Style cards must be consecutive 01–15")
gallery = (ROOT / "references/style-card-gallery.md").read_text(encoding="utf-8")
assets = re.findall(r"`(assets/style-previews/[^`]+\.png)`", gallery)
check(len(assets) == len(set(assets)) == 15, "Gallery needs 15 unique previews")
actual = {p.relative_to(ROOT).as_posix()
          for p in (ROOT / "assets/style-previews").glob("*.png")}
check(actual == set(assets), "Gallery and preview files differ")

for relative in assets:
    path = ROOT / relative
    if not path.is_file():
        check(False, f"Missing preview: {relative}")
        continue
    data = path.read_bytes()
    try:
        if data[:8] != b"\x89PNG\r\n\x1a\n":
            raise ValueError("not a PNG")
        check(struct.unpack(">II", data[16:24]) == (480, 453),
              f"Unexpected preview dimensions: {relative}")
        offset, image_data, complete = 8, bytearray(), False
        while offset < len(data):
            length = struct.unpack_from(">I", data, offset)[0]
            kind = data[offset + 4:offset + 8]
            payload = data[offset + 8:offset + 8 + length]
            crc = struct.unpack_from(">I", data, offset + 8 + length)[0]
            if zlib.crc32(kind + payload) & 0xffffffff != crc:
                raise ValueError("PNG CRC mismatch")
            if kind == b"IDAT":
                image_data.extend(payload)
            if kind == b"IEND":
                complete = True
                break
            offset += length + 12
        check(complete and bool(zlib.decompress(image_data)),
              f"Incomplete PNG: {relative}")
    except (ValueError, struct.error, zlib.error) as exc:
        check(False, f"Invalid PNG {relative}: {exc}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.relative_to(ROOT).parts:
        continue
    if path.suffix not in {".md", ".yaml", ".yml"}:
        continue
    text = path.read_text(encoding="utf-8")
    check(not re.search(r"/Users/|/private/var/|/var/folders/|gh[pousr]_[A-Za-z0-9]{20,}", text),
          f"Private local path or token-like string: {path.relative_to(ROOT)}")
    # Remove code blocks: the gallery includes a documented placeholder example.
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", prose):
        target = target.strip("<>").split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        destination = (path.parent / target).resolve()
        check(destination.is_relative_to(ROOT) and destination.exists(),
              f"Broken or escaping link in {path.relative_to(ROOT)}: {target}")

if errors:
    print("Package validation failed:\n- " + "\n- ".join(errors), file=sys.stderr)
    sys.exit(1)
print("PASS: skill entrypoint, 15 cards, 15 PNG previews, links and portable paths")
print("This validates packaging only, not rendering accuracy or Agent compatibility.")
