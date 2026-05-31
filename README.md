# BES Deep Mode

BES Deep Mode is an agent skill for applying **Bidirectional Evolutionary Planning (BEP)** to hard planning, architecture, debugging, research synthesis, and self-improvement tasks.

The skill is intentionally bounded: it generates multiple candidate approaches, works backward from the desired final state, recombines the strongest pieces, scores the result, and verifies before claiming success.

## Repository contents

- `skill/SKILL.md` — the installable skill.
- `references/original-research.md` — original BEP/BES research note.
- `references/install-guide.md` — portable installation and verification guide.
- `references/runner-service.md` — optional runner/service design notes.
- `references/local-runner-implementation.md` — local runner implementation notes.

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

## Safety and privacy

This repository contains no credentials, API keys, private paths, or personal data. The examples use generic placeholders and public-safe paths.

The skill explicitly requires confirmation before mutating credentials, config, cross-profile files, or other sensitive state unless that exact mutation was requested.

## Research status

This is original applied research for agent workflows. It is not a claimed reproduction of any external paper.

See `references/original-research.md` for the BEP method and limitations.

## License

MIT. See `LICENSE`.
