---
title: "DSPyCallback"
type: concept
tags: [dspy, observability, callbacks, instrumentation, hooks]
sources: [dspy-observability-tutorial]
last_updated: 2026-05-24
---

# DSPyCallback (`BaseCallback`)

**`dspy.utils.callback.BaseCallback`** is [[DSPy]]'s **custom-instrumentation interface** — the user-programmable tier of [[DSPyObservability|the three-tier observability stack]]. Subclass it, override the handlers you care about, and register the instance process-wide via `dspy.configure(callbacks=[...])`. Every framework component then fires the matching event into the handler.

## Handler surface — six pairs

The [[dspy-observability-tutorial|tutorial]] documents six start/end handler pairs covering the framework's full event surface:

| Handler pair | Fires on | Layer |
|---|---|---|
| `on_module_start` / `on_module_end` | Any [[DSPyModules|`dspy.Module`]] `__call__` | Top-level program flow |
| `on_lm_start` / `on_lm_end` | Any [[DSPyLM|`dspy.LM`]] call | LM-client boundary |
| `on_adapter_format_start` / `on_adapter_format_end` | [[DSPyAdapters|Adapter]] prompt-rendering pass | Pre-LM wire-format render |
| `on_adapter_parse_start` / `on_adapter_parse_end` | [[DSPyAdapters|Adapter]] response-parsing pass | Post-LM wire-format parse |
| `on_tool_start` / `on_tool_end` | [[DSPyTools|`dspy.Tool`]] invocation | Tool-call boundary |
| `on_evaluate_start` / `on_evaluate_end` | [[DSPyEvaluate|`dspy.Evaluate`]] run | Evaluation orchestration |

The pairing structure means **every event has a matched bracket** — start fires before the work, end fires after — letting callbacks measure duration, log inputs vs outputs symmetrically, and reliably increment/decrement state (e.g. a nesting depth counter).

## Registration

```python
import dspy
from dspy.utils.callback import BaseCallback

class MyCallback(BaseCallback):
    ...

dspy.configure(callbacks=[MyCallback()])
```

The `callbacks=[...]` kwarg sits alongside the standard [[DSPy]] configuration knobs (`lm=`, `adapter=`, `allow_tool_async_sync_conversion=`). It is **a list** — multiple callbacks can be registered simultaneously, all firing on every matching event. There is no priority / ordering API documented; the framework iterates the list.

## Canonical receipt — `AgentLoggingCallback`

The [[dspy-observability-tutorial|tutorial]]'s worked example logs only the **reasoning steps** of a [[react|`dspy.ReAct`]] agent, ignoring the action steps:

```python
from dspy.utils.callback import BaseCallback

class AgentLoggingCallback(BaseCallback):
    def on_module_end(self, call_id, outputs, exception):
        step = "Reasoning" if self._is_reasoning_output(outputs) else "Acting"
        print(f"== {step} Step ===")
        for k, v in outputs.items():
            print(f"  {k}: {v}")

    def _is_reasoning_output(self, outputs):
        return any(k.startswith("Thought") for k in outputs.keys())

dspy.configure(callbacks=[AgentLoggingCallback()])
```

Three structural properties this example exposes:

1. **`on_module_end` receives `outputs`** — the dict of [[DSPyPrediction|Prediction]] field values returned by the Module call. Inspecting field names is the canonical way to discriminate between Module subclasses (here, [[react|`dspy.ReAct`]]'s `Thought*` keys identify reasoning steps).
2. **`call_id` parameter** — opaque identifier the framework passes through; pairs `on_module_start` with the corresponding `on_module_end` for nested calls.
3. **`exception` parameter** — the `*_end` handlers receive an exception object if the call failed. Callbacks must tolerate `exception=None` (success path) and `exception=<Exception>` (failure path).

## Trade-off vs `mlflow.autolog`

The tutorial frames the tier-3 cost: *"Note that it requires a bit more boilerplate code, but it gives us more control over the logging behavior."*

| Property | `mlflow.autolog()` (tier 2) | `BaseCallback` (tier 3) |
|---|---|---|
| Coverage | All events automatically | Only events the user overrides |
| Filtering | All-or-nothing per event type | Arbitrary user logic |
| Output sink | [[MLflow]] tracking server | User-defined (print, log, DB, anywhere) |
| Setup cost | One install + one server | One Python class |
| Persistence | Yes — trace store | None unless user implements |
| Trace tree UI | Yes — MLflow UI | None unless user implements |

The two tiers are **stackable, not mutually exclusive** — register a `BaseCallback` for custom side effects (e.g. emit to a custom metrics pipeline) **alongside** MLflow autolog (for the persisted trace tree).

## Position vs other instrumentation idioms

- **vs Python `logging`** — `BaseCallback` is the framework-native event source; the user is free to forward callback events into `logging.getLogger(...).info(...)` rather than `print(...)`. This is the recommended production pattern but is not documented in the tutorial.
- **vs [[OpenTelemetry]]** — no first-party OTel exporter is documented in the DSPy tutorial corpus. `BaseCallback` is the integration seam — a user-written subclass can emit OTel spans from each handler.
- **vs [[MLflow]] autolog** — see [[DSPyObservability]] for the full three-tier comparison.

## Code receipt — measuring latency per Module

```python
import time
from dspy.utils.callback import BaseCallback

class LatencyCallback(BaseCallback):
    def __init__(self):
        self._start = {}

    def on_module_start(self, call_id, instance, inputs):
        self._start[call_id] = time.perf_counter()

    def on_module_end(self, call_id, outputs, exception):
        elapsed = time.perf_counter() - self._start.pop(call_id, None)
        print(f"{type(instance).__name__}: {elapsed*1000:.1f}ms")
```

Inferred from the tutorial's handler signatures — `call_id` pairs start with end, `instance` is the Module being called.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-observability-tutorial]] — canonical receipt: subclasses `BaseCallback`, overrides `on_module_end(call_id, outputs, exception)`, registers via `dspy.configure(callbacks=[AgentLoggingCallback()])`, and demonstrates selective filtering on a [[react|`dspy.ReAct`]] agent's reasoning vs action steps.

## Tracked sources

- **[[dspy-observability-tutorial]]** (2026-05-24) — canonical source; lists all six handler pairs and supplies the `AgentLoggingCallback` worked example.
- **[[DSPyObservability]]** — parent concept page placing `BaseCallback` as tier 3 of the observability stack.
