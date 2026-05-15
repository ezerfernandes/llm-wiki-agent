---
title: "Compute-Efficient Training"
type: concept
tags: [scaling, pretraining, training-recipe]
sources: [2001.08361-scaling-laws]
last_updated: 2026-05-10
---

# Compute-Efficient Training

The training regime that **minimizes test loss for a fixed compute budget** $C$, characterized by [[2001.08361-scaling-laws]] (Kaplan et al., 2020). The headline finding inverts prior practice: under [[ScalingLaws]] for Transformer LMs, the compute-optimal recipe trains **very large models on a relatively modest amount of data and stops significantly before convergence**.

## The allocation

Within a fixed compute budget $C$:
$$N \propto C^{0.73}, \quad B \propto C^{0.24}, \quad S \propto C^{0.03}, \quad D = B \cdot S$$

Concretely, every 10× increase in compute should be spent on:
- ~5× larger non-embedding parameter count $N$,
- ~2× larger batch size $B$ (scaled via the critical batch size $B_\mathrm{crit}(L)$),
- only ~1.07× more serial training steps $S$,
- ~1.86× more total data $D$ (= B × S).

The exponent on $S$ is so small that the empirical results are consistent with $S \propto C^0$ — the **number of serial training steps is roughly compute-invariant**. Data growth is also slow: $D \sim C^{0.27}$.

## Why this is counterintuitive

The dominant prior practice was to train smaller models to convergence. Under [[ScalingLaws]], this is **strictly suboptimal**: a smaller model trained to convergence reaches a higher final loss than a larger model trained for the same compute but stopped early. The critical insight is that **sample efficiency rises with model size** — large models reach a target loss in fewer steps and on fewer tokens — so the compute spent on extra training steps of a small model is better spent making the model larger.

## Critical batch size

The optimal batch size for compute efficiency is the **critical batch size** $B_\mathrm{crit}(L) \approx B_*/L^{1/\alpha_B}$ ([[2001.08361-scaling-laws]] §5.1, following [MKAT18]):

- Above $B_\mathrm{crit}$: diminishing returns from larger batches (compute is wasted).
- Below $B_\mathrm{crit}$: training takes more wall-clock steps than necessary.
- Training **at** $B_\mathrm{crit}$ uses $2 S_\min$ steps and $2 E_\min$ data examples for any target loss.
- $B_\mathrm{crit}$ depends only on the achieved loss, **not** on model size.

## Caveats from the source paper

- The optimal-allocation exponents are derived in the range studied (up to ~1.5B params, ~23B tokens, ~$10^4$ PF-days). They are not guaranteed beyond.
- The derivation predicts a contradiction at $C^* \sim 10^4$ PF-days where the compute-bound and data-bound laws intersect; the scaling laws (and therefore this allocation) must break before that point.
- The exponent $p_N = 0.73$ has since been challenged — "Chinchilla" follow-on work argues data and parameters should scale closer to 1:1, not at the $N \gg D$ ratio recommended here. That revision is **not present** in [[2001.08361-scaling-laws]] (this 2020 paper) and is a known live tension in the field.

## See also
- [[ScalingLaws]]
- [[PowerLaw]]
- [[Pretraining]]
- [[Transformer]]
