# BES Deep Mode

BES Deep Mode is an agent skill inspired by **Bidirectional Evolutionary Search (BES)** from Xu et al., 2026, adapted into a lightweight workflow for hard planning, architecture, debugging, research synthesis, and self-improvement tasks.

The skill is intentionally bounded: it generates multiple candidate approaches, works backward from the desired final state, recombines the strongest pieces, scores the result, and verifies before claiming success.

## Repository contents

- `skill/SKILL.md` — the installable skill.
- `references/original-research.md` — original BES paper links, citation, method summary, and benchmark results.
- `references/install-guide.md` — portable installation and verification guide.
- `references/runner-service.md` — optional runner/service design notes.
- `references/local-runner-implementation.md` — local runner implementation notes.
- `templates/codex-prompt.md` — paste-ready prompt for Codex-style agents.
- `templates/claude-code-prompt.md` — paste-ready prompt for Claude Code.
- `scripts/validate_skill.py` — opt-in public-release safety validator.

## Use cases

Use BES Deep Mode for:

- high-impact architecture decisions;
- hard debugging and root-cause analysis;
- migration or deployment planning;
- security-sensitive changes;
- agent/process improvement where first-pass answers are risky.

Do not use it for quick factual answers, simple formatting edits, arithmetic, or casual chat.

## Install

Copy `skill/SKILL.md` into your agent skill directory under `bes-deep-mode/SKILL.md`.

See `references/install-guide.md` for example paths and smoke checks.

## Codex / Claude Code

Use the templates when the target agent does not have a native skill loader:

- `templates/codex-prompt.md`
- `templates/claude-code-prompt.md`

Before publishing changes, run:

```bash
python scripts/validate_skill.py
```

The repository intentionally does not install git hooks, shell hooks, background services, or global config. Automation is opt-in and reviewable.

## Safety and privacy

This repository contains no credentials, API keys, private paths, or personal data. The examples use generic placeholders and public-safe paths.

The skill explicitly requires confirmation before mutating credentials, config, cross-profile files, or other sensitive state unless that exact mutation was requested.

## Research basis

This skill is based on the original BES research page and paper:

- Project page: <https://guoweixu.com/bes/>
- Paper: <https://arxiv.org/abs/2605.28814>
- Code: <https://github.com/Embodied-Minds-Lab/BES>

See `references/original-research.md` for the citation, method summary, and reported benchmark results.

## License

MIT. See `LICENSE`.
