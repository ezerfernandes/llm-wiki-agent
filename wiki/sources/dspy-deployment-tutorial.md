---
title: "DSPy Tutorial — Deployment"
type: source
tags: [dspy, deployment, fastapi, mlflow, asyncify, streaming, production, tutorial]
date: 2026-05-24
source_file: raw/dspy-deployment-tutorial.md
---

## Summary

Short single-page [[DSPy]] tutorial at `https://dspy.ai/tutorials/deployment/` that **canonicalizes the framework's production-serving surface** — two recommended packaging paths ([[FastAPI]] for lightweight REST, [[MLflow]] for versioned enterprise deployments) plus the **sync-to-async wrapper `dspy.asyncify(...)`** that converts a sync DSPy program into an async-callable runnable from inside an async web service. Sibling tutorial to [[dspy-async-tutorial]] (the dispatch axis) and [[dspy-streaming-tutorial]] (the streaming axis) — together the three constitute DSPy's framework-level *production-shape* documentation. Programming-stage-only — no metric, no [[DSPyOptimizers|Optimizer]], no dataset; the question is *how do I serve this program*, not *how do I make it better*.

## Key Claims

- **`dspy.asyncify(program)` is the canonical sync-program-to-async-callable wrapper for web services.** Distinct from `acall` / `aforward` on the [[DSPyAsync|async axis]] — `asyncify` takes a sync program and runs it on a thread pool (sized by `dspy.configure(async_max_workers=N)`, default 8); `acall` requires the program to be natively async. Pattern: sync DSPy code, async service shell.
- **[[FastAPI]] + [[Uvicorn]] is the lightweight serving path.** [[Pydantic]] `BaseModel` for request validation, `@app.post("/predict")` as the handler, `await dspy_program(...)` inside the handler. The tutorial's worked example wraps a [[chainofthought|`dspy.ChainOfThought`]] over a `"question -> answer"` [[DSPySignatures|signature]].
- **`dspy.streamify` composes cleanly with FastAPI's `StreamingResponse`.** The tutorial introduces `dspy.utils.streaming.streaming_response` — a helper that converts the [[DSPyStreaming|streaming generator]] into properly framed [[ServerSentEvents|Server-Sent Events]] (`media_type="text/event-stream"`). Closes the loop on the [[DSPyStreaming|Streaming concept page's]] forward reference to *"natural transports for the streaming generator at the web layer."*
- **[[MLflow]] is the enterprise path** — versioning, registry, packaging, container build. Minimum `mlflow>=2.18.0`. Requires wrapping the DSPy program in a **custom `dspy.Module` subclass with `forward()` accepting positional args** — `mlflow.dspy.log_model(...)` will not log a bare [[DSPyPredict|`dspy.Predict`]] / [[chainofthought|`dspy.ChainOfThought`]] directly. The constraint is MLflow's signature-inference requirement, not a DSPy limitation.
- **`task="llm/v1/chat"` exposes the served model behind an OpenAI-compatible chat interface.** `mlflow.dspy.log_model(..., task="llm/v1/chat")` makes the served endpoint accept `{"messages": [{"role": "...", "content": "..."}]}` — clients written against OpenAI's chat-completions schema work unchanged. Significant for migrating an existing OpenAI-client codebase to a DSPy-optimized program without rewriting the client.
- **`mlflow models build-docker` containerizes the logged model end-to-end.** One command produces a Docker image; `docker run -p 6000:8080 <name>` serves it. No Dockerfile authorship required.
- **`dspy.configure(async_max_workers=N)` controls the asyncify thread pool size** — default 8. Tuning knob for concurrent request capacity under the asyncify pattern. Distinct from `async_max_workers` on native `acall` (no thread pool — pure event loop).

## Key Quotes

> "DSPy is a powerful framework for building AI applications, and the natural next step is to deploy your application to production." — opening

> "There are many ways to deploy your DSPy application. In this guide, we will cover two common ways: FastAPI for lightweight deployments and MLflow for more production-grade deployments with program versioning and management."

> "Note that `dspy.asyncify` is used to convert the dspy program to run in async mode for high-throughput FastAPI deployments. Currently, this runs the dspy program on a separate thread and returns its result." — the asyncify thread-pool disclosure

> "We need to wrap our DSPy program in an MLflow custom model class. Without a class wrapper, we cannot use a pre-built dspy module like Predict or ChainOfThought directly." — the MLflow Module-wrapping constraint

> "MLflow integrates seamlessly with DSPy, offering the following benefits: Experiment Tracking, Reproducibility, Dependency Management." — the MLflow value-prop framing

## Connections

