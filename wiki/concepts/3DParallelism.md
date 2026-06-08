---
title: "3D Parallelism"
type: concept
tags: [cs324, llm]
sources: [cs324-parallelism]
last_updated: 2026-06-04
---

3D parallelism composes tensor (model) parallelism, pipeline parallelism, and data parallelism to train very large models across many devices. Combining all three dimensions distributes both the model and the batch, enabling training at scales no single axis can reach alone (e.g. Megatron-style training).

## Connections
- [[DataParallelism]] — one of the three composed dimensions
- [[ModelParallelism]] — one of the three composed dimensions
- [[PipelineParallelism]] — one of the three composed dimensions
- [[Megatron]] — system using 3D parallelism
- [[cs324-parallelism]] — discussed in this CS324 lecture
