---
title: "Replica Parallelism"
type: concept
tags: [parallelism, inference, serving, optimization]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Replica Parallelism

**The simplest parallelism strategy for inference: create multiple full copies of the model, each handling independent requests.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Replica parallelism is the most straightforward strategy to implement. It simply creates multiple replicas of the model you want to serve. More replicas allow you to handle more requests at the same time, potentially at the cost of using more chips."*

The training-time equivalent is **[[DataParallelism|data parallelism]]** — same idea, different naming convention (replicas handle different *data* in training; different *requests* at inference).

## The bin-packing problem

When you have:
- a mix of model sizes (e.g. 8B, 13B, 34B, 70B) and
- GPUs of varying memory (e.g. 24 GB, 40 GB, 48 GB, 80 GB),

deciding which models to replicate on which GPUs becomes a **bin-packing problem**. Ch 9 gives the two main framings:

1. **Fixed chips, choose replicas:** how many copies of each model on which GPUs to maximize service metrics? *(e.g. "three 13B on a 40 GB GPU, or one 34B?")*
2. **Fixed replicas, choose chips:** what GPUs to buy to minimize cost? *(rare in practice)*

## Why replica parallelism is Huyen's recommended lever

Closing summary of Ch 9:

> *"Across various use cases, the most impactful techniques are typically quantization (which generally works well across models), tensor parallelism (which both reduces latency and enables serving larger models), replica parallelism (which is relatively straightforward to implement), and attention mechanism optimization (which can significantly accelerate transformer models)."*

Replica parallelism is the **easy lever for latency-priority workloads**: more replicas = each one handles fewer requests = more resources per request = lower per-request latency.

## When replica parallelism is *not* enough

If the model **doesn't fit on a single machine**, replica parallelism alone won't help — you need [[TensorParallelism|tensor parallelism]] or [[PipelineParallelism|pipeline parallelism]] to split the model itself across machines. The three are **composable**: large frontier serving typically uses TP within a node, replica/data parallelism across nodes.

## Connections

- [[TensorParallelism]] — model-split sibling; reduces per-request latency.
- [[PipelineParallelism]] — model-split sibling; adds per-request latency.
- [[DataParallelism]] — training-time name for the same pattern.
- [[ContextParallelism]] / [[SequenceParallelism]] — LLM-specific parallelism variants.
- [[ModelParallelism]] — umbrella for non-replica parallelism.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
