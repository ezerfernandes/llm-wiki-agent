---
title: "Nucleus Sampling (Top-p)"
type: concept
tags: [llm, decoding, generation, sampling, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Nucleus Sampling (Top-p)

A sampling-based decoding strategy that **limits token sampling to the smallest set of tokens whose cumulative probability mass reaches p** (Holtzman et al. 2020), introducing controlled diversity ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). One of the three sampling knobs alongside **temperature** (scales logits before softmax) and **top-k** (restricts to the k highest-probability tokens).

Sampling adds minimal compute overhead vs [[GreedyDecoding|greedy decoding]] (which is fast but repetitive and cannot recover from early mistakes) but requires careful parameter tuning to balance quality and coherence — unlike [[BeamSearch|beam search]], which multiplies compute by the beam width (~5× at width 5). The decoding strategy is a per-token-latency and output-quality lever in [[LLMServing|LLM serving]].

## Connections

- [[GreedyDecoding]] / [[BeamSearch]] — the other decoding strategies on the quality-diversity-latency spectrum.
- [[Autoregressive]] / [[LLMServing]] — the generation regime these strategies select tokens within.
- [[TPOT]] — decoding strategy affects per-token latency.
- [[mlsysbook-ch13-model-serving]] — source.
