---
title: "Batch Inference"
type: concept
tags: [mlops, serving, inference]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Batch Inference

Running model predictions over large offline datasets in bulk (as opposed to online request/response). Optimized for throughput rather than latency; typical runtime for [[AnyscaleJobs]], [[DataPipeline]] feature backfills, and [[ETL]]-style ML workloads.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 makes an important **terminology disambiguation** between foundation-model batch APIs and traditional ML batch inference:

> *"A batch API for foundation models differs from batch inference for traditional ML. In traditional ML: Online inference means that predictions are computed after requests have arrived. Batch inference means that predictions are precomputed before requests have arrived."*

In traditional ML (e.g. recommendation systems), predictions are **precomputed** for all known users because inputs are predictable. For foundation models, inputs are open-ended user prompts — you can't precompute.

So FM "batch APIs" are really **deferred-online APIs**:
- Same model.
- Requests queued and processed in bulk for cost efficiency.
- Optimization techniques (larger batches, cheaper hardware) made possible by relaxed latency.
- **50% cost reduction** vs online APIs (Google Gemini, OpenAI as of late 2024).
- Turnaround "in the order of hours instead of seconds or minutes."

## Use cases for batch APIs (Ch 9)

- **Synthetic data generation**.
- **Periodic reporting** — summarizing Slack messages, sentiment analysis of brand mentions, customer support ticket analysis.
- **Onboarding new customers** with bulk document processing.
- **Migrating to a new model** that requires reprocessing all data.
- **Personalized recommendations / newsletters** at scale.
- **Knowledge-base reindexing**.

## Connections

- [[OnlineInference]] — the latency-priority counterpart.
- [[InferenceOptimization]] — broader discipline.
- [[Batching]] — at the per-request granularity (different from this macro-level mode).
- [[Goodput]] — meaningful only for online; batch APIs optimize raw cost.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
