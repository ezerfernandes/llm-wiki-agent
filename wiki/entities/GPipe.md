---
title: "GPipe"
type: entity
tags: [cs324, llm]
sources: [cs324-parallelism]
last_updated: 2026-06-04
---

GPipe is a Google pipeline-parallelism library that splits a model across devices by layer and uses micro-batching to keep all stages busy. It combines this with activation re-materialization (gradient checkpointing) to train models too large to fit on a single accelerator.

## Connections
- [[PipelineParallelism]] — GPipe is a foundational pipeline-parallel framework
- [[GradientCheckpointing]] — uses activation re-materialization to save memory
- [[cs324-parallelism]] — discussed in this CS324 lecture
