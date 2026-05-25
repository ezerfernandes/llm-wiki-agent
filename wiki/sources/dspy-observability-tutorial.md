---
title: "DSPy Tutorial — Debugging & Observability"
type: source
tags: [dspy, observability, tracing, mlflow, callbacks, debugging, tutorial]
date: 2026-05-24
source_file: https://dspy.ai/tutorials/observability/
---

## Summary

Short single-page [[DSPy]] tutorial at `https://dspy.ai/tutorials/observability/` that **canonicalizes the three-tier observability stack** of the framework: (tier 1) `dspy.inspect_history()` — zero-dep print of recent LM calls; (tier 2) [[MLflow]] tracing via `mlflow.autolog()` against a `mlflow server` backend — full trace tree with prompts, responses, timing, and module-relationship metadata; (tier 3) custom instrumentation via `dspy.utils.callback.BaseCallback` subclasses, registered process-wide with `dspy.configure(callbacks=[...])`. The tutorial's worked example threads a [[react|`dspy.ReAct`]] agent over a [[ColBERTv2]]-backed Wikipedia retrieval through all three tiers, uses the [[MLflow]] trace UI to **diagnose stale retrieval data** (the ColBERTv2 dump pre-dates Shohei Ohtani's 2024 Dodgers move), and resolves the bug by swapping the retriever for a [[Tavily]] web-search tool. The framing thesis: *"Without transparency, the prediction process can easily become a black box, making failures or quality issues difficult to diagnose."*

## Key Claims

- **Three observability tiers, increasing capability and setup cost.** `inspect_history()` ([[InspectHistory|tier 1]], zero deps, prints last *N* LM calls), [[MLflow]] auto-tracing ([[DSPyObservability|tier 2]], one-line install, full trace tree), and `BaseCallback` ([[DSPyCallback|tier 3]], custom code, fully programmable handlers).
- **`inspect_history(n=N)` has three documented limitations** the tutorial uses to motivate the upgrade to [[MLflow]]:
  1. *"It only captures LM calls, not other component activity"* — no [[DSPyTools|tool]] / [[DSPyAdapters|adapter]] / retriever visibility.
  2. *"It does not provide metadata like latency, module relationships, etc."* — flat list, no parent/child structure.
  3. *"In complex applications, multiple predictions are nested, making it difficult to organize them in the order they were made"* — ordering becomes ambiguous under interleaved sub-module calls.
