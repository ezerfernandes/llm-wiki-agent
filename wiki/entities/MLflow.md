---
title: "MLflow"
type: entity
tags: [tool, experiment-tracking, model-registry, dspy-tracing, model-gateway, model-serving]
sources: [madewithml-mlops-experiment-tracking, madewithml-mlops-jobs-and-services, madewithml-mlops-versioning, dspy-custom-module, dspy-rag-tutorial, dspy-tutorial-rag-as-agent, ai-engineering-ch10-architecture-feedback, dspy-entity-extraction-tutorial, dspy-optimizer-tracking-tutorial, dspy-observability-tutorial, dspy-deployment-tutorial, dspy-multihop-search-tutorial]
last_updated: 2026-05-24
---

# MLflow

Open-source platform for [[ExperimentTracking]] and [[ModelRegistry]]. Integrated via `MLflowLoggerCallback` in [[madewithml-mlops-experiment-tracking]]; uses [[PostgreSQL]] for the tracking store and [[AmazonS3]] for artifacts. Underlies [[Databricks]]'s managed offering.

## DSPy integration

The [[dspy-custom-module|DSPy Custom Module tutorial]] supplies the wiki's canonical DSPy-specific MLflow tracing recipe — a four-step opt-in:

```bash
pip install mlflow>=3.0.0
mlflow ui --port 5000 --backend-store-uri sqlite:///mlruns.db
```

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("DSPy")
mlflow.dspy.autolog()
```

The fourth step (`mlflow.dspy.autolog()`) is the bridge: every `__call__` on a [[DSPyModules|`dspy.Module`]] subclass after this point produces a trace span in the MLflow backend, visualized as a per-step tree in the MLflow UI. The autolog hook walks the `self.*` sub-module attributes set in `__init__` and renders each sub-module call (with prompts, responses, and timing) as a child span. Plain-function pipelines or inline sub-module use outside any `dspy.Module` are **invisible** to the autolog hook — one of the two operational reasons (alongside [[DSPyOptimizers|optimizer]] introspection) the tutorial recommends *"putting your logic with a custom module."* This is the second [[Databricks]]-touchpoint in the [[DSPy]] line, after [[MateiZaharia]]'s Databricks affiliation as senior author on [[2406.11695-mipro|MIPRO]] / [[2507.19457-gepa|GEPA]].

### Application to `dspy.ReAct` trajectories

The [[dspy-tutorial-rag-as-agent|Building RAG as Agent tutorial]] confirms `mlflow.dspy.autolog()` traces the full **think-act-observe trajectory** of a [[react|`dspy.ReAct`]] agent — every reasoning step, every tool call (`search_wikipedia` / `lookup_wikipedia`), every observation is a span in the tree. The autolog hook is the canonical introspection surface for debugging the [[react|ReAct]] loop, complementing the in-band `pred.trajectory` field. The tutorial also notes MLflow tracks evaluation metrics across [[MIPROv2]] optimization iterations — the same per-Module trace tree works equally well during compilation and inference.

### Optimizer-aware autologging — the three kwargs

The [[dspy-optimizer-tracking-tutorial|DSPy Optimizer Tracking tutorial]] supplies the **optimization-aware** form of `mlflow.dspy.autolog()` — three independent toggles that the bare-call recipe in [[dspy-custom-module]] / [[dspy-tutorial-rag-as-agent]] left implicit:

```python
mlflow.dspy.autolog(
    log_compiles=True,             # track the optimization workflow itself
    log_evals=True,                # track evaluation metric values
    log_traces_from_compile=True,  # track per-LM-call traces during compile()
)
```

| Kwarg | Captures | Cost |
|---|---|---|
| `log_compiles` | Optimizer config (`auto` preset, kwargs), intermediate program versions (instructions + demos per trial), metric-progression curve, training data snapshot | Lightweight |
| `log_evals` | Per-step evaluation values during compile() and standalone `dspy.Evaluate` calls | Moderate |
| `log_traces_from_compile` | Per-LM-call trace tree for every call inside the optimizer's bootstrap / proposal / search stages | **Heavy** — linear in (trials × demos × dataset size); disable for large datasets |

The tutorial also asserts a **minimum supported version**: `mlflow>=2.21.1` — older than the `mlflow>=3.0.0` floor [[dspy-custom-module]] called for, confirming the DSPy autolog surface predates MLflow 3.0 and is supported across both the 2.x and 3.x lines. The tracking backend recommendation is *"It is highly recommended to use SQL store when using MLflow tracing"* — `mlflow server --backend-store-uri sqlite:///mydb.sqlite` rather than the file-based default.

