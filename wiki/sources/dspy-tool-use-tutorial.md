---
title: "DSPy Tutorial — Advanced Tool Use (SIMBA on ToolHop)"
type: source
tags: [dspy, tutorial, simba, optimizer, tool-use, react, multi-hop, toolhop, bytedance, gpt-4o, func_timeout, agent, hand-rolled-react]
date: 2026-05-24
source_file: raw/dspy-tool-use-tutorial.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/tool_use/`. **First wiki-corpus benign-task receipt of [[SIMBA|`dspy.SIMBA`]]** — prior SIMBA receipt ([[2603.19247-prompt-optimization-jailbreaking]]) was an adversarial-search receipt with no public code; this is the **first SIMBA `compile(...)` invocation with all kwargs disclosed**, the first SIMBA receipt against a **benign benchmark** (multi-hop tool use), and the first SIMBA receipt with a **headline before/after accuracy number**. Trains a **hand-rolled ReAct-style agent** (not `dspy.ReAct` — a one-Signature `dspy.ChainOfThought` driving a manual `max_steps=5` trajectory loop over per-question tool dicts) on the [[ToolHop]] benchmark (ByteDance Research, ~995 datapoints; tutorial uses 100/300/595 splits) with [[GPT4o|GPT-4o]] (`temperature=0.7`). **Headline lift: 35.0% → 60.7% devset accuracy** (`+25.7 absolute / +71% relative`) at `dspy.SIMBA(metric, max_steps=12, max_demos=10)` with `seed=6793115`. **First wiki composition of [[func_timeout|`func_timeout`]]** (third-party tool-sandbox library) into a DSPy program — `@func_set_timeout(10)` decorator wraps every Python tool call with a 10-second deadline and an exception-to-`{return_value, errors}` dict mapping.

## Configuration receipt

| Slot | Value |
|---|---|
| LM | `openai/gpt-4o`, `temperature=0.7` |
| Program | `Agent(dspy.Module)` — single `dspy.ChainOfThought` over an **inline-string Signature** `'question, trajectory, functions -> next_selected_fn, args: dict[str, Any]'` with explicit `instructions` kwarg |
| Tool surface | Per-question Python dict `{fn_name: callable}` built by `exec()`-ing source-code strings shipped with each dataset row, after stripping the `# Example usage` suffix; plus a synthetic `finish(answer)` terminal tool |
| Tool sandbox | `@func_set_timeout(10)` + try/except → `{"return_value": ..., "errors": ...}` |
| Max trajectory steps | 5 |
| Metric | Lowercase + comma-strip + trailing-`.0`-strip → exact string match |
| Evaluator | `dspy.Evaluate(devset=devset, metric=metric, num_threads=24, display_progress=True, display_table=0, max_errors=999)` |
| Optimizer | `dspy.SIMBA(metric=metric, max_steps=12, max_demos=10)` invoked as `simba.compile(agent, trainset=trainset, seed=6793115)` |
| Dataset | [[ToolHop]] (`bytedance-research/ToolHop` on HuggingFace) loaded via `dspy.utils.download(...)` |
| Train / Dev / Test | 100 / 300 / 595 |

## Key Claims

