# Claude Code BES Deep Mode Prompt

Use this prompt when asking Claude Code to apply BES Deep Mode inside a repository.

```text
Use BES Deep Mode on this repository task.

Task: <specific coding/debugging/refactor/release task>
Relevant files: <paths if known, otherwise discover them first>
Acceptance criteria:
- <behavioral requirement>
- <affected callsites/docs/tests updated>
- <specific verification command or smoke check>

Follow this operating contract:
- Use repo tools to inspect before editing; do not guess file contents.
- Generate 2-4 candidate approaches, then decompose the desired end state backward into checkable requirements.
- Recombine into one chosen plan and score it on usefulness, reliability, cost/latency, maintainability, reversibility.
- Execute the smallest durable change satisfying the plan.
- Prefer editing existing files over creating new abstractions.
- Do not add git hooks, startup hooks, global config changes, background services, installers, or credential mutations unless I explicitly ask for them.
- Verify with targeted tests/checks and report only observed results.

Final answer format:
Done:
- <1-3 bullets>
Verification:
- <commands/checks and results>
Result:
- <final state or blocker>
```
