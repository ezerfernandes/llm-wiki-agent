---
title: "Dual Numbers"
type: concept
tags: [autodiff, frameworks, math]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Dual Numbers

**Dual numbers** are the mechanism behind [[ForwardModeAutodiff|forward-mode automatic differentiation]]: each value is augmented with its derivative, so every arithmetic operation is performed twice (once for the value, once for the derivative via the chain/product rule). Computing $f(x)=x^2\sin(x)$ at $x=2$ propagates the pair `(value, derivative)` through each step — `a=4.0, da=4.0` for $x^2$, `b=0.909, db=-0.416` for $\sin x$, combined by the product rule to `(3.636, 1.972)`.

This **2× per-input overhead** is acceptable for a single input but fatal for training: a model with $P$ parameters would need $P$ forward passes, which is why neural-network training universally uses [[ReverseModeAutodiff|reverse mode]] (one backward pass for all gradients). Forward mode / dual numbers keep niche uses with few inputs and many outputs (sensitivity analysis, feature importance).

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the differentiation problem; forward-mode mechanism.
- [[ForwardModeAutodiff]] — the mode dual numbers implement.
- [[ReverseModeAutodiff]] / [[AutomaticDifferentiation]] — the contrasting mode used for training.
- [[ChainRule]] — applied per operation.
