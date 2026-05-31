# Original Research: Bidirectional Evolutionary Planning for Agent Skills

## Abstract

Bidirectional Evolutionary Planning (BEP), implemented here as BES Deep Mode, is a bounded reasoning pattern for agent skills. It reduces first-pass planning errors by forcing an agent to search from both ends of a problem: forward from possible actions and backward from the desired final state. Candidate plans are recombined, scored, and reviewed before execution.

This repository does not claim to reproduce an external paper. It documents an original applied pattern for practical agent work.

## Problem

Single-pass agent planning tends to fail in four predictable ways:

1. It commits to the first plausible solution.
2. It misses constraints that are only obvious from the desired end state.
3. It overbuilds abstractions before proving they pay for themselves.
4. It treats review as narrative rather than as a gate that can reject the plan.

The failure mode is most expensive on architecture, debugging, security-sensitive work, migrations, and high-impact operational changes.

## Hypothesis

A small, explicit loop improves reliability if it requires the agent to:

- generate multiple forward candidates;
- derive backward requirements from the final state;
- recombine only the strongest plan fragments;
- score the merged plan against practical criteria;
- stop when repeated review passes find no material improvement.

## Method

BEP is intentionally lightweight. It is not a tree search engine and does not require model finetuning.

### 1. Forward candidates

Generate 2-4 approaches with different risk profiles:

- conservative/simple;
- robust/production;
- experimental/high-upside;
- hybrid when useful.

### 2. Backward requirements

Start from the desired final state and list what must be true:

- required behavior;
- failure modes;
- minimum useful implementation;
- verification evidence.

### 3. Evolutionary recombination

Merge candidate fragments using selection pressure:

- keep cheap robust pieces;
- discard complexity without clear payoff;
- add guardrails found by backward reasoning;
- preserve reversibility where possible.

### 4. Evaluation gate

Score the merged plan from 1 to 5 on:

- usefulness;
- reliability;
- cost/latency;
- maintainability;
- reversibility.

Any score below 4 forces one revision before acting.

### 5. Bounded self-review

After execution, run at most 3 review/patch cycles. Stop early after 2 consecutive reviews find no material issue.

## Safety properties

BEP is useful only if it stays bounded.

- It must not run for every message.
- It must not replace domain-specific tools or tests.
- It must not justify hidden mutation of credentials, config, or user-owned files.
- It must not present internal reasoning as proof.
- It must require concrete verification before claiming success.

## Practical result

The skill in `skill/SKILL.md` turns BEP into an agent-facing contract. The optional local `bes_runner` described in `references/runner-service.md` can make the loop deterministic by returning structured fields for candidates, requirements, recombination, scoring, and convergence.

## Terminology

- **BEP**: Bidirectional Evolutionary Planning, the general planning pattern.
- **BES**: Backward/Forward Evolutionary Search, the skill's concise operational name.
- **BES Deep Mode**: The packaged agent skill in this repository.

## Limitations

- BEP improves planning discipline; it does not guarantee correctness.
- External verification still comes from tests, inspections, smoke checks, and domain review.
- The loop has overhead and should be reserved for complex or high-impact work.
