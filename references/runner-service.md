# BES Runner/Service

## Current local tool

A local tool implementation can expose the BES loop as deterministic structure:

- source: `tools/bes_runner_tool.py`
- tool name: `bes_runner`
- toolset: `bes`
- tests: `tests/tools/test_bes_runner_tool.py`

It is deterministic and local. It does not call an LLM by itself. The agent supplies reasoning; the runner supplies the BES structure.

## Enable/use

In an agent session with the `bes` toolset enabled, call:

```json
{
  "goal": "Improve planning for complex tasks",
  "context": "Need concise, reversible, verified output",
  "mode": "self_improve",
  "max_candidates": 3,
  "iteration": 1
}
```

Modes:

- `plan`
- `debug`
- `review`
- `self_improve`

Output includes:

- `forward_candidates`
- `backward_requirements`
- `recombined_plan`
- `evaluation_gate`
- `convergence`

## Verification commands

```bash
python -m pytest tests/tools/test_bes_runner_tool.py -q
python - <<'PY'
import json
from tools.bes_runner_tool import _handle_bes_runner
print(_handle_bes_runner({"goal":"test BES runner", "mode":"plan"}))
PY
agent tools list | grep -i bes
```

## Production next step

For a real LLM-backed BES service:

```text
agent task -> bes_runner tool -> BES service -> model aliases -> evaluator -> plan -> agent executes
```

Recommended aliases:

- `bes-candidate`
- `bes-evaluator`
- `bes-synthesizer`

Keep the current local runner as fallback when model calls fail.
