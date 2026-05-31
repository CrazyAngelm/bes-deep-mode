# Codex BES Deep Mode Prompt

Use this prompt when asking Codex or another coding agent to apply BES Deep Mode.

```text
Use BES Deep Mode for this task.

Goal: <one-sentence goal>
Context: <repo, files, constraints, current failure, or desired change>
Acceptance criteria:
- <observable outcome 1>
- <observable outcome 2>
- <verification command or scenario>

Run the bounded BES loop:
1. Frame the goal, constraints, success criteria, failure modes, and overengineering risk.
2. Generate 2-4 forward candidate approaches.
3. Work backward from the desired final state into checkable requirements and verification evidence.
4. Recombine the strongest fragments into one plan.
5. Score the plan 1-5 on usefulness, reliability, cost/latency, maintainability, and reversibility. Revise once if any score is below 4.
6. Implement only the chosen plan. Do not implement competing branches unless explicitly asked.
7. Verify with real commands or tests before claiming success.
8. Final answer: Done / Verification / Result.

Safety constraints:
- Do not create hooks, installers, global config changes, background services, or credential mutations unless explicitly requested.
- Do not hide failures or substitute narrative confidence for verification.
- Do not broaden scope beyond the acceptance criteria.
```
