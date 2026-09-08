#!/usr/bin/env python3
"""Validate every SKILL.md in this pack against the Agent Skills spec.

Checks:
  - SKILL.md exists in each skill directory
  - YAML frontmatter is present, well formed, and closed
  - `name` and `description` are present and non-empty
  - `name` is <= 64 chars, lowercase, and only letters/numbers/hyphens
  - `name` matches the directory name
  - `name` contains no reserved words ("anthropic", "claude")
  - `description` is <= 1024 chars and contains no XML tags
  - SKILL.md body is under 500 lines
  - every referenced references/ file actually exists

Usage:  python3 scripts/validate_skills.py [skills_dir]
Exit code 0 = all valid, 1 = at least one error.
"""

import os
import re
import sys

NAME_RE = re.compile(r"^[a-z0-9-]+$")
XML_RE = re.compile(r"<[^>]+>")
REF_RE = re.compile(r"`(references/[A-Za-z0-9._/-]+)`")
RESERVED = ("anthropic", "claude")

NAME_MAX = 64
DESC_MAX = 1024
BODY_MAX_LINES = 500


def parse_frontmatter(text):
    """Return (fields, body) or raise ValueError."""
    if not text.startswith("---"):
        raise ValueError("file does not open with a --- frontmatter fence")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("frontmatter fence is never closed")
    raw, body = parts[1], parts[2]
    fields, key = {}, None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) and key:
            fields[key] += " " + line.strip()
            continue
        if ":" not in line:
            raise ValueError("unparseable frontmatter line: %r" % line)
        key, value = line.split(":", 1)
        key = key.strip()
        fields[key] = value.strip()
    return fields, body


def validate(skill_dir):
    errors, warnings = [], []
    slug = os.path.basename(skill_dir.rstrip("/"))
    path = os.path.join(skill_dir, "SKILL.md")

    if not os.path.isfile(path):
        return ["%s: no SKILL.md" % slug], []

    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    try:
        fields, body = parse_frontmatter(text)
    except ValueError as exc:
        return ["%s: %s" % (slug, exc)], []

    name = fields.get("name", "")
    desc = fields.get("description", "")

    if not name:
        errors.append("%s: missing name" % slug)
    else:
        if len(name) > NAME_MAX:
            errors.append("%s: name is %d chars, limit %d" % (slug, len(name), NAME_MAX))
        if not NAME_RE.match(name):
            errors.append("%s: name %r must be lowercase letters, numbers, hyphens" % (slug, name))
        if name != slug:
            errors.append("%s: name %r does not match directory" % (slug, name))
        for word in RESERVED:
            if word in name:
                errors.append("%s: name contains reserved word %r" % (slug, word))

    if not desc:
        errors.append("%s: missing description" % slug)
    else:
        if len(desc) > DESC_MAX:
            errors.append("%s: description is %d chars, limit %d" % (slug, len(desc), DESC_MAX))
        if XML_RE.search(desc):
            errors.append("%s: description contains an XML tag" % slug)
        if len(desc) < 120:
            warnings.append("%s: description is short (%d chars), triggering may suffer" % (slug, len(desc)))
        if " Use " not in desc and " use " not in desc:
            warnings.append("%s: description states no trigger condition" % slug)

    body_lines = body.strip().splitlines()
    if len(body_lines) > BODY_MAX_LINES:
        errors.append("%s: body is %d lines, limit %d" % (slug, len(body_lines), BODY_MAX_LINES))

    for ref in set(REF_RE.findall(body)):
        if not os.path.isfile(os.path.join(skill_dir, ref)):
            errors.append("%s: references missing file %s" % (slug, ref))

    if not errors:
        print("  ok   %-32s name=%-32s desc=%4d chars  body=%3d lines"
              % (slug, name, len(desc), len(body_lines)))
    return errors, warnings


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "skills")

    dirs = sorted(
        os.path.join(root, d) for d in os.listdir(root)
        if os.path.isdir(os.path.join(root, d))
    )
    if not dirs:
        print("no skill directories found in %s" % root)
        return 1

    print("Validating %d skills in %s\n" % (len(dirs), root))
    all_errors, all_warnings = [], []
    for d in dirs:
        errors, warnings = validate(d)
        all_errors += errors
        all_warnings += warnings

    print()
    for warning in all_warnings:
        print("  warn %s" % warning)
    for error in all_errors:
        print("  FAIL %s" % error)

    if all_errors:
        print("\n%d error(s)." % len(all_errors))
        return 1
    print("\nAll %d skills valid. %d warning(s)." % (len(dirs), len(all_warnings)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
