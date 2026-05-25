---
title: "Hand-Rolled ReAct (in DSPy)"
type: concept
tags: [dspy, agent, react, design-pattern, custom-module, tool-use]
sources: [dspy-tool-use-tutorial]
last_updated: 2026-05-24
---

# Hand-Rolled ReAct

A **hand-rolled ReAct** is a [[DSPy]] agent pattern that **bypasses [[react|`dspy.ReAct`]]** in favor of a manual `for` loop over a single [[chainofthought|`dspy.ChainOfThought`]] Signature, with the agent's `forward()` method managing trajectory state, tool selection, tool invocation, and termination. The pattern is the minimum-viable ReAct: one Signature, one loop, one terminal-tool convention.

## Canonical shape

```python
class Agent(dspy.Module):
    def __init__(self, max_steps=5):
        self.max_steps = max_steps
        signature = dspy.Signature(
            'question, trajectory, functions -> next_selected_fn, args: dict[str, Any]',
            instructions="..."
        )
        self.react = dspy.ChainOfThought(signature)

    def forward(self, question, functions):
        tools = {fn_name: fn_metadata(fn) for fn_name, fn in functions.items()}
        trajectory = []
        for _ in range(self.max_steps):
            pred = self.react(question=question, trajectory=trajectory, functions=tools)
            selected_fn = pred.next_selected_fn.strip('"').strip("'")
            fn_output = wrap_function_with_timeout(functions[selected_fn])(**pred.args)
            trajectory.append(dict(reasoning=pred.reasoning, selected_fn=selected_fn,
                                   args=pred.args, **fn_output))
            if selected_fn == "finish":
                break
        return dspy.Prediction(answer=fn_output.get("return_value", ''), trajectory=trajectory)
```

The canonical receipt is the [[dspy-tool-use-tutorial|DSPy tool-use tutorial]] against [[ToolHop]].

## When to escape `dspy.ReAct`

[[react|`dspy.ReAct`]] is the right default; the hand-rolled pattern is appropriate when:

1. **Tool sets vary per example.** ToolHop ships a different `functions` dict per datapoint — the agent receives tools as a runtime input, not a constructor kwarg. `dspy.ReAct(signature, tools=[...])` binds tools at construction.
2. **Termination needs custom logic.** A synthetic `finish(answer: str)` tool gives the model *explicit* control over termination, distinct from `dspy.ReAct`'s default termination heuristics.
3. **Tool metadata format needs control.** The hand-rolled pattern exposes tools to the LM as a `dict[str, Any]` Signature field — author controls the schema. `dspy.ReAct` uses `dspy.Tool` and an internal format.
4. **Untrusted tool code requires sandbox-aware invocation.** [[func_timeout|`func_timeout`]] wrapping, exception-to-dict mapping (`{"return_value": ..., "errors": ...}`), and side-effect tracking are easier to bolt on at the loop level than inside `dspy.ReAct`'s closed implementation.

## Trade-offs vs `dspy.ReAct`

| Property | `dspy.ReAct` | Hand-rolled |
|---|---|---|
| Tool binding | Constructor (`tools=[...]`) | Runtime (`forward(functions=...)`) |
| Tool format | `dspy.Tool` (auto-derived metadata) | Author-controlled `dict[str, Any]` |
| Termination | Framework heuristics | Custom (synthetic `finish` tool) |
| Tracing | Framework-managed | Author-managed |
| Optimizer compatibility | Full ([[MIPROv2]] / [[SIMBA]] / [[GEPA]] / [[ArborGRPO]]) | Full — same `dspy.Module` surface |
| Lines of code | 1 | ~20 |

The hand-rolled pattern is **not less powerful** — it composes with every DSPy optimizer because the agent is a regular `dspy.Module`. The choice is between framework convenience and per-step control.

## Optimizer composition

The [[dspy-tool-use-tutorial|tool-use tutorial]] composes hand-rolled ReAct with [[SIMBA|`dspy.SIMBA(max_steps=12, max_demos=10)`]] for **35.0% → 60.7%** lift on [[ToolHop]] dev accuracy. **First wiki receipt of a hand-rolled ReAct + prompt-space optimizer combination**. Prior hand-rolled-agent receipts ([[dspy-rl-multihop-tutorial]]'s [[ResearchHop]]) used weight-space [[ArborGRPO]] instead.

## Comparison to `ResearchHop`

[[ResearchHop]] (from [[dspy-rl-multihop-tutorial]]) is a different flavour of hand-rolled agent: two named `dspy.ChainOfThought` sub-modules (`generate_query`, `append_notes`) in a hop-loop, with deterministic title-recall as reward and an [[ArborGRPO]] weight-space optimizer. The tool-use tutorial's `Agent` is a **single-Signature** hand-rolled agent (tool selection + arg generation in one ChainOfThought) with a brittle exact-match metric and a [[SIMBA]] prompt-space optimizer. **Two distinct hand-rolled-agent shapes** in the wiki: ResearchHop's *multi-Signature hop-loop* and the tool-use tutorial's *single-Signature tool-selector loop*.

## Connections

- [[react|`dspy.ReAct`]] — the framework-provided alternative.
- [[dspy-tool-use-tutorial]] — canonical receipt (single-Signature variant).
- [[ResearchHop]] / [[dspy-rl-multihop-tutorial]] — sibling hand-rolled-agent receipt (multi-Signature variant).
- [[chainofthought|`dspy.ChainOfThought`]] — the Module the loop wraps.
- [[DSPyModules]] — the `dspy.Module` base class.
- [[DSPySignatures]] — the inline `dspy.Signature(str_spec, instructions_str)` form is the natural construction surface for the loop's Signature.
- [[DSPyTools]] — the framework's tool surface; the hand-rolled pattern bypasses `dspy.Tool`.
- [[SIMBA]] — the optimizer in the canonical receipt.
- [[ToolHop]] — the canonical benchmark.
- [[func_timeout]] — the typical tool-sandbox companion.
- [[TrustedMonitor]] — adjacent custom-`dspy.Module` pattern (`MonitorTrainerProgram` is a hand-rolled wrapper around a single-Signature classifier for the same reason: optimizer needs to see paired rollouts).
