---
title: "Colossal-AI"
type: entity
tags: [tool, distributed-training, framework, open-source]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Colossal-AI

An open-source **distributed training framework** for large-scale model training and finetuning. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "To finetune a model using more than one machine, you'll need a framework that helps you do distributed training, such as DeepSpeed, PyTorch Distributed, and ColossalAI."

## What it offers

- **Multi-dimensional parallelism**: data, tensor, pipeline, sequence, and expert parallelism in one framework.
- **ZeRO-style offloading**: similar to [[DeepSpeed]]'s [[ZeRO]] optimizer.
- **Heterogeneous training**: supports CPU/GPU/NVMe offloading.
- **Reduces memory pressure** for very large models that don't fit on a single GPU.

## Position relative to siblings

| Framework | Strength |
|---|---|
| **[[DeepSpeed]]** | Industry-standard; large community |
| **[[PyTorchDistributed]]** | Built into PyTorch; minimal dependencies |
| **Colossal-AI** | Multi-dimensional parallelism out-of-the-box |

For finetuning use cases that fit on a single machine, the single-machine frameworks ([[LLaMAFactory]], [[Unsloth]], [[Axolotl]], [[LitGPT]]) are usually sufficient. Colossal-AI shines for multi-node training.

## Connections

- [[DeepSpeed]] / [[PyTorchDistributed]] — sibling distributed-training frameworks.
- [[ZeRO]] — the memory-optimization technique Colossal-AI also implements.
- [[CPUOffloading]] — supported.
- [[FineTuning]] / [[FullFinetuning]] — the operations it enables at scale.
- [[ai-engineering-ch07-finetuning]] — wiki source.