### Parent/child run hierarchy for optimization runs

The same tutorial canonicalizes the **two-level run tree** MLflow imposes on a [[MIPROv2]] (or any `compile()`-based) optimization run:

| Level | Represents | Stored artifacts |
|---|---|---|
| **Parent run** | The overall `teleprompter.compile(...)` call | Optimizer config, final optimized program JSON, training data, metric progression curve across all trials |
| **Child run** | One intermediate program version produced during the optimizer's discrete-search stage | Per-attempt parameters (which instruction / demo-set combination was tested), the intermediate program's JSON, the Traces tab (step-by-step LM-call tree) |

Clicking through child runs is **the** canonical introspection surface for [[MIPROv2|MIPROv2's]] [[BayesianOptimization|Bayesian-surrogate]] discrete-search trajectory — every instruction the grounded-proposal stage drafted and every demo combination the search sampled is materialized as a navigable artifact tree. This run hierarchy is **specific to compile-time use**; inference-time `mlflow.dspy.autolog()` produces a single trace tree per `__call__` (no parent/child runs).

### Optimized-program load round-trip via `mlflow.artifacts.download_artifacts(...)`

The [[dspy-optimizer-tracking-tutorial|Optimizer Tracking tutorial]] is also the wiki's canonical source for **loading an optimized DSPy program back from the MLflow artifact store**:

```python
model_path = mlflow.artifacts.download_artifacts("mlflow-artifacts:/path/to/best_model.json")
program.load(model_path)
```

This is the **second documented load path** in the wiki — the first being the plain-JSON `program.save(path)` / `program.load(path)` round-trip ([[dspy-optimizers|Optimizers page]], [[dspy-entity-extraction-tutorial]], [[dspy-tutorial-rag-as-agent]]). The MLflow path adds **provenance** (the artifact is stored against a tracked run with the optimizer config + metric progression that produced it) at the cost of a running tracking server. Both ultimately route through `program.load(...)` against a JSON file; the difference is the artifact's *origin* (filesystem vs. MLflow artifact store) and *audit trail* (none vs. parent-run-anchored).

### First-party DSPy endorsement and the unscoped `mlflow.autolog()` form

The [[dspy-observability-tutorial|DSPy Debugging & Observability tutorial]] is the wiki's source for **MLflow as the framework's recommended observability backend** — *"MLflow is an end-to-end machine learning platform that seamlessly integrates with DSPy to support best practices in LLMOps. Using MLflow's automatic tracing capability with DSPy is straightforward; no API key or sign up required."* This is the first-party endorsement quote; [[DSPyObservability]] places MLflow autolog as tier 2 of the three-tier observability stack.

The tutorial uses the **unscoped form** of autolog — `mlflow.autolog()` rather than `mlflow.dspy.autolog(...)`:

```python
import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("DSPy")
mlflow.autolog()
```

Both invocations route to the same DSPy integration; the scoped form documented above is the canonical surface for kwarg-bearing toggles (`log_compiles`, `log_evals`, `log_traces_from_compile`). The unscoped form is sufficient for inference-time tracing and is the form the observability tutorial uses end-to-end.

The tutorial also cites a **`mlflow>=2.18.0`** floor — the **lowest** floor in the wiki's DSPy tutorial corpus, beneath the `mlflow>=2.21.1` floor in [[dspy-optimizer-tracking-tutorial]] and the `mlflow>=3.0.0` floor in [[dspy-custom-module]]. Inference-time DSPy autologging is supported on the MLflow 2.x line from 2.18 forward; later floors reflect compile-time features added in 2.21 / 3.0.

### Canonical stale-retrieval diagnosis pattern

The [[dspy-observability-tutorial|tutorial]] establishes the **canonical retrieval-staleness diagnosis pattern** for the DSPy corpus: a [[react|`dspy.ReAct`]] agent over a [[ColBERTv2]] Wikipedia dump returns a fluent but **stale** answer ("Hokkaido Nippon-Ham Fighters" for Shohei Ohtani's team — the dump pre-dates his 2024 Dodgers signing). The bug is **invisible at the LM-output layer** (chain-of-thought looks well-grounded) and only becomes visible by **hovering the retriever span in the MLflow trace UI** to read the returned article directly. Fix: substitute a [[Tavily]] web-search [[DSPyTools|`dspy.Tool`]] for the ColBERTv2 retriever; re-run; confirm via the same trace UI.

This pattern is the operational receipt for the framing thesis *"Without transparency, the prediction process can easily become a black box"* — the bug is **literally** indistinguishable from a hallucination without the MLflow trace, and **literally** obvious with it.

### DSPy program serving — `mlflow.dspy.log_model` and `mlflow models serve`

[[dspy-deployment-tutorial|The Deployment tutorial]] canonicalizes MLflow as DSPy's **enterprise serving path** — versioning, registry, packaging, container build. Minimum `mlflow>=2.18.0`.

```python
import dspy, mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000/")
mlflow.set_experiment("deploy_dspy_program")

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class MyProgram(dspy.Module):
    def __init__(self):
        super().__init__()
        self.cot = dspy.ChainOfThought("question -> answer")

    def forward(self, messages):
        return self.cot(question=messages[0]["content"])

with mlflow.start_run():
    mlflow.dspy.log_model(
        MyProgram(),
        "dspy_program",
        input_example={"messages": [{"role": "user", "content": "What is LLM agent?"}]},
        task="llm/v1/chat",
    )
```

```bash
mlflow models serve -m runs:/{run_id}/model -p 6000
mlflow models build-docker -m "runs:/{run_id}/model" -n "dspy-program"
docker run -p 6000:8080 dspy-program
```

Three load-bearing structural details:

1. **Custom `dspy.Module` subclass with positional `forward()` is mandatory** — *"Without a class wrapper, we cannot use a pre-built dspy module like Predict or ChainOfThought directly"* (tutorial). MLflow's signature-inference walks positional args; bare [[DSPyPredict|`dspy.Predict`]] / [[chainofthought|`dspy.ChainOfThought`]] won't log. Re-anchors [[DSPyModules|the Modules-page]] *"put your logic in a custom module"* discipline as a **deployment-time** requirement, complementing its [[MLflow|autolog]]-time and [[DSPyOptimizers|optimizer]]-time uses.
2. **`task="llm/v1/chat"` exposes the served model behind an OpenAI-compatible chat interface** — `{"messages": [{"role": "...", "content": "..."}]}` request shape. Clients written against OpenAI's chat-completions schema work unchanged. Significant for **migrating an existing OpenAI-client codebase to a DSPy-optimized program without rewriting the client**.
3. **`mlflow models build-docker` containerizes end-to-end** — one command produces a Docker image; no Dockerfile authorship required. The dependency snapshot logged with the model ([[Conda|`conda.yaml`]] / `requirements.txt`) is what makes this reproducible.

This is the wiki's first MLflow receipt that **serves** a DSPy program (the prior receipts cover **track / trace / store** — autolog, artifact download, run hierarchy). Together they span the full MLflow lifecycle: experiment-time observability → optimization-time artifact storage → serve-time model packaging.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 names **MLflow AI Gateway** as one of the canonical off-the-shelf [[ModelGateway|model-gateway]] solutions:

> *"There are many off-the-shelf gateways. Examples include Portkey's AI Gateway, MLflow AI Gateway, Wealthsimple's LLM Gateway, TrueFoundry, Kong, and Cloudflare."* — Ch 10

MLflow AI Gateway is the LLM-app-side product surface of the broader MLflow platform — a unified interface over LLM providers with route management, rate limiting, and provider abstraction. Its inclusion in Huyen's gateway list places MLflow alongside both general-API-gateway vendors ([[Kong]], [[Cloudflare]]) and AI-specific ones ([[Portkey]], [[TrueFoundry]]).

This gateway role is **additive** to MLflow's traditional experiment-tracking and model-registry responsibilities documented above — it extends the platform from "ML pipeline lifecycle" into "LLM-app inference surface," reflecting the broader MLflow expansion toward end-to-end LLM platform coverage.
