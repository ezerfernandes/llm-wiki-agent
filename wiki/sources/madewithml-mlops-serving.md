---
title: "Made With ML — Model Serving"
type: source
tags: [mlops, made-with-ml, serving, deployment]
date: 2026-05-15
source_file: raw/madewithml/mlops-serving.md
---

## Summary
Made With ML lesson on serving ML models with high throughput and low latency. Compares batch (offline) vs online (real-time) inference, surveys frameworks (Ray Serve, Triton, HuggingFace Endpoints, BentoML), and walks through a Ray Serve + FastAPI implementation. Demonstrates how to wrap a `TorchPredictor` for batch inference via `map_batches` and as a `serve.deployment` for online inference, and shows how to add a confidence-threshold custom logic layer that routes uncertain predictions to an `other` class.

## Key Claims
- Serving framework selection should weigh five axes: Pythonic API, framework-agnosticism, scaling, model composition, and integrations (FastAPI, LangChain, Kubernetes).
- Batch inference is appropriate when low latency is not required; Ray Data's `map_batches` with an `ActorPoolStrategy` autoscales the predictor across a pool.
- Online inference for real-time content categorization is preferred for user-facing products that need fast feedback.
- [[RayServe]] composes naturally with FastAPI via `serve.ingress`, and deployment configuration (replicas, CPU/GPU per actor) is decorator-driven.
- LLMs and neural classifiers are notoriously overconfident: even random-noise input gets a confident class prediction.
- Custom serving logic (threshold-based fallback to an `other` class) is cleaner than retraining the model when product specifications change — it preserves separation between product logic and ML.
- The same MLflow tracking URI must be set inside the deployment so distributed workers can resolve the model registry.

## Key Quotes
> "It's easier to incorporate custom logic instead of altering the model itself. This way, we won't have to collect new data, change the model's architecture or retrain it." — on the value of post-prediction product logic

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher / Ray maintainer
- [[Ray]] — distributed runtime
- [[RayServe]] — primary serving framework used
- [[FastAPI]] — HTTP layer
- [[NvidiaTriton]] — alternative serving framework
- [[HuggingFace]] — alternative serving option
- [[BentoML]] — alternative serving framework
- [[MLflow]] — model registry / tracking URI
- [[PyTorch]] — model framework
- [[ModelServing]] — core concept
- [[BatchInference]] — offline pattern
- [[OnlineInference]] — real-time pattern
- [[MLOps]] — discipline
- [[Autoscaling]] — replica/actor scaling
- [[ModelComposition]] — combining models + business logic

## Contradictions
- None identified.