- **[[MLflow]] is the recommended observability framework** (first-party endorsement): *"MLflow is an end-to-end machine learning platform that seamlessly integrates with DSPy to support best practices in LLMOps. Using MLflow's automatic tracing capability with DSPy is straightforward; no API key or sign up required."*
- **The MLflow setup is a four-step opt-in**: `pip install -U mlflow>=2.18.0`; `mlflow server --backend-store-uri sqlite:///mydb.sqlite` (background); `mlflow.set_tracking_uri("http://127.0.0.1:5000")` + `mlflow.set_experiment("DSPy")`; `mlflow.autolog()`.
- **`mlflow>=2.18.0` is the floor version** this tutorial cites — older than the `mlflow>=3.0.0` floor [[dspy-custom-module]] uses, and consistent with the `mlflow>=2.21.1` floor in [[dspy-optimizer-tracking-tutorial]]. The DSPy autolog surface is supported on the MLflow 2.x line from 2.18 forward.
- **`mlflow.autolog()` captures every component activity automatically** — *"such as DSPy modules, LM calls, retriever invocations, and tool executions"* — no instrumentation code required.
- **MLflow tracing is the canonical debugging surface for retriever failures.** The worked example diagnoses an outdated [[ColBERTv2]] index (returns a 2018 article naming the Hokkaido Nippon-Ham Fighters as Ohtani's team) by inspecting the **retriever's output span** in the MLflow trace UI — *"hovering on the steps will show their details, such as inputs, outputs, and metadata"*.
- **`BaseCallback` is a six-pair handler interface** for custom instrumentation:
  | Handler pair | Captures |
  |---|---|
  | `on_module_start` / `on_module_end` | Any [[DSPyModules|`dspy.Module`]] `__call__` |
  | `on_lm_start` / `on_lm_end` | Any [[DSPyLM|`dspy.LM`]] call |
  | `on_adapter_format_start` / `on_adapter_format_end` | [[DSPyAdapters|Adapter]] prompt-rendering pass |
  | `on_adapter_parse_start` / `on_adapter_parse_end` | [[DSPyAdapters|Adapter]] response-parsing pass |
  | `on_tool_start` / `on_tool_end` | [[DSPyTools|`dspy.Tool`]] invocation |
  | `on_evaluate_start` / `on_evaluate_end` | [[DSPyEvaluate|`dspy.Evaluate`]] run |
- **Callbacks attach process-wide via `dspy.configure`** — `dspy.configure(callbacks=[AgentLoggingCallback()])` — the same configuration mechanism that registers the LM, adapter, and async kwargs.
- **The tutorial's `AgentLoggingCallback` example logs only the reasoning step**, demonstrating selective per-prediction-name filtering: the handler inspects `instance.signature.__name__` and acts only when it equals `"Thought"`, leveraging the [[react|`dspy.ReAct`]] internal Signature names.
- **The retrieval bug is real and load-bearing**: the ColBERTv2 Wikipedia dump in the [[DSPy]] tutorial corpus is from 2018-12; Ohtani's Dodgers signing is 2024-01. Without MLflow tracing the model returns a plausible-sounding but stale answer, indistinguishable from a hallucination without retriever-span inspection.
- **Tavily search is the tutorial's recommended fix** — *"Tavily is an AI-powered search engine that provides real-time information from the web"* — wrapped as a [[DSPyTools|`dspy.Tool`]] and substituted into the `dspy.ReAct(tools=[...])` list. Re-running the agent through the MLflow trace UI confirms the corrected answer ("Los Angeles Dodgers").

## Key Quotes

> *"As AI systems grow more sophisticated, the ability to understand what your system is doing becomes critical."* — opening framing
>
> *"Without transparency, the prediction process can easily become a black box, making failures or quality issues difficult to diagnose."* — thesis sentence
>
> *"DSPy library comes with the handy utility function called `inspect_history()`, which prints out all LLM invocations made so far."* — tier 1 definition
>
> *"MLflow is an end-to-end machine learning platform that seamlessly integrates with DSPy to support best practices in LLMOps. Using MLflow's automatic tracing capability with DSPy is straightforward; no API key or sign up required."* — first-party MLflow endorsement
>
> *"With just a few lines of code, MLflow automatically captures each step of your DSPy program."* — autolog promise
>
> *"For tailoring the logging behavior to your needs, DSPy offers `callback` mechanism. The `BaseCallback` class provides several handlers that can be customized to log different events."* — tier 3 definition
>
> *"It demonstrates how to log the intermediate reasoning steps for the agent. Note that it requires a bit more boilerplate code, but it gives us more control over the logging behavior."* — callback trade-off framing

## Code receipts

### Tier 1 — `inspect_history`

```python
dspy.inspect_history(n=2)
```

### Tier 2 — MLflow autolog (four-step opt-in)

```bash
pip install -U mlflow>=2.18.0
mlflow server --backend-store-uri sqlite:///mydb.sqlite
```

```python
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("DSPy")
mlflow.autolog()

# Existing DSPy code unchanged — every __call__ is now a trace span.
agent = dspy.ReAct("question -> answer", tools=[search_wikipedia])
agent(question="Which baseball team does Shohei Ohtani play for?")
```

### Tier 3 — `BaseCallback`

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
agent(question="Which baseball team does Shohei Ohtani play for?")
```

## Connections

- [[DSPy]] — the framework whose observability surface this tutorial canonicalizes.
- [[DSPyObservability]] — new concept page minted by this ingest; consolidates the three-tier stack.
- [[DSPyCallback]] — new concept page minted by this ingest; canonical receipt for the `BaseCallback` handler interface.
- [[InspectHistory]] — new concept page minted by this ingest; the tier-1 print utility.
- [[MLflow]] — the recommended tier-2 backend. The `mlflow.autolog()` recipe here uses `autolog()` rather than `mlflow.dspy.autolog()`; both invocations route to the same DSPy integration but the `dspy`-scoped form (used by [[dspy-custom-module]], [[dspy-optimizer-tracking-tutorial]]) is the kwarg-bearing form.
- [[react|`dspy.ReAct`]] — the worked-example module; the tutorial confirms MLflow traces every think-act-observe step.
- [[ColBERTv2]] — the retriever in the worked example; the tutorial uses its 2018-vintage Wikipedia dump to demonstrate stale-retrieval diagnosis.
- [[DSPyTools|`dspy.Tool`]] — the tier-3 callback `on_tool_*` pair captures every `dspy.Tool` invocation; the Tavily fix re-wraps a web-search call as a `dspy.Tool`.
- [[DSPyAdapters|Adapters]] — the tier-3 callback `on_adapter_format_*` and `on_adapter_parse_*` pairs expose the prompt-rendering and response-parsing passes the [[DSPyAdapters|Adapter]] layer performs.
- [[DSPyLM]] — the `on_lm_*` handlers attach to every LM call; complements [[DSPyLM|`dspy.LM.history`]] (per-client wire-level log) and `inspect_history` (global recent-call print).
- [[DSPyEvaluate]] — the `on_evaluate_*` handlers attach to `dspy.Evaluate` runs.
- [[DSPyModules]] — the `on_module_*` handlers attach to every `dspy.Module.__call__`.
- [[Tavily]] — new entity page minted by this ingest; the web-search service the tutorial wraps as a `dspy.Tool` to fix the stale-retrieval bug.
- [[ShoheiOhtani]] — worked-example subject; the 2024 Dodgers signing post-dates the [[ColBERTv2]] dump and surfaces the retrieval staleness.

## Contradictions

- **None substantive.** The `mlflow>=2.18.0` floor cited here is **older** than the `mlflow>=3.0.0` floor in [[dspy-custom-module]] and slightly older than the `mlflow>=2.21.1` floor in [[dspy-optimizer-tracking-tutorial]] — but these are *minimum* versions per tutorial, not contradictions. The DSPy autolog surface is supported on the 2.x line from 2.18 forward; later tutorials raise the floor because they exercise features that require newer MLflow APIs (e.g. compile-time tracking in 2.21+).
- **Naming surface — `mlflow.autolog()` vs `mlflow.dspy.autolog()`.** This tutorial uses the unscoped `mlflow.autolog()` (relies on MLflow's autolog-by-presence detection of the `dspy` import); [[dspy-custom-module]], [[dspy-tutorial-rag-as-agent]], and [[dspy-optimizer-tracking-tutorial]] use the scoped `mlflow.dspy.autolog(...)` form with kwargs. Both call paths land on the same DSPy integration; the scoped form is the canonical surface for kwarg-bearing toggles (`log_compiles`, `log_evals`, `log_traces_from_compile`).
