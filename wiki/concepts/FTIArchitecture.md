---
title: "FTI Architecture (Feature/Training/Inference Pipelines)"
type: concept
tags: [architecture, mlops, system-design, llm-engineering]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## Definition
The **Feature/Training/Inference (FTI) pipeline pattern** decomposes any ML system into three independent pipelines — a **feature pipeline** that transforms raw data into versioned features, a **training pipeline** that consumes features and emits model artifacts, and an **inference pipeline** that loads a model and applies it to fresh requests. It is the ML analogue of the classic database/business-logic/UI three-layer split in conventional software and is credited to Jim Dowling of [[Hopsworks]].

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] introduces FTI as the architectural backbone of the entire LLM Twin project, contrasting it with two anti-patterns ([[MonolithicBatchArchitecture]] and [[StatelessRealTimeArchitecture]]) and the over-engineered [[GoogleCloudMLOpsReference]]. The chapter argues FTI works because each pipeline is independently scalable (CPU horizontal for feature/data work, GPU vertical for training, latency-bounded horizontal for inference), independently replaceable, and can be owned by different teams. The LLM Twin extends FTI to four pipelines by prepending a [[DataCollectionPipeline]] owned by data engineering before the FTI trio owned by ML engineering. [[leh-ch11-mlops-and-llmops]] confirms that this modular FTI design plus "starting with an orchestrator on day 0" is what makes the later [[ContinuousTraining]] pipeline tractable — every pipeline already communicates only through versioned storage, never ad-hoc CLI flags.

## Key details
- Three pipelines with sharply different compute profiles: feature (CPU-heavy, horizontal scale), training (GPU-heavy, vertical scale), inference (mixed, horizontal scale on requests with latency SLOs).
- Eliminates [[TrainingServingSkew]] by persisting features into a versioned [[FeatureStore]] that both training and inference consume.
- Each pipeline owns its own contract; swapping the training stack (e.g., from Mistral to Llama) does not touch feature or inference code.
- The authors explicitly call the pattern a "tool used to clarify how to design ML systems," not a rigid rule.
- The LLM Twin's FTI variant uses a [[LogicalFeatureStore]] ([[VectorDatabase]] + versioned artifacts) instead of a specialized feature store.

## Connections
- [[MLOps]] — FTI is the production-grade alternative to monolithic ML; it operationalizes the MLOps principles of versioning, reusability, and lineage.
- [[LLMOps]] — inherits FTI; the LLM Twin's four-pipeline variant is a direct LLMOps blueprint.
- [[FeatureStore]] / [[LogicalFeatureStore]] — the shared interface between feature and training/inference pipelines.
- [[TrainingServingSkew]] — the canonical failure mode FTI eliminates.
- [[DataCollectionPipeline]] — the upstream data-engineering pipeline that precedes the FTI trio in the LLM Twin design.
- [[ContinuousTraining]] — CT is the automated event that re-runs training pipelines when fresh feature snapshots land.
- [[MonolithicBatchArchitecture]] / [[StatelessRealTimeArchitecture]] — the two anti-patterns FTI displaces.
- [[Hopsworks]] / [[JimDowling]] — origin of the pattern.
- [[ZenML]] — concrete orchestrator used in the book to express FTI pipelines as `@pipeline` / `@step` graphs.
- [[LLMTwin]] — the book-spanning project built on FTI.
