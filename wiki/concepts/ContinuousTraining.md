---
title: "Continuous Training (CT)"
type: concept
tags: [mlops, llmops, cicd, automation]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch11-mlops-and-llmops, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

## Definition
**Continuous Training (CT)** is the MLOps practice of automatically retraining (or fine-tuning) a model when fresh data, code, or hyperparameter changes warrant it — without manual intervention. CT is the ML/LLM-specific peer of [[CICD]]: CI/CD builds and deploys code, CT rebuilds and redeploys models.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] introduces CT as the trigger fired when a new [[InstructDataset]] artifact lands in the [[FeatureStore]], chaining feature → training → evaluation → optional manual approval → deployment. The chapter emphasizes that "even in a fully automated ML system, it is recommended to have a manual step before accepting a new production model" — the "red button" guardrail. [[leh-ch11-mlops-and-llmops]] expands CT into a full pipeline (`end_to_end_data` master pipeline) that chains data collection ETL → feature engineering → instruct-dataset generation → training → deploy, and enumerates three trigger types: **manual** (CLI/dashboard, used by the LLM Twin because data sources are static), **REST API** (`Client().trigger_pipeline(...)` invoked by a watcher service), and **scheduled** (cron expressions). The chapter argues two design choices make CT tractable: the [[FTIArchitecture|FTI architecture]] (modular pipelines with clear interfaces) and "starting with an orchestrator on day 0" (forcing inter-pipeline communication through versioned storage).

## Key details
- CT distinguishes ML from traditional software: a code-frozen system may still need a new build when only data changes.
- Three CT trigger categories: manual, event/REST API, scheduled.
- Recommended pattern: chain pipelines via `trigger_pipeline()` calls so each stays isolated; the book's `end_to_end_data` monolith is explicitly an anti-pattern adopted only to dodge ZenML free-tier's 3-pipeline cap.
- A keep-a-human-in-the-loop "red button" approval step is recommended before promoting any new model to production.
- LLMOps inherits CT but typically retrains as a fine-tune of an existing foundation model, not a from-scratch run.

## Connections
- [[CICD]] — peer automation discipline; CT, CI, and CD together form the "CT/CI/CD" triad.
- [[MLOps]] / [[LLMOps]] — CT is one of the three automation tiers (manual → CT → full CI/CD).
- [[FTIArchitecture]] — the architecture that makes CT tractable.
- [[ZenML]] — the orchestrator used to express CT pipelines in the book.
- [[ModelRegistry]] — destination of every CT-produced model candidate.
- [[FeatureStore]] — source of CT input data.
- [[InstructDataset]] — the LLM-specific artifact whose arrival can trigger CT.
- [[CanaryDeployment]] / [[ShadowDeployment]] — progressive-rollout patterns that complement CT's "red button" gate.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 covers continuous-training pipelines with retraining triggers (drift/performance) feeding the CI/CD loop.

