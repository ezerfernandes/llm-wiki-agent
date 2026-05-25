---
title: "Megatron-LM"
type: entity
tags: [tool]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## What it is
NVIDIA framework introducing tensor parallelism for Transformers.

## In LLM Engineer's Handbook
Megatron-LM (Shoeybi, Patwary, Puri et al. 2019/2020, *Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism*) originated [[TensorParallelism]] for Transformer layers. Per [[leh-ch08-inference-optimization]] it is the canonical implementation referenced alongside [[DeepSpeed]] and [[PiPPy]].
