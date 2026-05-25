---
title: "Context Parallelism"
type: concept
tags: [parallelism, inference, long-context, llm-engineering]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Context Parallelism

**A parallelism strategy that splits the *input sequence* across devices, with each device processing a contiguous portion of the input.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"In context parallelism, the input sequence itself is split across different devices to be processed separately. For example, the first half of the input is processed on machine 1 and the second half on machine 2."*

A long-input-sequence-specific parallelism strategy, developed alongside [[SequenceParallelism|sequence parallelism]] to make long-context LLM serving practical.

## When context parallelism matters

The cost of the attention mechanism is `O(n²)` in sequence length `n`. For long contexts (32K, 128K, 1M tokens) a single GPU runs out of compute time and memory long before the model itself does. Context parallelism distributes the **input** instead of the model.

## Position in the parallelism family

| Strategy | What it splits |
|---|---|
| [[ReplicaParallelism]] | Independent requests (each device runs the full model) |
| [[TensorParallelism]] | Weight matrices within a layer |
| [[PipelineParallelism]] | Layers across devices |
| **[[ContextParallelism]]** | **Input sequence positions** |
| [[SequenceParallelism]] | Operators applied to the entire input |

## Ch 9's framing

Ch 9 treats both context and sequence parallelism as "less common" but illustrative of the diversity of parallelism strategies for LLMs — they're "developed to make long input sequence processing more efficient."

## Connections

- [[SequenceParallelism]] — closely related sibling strategy.
- [[TensorParallelism]] / [[PipelineParallelism]] / [[ReplicaParallelism]] — the broader family.
- [[Attention]] — the `O(n²)` mechanism context parallelism distributes.
- [[KVCache]] — the structure context parallelism partitions.
- [[FlashAttention]] — orthogonal long-context optimization.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
