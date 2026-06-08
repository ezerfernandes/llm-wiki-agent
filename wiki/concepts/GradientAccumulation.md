---
title: "Gradient Accumulation"
type: concept
tags: [training, memory, batch-size]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models, mlsysbook-ch08-model-training]
last_updated: 2026-06-05
---

# Gradient Accumulation

A training technique that **simulates a large batch size by accumulating gradients across multiple small forward+backward passes before updating the model weights**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Often, models are so large, and memory is so constrained, that only small batch sizes can be used. This can lead to unstable model weight updates. To address this, instead of updating the model weights after each batch, you can accumulate gradients across several batches and update the model weights once enough reliable gradients are accumulated. This technique is called gradient accumulation."

## How it works

For an effective batch size of `B` but a per-step batch size of `b` that fits in memory:
1. Run `B / b` forward+backward passes, each with batch size `b`.
2. **Sum** (or average) the gradients across these passes.
3. Update the model weights using the accumulated gradient.
4. Reset the accumulator and repeat.

The result is **mathematically equivalent** to a single forward+backward pass with batch size `B`, but the per-step memory cost is only that of batch size `b`.

## The trade-off

- **Memory**: drops to `b`-batch-size scale instead of `B`-batch-size scale.
- **Wall-clock time**: grows by `B/b` × the per-step time (extra forward+backward passes).
- **Convergence behavior**: identical to large-batch training (modulo BatchNorm-style stats, which need attention).

## When to use

- When the effective batch size you want is too large to fit in GPU memory.
- When [[BatchSize|small batches]] (<8) cause unstable updates ([[ChipHuyen|Huyen]]'s threshold in Ch 7).
- In **distributed training**, where gradient accumulation pairs naturally with all-reduce: accumulate locally, then reduce across devices.

## Historical note

Ch 7's footnote: *"I tried to find the first paper where gradient accumulation was introduced but couldn't. Its use in deep learning was mentioned as early as 2016 in 'Ako: Decentralised Deep Learning with Partial Gradient Exchange' (Watcharapichat et al., Proceedings of the Seventh ACM Symposium on Cloud Computing, 2016). The concept seems to come from distributed training, where gradients computed on different machines need to be accumulated and used to update the model's weights."*

## From [[mlsysbook-ch08-model-training|mlsysbook Ch 8 (Model Training)]]

Ch 8 frames gradient accumulation as a *cost* lever as much as a memory one: GPT-2 reaches effective batch 512 on **8 V100s** (micro-batch 16 × 4 accumulation steps) instead of **32 GPUs** — a 75% cluster-cost cut. The `no_sync()` context suppresses [[AllReduce]] on the first $k-1$ micro-batches so gradient sync fires once per effective batch (75% less communication). It's mathematically exact because gradients are additive; BERT-Large hit 99.5% of full-batch performance at effective batch 256 over 8 steps. Cost: ~8–15% wall-clock overhead from micro-batch serialization. **Convention gotcha**: when loss is divided by $k$ the LR needs no change; when gradients are summed without division the LR must drop $k\times$ — a common subtle bug.

## Connections

- [[mlsysbook-ch08-model-training]] — the cost/communication framing; `no_sync()` AllReduce reduction; loss-division convention gotcha.
- [[BatchSize]] — what gradient accumulation effectively scales.
- [[MemoryBottleneck]] — what gradient accumulation mitigates.
- [[Backpropagation]] — the per-step operation being accumulated.
- [[Gradient]] / [[OptimizerState]] — what's being accumulated.
- [[DistributedTraining]] — the historical context.
- [[ai-engineering-ch07-finetuning]] — primary source.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* configures `per_device_train_batch_size=2` + `gradient_accumulation_steps=4` for both the SFT and DPO QLoRA stages — an **effective batch size of 8** assembled from four per-device micro-batches of 2. The pairing is the chapter's standard memory-vs-stability lever for fitting [[TinyLlama|TinyLlama-1.1B]] training onto a free Google Colab Tesla T4.
