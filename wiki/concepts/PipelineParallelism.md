---
title: "Pipeline Parallelism"
type: concept
tags: [llm-engineering, parallelism, inference, training]
sources: [leh-ch08-inference-optimization, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

## Definition
GPipe-style layer partitioning across GPUs.

## In LLM Engineer's Handbook
Pipeline Parallelism (GPipe, Huang et al. 2019) assigns consecutive blocks of layers to different GPUs; activations flow forward through the pipeline. Per [[leh-ch08-inference-optimization]], pipeline bubbles are mitigated by [[MicroBatching]]. Implemented in [[MegatronLM]], [[DeepSpeed]], and [[PiPPy]]; among inference engines covered in Ch. 8, only [[TensorRTLLM]] supports PP.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 frames pipeline parallelism as a **training-favored, inference-disfavored** parallelism strategy:

> *"While pipeline parallelism enables serving large models on multiple machines, it increases the total latency for each request due to extra communication between pipeline stages. Therefore, for applications with strict latency requirements, pipeline parallelism is typically avoided in favor of replica parallelism. However, pipeline parallelism is commonly used in training since it can help increase throughput."*

### Why it hurts inference latency

Per-request latency = sum of per-stage processing + per-stage handoff communication. Since the request must traverse all stages sequentially, you've **added** all the inter-stage transfer costs to each request's wall-clock — even if each stage's processing time is divided.

### Why it helps training throughput

In training, micro-batching (Huang et al. 2019, GPipe) fills the pipeline so that *while* stage k is processing micro-batch i, stage k+1 is processing micro-batch i-1 — many requests "in flight" simultaneously. The aggregate throughput rises even though each request's latency increases.

### Combination with TP

Standard modern LLM training stack:
- **[[TensorParallelism|TP]] within a node** — fast NVLink interconnect handles per-layer all-reduce.
- **PP across nodes** — slower inter-node communication amortized over micro-batches.
- **DP across replicas** — independent of model state.

For inference, this typically collapses to TP-within-node + replica-parallelism, with PP avoided.

### Inference-engine support

Per [[leh-ch08-inference-optimization|LEH Ch 8]] (cited above), among the major inference engines (TGI, vLLM, TensorRT-LLM), **only TensorRT-LLM supports PP** — consistent with Ch 9's verdict that PP is uncommon for inference.
