---
title: "DSPyObservability"
type: concept
tags: [dspy, observability, tracing, debugging, mlflow, callbacks, llmops]
sources: [dspy-observability-tutorial, dspy-custom-module, dspy-tutorial-rag-as-agent, dspy-optimizer-tracking-tutorial]
last_updated: 2026-05-24
---

# DSPy Observability

The **three-tier observability stack** [[DSPy]] ships for debugging and inspecting program execution. The [[dspy-observability-tutorial|Debugging & Observability tutorial]] is the canonical source for the stack as a *whole*; each tier has its own dedicated wiki page.

## The three tiers

| Tier | Surface | Setup cost | Captures | Reference |
|---|---|---|---|---|
| **1. Print** | `dspy.inspect_history(n=N)` | Zero — built into the framework | Last *N* LM calls, prompt + response | [[InspectHistory]] |
| **2. Trace** | `mlflow.autolog()` against a [[MLflow]] tracking server | One install (`pip install mlflow`) + one server process | Every [[DSPyModules|Module]] / [[DSPyLM|LM]] / retriever / [[DSPyTools|tool]] call, with timing, prompts, responses, parent/child structure | [[MLflow]], [[dspy-observability-tutorial]] |
| **3. Callbacks** | `dspy.utils.callback.BaseCallback` subclass + `dspy.configure(callbacks=[...])` | Custom Python code per handler | Whatever the user implements; six handler pairs cover modules, LMs, adapters, tools, evaluate | [[DSPyCallback]] |

The tiers are **additive, not mutually exclusive** — `inspect_history`, MLflow autolog, and registered callbacks can all be active in the same process. They capture overlapping but non-identical surfaces.

## Motivation — the three `inspect_history` limitations

The [[dspy-observability-tutorial|tutorial]] uses three concrete limitations of tier 1 to motivate the upgrade to tier 2:

1. *"It only captures **LM calls**, not other component activity"* — no [[DSPyTools|tool]] / retriever / [[DSPyAdapters|adapter]] visibility. A `dspy.ReAct` agent that issues 0 LM calls but 5 tool calls appears empty.
2. *"It does not provide **metadata** like latency, module relationships, etc."* — flat unordered list; no way to tell which sub-Module owns which LM call.
3. *"In **complex applications**, multiple predictions are nested, making it difficult to organize them in the order they were made"* — interleaved sub-module calls render ordering ambiguous.

These three properties — **non-LM activity**, **metadata**, **call-tree structure** — are precisely what `mlflow.autolog()` adds at tier 2, and what `BaseCallback` lets the user capture programmatically at tier 3.

## Tier 2 — MLflow autolog

The recommended observability backend. See [[MLflow]] for the canonical four-step recipe; the [[dspy-observability-tutorial|observability tutorial]] cites a `mlflow>=2.18.0` floor, [[dspy-optimizer-tracking-tutorial]] requires `mlflow>=2.21.1`, and [[dspy-custom-module]] uses `mlflow>=3.0.0`. All three call paths land on the same DSPy integration.

Two invocation forms appear across the corpus:

- **`mlflow.autolog()`** — unscoped, relies on MLflow's autolog-by-presence detection. Used by [[dspy-observability-tutorial]].
- **`mlflow.dspy.autolog(log_compiles=..., log_evals=..., log_traces_from_compile=...)`** — scoped, accepts kwargs. Used by [[dspy-custom-module]], [[dspy-tutorial-rag-as-agent]], [[dspy-optimizer-tracking-tutorial]]. The scoped form is the canonical surface for kwarg-bearing toggles; see [[MLflow]] for the three kwargs.

Both forms produce the same per-`__call__` trace tree at inference time. The kwargs only affect compile-time behavior (optimizer runs).

### What autolog captures at inference time

Per [[dspy-observability-tutorial]]: *"DSPy modules, LM calls, retriever invocations, and tool executions"*. The [[MLflow]] page documents that the autolog hook walks the `self.*` sub-module attributes set in [[DSPyModules|`dspy.Module.__init__`]] and renders each sub-module call as a child span — meaning **plain-function pipelines or inline sub-module use outside any `dspy.Module` are invisible** to the autolog hook. This is one of two operational reasons (alongside [[DSPyOptimizers|optimizer]] introspection) the framework recommends *"putting your logic with a custom module."*

### What autolog captures at compile time

Per [[dspy-optimizer-tracking-tutorial]] (via the three kwargs documented on [[MLflow]]): optimizer config, intermediate program versions, metric progression, training data snapshot, per-LM-call traces during `compile()`. The compile-time surface is **strictly larger** than the inference-time surface and uses a parent/child run hierarchy unique to optimization runs.

