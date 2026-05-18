---
title: "Gated Delta-Rule Learning"
type: concept
tags: [concept, online-learning, associative-memory, hebbian]
sources: [2605.12357-delta-mem]
last_updated: 2026-05-15
---

# Gated Delta-Rule Learning

Update rule for the [[onlinestateofassociativememory|OSAM]] matrix used in [[deltamem|δ-mem]]:

$$\mathbf{S}_t = \mathrm{Diag}(\boldsymbol{\lambda}_t)\mathbf{S}_{t-1} + \mathrm{Diag}(\boldsymbol{\beta}_t)(\mathbf{v}_t^m - \mathbf{S}_{t-1}\mathbf{k}_t^m)(\mathbf{k}_t^m)^\top$$

## Interpretation
Expanding:

$$\mathbf{S}_t = \underbrace{\mathrm{Diag}(\boldsymbol{\lambda}_t)\mathbf{S}_{t-1}}_{\text{retain}} - \underbrace{\mathrm{Diag}(\boldsymbol{\beta}_t)\mathbf{S}_{t-1}\mathbf{k}_t^m(\mathbf{k}_t^m)^\top}_{\text{erase old prediction}} + \underbrace{\mathrm{Diag}(\boldsymbol{\beta}_t)\mathbf{v}_t^m(\mathbf{k}_t^m)^\top}_{\text{write new value}}$$

Three roles: retain previous state, erase the existing prediction along the current key direction, write the new value in the same direction. Updates are **residual** — well-learned associations induce negligible change, predictive errors dominate.

## Connection to SGD
Without the gates, this is the gradient step on the online regression loss $\mathcal{L}_t(\mathbf{S}) = \frac{1}{2}\|\mathbf{S}\mathbf{k}_t - \mathbf{v}_t\|^2$ with step size $\beta_t$ — i.e. classical delta rule (Widrow-Hoff). The Qwen-Next-inspired forget gate $\boldsymbol{\lambda}_t \in \mathbb{R}^r$ adds **dimension-wise** retention control: some dimensions of the state can preserve long-range history while others actively rewrite.

## Gate parametrization
$\boldsymbol{\beta}_t = \sigma(\mathbf{W}_\beta \mathbf{x}_t + \mathbf{b})$ and $\boldsymbol{\lambda}_t = \mathbf{1} - \boldsymbol{\beta}_t$ — sigmoidal, conditioned on the current hidden state.

## Why this and not a vanilla outer-product Hebbian
Pure Hebbian $\mathbf{S}_t = \mathbf{S}_{t-1} + \mathbf{v}_t \mathbf{k}_t^\top$ accumulates interference unboundedly. The delta-rule's *residual* form (subtract the existing prediction first) prevents repeated keys from saturating the state.

## Lineage
Inspired by the **Qwen-Next retention design** (Yang et al. 2025) for long-range state evolution.
