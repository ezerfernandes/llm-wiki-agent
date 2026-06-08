---
title: "Lottery Ticket Hypothesis (LTH)"
type: concept
tags: [model-compression, pruning, sparsity, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Lottery Ticket Hypothesis (LTH)

**The conjecture (Frankle & Carbin) that within a large randomly-initialized network there exist small, well-initialized sparse subnetworks ("winning tickets") that, trained in isolation, match the full model's accuracy.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], LTH reframes [[Pruning|pruning]] from a post-training compression step into an early-training *discovery* mechanism.

## How it's validated

Train to convergence → prune lowest-magnitude weights → **reset surviving weights to their original initialization** (not re-randomized) → repeat iteratively. The remaining subnetwork is the winning ticket. ResNet-18 subnets at 10–20% of original size reach 93.2% vs 94.1% full-model accuracy.

## Systems implication

If winning tickets exist at initialization, the memory and compute spent training the other 80–90% of parameters is pure overhead. This motivates research into detecting subnetworks *before* full training (sparse training). LTH also reinforces why [[Pruning|iterative pruning]] beats one-shot and underscores the importance of weight initialization.

## Connections

- [[Pruning]] — LTH is the theoretical lens on iterative magnitude pruning.
- [[Sparsity]] — winning tickets are sparse subnetworks.
- [[ModelCompression]] — challenges the assumption that model size is necessary for learning.
- [[mlsysbook-ch10-model-compression]] — source.
