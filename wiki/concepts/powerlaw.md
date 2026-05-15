---
title: "Power Law"
type: concept
tags: [scaling, mathematics, foundational]
sources: [2001.08361-scaling-laws]
last_updated: 2026-05-10
---

# Power Law

A **power-law** relationship between two quantities has the form $y = A x^{-\alpha}$ — a straight line on a log-log plot with slope $-\alpha$. Power laws appear in physics (critical phenomena), economics (Zipf's law), random forest density estimation, and — most importantly for this wiki — in **[[ScalingLaws]] for neural language models**.

## In the wiki

[[2001.08361-scaling-laws]] establishes that the cross-entropy test loss of an autoregressive Transformer LM is a power law in non-embedding parameter count $N$, dataset size $D$, training compute $C$, and the critical batch size $B_\mathrm{crit}$. The same paper notes that power-law exponents have a rough interpretation as **the inverse of the number of relevant features in the data** ([THK18]) and can also arise from random forest density estimation ([Was06, Bia12]).

## Why power laws are useful

- **Extrapolatable.** Linear on log-log axes, so a fit over 3–4 orders of magnitude can be projected forward with quantified uncertainty.
- **Composable.** Joint scaling laws can be derived by combining univariate power laws under limit constraints (e.g. the joint $L(N, D)$ ansatz of [[2001.08361-scaling-laws]] requires the loss to reduce to $L(N)$ at $D \to \infty$ and $L(D)$ at $N \to \infty$).
- **Architecture-agnostic.** [[2001.08361-scaling-laws]] finds the same exponent $\alpha_N$ across a wide range of Transformer shapes, suggesting the exponent captures something universal about the data + objective, not the model.

## Limits

- Power laws **must eventually break**. Test loss cannot fall below the entropy of natural language; the [[2001.08361-scaling-laws]] paper estimates the break point at $C^* \sim 10^4$ PF-days, $L^* \sim 1.7$ nats/token.
- Power-law constants depend on tokenizer/vocab choices ([[2001.08361-scaling-laws]] §4.1): only the exponents are meaningful.

## See also
- [[ScalingLaws]]
- [[ComputeEfficientTraining]]
