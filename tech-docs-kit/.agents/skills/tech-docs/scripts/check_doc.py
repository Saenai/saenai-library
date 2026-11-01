#!/usr/bin/env python3
"""Structural checks for Markdown documents written with the tech-docs skill.

usage: check_doc.py PATH [PATH ...] [--type TYPE]

PATH is a file, or a directory whose *.md files are all checked.
The document type comes from --type, otherwise from the file name:
*.design.md, *.runbook.md, *.reference.md, adr/NNNN-*.md, README.md.

Checks: one title, required sections for the type, local links and line
ranges, in-page anchors, Mermaid diagram types, leftover placeholders and
lifecycle fields. Content correctness is for review, not for this script.
Exit status 1 if anything is reported.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REQUIRED = {
    "design": ["Summary", "Context", "Interfaces", "Behavior", "Decisions", "Verification", "Open Questions"],
    "runbook": ["Before you start", "Steps", "Check the result", "Troubleshooting"],
    "adr": ["Context", "Decision", "Consequences", "Alternatives Considered"],
}
OPTIONAL = {"runbook": ["Undo"]}
TYPES = ["design", "runbook", "adr", "reference", "readme"]

FRONT_MATTER = re.compile(r"\A---\n.*?\n---[ \t]*\n", re.S)
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})([^\n]*)\n(.*?)^ {0,3}\1[ \t]*$", re.M | re.S)
INLINE_CODE = re.compile(r"`+[^`\n]*`+")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\)")
MERMAID = re.compile(r"^(flowchart|graph|sequenceDiagram|stateDiagram(-v2)?|erDiagram|classDiagram|gantt|journey|gitGraph|mindmap|timeline|pie|quadrantChart)\b")
PLACEHOLDER = re.compile(r"\{\{|\b(TODO|TBD|FIXME)\b")
LIFECYCLE = re.compile(r"^\W*(Status|Approved by|Approval|Revision|Last reviewed|Reviewed by)\W*:", re.I)
LIFECYCLE_HEADING = re.compile(r"^#{2,6} +(change ?log|revision history|change history|document history)\s*$", re.I)


def doc_type(path: Path, override: str | None) -> str | None:
    if override:
        return override
    if path.name.lower() == "readme.md":
        return "readme"
    m = re.search(r"\.(design|runbook|reference)\.md$", path.name)
    if m:
        return m.group(1)
    if path.parent.name == "adr" and re.match(r"\d{4}-", path.name):
        return "adr"
    return None


def slug(heading: str) -> str:
    """GitHub-style heading anchor."""
    text = re.sub(r"[`*_]", "", heading.strip().lower())
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def strip_code(text: str) -> str:
    """Blank out front matter and code so they are not checked as prose; keep line numbers."""
    text = FRONT_MATTER.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    text = FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    return INLINE_CODE.sub(lambda m: " " * len(m.group(0)), text)


def anchors(path: Path) -> set[str]:
    lines = strip_code(path.read_text(encoding="utf-8")).splitlines()
    return {slug(m.group(1)) for line in lines if (m := re.match(r"^#{1,6} +(.+?)\s*#*\s*$", line))}


def check(path: Path, override: str | None = None) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8")
    problems: list[tuple[int, str]] = []

    for m in FENCE.finditer(text):
        if m.group(2).strip().lower() == "mermaid":
            first = next((s.strip() for s in m.group(3).splitlines() if s.strip() and not s.strip().startswith("%%")), "")
            if not MERMAID.match(first):
                problems.append((text.count("\n", 0, m.start()) + 1, f"unknown Mermaid diagram type: {first!r}"))

    lines = strip_code(text).splitlines()

    titles = [i for i, line in enumerate(lines, 1) if re.match(r"^# \S", line)]
    first = next((i for i, line in enumerate(lines, 1) if line.strip()), 1)
    if len(titles) != 1 or titles[0] != first:
        problems.append((first, "the document must start with exactly one '# ' title"))

    sections = [(i, m.group(1)) for i, line in enumerate(lines, 1) if (m := re.match(r"^## +(.+?)\s*#*\s*$", line))]
    kind = doc_type(path, override)
    if kind in REQUIRED:
        required = REQUIRED[kind]
        allowed = required + OPTIONAL.get(kind, [])
        for line_no, name in sections:
            if name not in allowed:
                problems.append((line_no, f"'## {name}' is not a {kind} section (use ### inside a section)"))
        present = [name for _, name in sections if name in required]
        if present != required:
            missing = [name for name in required if name not in present]
            detail = f"missing: {', '.join(missing)}" if missing else "wrong order"
            problems.append((1, f"a {kind} needs: {', '.join(required)} ({detail})"))
        raw_lines = text.splitlines()
        for k, (line_no, name) in enumerate(sections):
            end = sections[k + 1][0] - 1 if k + 1 < len(sections) else len(raw_lines)
            if not "\n".join(raw_lines[line_no:end]).strip():
                problems.append((line_no, f"'## {name}' is empty; write 'None.' if there is nothing to say"))

    own_anchors = None
    for line_no, line in enumerate(lines, 1):
        if PLACEHOLDER.search(line):
            problems.append((line_no, "unfilled placeholder or TODO"))
        if LIFECYCLE.match(line) or LIFECYCLE_HEADING.match(line):
            problems.append((line_no, "status, approval and history belong in Git, not in the document"))
        for m in LINK.finditer(line):
            dest = unquote(m.group(1))
            if re.match(r"^[a-z][a-z0-9+.-]*:", dest, re.I):
                continue
            file_part, _, fragment = dest.partition("#")
            target = (path.parent / file_part).resolve() if file_part else path
            if not target.exists():
                problems.append((line_no, f"broken link: {dest}"))
                continue
            if not fragment or not target.is_file():
                continue
            span = re.fullmatch(r"L(\d+)(?:-L(\d+))?", fragment)
            if span:
                start, end = int(span.group(1)), int(span.group(2) or span.group(1))
                count = len(target.read_text(encoding="utf-8", errors="replace").splitlines())
                if start < 1 or end < start or end > count:
                    problems.append((line_no, f"line range {fragment} is outside {file_part or path.name} ({count} lines)"))
            elif target.suffix.lower() == ".md":
                if target == path:
                    own_anchors = own_anchors if own_anchors is not None else anchors(path)
                    found = own_anchors
                else:
                    found = anchors(target)
                if fragment.lower() not in found:
                    problems.append((line_no, f"no heading for anchor #{fragment} in {file_part or path.name}"))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Structural checks for tech-docs Markdown documents.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--type", choices=TYPES, help="document type; default: from the file name")
    args = parser.parse_args()

    files = []
    for p in args.paths:
        files += sorted(p.rglob("*.md")) if p.is_dir() else [p]

    total = 0
    for f in files:
        for line_no, message in check(f, args.type):
            print(f"{f}:{line_no}: {message}")
            total += 1
    print(f"{len(files)} file(s), {total} problem(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
