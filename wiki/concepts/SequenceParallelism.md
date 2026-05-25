---
title: "Sequence Parallelism"
type: concept
tags: [parallelism, inference, long-context, llm-engineering]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Sequence Parallelism

**A parallelism strategy that distributes the *operators* applied to the entire input across devices** — e.g. attention on one machine, feedforward on another. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"In sequence parallelism, operators needed for the entire input are split across machines. For example, if the input requires both attention and feedforward computation, attention might be processed on machine 1 while feedforward is processed on machine 2."*

## Position in the parallelism family

Distinct from [[ContextParallelism|context parallelism]] (which splits the **sequence positions** across devices). Sequence parallelism splits the **operators** that run on each position.

| Strategy | Split |
|---|---|
| [[ContextParallelism]] | Positions of the input sequence |
| **Sequence parallelism** | **Operators applied to each position** |
| [[TensorParallelism]] | Weight matrices within an operator |
| [[PipelineParallelism]] | Layers |
| [[ReplicaParallelism]] | Independent requests |

## Megatron-LM lineage

The existing [[TensorParallelism]] page notes: *"Sequence parallelism (Megatron-LM, 2019) generalizes TP to LayerNorm and Dropout activations."* This earlier Megatron-LM usage is closely related but operator-specific (LayerNorm, Dropout). Ch 9's sequence-parallelism description is more general.

## Why it exists

Long input sequences create activation memory pressure even on otherwise-fitting models — splitting operators across devices alleviates this without changing the model architecture.

## Ch 9's framing

Like [[ContextParallelism|context parallelism]], Ch 9 mentions sequence parallelism as a less common but illustrative parallelism strategy for "long input sequence processing."

## Connections

- [[ContextParallelism]] — closely related sibling (splits positions instead of operators).
- [[TensorParallelism]] / [[PipelineParallelism]] / [[ReplicaParallelism]] — broader parallelism family.
- [[Attention]] / [[FeedForwardNetwork]] — the operators sequence parallelism distributes.
- [[ActivationMemory]] — what sequence parallelism relieves pressure on.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