## Tier 3 — `BaseCallback`

Custom instrumentation via subclass of `dspy.utils.callback.BaseCallback`. Six handler pairs cover the framework's full event surface — see [[DSPyCallback]] for the canonical handler list, signatures, and the [[dspy-observability-tutorial|tutorial]]'s `AgentLoggingCallback` example.

The tier-3 advantage over tier 2: **programmability**. The tutorial's example shows selective per-prediction-name filtering — `on_module_end` checks `instance.signature.__name__ == "Thought"` and logs only the [[react|`dspy.ReAct`]] reasoning steps, ignoring the action steps. MLflow autolog has no equivalent filter — it captures everything or nothing.

## Worked example — diagnosing a stale retriever

The [[dspy-observability-tutorial|tutorial]]'s load-bearing demonstration: a [[react|`dspy.ReAct`]] agent asks *"Which baseball team does Shohei Ohtani play for?"* against a [[ColBERTv2]]-backed Wikipedia retrieval. The agent returns the **stale** answer (Hokkaido Nippon-Ham Fighters — Ohtani's pre-2018 team) because the [[ColBERTv2]] Wikipedia dump pre-dates his 2024 Dodgers signing.

The bug is **indistinguishable from a hallucination** at the LM-output layer — `inspect_history()` shows a fluent, well-grounded chain-of-thought citing the (stale) retrieved article. The bug only becomes visible by **hovering the retriever span in the MLflow trace UI** and reading the returned article text directly.

The fix: replace the [[ColBERTv2]] tool with a [[Tavily]] web-search [[DSPyTools|`dspy.Tool`]], re-run, confirm the corrected answer ("Los Angeles Dodgers") via the same MLflow trace UI. This is the **canonical retrieval-staleness diagnosis pattern** for the DSPy corpus.

## Position in the LLMOps stack

The [[dspy-observability-tutorial|tutorial]]'s framing — *"MLflow is an end-to-end machine learning platform that seamlessly integrates with DSPy to support best practices in **LLMOps**"* — places DSPy observability inside the broader [[MLOps]] / LLMOps lineage. The [[MLflow]] integration extends the framework from prompt-programming surface into **production-monitoring surface**, complementing [[DSPyEvaluate|evaluation]] (offline metric measurement) and [[DSPyOptimization|optimization]] (compile-time program search) with **runtime introspection**.

## Cross-tier overlap with other DSPy logging surfaces

DSPy carries three other history/log surfaces that **predate or run alongside** the observability stack documented here:

- **[[DSPyLM|`dspy.LM.history`]]** — per-`dspy.LM`-instance wire-level request/response log. Different layer from `inspect_history` (which prints from a global recent-call buffer). Used by [[DSPyOptimizers|Optimizers]] for replay.
- **[[DSPyHistory|`dspy.History`]]** — [[DSPySignatures|Signature]] field type for *conversation* history. Unrelated to observability despite the shared word — `dspy.History` is for conditioning the model on prior turns, not for inspecting program execution.
- **[[react|`dspy.ReAct`]] `trajectory`** — intra-call think-act-observe log. Orthogonal to `inspect_history` (which is inter-call) and to `BaseCallback` (which is event-driven).

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-observability-tutorial]] — canonical receipt: all three tiers (`dspy.inspect_history(n=2)`, `mlflow.autolog()` against a four-step `mlflow server` opt-in, and a `BaseCallback` subclass) threaded through the stale-retriever [[ColBERTv2]] → [[Tavily]] diagnosis.
- [[dspy-multihop-search-tutorial]] — references `mlflow.autolog` to make MIPROv2's long compile-time loop legible — per-call traces across the bootstrap teacher / proposer / mini-batch evaluation phases.
- [[dspy-rl-multihop-tutorial]] — flags MLflow run-visibility as the natural composition point for long [[grpo|GRPO]] rollouts over `Hop`; tutorial documents this as an unexercised extension rather than a worked receipt.

## Tracked sources

- **[[dspy-observability-tutorial]]** (2026-05-24) — canonical source; defines the three-tier stack, the three `inspect_history` limitations, and the stale-retriever worked example.
- **[[MLflow]]** — entity page consolidating the autolog recipe across the DSPy tutorial corpus.
- **[[dspy-custom-module]]**, **[[dspy-tutorial-rag-as-agent]]**, **[[dspy-optimizer-tracking-tutorial]]** — supplementary DSPy ↔ MLflow integration receipts; the latter is the canonical source for the three `mlflow.dspy.autolog(...)` kwargs.
