---
title: "LoRA"
type: concept
tags: [stub, pft, adaptation]
sources: []
last_updated: 2026-05-15
---

# LoRA — Low-Rank Adaptation

*Stub — referenced by other wiki pages but not yet ingested as a primary source.*

Hu et al. (2022, ICLR) — Low-Rank Adaptation of Large Language Models. LoRA freezes the pretrained weight matrix $W_0$ and adds a trainable low-rank update $\Delta W = B A$ with $B\in\mathbb{R}^{d\times r}, A\in\mathbb{R}^{r\times k}, r\ll\min(d,k)$. Used in [[2605.12966-agentic-ai-to-agi]] (§3.2) as empirical evidence for the central thesis: *specialized adapters are significantly more data-efficient than monolithic fine-tunes* — a low-dimensional, task-specific projection captures most of the gain.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
