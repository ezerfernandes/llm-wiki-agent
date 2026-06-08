---
title: "vLLM"
type: entity
tags: [tool, inference, serving, mlsysbook]
sources: [leh-ch07-evaluating-llms, leh-ch08-inference-optimization, ai-engineering-ch09-inference-optimization, mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

## What it is
High-throughput LLM serving engine from UC Berkeley; first to ship PagedAttention.

## In LLM Engineer's Handbook
vLLM is the open-source LLM serving engine originating at UC Berkeley. It was the first production implementation of [[PagedAttention]] and supports [[ContinuousBatching]], [[FlashAttention2]], [[TensorParallelism]], and [[AWQ]] (no [[GPTQ]] or [[EXL2]] at writing). [[leh-ch07-evaluating-llms]] uses it for fast batch generation in evaluation pipelines (`temperature=0.8`, `top_p=0.95`, `max_tokens=4096`).

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 cites vLLM in two specific roles:

### Origin of PagedAttention

> *"One of the fastest growing inference frameworks, vLLM, gained popularity for introducing PagedAttention, which optimizes memory management by dividing the KV cache into non-contiguous blocks, reducing fragmentation, and enabling flexible memory sharing to improve LLM serving efficiency (Kwon et al., 2023)."*

[[PagedAttention]] is the headline KV-cache management technique in Ch 9's "optimize the KV cache" bucket, and vLLM is the framework that introduced it.

### Speculative decoding implementation

vLLM is one of three frameworks Ch 9 names as having integrated speculative decoding:

> *"It's been incorporated into popular inference frameworks such as vLLM, TensorRT-LLM, and llama.cpp."*

## From [[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]

Ch 13 ("Virtual LLM") credits vLLM with introducing [[PagedAttention]] (SOSP 2023, Kwon et al.) — the OS-virtual-memory analogy that cuts KV-cache fragmentation from 40–80% to <4% (>95% memory utilization vs 50–60%), enabling 2–4× higher throughput and the [[ContinuousBatching|continuous batching]] it makes fine-grained admission possible for. The standard for production [[LLMServing|LLM serving]]. See also [[mlsysbook-ch13-model-serving]].
