---
title: "func_timeout"
type: entity
tags: [python, library, sandbox, tool-runtime, timeout]
sources: [dspy-tool-use-tutorial]
last_updated: 2026-05-24
---

# func_timeout

**`func_timeout`** is a third-party Python package (originally by kata198 / James W. Smith) exposing thread-based timeouts for arbitrary function calls. PyPI: `func_timeout`. Canonical API:

```python
from func_timeout import func_set_timeout, FunctionTimedOut

@func_set_timeout(10)
def slow_function(x):
    ...
```

If `slow_function` runs longer than 10 seconds, `func_timeout` interrupts it (via thread-stop on CPython, raising `FunctionTimedOut`). Distinct from `asyncio.wait_for(...)` (requires the inner function to be coroutine-compatible) and `signal.alarm(...)` (Unix-only, main-thread-only).

## Role in DSPy

The [[dspy-tool-use-tutorial|DSPy tool-use tutorial]] uses `func_set_timeout` as the **tool-runtime sandbox** for `exec()`-ed [[ToolHop]] tools:

```python
def wrap_function_with_timeout(fn):
    @func_set_timeout(10)
    def wrapper(*args, **kwargs):
        try:
            return {"return_value": fn(*args, **kwargs), "errors": None}
        except Exception as e:
            return {"return_value": None, "errors": str(e)}
    return wrapper
```

The wrapper does two things at once:

1. **Bounds runtime** to 10 seconds (`@func_set_timeout(10)`).
2. **Maps exceptions to a dict** so the [[HandRolledReAct|hand-rolled ReAct]] loop can read either a return value or an error string from each tool call — no try/except inside the loop body.

## Caveats

`func_timeout` is a **runtime** bound, not a **side-effect** bound. A tool can write files, open network connections, or invoke `os.system(...)` within its 10-second budget. The tutorial does not address this — the assumption is that the dataset is trusted.

For untrusted-code execution, a child-process or container isolation layer (subprocess + `seccomp`, gVisor, Firecracker, [[ModelContextProtocol|MCP]] stdio server) is the correct boundary; `func_timeout` is **complementary** but not sufficient.

## Connections

- [[dspy-tool-use-tutorial]] — the wiki's first DSPy receipt using `func_timeout`.
- [[HandRolledReAct]] — the typical DSPy companion pattern.
- [[ToolHop]] — the benchmark that motivates the sandbox (per-question `exec()`-ed tool code).
- [[DSPyTools]] — `func_timeout` is orthogonal to `dspy.Tool`; both can wrap tool callables.
- [[ModelContextProtocol]] — adjacent isolation pattern (child-process boundary instead of timeout).
- [[Python]] — host language.
