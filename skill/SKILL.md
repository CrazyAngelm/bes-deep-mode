---
name: bes-deep-mode
version: 1.0.2
author: BES Deep Mode contributors
license: MIT
description: Apply a BES/BEP-inspired deep reasoning loop for hard planning, architecture, debugging, research synthesis, and self-improvement tasks. Uses forward proposals, backward decomposition, evolutionary recombination, and evaluator gates before acting.
triggers:
  - "use BES"
  - "use BEP"
  - "BES mode"
  - "BEP mode"
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
  tags: [deep-reasoning, planning, debugging, self-improvement, bes, bep]
  related_skills: [systematic-debugging, writing-plans, requesting-code-review, test-driven-development]
---

# BES Deep Mode

BES Deep Mode is a practical skill for applying Bidirectional Evolutionary Planning (BEP): a bounded reasoning loop that combines forward candidate generation, backward requirement analysis, evolutionary recombination, and explicit evaluation gates.

## Contract
- Use only for hard/high-impact tasks; avoid for simple answers.
- Generate multiple candidate approaches before changing files or config.
- Score candidates with explicit criteria, then merge the strongest parts.
- Verify the result with an adversarial/self-review pass.
- Stop after convergence: no material improvement remains after 2 consecutive review passes.

## When To Trigger
Use this skill when the user asks to:
- “use BES”, “use BEP”, “BES mode”, “BEP mode”, or “deep mode”;
- think hard about a genuinely complex/high-impact task;
- iterate until convergence;
- design architecture or commercial deployment;
- debug root causes;
- make a concrete durable agent/process improvement;
- produce a high-stakes plan where first-pass answers are risky.

If a domain-specific skill applies, load it too and use BES as the meta-loop around that skill, not as a replacement.

Do NOT trigger for:
- quick factual answers;
- small formatting edits;
- simple arithmetic/lookups;
- casual chat.

## BES Loop

### 1. Frame
Write the goal in one sentence.
List constraints, success criteria, and risk of overengineering.

### 2. Forward Search
Generate 2-4 candidate approaches:
- conservative/simple;
- robust/production;
- experimental/high-upside;
- hybrid if useful.

### 3. Backward Search
Start from the desired final state and ask:
- what must be true for this to work?
- what can break?
- what is the minimum useful implementation?
- what verification proves it?

### 4. Evolutionary Recombination
Combine the best pieces into one plan:
- keep what is cheap and robust;
- discard complex parts without clear payoff;
- add guardrails from the backward pass.

### 5. Evaluation Gate
Score the merged plan 1-5 on:
- usefulness;
- reliability;
- cost/latency;
- maintainability;
- reversibility.

If any score is under 4, revise once before acting.

### 6. Act
Execute the smallest durable improvement that satisfies the goal:
- create or patch a skill;
- patch docs/config only when explicitly in scope;
- write a wrapper/tool only if needed;
- run tests or smoke checks.

Before mutating config, skills, cron, credentials, or cross-profile files, confirm scope unless the user explicitly requested that exact change.
For self-improvement requests, prefer patching or creating a skill only after identifying a concrete repeated failure or workflow gap. Do not claim global self-improvement from one prompt.

### 7. Self-Review Iteration
Run a review pass against the result:
- missing trigger?
- too verbose?
- unsafe mutation?
- hard to verify?
- does it actually improve future behavior?

Patch if useful.
Run at most 3 review/patch cycles after the first implementation. Stop early after 2 consecutive reviews with no material findings.

## Output Format
Keep the BES loop concise and mostly internal. In the final answer, expose only the chosen plan, key tradeoff, verification, and result unless the user asks for the full reasoning trace.

User-facing output should stay short:
- `Done:` 1-3 bullets.
- `Verification:` concrete checks/results.
- `Result:` whether BES is integrated enough or what remains.
- Avoid long explanations unless explicitly asked; for chat surfaces, prefer compact bullets over walls of text.

## Anti-Patterns
- Calling BES on every message.
- Infinite iteration or fake “self-improvement” claims.
- Replacing real verification with vibes.
- Creating code services when a skill is enough.
- Making hidden irreversible config changes without need.

## BES Runner Tool

When `bes_runner` is available, call it before acting on complex tasks that need explicit search/evaluation structure.

Recommended call pattern:
- First pass: `bes_runner(goal, context, mode="plan"|"debug"|"self_improve", max_candidates=3)`.
- After implementation: `bes_runner(goal, context, mode="review", iteration=2, previous_findings=[...])`.
- Stop after the tool indicates convergence or after 3 iterations.

Use the tool output as a scaffold, not as a substitute for real verification. Still run tests, file readbacks, smoke checks, or external review.

## Notes
This is original applied research, not a full implementation of any external paper. It improves agent behavior by combining this skill with a deterministic local `bes_runner` scaffold. For production use, the next step is an LLM-backed runner/service behind a model-routing layer.

## References
- `references/original-research.md` — original research note defining the BES/BEP reasoning pattern used by this skill.
- `references/install-guide.md` — portable install/verification notes for copying this skill to another agent instance, profile, Docker tenant, or commercial image.
- `references/runner-service.md` — local runner/service notes and production LLM-backed next step.
- `references/local-runner-implementation.md` — concrete local tool implementation and verification recipe for the local BES runner.
