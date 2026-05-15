---
title: "Hazy Research"
type: entity
tags: [lab, university, systems]
sources: [2205.14135-flashattention]
last_updated: 2026-05-10
---

# Hazy Research

Christopher Ré's research group at [[StanfordUniversity]]. Focus on **systems and algorithms for machine learning** — historically weak supervision (Snorkel), now efficient sequence modeling (FlashAttention, state-space models, Mamba).

## Tracked contributions
- **[[2205.14135-flashattention]]** (Dao, Fu, Ermon, Rudra & Ré, 2022) — IO-aware exact attention. Open-sourced at https://github.com/HazyResearch/flash-attention.

## Downstream work (not yet in this wiki)
- FlashAttention-2 / FlashAttention-3 — kernel-level improvements; default attention implementations across PyTorch SDPA, xformers, vLLM, TensorRT-LLM.
- Mamba and the broader state-space-model (SSM) line — alternative to attention for long-context sequence modeling.
- Together AI — Ré is a co-founder; ships open-weight LLM training/inference infrastructure built on Hazy Research's systems work.

## See also
- [[StanfordUniversity]]
- [[FlashAttention]]
