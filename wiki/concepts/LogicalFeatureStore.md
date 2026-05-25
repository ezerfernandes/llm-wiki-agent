---
title: "Logical Feature Store"
type: concept
tags: [mlops, feature-engineering, architecture, rag]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch04-rag-feature-pipeline]
last_updated: 2026-05-22
---

## Definition
A **logical feature store** is a pragmatic substitute for a specialized [[FeatureStore]] product, assembled from existing infrastructure — typically a [[VectorDatabase]] (for online retrieval) plus versioned artifacts in object storage (for offline training access) — that together satisfy the feature-store contract without requiring a dedicated platform like Hopsworks, Tecton, or Featureform.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] introduces the logical feature store as the LLM Twin's deliberately MVP-sized alternative to a specialized feature store: a [[Qdrant]] vector DB serves the online retrieval path (used by the inference pipeline for vector search) while [[ZenML]] versioned artifacts in [[AmazonS3|S3]] serve the offline path (used by the training pipeline to materialize instruct datasets). [[leh-ch04-rag-feature-pipeline]] makes the design concrete: the feature pipeline stores **two snapshots** in Qdrant — a cleaned snapshot indexed only on metadata (for fine-tuning) and a chunked+embedded snapshot with the vector index (for RAG) — leveraging Qdrant's metadata index as a NoSQL store for the cleaned-only collection. The choice trades dedicated feature-store ergonomics (point-in-time correctness, feature lineage UI) for simpler operations and lower cost.

## Key details
- Two access paths from one logical store: online (low-latency vector search for inference) and offline (versioned artifacts for training).
- Eliminates [[TrainingServingSkew]] because both paths read from the same underlying feature snapshots.
- Uses an existing vector DB's metadata index for non-vector lookups instead of a separate scalar store.
- Cheaper and simpler than a specialized feature store; sufficient for a single-product MVP.
- The chapter recommends graduating to a true feature store (Hopsworks, Tecton, Featureform) only when feature reuse across products and point-in-time correctness become real requirements.

## Connections
- [[FeatureStore]] — the canonical concept this approximates.
- [[VectorDatabase]] / [[Qdrant]] — the online half of the logical store.
- [[FTIArchitecture]] — the feature-store contract the FTI pattern depends on.
- [[Hopsworks]] / [[Tecton]] / [[Featureform]] — specialized feature-store alternatives.
- [[TrainingServingSkew]] — the failure mode any feature store (logical or specialized) eliminates.
- [[Artifact]] / [[ZenML]] — the offline-access layer; versioned artifacts produced by orchestrated pipelines.
