---
title: "Monolithic Batch Architecture"
type: concept
tags: [architecture, mlops, anti-pattern]
sources: [leh-ch01-understanding-llm-twin-concept]
last_updated: 2026-05-22
---

## Definition
A **monolithic batch architecture** is an ML deployment pattern in which a single process loads data, computes features, trains a model, and emits predictions in one batch job — coupling feature engineering, training, and inference into a single unit of code and compute. The *LLM Engineer's Handbook* labels it an anti-pattern relative to the [[FTIArchitecture|FTI pipeline pattern]].

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] critiques the monolithic batch architecture as one of two patterns that motivated the FTI design. Its failure modes are concrete: features cannot be reused across models or products; scaling the data layer to PySpark or Ray requires rewriting the model code; the inference module cannot be ported to C++ / Java / Rust because it is welded to Python training code; work cannot be split cleanly across teams; and streaming or real-time training is impossible because the architecture is fundamentally batch-coupled.

## Key details
- Single process owns extraction + features + training + inference.
- No reusable feature artifacts and no [[FeatureStore]].
- Cannot independently scale CPU-heavy feature work and GPU-heavy training.
- Cannot swap the inference language/runtime independently of training.
- Streaming-style updates and online inference are precluded.

## Connections
- [[FTIArchitecture]] — the pattern that replaces this anti-pattern.
- [[StatelessRealTimeArchitecture]] — the second anti-pattern the book rejects.
- [[FeatureStore]] — the abstraction that decouples training from inference.
- [[MLOps]] — the discipline this anti-pattern fails.
- [[TrainingServingSkew]] — failure mode that monolithic batch makes harder to detect.
