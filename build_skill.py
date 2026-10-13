#!/usr/bin/env python3
"""
build_skill.py: package the skill folder into a .skill file (a zip archive).

Usage:
    python build_skill.py                       # builds ./dist/umkm-print-prompt-architect.skill
    python build_skill.py --skill-dir PATH      # another skill folder
    python build_skill.py --out DIR             # another output folder

Uses only the Python standard library (3.8+). Validates before packaging:
  - SKILL.md exists, with YAML frontmatter (name, description)
  - name is kebab-case and matches the folder name
  - description length <= 1024 chars
  - exactly one SKILL.md in the skill
  - every references/*.md file is mentioned in SKILL.md (no orphan files)
  - every references/... path mentioned in SKILL.md exists (no broken links)
"""
import argparse
import re
import sys
import zipfile
from pathlib import Path

EXCLUDE_DIRS = {"__pycache__", "node_modules", ".git", "dist"}
EXCLUDE_FILES = {".DS_Store", "Thumbs.db"}
EXCLUDE_SUFFIXES = {".pyc", ".skill"}


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None
    data, key = {}, None
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if kv:
            key = kv.group(1)
            data[key] = kv.group(2).strip()
        elif key and line.startswith((" ", "\t")):
            data[key] += " " + line.strip()
    return data


def validate(skill_dir: Path):
    errors = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["SKILL.md not found"]
    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if not fm:
        return ["SKILL.md has no valid YAML frontmatter (--- ... ---)"]
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name:
        errors.append("frontmatter: missing 'name'")
    elif not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        errors.append(f"frontmatter: name '{name}' must be kebab-case")
    elif name != skill_dir.name:
        errors.append(f"frontmatter name '{name}' != folder name '{skill_dir.name}'")
    if not desc:
        errors.append("frontmatter: missing 'description'")
    elif len(desc) > 1024:
        errors.append(f"frontmatter: description is {len(desc)} chars (max 1024)")
    if "<" in desc or ">" in desc:
        errors.append("frontmatter: description must not contain angle brackets")

    skill_mds = [p for p in skill_dir.rglob("SKILL.md")]
    if len(skill_mds) != 1:
        errors.append(f"expected exactly 1 SKILL.md, found {len(skill_mds)}")

    ref_dir = skill_dir / "references"
    if ref_dir.exists():
        for f in sorted(ref_dir.glob("*.md")):
            if f.name not in text and f.stem not in text:
                errors.append(f"orphan reference (not mentioned in SKILL.md): references/{f.name}")
    mentioned = set(re.findall(r"references/([A-Za-z0-9_.-]+\.md)", text))
    for m in sorted(mentioned):
        if not (ref_dir / m).exists():
            errors.append(f"broken link in SKILL.md: references/{m}")
    return errors


def should_skip(path: Path, skill_dir: Path):
    rel = path.relative_to(skill_dir)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return True
    return path.name in EXCLUDE_FILES or path.suffix in EXCLUDE_SUFFIXES


def build(skill_dir: Path, out_dir: Path):
    skill_dir = skill_dir.resolve()
    if not skill_dir.is_dir():
        sys.exit(f"Skill folder not found: {skill_dir}")
    errors = validate(skill_dir)
    if errors:
        print("Validation failed:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("Validation passed")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{skill_dir.name}.skill"
    count = 0
    with zipfile.ZipFile(out_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file() and not should_skip(path, skill_dir):
                arcname = Path(skill_dir.name) / path.relative_to(skill_dir)
                zf.write(path, arcname.as_posix())
                print("  added:", arcname.as_posix())
                count += 1
    print(f"\nBuilt {out_file} ({count} files, {out_file.stat().st_size / 1024:.1f} KB)")
    return out_file


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description="Build a .skill package")
    ap.add_argument("--skill-dir", default=str(here / "umkm-print-prompt-architect"))
    ap.add_argument("--out", default=str(here / "dist"))
    a = ap.parse_args()
    build(Path(a.skill_dir), Path(a.out))
