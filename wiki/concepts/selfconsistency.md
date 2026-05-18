---
title: "Self-Consistency"
type: concept
tags: [ml-method, reasoning, inference, test-time-scaling]
sources: [2605.08083-autotts]
last_updated: 2026-05-15
---

# Self-Consistency

Sample $N$ independent chain-of-thought trajectories from a base model and return the **majority-voted** final answer (Wang et al., arXiv 2203.11171, 2022). Often referred to as **SC@N** (e.g. SC@64 = 64 samples).

The canonical [[parallelreasoning|parallel reasoning]] / [[bestofn|best-of-N]] baseline in the [[testtimescaling|TTS]] literature, and the "fixed full-budget corner" of the [[WidthDepthSearch|width–depth control space]] in [[2605.08083-autotts|AutoTTS]]. Used as the dominant handcrafted baseline in AutoTTS: at $\beta=0.5$ the discovered [[ConfidenceMomentumController|CMC]] reduces tokens by ~69.5% at matched accuracy.

A **Beta-majority confidence** variant — used as the underlying confidence signal in many adaptive TTS controllers including [[ConfidenceMomentumController|CMC]], IBC, SCR, DGCC — derives a smoother confidence estimate from the (top1, top2) vote-count pair than raw plurality.

## Connections

- [[2605.08083-autotts]] — the AutoTTS paper's primary baseline.
- [[testtimescaling|Test-Time Scaling]] — parent concept.
- [[parallelreasoning|Parallel Reasoning]] — the width-axis pattern SC instantiates.
- [[bestofn|Best-of-N]] — SC = BoN + majority vote.
- [[chainofthought|Chain-of-Thought]] — the per-branch reasoning substrate.
- [[ConfidenceMomentumController|CMC]] — uses Beta-majority confidence over pool of SC-style branches.
- [[WidthDepthSearch]] — places SC@64 as the "fixed full-budget corner."
