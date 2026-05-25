---
title: "Sparse Upcycling"
type: concept
tags: [model-merging, moe, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Sparse Upcycling

**Turning a dense pre-trained model into a [[MixtureOfExperts|Mixture-of-Experts]] model via [[LayerStacking|layer stacking]] + routing.** Introduced by [[Komatsuzaki2022SparseUpcycling|Komatsuzaki et al. (2022)]] — *"Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints."* Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Rather than training an MoE from scratch, you take a pre-trained model and make multiple copies of certain layers or modules. A router is then added to send each input to the most suitable copy. You then further train the merged model along with the router to refine their performance."

## The recipe (Ch 7)

1. **Start with a pre-trained dense model** — any transformer-based checkpoint.
2. **Replicate certain layers** N times (typically the FFN layers; attention layers usually stay shared).
3. **Insert a router** that sends each input to the most suitable copy of the replicated layer.
4. **Further train** the merged model + router to refine performance.

## Why this is interesting

- **Reuses the dense pre-training compute.** MoEs typically need to be trained from scratch — expensive. Sparse upcycling lets you reuse a dense checkpoint you already have (or downloaded).
- **Komatsuzaki et al. showed sparse-upcycled MoEs can outperform MoEs trained from scratch.** This is the killer empirical result — dense pre-training is a *better starting point* than random MoE init.
- **Bridges dense and sparse architectures.** Lets you have a dense base model and an MoE descendant for the same task family, sharing pre-training compute.

## Connection to [[MixtureOfAgents]]

[[TogetherAI]]'s [[MixtureOfAgents]] (Wang et al., 2024) is morally an extension of sparse upcycling at the model level: take six weaker open-source models, combine them via layer stacking + routing, and produce a system that approaches [[gpt54|GPT-4o]] on some benchmarks. The "experts" here are entire models, not just layers.

## Connections

- [[ModelMerging]] / [[LayerStacking]] — parent operations.
- [[MixtureOfExperts]] — what sparse upcycling produces.
- [[MixtureOfAgents]] — the model-level sibling.
- [[Komatsuzaki2022SparseUpcycling]] — the foundational paper.
- [[ai-engineering-ch07-finetuning]] — primary source.
