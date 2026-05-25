---
title: "ZeRO"
type: concept
tags: [optimization, memory, distributed-training]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# ZeRO — Zero Redundancy Optimizer

**Rajbhandari, Rasley, Ruwase & He (SC20, 2020) — *"Zero: Memory optimizations toward training trillion parameter models."*** Distributed-training memory-optimization scheme that partitions optimizer states, gradients, and parameters across data-parallel workers to eliminate replicated memory overhead. Foundational for training models that don't fit on a single GPU.

In [[2408.08849-ecg-chat|ECG-Chat]]: used to fit **[[Vicuna13B|Vicuna-13B]] + [[ECGEncoder|ECG encoder]] + projector + [[lora]] adapters** into the 32GB-per-GPU memory budget of an **8×V100** training cluster. Without ZeRO, the 13B-scale instruction-tuning stage would not fit on V100 hardware.

## Connections
- [[2408.08849-ecg-chat]] — practical user; V100-budget training.
- [[Vicuna13B]] / [[lora]] — what ZeRO enables on the constrained hardware.
- [[flashattention]] — the other major memory-reduction primitive for Transformer training.