- [[DSPy]] — the framework whose production-serving surface this tutorial canonicalizes.
- [[DSPyAsync]] — sibling-axis concept page; `asyncify` is a **third async surface** alongside `acall` (built-in modules) and `aforward` (custom modules). Where `acall` / `aforward` require the program to be **natively async**, `asyncify` takes a **sync program** and wraps it for async consumption via a thread pool. Distinct cost model and distinct use case (existing sync code into an async web service vs writing async-native code from the start).
- [[DSPyStreaming]] — sibling-axis concept page; this tutorial **closes the forward reference** to *"natural transports for the streaming generator at the web layer."* `dspy.utils.streaming.streaming_response` + FastAPI's `StreamingResponse` is the canonical [[ServerSentEvents|SSE]] transport.
- [[chainofthought|ChainOfThought]] — the worked-example module (`dspy.ChainOfThought("question -> answer")`).
- [[DSPySignatures]] — `"question -> answer"` inline string signature; the [[DSPyAdapters|Adapter]] serializes I/O on the wire.
- [[DSPyModules]] — MLflow's custom-wrapper constraint forces a `dspy.Module` subclass with `forward(self, messages)` — re-anchors [[DSPyModules|the Modules-page]] *"put your logic in a custom module"* discipline as a **deployment-time** requirement, not only an [[MLflow|autolog]]-time one.
- [[DSPyLM]] — `dspy.LM("openai/gpt-4o-mini")` in both serving paths.
- [[DSPyPredict]] — referenced as the *cannot-log-directly* case under MLflow (must wrap in custom Module).
- [[FastAPI]] — lightweight serving path; first wiki receipt of a **DSPy-program-fronting** FastAPI app (prior FastAPI receipts: [[madewithml-mlops-serving|RayServe wrapper]], [[leh-ch10-inference-pipeline-deployment|LLM Twin]], [[dspy-sample-code-generation-tutorial|LM-driven analysis target]]).
- [[Uvicorn]] — ASGI server running the FastAPI app (`uvicorn fastapi_dspy:app --reload`).
- [[Pydantic]] — `BaseModel` for request schema validation. The tutorial uses Pydantic in its **canonical FastAPI request-validation role**, distinct from its [[DSPySignatures|tier-three DSPy type]] role.
- [[MLflow]] — enterprise serving path; first wiki receipt of `mlflow.dspy.log_model(...)` (prior MLflow receipts cover [[MLflow|autologging / tracing / artifact storage]]). Closes the gap from *experiment-time MLflow* (autolog, artifact store) to *serve-time MLflow* (log_model, models serve, build-docker).
- [[Docker]] — `mlflow models build-docker` + `docker run` for container deployment.
- [[ServerSentEvents]] — the streaming transport; `media_type="text/event-stream"` in the `StreamingResponse`.
- [[openai|OpenAI]] — the LM provider in the worked example (`gpt-4o-mini`).
- [[dspy-async-tutorial]] — sibling tutorial on the async-dispatch axis; `acall` / `aforward` complement (do not replace) `asyncify`.
- [[dspy-streaming-tutorial]] — sibling tutorial on the streaming axis; `dspy.streamify` is the upstream of this tutorial's `streaming_response` integration.
- [[dspy-learn-index]] / [[dspy-programming-overview]] — the broader DSPy *Learn* / Tutorials index this page sits within.

## Contradictions

None. The tutorial **extends** the wiki along an orthogonal *serve* axis:

- [[DSPyAsync]]'s `acall` / `aforward` pattern is augmented (not replaced) by `asyncify` — the three serve distinct populations (existing sync code, async-native code, async-native code).
- [[DSPyStreaming]]'s forward reference to web-layer transports is **resolved** by the FastAPI + SSE recipe here.
- [[MLflow]]'s wiki page documented autologging / tracing / artifact storage but not model serving — this tutorial closes that gap with `mlflow.dspy.log_model(...)` + `mlflow models serve` + `build-docker`.

## Gaps

- **No production-monitoring recipe.** The tutorial names *"Production Monitoring"* as a best practice but supplies no code (no [[Prometheus]] / [[Grafana]] / structured-logging snippet).
- **No load-test / throughput numbers.** `async_max_workers=4` is tunable but the tutorial gives no concrete throughput / latency measurement to anchor the choice.
- **No authentication / authorization.** The FastAPI worked example is wide-open (no API key, no JWT, no rate limiting). The [[dspy-sample-code-generation-tutorial|sample code generation tutorial]]'s JWT recipe is one place a reader can borrow from; this tutorial does not cross-reference it.
- **No `aforward`-routed program example.** The MLflow custom-Module wrapper uses `forward()`, not `aforward()` — the deployment story for natively-async DSPy programs (`aforward` + `mlflow.dspy.log_model`) is not exercised.
- **No cost / observability under `asyncify`.** `dspy.Prediction.get_lm_usage()` / [[MLflow|`mlflow.dspy.autolog()`]] behavior under the thread-pool dispatch is presumed to work but not demonstrated.
- **No multi-program serving.** The MLflow path serves one model per port; serving multiple DSPy programs from one process (or one container) is not discussed.
- **No batched inference.** Per-request `predict` calls only; the [[BatchInference|batch-inference]] shape (multiple questions in one request) is not exercised.
- **No streaming + MLflow combination.** The streaming example uses FastAPI; whether `mlflow models serve` supports SSE for `dspy.streamify`-wrapped programs is not covered.
- **No graceful shutdown / health check.** Production endpoints typically need `/health` and `/ready` — neither shown.
