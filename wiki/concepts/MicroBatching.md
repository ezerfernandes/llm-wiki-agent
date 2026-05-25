---
title: "Micro-Batching"
type: concept
tags: [llm-engineering]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## Definition
Splits a batch into smaller sub-batches to fill pipeline parallelism bubbles.

## In LLM Engineer's Handbook
Technique in [[PipelineParallelism]] to mitigate pipeline bubbles. The input batch is divided into smaller sub-batches; as soon as the first stage finishes sub-batch 0, it can begin sub-batch 1 while the second stage processes sub-batch 0. Per [[leh-ch08-inference-optimization]] this overlap keeps all stages busy, dramatically reducing pipeline idle time.
