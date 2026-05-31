---
name: bes-deep-mode
version: 1.1.0
author: BES Deep Mode contributors
license: MIT
description: Use this skill for complex or high-impact agent tasks where first-pass plans are risky: architecture decisions, hard debugging, migrations, security-sensitive changes, research synthesis, or self-improvement. It adapts Xu et al.'s Bidirectional Evolutionary Search (BES) into a bounded workflow for Claude Code, Codex, and other coding agents: generate forward candidates, decompose the desired end state backward into checkable requirements, recombine the best fragments, score the plan, execute only the chosen plan, and verify before claiming success. Do not use for quick factual answers or simple edits.
triggers:
  - "use BES"
  - "BES mode"
  - "deep mode"
  - "iterate until convergence"
  - "think carefully about this complex task"
tools:
  - todo
  - delegation
  - terminal
  - file
  - skills
mutating: true
metadata:
  tags: [deep-reasoning, planning, debugging, self-improvement, bes]
  related_skills: [systematic-debugging, writing-plans, requesting-code-review, test-driven-development]
---

# BES Deep Mode

BES Deep Mode adapts **Bidirectional Evolutionary Search** (Xu et al., 2026) into a practical workflow for coding agents. Use it when the cost of a wrong first answer is high enough to justify a short search-and-review loop.

## Contract

- Use only for complex/high-impact tasks; skip for simple answers and mechanical edits.
- Keep the loop bounded: 2-4 candidates, one merged plan, one revision if a score is below threshold, then act.
- Search both directions: forward from possible actions, backward from the desired final state.
- Execute only the merged plan; do not implement multiple candidate branches unless the user explicitly asks for prototypes.
- Verify with real checks before claiming success.

## When to Trigger

Trigger when the user asks to:

- use BES, BES mode, or deep mode;
- think hard about a complex/high-impact coding task;
- design architecture, APIs, migrations, deployment, or security-sensitive changes;
- debug an unclear root cause;
- improve an agent/process/tooling workflow;
- synthesize research into an implementation plan.

If a domain-specific skill applies, load it too. BES is the meta-loop around that skill, not a replacement.

Do not trigger for quick factual answers, small formatting changes, arithmetic, single-command help, or casual chat.

## Operating Loop

### 1. Frame

Write one sentence for the goal, then list:

- constraints;
- success criteria;
- likely failure modes;
- risk of overengineering.

### 2. Forward search

Generate 2-4 candidate approaches with different risk profiles:

- conservative/simple;
- robust/production;
- experimental/high-upside;
- hybrid, only if it is meaningfully different.

For coding work, include likely files or components touched. For debugging, include the reproduction or instrumentation path.

### 3. Backward search

Start from the desired final state and decompose it into checkable requirements:

- what observable behavior must be true?
- what invariants must hold?
- what can break?
- what is the minimum useful implementation?
- what verification proves it?

This is the key BES move: use the backward requirements as dense feedback to reject weak forward candidates before editing.

### 4. Recombine

Merge only the strongest fragments:

- keep cheap robust pieces;
- discard complexity without clear payoff;
- add guardrails discovered by backward search;
- preserve reversibility where possible.

Name the chosen plan in one compact paragraph or checklist.

### 5. Evaluation gate

Score the chosen plan 1-5 on:

- usefulness;
- reliability;
- cost/latency;
- maintainability;
- reversibility.

If any score is below 4, revise the plan once. If it is still below 4, state the blocker or choose the simpler safe path.

### 6. Act

Execute the smallest durable change satisfying the chosen plan:

- edit existing files before creating new ones;
- avoid hidden mutation of credentials, config, hooks, or cross-profile state;
- keep tool output grounded;
- remove obsolete code when replacing behavior.

Before mutating credentials, startup hooks, shell profiles, git remotes, global config, or cross-profile files, confirm scope unless the user explicitly requested that exact mutation.

### 7. Verify

Run the narrowest real check that covers the change:

- tests for code behavior;
- smoke command for scripts/tools;
- link/content checks for documentation-only changes;
- security/privacy scans before publishing public repos.

Do not claim integration, performance, or safety unless that exact property was checked.

### 8. Bounded review

Run one adversarial review pass:

- missing trigger or edge case?
- unsafe mutation?
- too verbose or too hidden?
- verification too weak?
- mismatch with BES paper terminology?

Patch if useful. Stop after 2 consecutive review passes with no material finding or after 3 total review passes.

## Codex / Claude Code Usage

This skill works best when the agent has filesystem and terminal tools. Use these bundled prompt templates when you want to paste the workflow into another agent:

- `templates/codex-prompt.md` for Codex-style coding agents.
- `templates/claude-code-prompt.md` for Claude Code.

For public-release or repo-prep work, run `python scripts/validate_skill.py` before publishing. The script checks for non-English Cyrillic text, common secret patterns, private absolute paths, and required public-release files.

## Output Format

Keep the BES loop mostly internal. In the final answer, expose only:

- `Done:` 1-3 bullets.
- `Verification:` concrete checks/results.
- `Result:` final state or remaining blocker.

Include the full candidate table only if the user asks for the reasoning trace or if a decision needs explicit review.

## Anti-Patterns

- Calling BES on every message.
- Treating more candidates as better after the plan has converged.
- Implementing multiple branches instead of selecting one.
- Replacing real verification with narrative confidence.
- Creating services, hooks, or scripts when a skill prompt is enough.
- Making hidden irreversible config changes.

## BES Runner Tool

When `bes_runner` is available, call it before acting on complex tasks that need explicit search/evaluation structure.

Recommended call pattern:

- First pass: `bes_runner(goal, context, mode="plan"|"debug"|"self_improve", max_candidates=3)`.
- After implementation: `bes_runner(goal, context, mode="review", iteration=2, previous_findings=[...])`.
- Stop after the tool indicates convergence or after 3 iterations.

Use the tool output as a scaffold, not as a substitute for real verification. Still run tests, file readbacks, smoke checks, or external review.

## Notes

This is a practical agent-skill adaptation of Bidirectional Evolutionary Search (Xu et al., 2026), not a full reproduction of the paper's training or inference system. It improves agent behavior by combining the BES planning discipline with a deterministic local `bes_runner` scaffold.

Do not add hooks, installers, global config changes, or background services unless the user explicitly asks for them. Prefer opt-in scripts and copy-paste templates.

## References

- `references/original-research.md` — upstream BES links, citation, method summary, and reported benchmark results.
- `references/install-guide.md` — portable install/verification notes for copying this skill to another agent instance, profile, Docker tenant, or commercial image.
- `references/runner-service.md` — local runner/service notes and production LLM-backed next step.
- `references/local-runner-implementation.md` — concrete local tool implementation and verification recipe for the local BES runner.
