# Local BES runner implementation notes

BES becomes more useful when it moves from a pure prompt/skill scaffold to a deterministic local agent tool.

## Current pattern

Implement a local runner as a normal agent tool:

- file: `tools/bes_runner_tool.py`
- registry: top-level `registry.register(...)`
- tool name: `bes_runner`
- toolset: `bes`
- add to the core tool list when it should be available in default chat surfaces
- tests: `tests/tools/test_bes_runner_tool.py`

## Tool behavior

The local runner should be deterministic and safe:

- no shell execution;
- no file mutation;
- no network calls;
- no credentials;
- returns JSON via the host agent's tool result API.

It does not replace LLM reasoning. It gives the agent a structured BES scaffold:

- forward candidates;
- backward requirements;
- recombined plan;
- evaluation gate;
- convergence/next-step guidance.

## Verification recipe

Run targeted tests:

```bash
python -m pytest tests/tools/test_bes_runner_tool.py tests/test_toolsets.py::TestToolsetConsistency::test_platforms_share_core_tools -q
```

Smoke-dispatch through agent internals:

```python
import json
from model_tools import get_tool_definitions, handle_function_call

defs = get_tool_definitions(enabled_toolsets=['agent-cli'], disabled_toolsets=[], quiet_mode=True)
assert any(d.get('function', {}).get('name') == 'bes_runner' for d in defs)

raw = handle_function_call(
    'bes_runner',
    {'goal': 'Final BES runner verification', 'mode': 'review', 'max_candidates': 2},
    enabled_toolsets=['agent-cli'],
    disabled_toolsets=[],
)
data = json.loads(raw)
assert data['success'] is True
```

## When to go beyond this

Only build an LLM-backed BES service when the user needs premium/high-stakes mode:

```text
agent task -> local bes_runner/classifier -> LLM-backed BES service -> model aliases -> evaluator -> synthesized plan -> agent executes
```

Keep local `bes_runner` as fallback and default because it is cheap, fast, and reliable.
