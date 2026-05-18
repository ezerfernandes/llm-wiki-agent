---
title: "Beta Parameterization"
type: concept
tags: [test-time-scaling, search, hyperparameters, agentic-discovery]
sources: [2605.08083-autotts]
last_updated: 2026-05-15
---

# Beta Parameterization

Search-tractability mechanism introduced in [[2605.08083-autotts]]: every candidate TTS controller exposes **only one scalar** $\beta\in[0,1]$ and implements a deterministic map $\beta\to(\text{all internal hyperparameters})$. Without this constraint, explorer LLMs ([[claudecode|Claude Code]] in the AutoTTS loop) propose controllers with up to 10 free hyperparameters, leading the search to overfit $\mathcal{E}_{search}$ via brittle aggressive-pruning thresholds.

## Requirements

1. **Monotonicity**: larger $\beta$ ⇒ larger token budget. Budget-related parameters non-decreasing in $\beta$; stopping thresholds non-increasing in $\beta$.
2. **Conservative anchor**: at $\beta=1$, controller reluctant to terminate on shallow consensus, avoids overly aggressive pruning, approaches near-full use of the shared `max_branch=64` ceiling.
3. **Coverage**: varying $\beta$ traces a meaningful frontier from low-budget to near-full-budget regimes.
4. **Single-knob schedule**: all behavior-critical hyperparameters must be deterministic functions of $\beta$, computed once in `__init__` from a `_schedule(beta) -> dict` helper. No additional tunable knobs exposed to `eval.py` beyond $\beta$.
5. **Simple analytic forms** preferred (linear, sigmoid, clipped ramp); avoid piecewise logic with hand-placed breakpoints.

## Example Schedule (CMC, [[2605.08083-autotts]] App. D)

```
n_init        = max(2, round(2 + 6b))         # [2,8]
max_branch_use = min(64, round(4 + 60b))      # [4,64]
ema_alpha     = 0.70 − 0.40·b                 # [0.30, 0.70], NON-INCREASING
conf_thresh   = 0.85 + 0.12·b                 # [0.85, 0.97]
delta_slack   = 0.04 − 0.03·b                 # [0.01, 0.04]
trend_thresh  = 0.04 − 0.03·b                 # NON-INCREASING (more widening at high β)
abandon_patience = max(3, round(3 + 9·b))     # [3, 12]
```

## Ablation Evidence

[[2605.08083-autotts]] §5.4 / Table 3: removing beta parameterization (allowing controllers full hyperparameter freedom) drops held-out accuracy 53.1→49.0 *and* collapses token usage 575.5K→93.3K — the search converges on aggressive pruning thresholds that overfit $\mathcal{E}_{search}$ and fail to generalize. Search cost also rises ($39.9→$46.4) because over-parameterized controllers need more iterations to settle.

## Why It Generalizes

Beta parameterization is structurally analogous to *learning a controller family parametrized by a single budget knob*, similar in spirit to:
- Conditional computation networks where a single capacity dial controls all gating decisions.
- Temperature-controlled sampling: one scalar dial governs an entire downstream distribution.
- Pareto-front sweep methods in multi-objective optimization, where one scalarization weight is varied.

The mechanism is plausibly transferable to other agentic-algorithm-discovery domains where the explorer LLM tends to over-parameterize.

## Connections

- [[2605.08083-autotts]] — origin.
- [[AutoTTS]] — the framework this enables.
- [[ConfidenceMomentumController]] — concrete controller whose entire schedule is a `_schedule(beta)`.
- [[AgenticAlgorithmDiscovery]] — discipline for LLM-driven program search; beta parameterization is a generalizable constraint.
- [[ExecutionTraceFeedback]] — the *other* essential affordance for AutoTTS, ablated separately.