- **First wiki receipt of `dspy.SIMBA` invocation syntax** — prior [[SIMBA]] page documented the algorithm conceptually and the [[2603.19247-prompt-optimization-jailbreaking|Shamsi et al.]] empirical anchor but did not show the `dspy.SIMBA(...)` Python constructor or its kwargs. Tutorial reveals: `metric` (positional-or-keyword), `max_steps` (default unknown; tutorial picks 12), `max_demos` (default unknown; tutorial picks 10), and the `compile(student, trainset, seed=int)` invocation surface — including the **explicit `seed` parameter**, a structurally new disclosure (the wiki had no prior receipt of a DSPy optimizer accepting an explicit deterministic seed).
- **First wiki benign-task SIMBA receipt with headline numbers.** Prior SIMBA receipt: 0.046–0.792 *danger scores* on jailbreaks (no accuracy). This: 35.0% → 60.7% on multi-hop tool-use accuracy. **The +71% relative lift is now the canonical SIMBA performance number** for benign-task tool-use optimization.
- **First wiki receipt of the *hand-rolled ReAct* pattern in DSPy.** Prior agentic DSPy tutorials ([[dspy-customer-service-agent]], [[dspy-yahoo-finance-react-tutorial]], [[dspy-tutorial-rag-as-agent]], [[dspy-mem0-react-tutorial]]) all invoke `dspy.ReAct(signature, tools=[...])`. This tutorial **bypasses [[react|`dspy.ReAct`]]** in favor of a manual `max_steps=5` for-loop driving a single `dspy.ChainOfThought` Signature that emits `(next_selected_fn, args: dict[str, Any])` per step — with the agent's `forward()` calling the chosen tool, appending the result to the `trajectory` list, and breaking on `selected_fn == "finish"`. The implicit motivation (not stated but structurally clear): the per-question tool set varies, and the synthetic `finish` tool provides termination control that `dspy.ReAct`'s default action set may not expose as ergonomically. **Wiki's first concrete view of when to escape `dspy.ReAct`** in favor of a custom loop.
- **First wiki receipt of `dspy.Signature(str_spec, instructions_str)` inline-Signature construction.** Prior DSPy receipts used the class-form (`class MySignature(dspy.Signature): """docstring"""; field: Type = dspy.InputField()`) — see [[DSPySignatures]]. The inline form `dspy.Signature('a, b -> c, d: dict[str, Any]', "instructions")` takes the field list and the instructions as positional/keyword args, with **`dict[str, Any]` as a parsed-from-string type annotation in the output spec** — first wiki receipt of a non-trivial output-type annotation in inline-string form.
- **First wiki receipt of [[func_timeout|`func_timeout`]] library** (third-party Python package by James W. Smith / kata198) used inside a DSPy program. `@func_set_timeout(10)` is the canonical Python idiom for "kill this function after N seconds via a separate thread" — orthogonal to async/await, useful for **untrusted-code sandbox** when the tools themselves are dynamically `exec()`-ed strings (which they are here).
- **First wiki receipt of `exec()`-based tool construction.** ToolHop ships each datapoint with a `functions: list[str]` field containing **Python source-code strings**; the tutorial parses the function name via regex (`re.search(r"^\s*def\s+([a-zA-Z0-9_]+)\s*\("`), strips the `# Example usage` suffix, then `exec(cleaned_code, {}, local_vars)` to bind the function into a dict. Structurally novel and **security-relevant**: every tool is dynamically-compiled untrusted code, which is why the `func_timeout` wrapper is necessary (and arguably insufficient — `exec()` of untrusted strings is a sandbox-escape vector regardless of timeout).
- **First wiki receipt of `dspy.utils.download(url)` for direct dataset URL fetch** — distinct from `datasets.load_dataset(...)`. The tutorial fetches `https://huggingface.co/datasets/bytedance-research/ToolHop/resolve/main/data/ToolHop.json` directly as a JSON file, then parses with `orjson.loads(...)` — bypassing the [[HuggingFace|HF]] `datasets` library entirely despite the dataset being HF-hosted.
- **First wiki receipt of `orjson`** (Rust-backed JSON parser) in a DSPy tutorial. Prior DSPy tutorials used stdlib `json` or `datasets.load_dataset`. `orjson.loads(open(path).read())` is the tutorial's go-to.
- **GPT-4o (no version suffix) as student**, `temperature=0.7`. Distinct from prior tutorials that pin dated checkpoints (e.g. [[dspy-tutorial-gepa-trusted-monitor]]'s `openai/gpt-4.1-nano-2025-04-14`). The lift is on GPT-4o — a model strong enough that prompt optimization has clear headroom (35% baseline) without the optimization regime being model-scale-bottlenecked.
- **Metric is brittle by design.** The normalization (`str(...).rstrip(".0").replace(",", "").lower()`) is the **smallest viable answer normalizer** for the dataset — strip trailing zeroes from numbers, remove thousands separators, case-fold. The Signature's instruction (`"format dates as YYYY-MM-DD, names as Firstname Lastname, and numbers without leading 0s"`) makes the model's output schema **the dual of the metric's normalization**: the optimizer's primary lift target is teaching GPT-4o to **emit answers in the metric's expected shape**, not to do better multi-hop reasoning per se. **First wiki receipt of metric-and-instruction co-design as the primary optimization target.**
- **`max_demos=10`** — first wiki documentation of SIMBA's demo-budget kwarg. With 10 bootstrapped demos and 12 mini-batch steps, the budget is meaningfully smaller than [[2603.19247-prompt-optimization-jailbreaking]]'s 4 steps × batch 16 = 64 proposals.
- **`seed=6793115`** — first wiki documentation of a DSPy optimizer's `compile(...)` accepting an explicit deterministic seed. Reproducibility surface that prior DSPy tutorials never invoked.

## Key Quotes

> "For the final answer, produce short (not full sentence) answers in which you format dates as YYYY-MM-DD, names as Firstname Lastname, and numbers without leading 0s." (the baseline Signature `instructions` string — the seed SIMBA evolves)

> "An agent that can use tools to implement the given signature." (the [[react|`dspy.ReAct`]] docstring this tutorial **does not** invoke — choosing to roll its own ReAct loop instead)

> "Conclude the trajectory and return the final answer." (the docstring of the synthetic `finish(answer: str)` tool — the hand-rolled-ReAct's termination signal)

## Code Receipt — minimum viable hand-rolled ReAct in DSPy

```python
def finish(answer: str):
    """Conclude the trajectory and return the final answer."""
    return answer

class Agent(dspy.Module):
    def __init__(self, max_steps=5):
        self.max_steps = max_steps
        instructions = (
            "For the final answer, produce short (not full sentence) answers "
            "in which you format dates as YYYY-MM-DD, names as Firstname "
            "Lastname, and numbers without leading 0s."
        )
        signature = dspy.Signature(
            'question, trajectory, functions -> next_selected_fn, args: dict[str, Any]',
            instructions
        )
        self.react = dspy.ChainOfThought(signature)

    def forward(self, question, functions):
        tools = {fn_name: fn_metadata(fn) for fn_name, fn in functions.items()}
        trajectory = []
        for _ in range(self.max_steps):
            pred = self.react(question=question, trajectory=trajectory, functions=tools)
            selected_fn = pred.next_selected_fn.strip('"').strip("'")
            fn_output = wrap_function_with_timeout(functions[selected_fn])(**pred.args)
            trajectory.append(dict(
                reasoning=pred.reasoning,
                selected_fn=selected_fn,
                args=pred.args,
                **fn_output,
            ))
            if selected_fn == "finish":
                break
        return dspy.Prediction(answer=fn_output.get("return_value", ''), trajectory=trajectory)

simba = dspy.SIMBA(metric=metric, max_steps=12, max_demos=10)
optimized_agent = simba.compile(agent, trainset=trainset, seed=6793115)
```

## Cross-receipt convergence

### Against [[2603.19247-prompt-optimization-jailbreaking]] (the prior SIMBA receipt)

| | Shamsi et al. (jailbreaking) | This tutorial (benign tool use) |
|---|---|---|
| Task | Adversarial system-prompt search | Multi-hop tool composition |
| Reward | [[DangerScore]] (LLM-judged harm 0–1) | Lowercase exact-match accuracy |
| Models | Claude 4.5, LLaMA 4, Qwen 3-8B, Gemini 2.5-Pro | GPT-4o |
| SIMBA config | `batch=16, max_steps=4` (≤64 proposals) | `max_steps=12, max_demos=10, seed=6793115` |
| Code disclosed | No (paper-anchored only) | **Yes (full `dspy.SIMBA(...)` invocation)** |
| Numbers | 0.046 → 0.347 mean danger (Claude); 0.215 → 0.623 (LLaMA); 0.090 → 0.792 (Qwen); 0.645 → 0.774 (Gemini) | 35.0% → 60.7% dev accuracy |
| Lift framing | SIMBA beats [[MIPROv2]] / [[GEPA]] in same paper | **No head-to-head; absolute lift only** |

This tutorial **completes the SIMBA receipt corpus** by adding the missing executable invocation surface. The wiki now has both the **adversarial-objective** result (Shamsi et al.) and a **benign-objective** result (this tutorial). The two together make SIMBA's positioning clearer: it's the **high-exploration optimizer** in the DSPy catalog — works on both attack and defense objectives because the same variance-over-exploitation property helps either way.

### Against the prior agentic-DSPy tutorial cluster

| Tutorial | Agent shape | Optimizer | Receipt |
|---|---|---|---|
| [[dspy-customer-service-agent]] | `dspy.ReAct` with airline customer-service tools | none | Programming-stage only |
| [[dspy-yahoo-finance-react-tutorial]] | `dspy.ReAct` with `from_langchain` tool composition | none | Programming-stage only |
| [[dspy-tutorial-rag-as-agent]] | `dspy.ReAct` for multi-hop HoVer retrieval | [[MIPROv2]] (`auto="light"`) | 8% → 41.67% top-5 recall |
| [[dspy-rl-multihop-tutorial]] | Hand-rolled `dspy.ChainOfThought` × 2 (`ResearchHop`) | [[ArborGRPO]] | 61.8% → 66.2% recall |
| [[dspy-mem0-react-tutorial]] | `dspy.ReAct` + [[mem0]] memory | none | Programming-stage only |
| **This tutorial** | **Hand-rolled `dspy.ChainOfThought` + manual loop with `finish` tool** | **[[SIMBA]]** | **35.0% → 60.7%** |

**Position**: this is the **first wiki receipt of a hand-rolled ReAct optimized by an instruction optimizer** — [[dspy-rl-multihop-tutorial|rl_multihop]] was the only prior hand-rolled-loop agent, and it used weight-space RL. This tutorial proves the hand-rolled pattern composes with SIMBA's prompt-space optimization.

### Against [[dspy-tools]] (the *Learn* tools page)

[[dspy-tools]] documented `dspy.Tool` and the three tool-construction paths (plain callable / MCP / LangChain). This tutorial introduces a **fourth construction path**: a **per-question tool dict** built by `exec()`-ing dataset-shipped Python source strings, with [[func_timeout|`func_timeout`]] as the sandbox boundary and a synthetic `finish` tool for termination. Notable: this **does not use `dspy.Tool`** at all — the agent receives raw callables in a dict, computes metadata via stdlib `inspect.signature(...)` + `inspect.getdoc(...)`, and presents the metadata as a `dict[str, Any]` field to the ChainOfThought. **First wiki receipt of `dict[str, Any]`-via-Signature as a DSPy tool-presentation surface**, distinct from `dspy.Tool` and its three documented construction paths.

## What's new in the wiki after this ingest

### First wiki receipts

- **`dspy.SIMBA(...)` constructor surface** with `metric`, `max_steps`, `max_demos` kwargs and `compile(student, trainset, seed=int)` invocation.
- **SIMBA on a benign-objective task** with explicit before/after accuracy numbers.
- **Hand-rolled ReAct in DSPy** (manual loop over `dspy.ChainOfThought`, not `dspy.ReAct`).
- **`dspy.Signature(str_spec, instructions_str)` inline construction** with `dict[str, Any]` output annotation parsed from string.
- **[[func_timeout|`func_timeout`]] library** in a DSPy program.
- **`@func_set_timeout(N)` + try/except → `{return_value, errors}` dict** as the tool sandbox idiom.
- **`exec()`-based tool construction from dataset-shipped source strings** with regex name extraction.
- **`dspy.utils.download(url)`** for direct HF dataset URL fetch (bypassing the `datasets` library).
- **`orjson`** as a DSPy tutorial JSON parser.
- **[[ToolHop]]** benchmark in the wiki.
- **Synthetic `finish(answer)` terminal tool pattern** — agent-controlled termination via a no-op tool whose return value is the final answer.
- **DSPy optimizer `compile(..., seed=int)`** reproducibility surface.
- **Metric-and-instruction co-design** as primary optimization target — output schema mirrors metric normalization.
- **Plain `dict[str, Any]`-via-Signature tool-presentation surface** (no `dspy.Tool` wrapper).

### Pages updated in place

- [[SIMBA]] — adds the first executable receipt, benign-task lift numbers (35.0% → 60.7%), and all kwargs (`max_steps=12, max_demos=10, seed=6793115`). Page previously had algorithm description + adversarial-task anchor only.
- [[react]] — adds the hand-rolled ReAct pattern as a contrast case (when to escape `dspy.ReAct` in favor of a manual `dspy.ChainOfThought` loop) and notes the synthetic `finish` terminal-tool idiom.
- [[DSPyTools]] — adds the **fourth tool-construction path** (per-question dict of raw callables with `inspect`-derived metadata) and the [[func_timeout|`func_timeout`]]-based untrusted-code sandbox idiom.
- [[DSPyOptimizers]] — adds the SIMBA benign-task receipt to the catalog.
- [[DSPySignatures]] — adds the inline `dspy.Signature(str_spec, instructions_str)` construction form with `dict[str, Any]` output type.

### New pages minted

- [[ToolHop]] (concept) — the ByteDance multi-hop tool-use benchmark with `exec()`-able Python source-code tools per datapoint.
- [[func_timeout]] (entity) — the kata198 Python library exposing `@func_set_timeout(N)` for threaded function timeouts.
- [[ByteDanceResearch]] (entity) — `bytedance-research` HuggingFace org; origin of ToolHop.
- [[HandRolledReAct]] (concept) — the manual `dspy.ChainOfThought` + trajectory-loop pattern as an alternative to `dspy.ReAct`.

## Contradictions

- **Untrusted `exec()` of dataset strings**. The tutorial dynamically compiles arbitrary Python source code shipped with each dataset row. `func_timeout(10)` bounds runtime but does not bound side effects (file writes, network calls, `os.system(...)`). The tutorial does not flag this as a security concern. **First wiki receipt of a DSPy tutorial executing untrusted dataset code without an isolation boundary** — contrasts with [[dspy-tutorial-rag-as-agent]]'s static tool list and [[dspy-mcp-tutorial]]'s child-process MCP isolation.
- **`temperature=0.7` on the student** is unusual for a ChainOfThought-driven trajectory agent — high enough to risk per-step inconsistency in tool selection across the `max_steps=5` loop. Tutorial does not justify the choice. Most prior DSPy receipts use `temperature=1.0` (creative, with diverse rollouts) or `temperature=0.0` (deterministic).
- **Metric does not match Signature instruction precisely.** Metric: `rstrip(".0").replace(",", "").lower()`. Signature: *"format dates as YYYY-MM-DD, names as Firstname Lastname, and numbers without leading 0s."* The metric does **not** check date format or name capitalization (lowercased before compare); the model is asked to obey rules the metric ignores. This **over-specifies the prompt vs the loss** — possibly a feature for human readability of intermediate outputs, possibly a bug (the optimizer can't learn to enforce dates strictly if the metric is permissive).
- **Test set unused.** `testset = examples[400:]` is constructed but never evaluated in the rendered tutorial — only the devset (300 items) gets the headline 35.0 → 60.7 numbers. Held-out test generalization is not surfaced.
- **No `temperature` on SIMBA's internal proposer LM.** Tutorial does not configure SIMBA's prompt-proposal LM separately — implies SIMBA uses the same `gpt4o` student for both program execution and reflection-on-traces, breaking the asymmetric-pair pattern that [[dspy-tutorial-gepa-aime]] / [[dspy-tutorial-gepa-papillon]] / [[dspy-tutorial-gepa-trusted-monitor]] / [[dspy-tutorial-gepa-facility-support-analyzer]] all use for GEPA.
- **No `dspy.ReAct` baseline comparison.** Tutorial picks the hand-rolled pattern without justifying it vs the framework-provided `dspy.ReAct(signature, tools=[...])`. The same SIMBA optimization applied to `dspy.ReAct(question -> answer, tools=tool_list)` would have provided a control for the *"is the hand-rolled pattern necessary"* question.

## Scope-limit gaps

1. **No optimized-Signature dump.** Tutorial reports the +71% lift but does not show the evolved `signature.instructions` text. The dual-narrative-vs-discriminator artifact taxonomy ([[ReflectivePromptMutation]]) from the GEPA tutorials cannot be applied here.
2. **No comparison against [[MIPROv2]] / [[GEPA]] / [[BootstrapFewShotWithRandomSearch]]** on the same setup. SIMBA is the only optimizer tried; no claim that SIMBA is *optimal* for this task.
3. **No ablation on `max_steps`, `max_demos`, or `seed`.** Tutorial picks 12/10/6793115 without justification or sensitivity analysis.
4. **No cost disclosure.** GPT-4o pricing × 100 trainset × 5 max-steps × 12 SIMBA-steps × an unknown number of internal proposals = non-trivial; not surfaced.
5. **No latency disclosure.** SIMBA's `compile(...)` is a noisy mini-batch loop; wall-clock time not reported.
6. **No test-set generalization.** As above.
7. **No security analysis** of the `exec(untrusted_string)` pattern beyond the `func_timeout(10)` wrapper.
8. **Hand-rolled ReAct vs `dspy.ReAct` head-to-head** not run.
9. **No streaming / async / observability composition** ([[dspy-streaming-tutorial]] / [[dspy-async-tutorial]] / [[dspy-observability-tutorial]]) over the optimized agent.
10. **No save/load receipt** — `optimized_agent` is not persisted via [[DSPySaving|`.save(...)`]].

## Connections

### Canonical anchors

- [[SIMBA]] — the optimizer concept page. **First runnable trace** in the wiki (page previously had algorithm description + adversarial-task anchor only).
- [[ToolHop]] — the benchmark. New concept page minted with this ingest.
- [[react|`dspy.ReAct`]] — the framework-provided pattern this tutorial **does not** use; the hand-rolled alternative is the structural contrast.
- [[HandRolledReAct]] — the manual `dspy.ChainOfThought` + trajectory-loop pattern. New concept page minted with this ingest.
- [[func_timeout]] — the tool-sandbox library. New entity page minted with this ingest.
- [[ByteDanceResearch]] — the dataset author. New entity page minted with this ingest.

### Sibling DSPy tutorials

- [[dspy-customer-service-agent]] — first wiki receipt of `dspy.ReAct`; programming-stage only. This tutorial is the optimized counterpart on a different task.
- [[dspy-yahoo-finance-react-tutorial]] — `dspy.ReAct` + `from_langchain`; programming-stage only.
- [[dspy-tutorial-rag-as-agent]] — `dspy.ReAct` + [[MIPROv2]] on [[HoVer]]; the **first wiki receipt of an optimized agentic DSPy program**. This tutorial is the SIMBA-equivalent on a different agentic benchmark.
- [[dspy-mem0-react-tutorial]] — `dspy.ReAct` + [[mem0]] memory; orthogonal axis.
- [[dspy-rl-multihop-tutorial]] — hand-rolled agent + [[ArborGRPO]] on [[HoVer]]; the **weight-space companion** to this tutorial's prompt-space approach. Together: the wiki's first hand-rolled-agent × prompt-vs-weight-space side-by-side.
- [[dspy-tools]] — the *Learn* tools page; this tutorial introduces the fourth tool-construction path.
- [[dspy-optimizers]] — page-13 catalog; SIMBA entry now has an executable trace.
- [[dspy-tutorial-math]] — sibling [[MIPROv2]] receipt; different optimizer family on a different task.
- [[dspy-evaluation-overview]] — the metric-contract sibling; this tutorial's metric is the **smallest viable normalizer** receipt.

### Concept neighborhood

- [[DSPyOptimizers]] — the catalog SIMBA belongs to.
- [[DSPyOptimization]] — the workflow.
- [[chainofthought|`dspy.ChainOfThought`]] — the Module the hand-rolled ReAct loop wraps.
- [[DSPyPredict|`dspy.Predict`]] — the underlying Predict.
- [[DSPySignatures]] — the inline `dspy.Signature(str_spec, instructions_str)` construction form is added by this tutorial.
- [[DSPyModules]] — `Agent` subclasses `dspy.Module` to implement the manual loop.
- [[DSPyExample]] — `dspy.Example(question=..., answer=..., functions=...).with_inputs("question", "functions")` carries Python callables in the `functions` field — first wiki receipt of `dspy.Example` carrying live callables, not just primitive data.
- [[DSPyMetrics]] — the metric contract.
- [[DSPyEvaluate]] — `num_threads=24, display_progress=True, display_table=0, max_errors=999` — the multi-thread evaluator surface.
- [[DSPyTools]] — `dspy.Tool` is **not** used here; this tutorial demonstrates the per-question raw-callable-dict alternative.
- [[MIPROv2]] / [[GEPA]] / [[BootstrapFewShotWithRandomSearch]] / [[COPRO]] — sibling optimizers not invoked but in the same catalog family.

### LMs invoked

- [[GPT4o|GPT-4o]] — `openai/gpt-4o`, `temperature=0.7`. Student LM. First wiki SIMBA × GPT-4o receipt.
- [[openai|OpenAI]] — provider.

### External datasets / libraries

- [[ToolHop]] — ByteDance Research multi-hop tool-use benchmark.
- [[HuggingFaceDatasets]] — host (the tutorial bypasses `datasets.load_dataset` in favor of direct URL fetch).
- [[ByteDanceResearch]] — dataset author.
- [[func_timeout]] — Python tool-timeout library.
- [[orjson]] — Rust-backed JSON parser.
- [[mlflow|MLflow]] — optional autolog integration (`mlflow.dspy.autolog()`).

### Adjacent threat models

- [[promptinjection]] / [[IndirectPromptInjection]] — the `exec(untrusted_string)` pattern is a direct sandbox-escape vector; `func_timeout(10)` does not defend against it. Adjacent to the AI-safety neighborhood of [[dspy-tutorial-gepa-trusted-monitor]] but **opposite-signed**: that tutorial trains a monitor against attack code, this tutorial *runs* attack-shaped (untrusted) code as part of normal operation.
- [[ToolPoisoning]] — if a ToolHop datapoint shipped a malicious `functions` string, this pipeline would `exec()` it inside the agent's process. The tutorial does not address this risk.

### Multi-hop benchmark neighborhood

- [[hotpotqa|HotPotQA]] / [[HoVer]] / [[MultiHopQA]] / [[MultiHopRAG]] — adjacent multi-hop QA benchmarks. ToolHop is the **tool-composition variant** (the hops are tool calls, not text retrievals).
- [[HotPotQAConditional]] — the conditional-rule variant of HotPotQA that [[MIPROv2]] paper used to demonstrate Lesson-3 conditional optimization.

### Agent / harness adjacency

- [[2604.25850-agentic-harness-engineering]] — the harness-engineering position paper; this tutorial's hand-rolled pattern is a minimal agent harness for a DSPy-shaped pipeline.
- [[2604.21590-agenticqwen]] — adjacent agentic-LLM line of work.
