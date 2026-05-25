---
title: "ToolHop"
type: concept
tags: [benchmark, tool-use, multi-hop, agent, dspy, bytedance, exec-tools]
sources: [dspy-tool-use-tutorial]
last_updated: 2026-05-24
---

# ToolHop

**ToolHop** is a multi-hop tool-use benchmark released by [[ByteDanceResearch]] (`bytedance-research/ToolHop` on HuggingFace). Each datapoint pairs a natural-language question with a **per-question bundle of Python tool source-code strings** and a gold answer requiring **multi-hop composition** of those tools. Hops are *tool calls*, not text retrievals — distinguishing ToolHop from sibling multi-hop QA benchmarks like [[hotpotqa|HotPotQA]] / [[HoVer]] / [[MultiHopQA]].

## Data shape

Each datapoint contains:

- `question`: natural-language query.
- `answer`: gold short-form answer (date / name / number / string).
- `functions`: list of Python source-code strings, each defining one tool function. Each string includes a `# Example usage` suffix that must be **stripped before `exec()`**.

The `functions` field is the structurally novel part: each datapoint **ships its own dynamically-compiled tool set**, so the agent's tool list varies across the benchmark. There is no static tool registry.

## Tool-construction recipe

The [[dspy-tool-use-tutorial|DSPy tool-use tutorial]] shows the canonical loader:

```python
for datapoint in data:
    func_dict = {}
    for func_code in datapoint["functions"]:
        cleaned_code = func_code.rsplit("\n\n# Example usage", 1)[0]
        fn_name = re.search(r"^\s*def\s+([a-zA-Z0-9_]+)\s*\(", cleaned_code).group(1)
        local_vars = {}
        exec(cleaned_code, {}, local_vars)
        func_dict[fn_name] = local_vars[fn_name]
    func_dict["finish"] = finish  # synthetic terminal tool
```

Three security implications follow from the `exec()` step:

1. **Untrusted code by default.** The dataset is treated as trusted, but the pipeline `exec()`-es arbitrary Python in the agent's process — sandbox escape if the dataset is malicious.
2. **Tool-runtime bounds via [[func_timeout|`func_timeout`]].** The tutorial wraps every tool call in `@func_set_timeout(10)` to kill runaway computations. Does not bound side effects (filesystem, network).
3. **Per-question synthetic `finish` tool.** The agent terminates by *selecting* a `finish(answer: str)` tool whose return value is the trajectory's final answer — pattern works because the tool-selection mechanism is the same one used for "real" tools.

## Splits (DSPy tutorial)

- **Train**: 100 examples
- **Dev**: 300 examples
- **Test**: 595 examples (unused in the tutorial's reported numbers)

## Benchmark numbers

The [[dspy-tool-use-tutorial|DSPy tool-use tutorial]] reports:

- Baseline (GPT-4o, `temperature=0.7`, hand-rolled ReAct, `max_steps=5`): **35.0% dev accuracy**.
- Optimized ([[SIMBA|`dspy.SIMBA`]] `max_steps=12, max_demos=10, seed=6793115`): **60.7% dev accuracy**.
- Relative lift: **+71%** (+25.7 absolute points).

**First wiki SIMBA × tool-use benchmark receipt.**

## Connections

- [[dspy-tool-use-tutorial]] — the canonical DSPy receipt.
- [[ByteDanceResearch]] — dataset author.
- [[SIMBA]] — the optimizer used in the canonical receipt.
- [[HandRolledReAct]] — the agent pattern the tutorial pairs with ToolHop.
- [[func_timeout]] — the runtime-bound library used to sandbox tool calls.
- [[hotpotqa|HotPotQA]] / [[HoVer]] / [[MultiHopQA]] / [[MultiHopRAG]] — sibling multi-hop QA benchmarks (text-retrieval rather than tool-composition).
- [[HotPotQAConditional]] — conditional-rule variant the [[MIPROv2]] paper used.
- [[HuggingFace]] — host.
- [[DSPyTools]] — the wiki's tool-surface page; ToolHop introduces the *fourth* tool-construction path (per-question raw-callable dict).
- [[DSPyOptimizers]] — the catalog this tutorial extends.
- [[react|`dspy.ReAct`]] — the framework-provided pattern; the ToolHop tutorial bypasses it.
- [[GPT4o|GPT-4o]] — the canonical student LM.
- [[Benchmarking]] / [[PublicBenchmark]] — broader benchmark family.
