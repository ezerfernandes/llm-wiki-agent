---
title: "DAPO"
type: concept
tags: [rl-algorithm, grpo-variant, policy-optimization]
sources: [dspy-tutorial-rl-papillon, dspy-rl-multihop-tutorial]
last_updated: 2026-05-24
---

# DAPO

**D**ecoupled **c**lip **a**nd dynamic sampling **P**olicy **O**ptimization. A [[grpo|GRPO]] variant that decouples the policy-ratio clip from the token-level loss and adds dynamic sampling. Used in the wild via Hugging Face TRL / [[Arbor]] as the `loss_type="dapo"` setting that both [[dspy-tutorial-rl-papillon|the DSPy `rl_papillon` tutorial]] (training [[PAPILLON]] on [[PUPA]]) and [[dspy-rl-multihop-tutorial|the DSPy `rl_multihop` tutorial]] (training [[ResearchHop]] on [[HoVer]]) use by default when training with [[ArborGRPO]].

The wiki holds DAPO as a **named GRPO-family loss type** that ArborGRPO surfaces; full algorithmic detail is not on record here — see the source paper (DAPO, ByteDance Seed 2025) and the TRL implementation.

## Why it matters in this wiki

- It is the **actual loss function** of both [[grpo|GRPO]] training receipts the wiki has on multi-module DSPy programs.
- Both tutorials set `beta=0.00` (no [[KLPenalty|KL]] anchor) — **DAPO's clip behavior is the only thing keeping the policy from drifting arbitrarily** across the 500-step ([[dspy-tutorial-rl-papillon|PAPILLON]]) and 1000-step ([[dspy-rl-multihop-tutorial|rl_multihop]]) runs.
- The same `loss_type="dapo"` + `beta=0.00` + LoRA(r=8, α=16, dropout=0.05) recipe recurs across two independent task families — **evidence DAPO is the operational default [[ArborGRPO]] is shipping with**.

## Connections

- [[grpo|GRPO]] — the parent algorithm family; DAPO modifies the clip + sampling rule.
- [[ArborGRPO]] — exposes `loss_type="dapo"`.
- [[dspy-tutorial-rl-papillon]] — the wiki's first receipt of DAPO in action (PAPILLON + LLM-judge reward).
- [[dspy-rl-multihop-tutorial]] — the wiki's second DAPO receipt (`ResearchHop` over HoVer + deterministic recall reward).
- [[PPO]] — the original clip-objective ancestor of both GRPO and DAPO.
- [[ClippedSurrogateObjective]] — the structural component DAPO modifies.
