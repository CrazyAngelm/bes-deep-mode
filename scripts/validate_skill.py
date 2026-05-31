#!/usr/bin/env python3
"""Validate BES Deep Mode public-release safety and required references."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEXT_EXTENSIONS = {".md", ".py", ".txt", ".yml", ".yaml", ".json", ""}
REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "skill/SKILL.md",
    "references/original-research.md",
    "templates/codex-prompt.md",
    "templates/claude-code-prompt.md",
]
REQUIRED_STRINGS = {
    "README.md": [
        "https://guoweixu.com/bes/",
        "https://arxiv.org/abs/2605.28814",
        "https://github.com/Embodied-Minds-Lab/BES",
    ],
    "references/original-research.md": [
        "Self-Improving Language Models with Bidirectional Evolutionary Search",
        "MuSiQue",
        "Circle Packing",
        "Heilbronn",
    ],
    "skill/SKILL.md": [
        "Bidirectional Evolutionary Search",
        "templates/codex-prompt.md",
        "templates/claude-code-prompt.md",
        "scripts/validate_skill.py",
        "Do not add hooks",
    ],
}

CHECKS = [
    ("cyrillic text", re.compile(r"[\u0400-\u04FF]")),
    ("private Windows user path", re.compile(r"C:\\\\Users\\\\[A-Za-z0-9._-]+", re.I)),
    ("private Unix home path", re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]+", re.I)),
    ("OpenAI-style secret", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("GitHub classic token", re.compile(r"ghp_[A-Za-z0-9_]{20,}")),
    ("GitHub fine-grained token", re.compile(r"github_pat_[A-Za-z0-9_]{20,}")),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("password assignment", re.compile(r"password\s*[:=]", re.I)),
    ("secret assignment", re.compile(r"secret\s*[:=]", re.I)),
    ("token assignment", re.compile(r"token\s*[:=]", re.I)),
    ("dangerous recursive delete", re.compile(r"rm\s+-rf", re.I)),
    ("pipe remote script to shell", re.compile(r"(?:curl|wget)\s+[^\n]*\|\s*(?:sh|bash)", re.I)),
]


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_dir():
            parts = set(path.parts)
            if parts & {".git", "__pycache__", "node_modules", ".pytest_cache"}:
                continue
        if not path.is_file():
            continue
        if any(part in {".git", "__pycache__", "node_modules", ".pytest_cache"} for part in path.parts):
            continue
        if path.suffix in TEXT_EXTENSIONS:
            files.append(path)
    return files


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required file: {rel}")

    for rel, needles in REQUIRED_STRINGS.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{rel}: missing required text: {needle}")

    for path in iter_text_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for label, pattern in CHECKS:
            match = pattern.search(text)
            if match:
                line = text[: match.start()].count("\n") + 1
                failures.append(f"{rel}:{line}: {label}: {match.group(0)!r}")

    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Validation passed.")
    print(f"Checked {len(iter_text_files())} text files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
