---
title: "Successive Halving"
type: concept
tags: [hpo, multi-fidelity, scheduler]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Successive Halving

A [[MultiFidelityOptimization|multi-fidelity]] HPO scheduler that trains many configurations for a small budget, keeps the top fraction, gives them a larger budget, and iterates — concentrating compute on configurations whose learning curves look promising ([[Jamieson]] & Talwalkar 2016; [[Karnin]] et al. 2013). Implemented in [[d2l-hyperparameter-optimization]] §sh-intro as `SuccessiveHalvingScheduler(HPOScheduler)`.

## Algorithm

Inputs: minimum budget $r_\text{min}$, maximum budget $r_\text{max}$, halving constant $\eta\in\{2, 3, \dots\}$. Assume $r_\text{max} = r_\text{min}\eta^K$, so $N=\eta^K$ initial configs.

1. Sample $N$ configurations from the prior. Train each for $r_\text{min}$ epochs (rung 0).
2. Sort by validation error; keep the top $1/\eta$ fraction ($\eta^{K-1}$ configs). Train each for $r_\text{min}\eta$ epochs (rung 1).
3. Iterate. At rung $i$, $\eta^{K-i}$ configs train for $r_\text{min}\eta^i$ epochs.
4. Exactly one configuration reaches the full budget $r_\text{max}$.
5. Start a new round with fresh random configs and repeat until the global budget is spent.

The rung set is $\mathcal{R} = \{r_\text{min}, r_\text{min}\eta, r_\text{min}\eta^2, \dots, r_\text{max}\}$. D2L's running example uses $r_\text{min}=2$, $\eta=2$, $r_\text{max}=10$ → rungs $\{2, 4, 8, 10\}$.

## Two failure modes (and their fixes)

1. **Hyperparameter choice — $n$ vs $r$ trade-off.** $r_\text{min}$ too small and the early-stopping decisions are noisy; $r_\text{min}$ too large and most of the compute is wasted before halving kicks in. Fixed by **[[Hyperband]]** (Li et al. 2018), which hedges over multiple $(n, r)$ configurations.
2. **Synchronization barrier in distributed settings.** Workers must finish *all* configs on the current rung before promoting; stragglers force idle workers ([[d2l-hyperparameter-optimization]] §sh-async). Fixed by **[[ASHA]]** (Li et al. 2018), which promotes the moment $\eta$ observations exist on a rung.

## Connections

- [[d2l-hyperparameter-optimization]] — D2L's canonical reference; `SuccessiveHalvingScheduler`.
- [[Jamieson]] — co-author of *Non-stochastic Best Arm Identification and Hyperparameter Optimization* (2016).
- [[Karnin]] — co-author of *Almost Optimal Exploration in Multi-Armed Bandits* (2013) — the bandit framing of SH.
- [[Hyperband]] — wraps SH in an outer bracket hedging over $(n, r)$.
- [[ASHA]] — the asynchronous version that eliminates SH's synchronization barrier.
- [[MultiFidelityOptimization]] — the umbrella concept SH belongs to.
- [[HyperparameterOptimization]] — parent concept.
- [[LishaLi]] / [[SyneTune]] — production implementations.
