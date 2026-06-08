---
title: "TeraPipe"
type: entity
tags: [cs324, llm]
sources: [cs324-parallelism]
last_updated: 2026-06-04
---

TeraPipe is a token-level (sequence-dimension) pipeline parallelism technique that pipelines computation across the sequence positions of Transformer training. It reports roughly a 5x training speedup on GPT-3 175B compared to prior pipeline schemes.

## Connections
- [[PipelineParallelism]] — TeraPipe is a sequence-dimension pipeline-parallel method
- [[GPT-3]] — demonstrated speedups training GPT-3 175B
- [[cs324-parallelism]] — discussed in this CS324 lecture
