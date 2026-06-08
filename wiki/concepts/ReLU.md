---
title: "ReLU"
type: concept
tags: [activation-function, neural-networks, foundational]
sources: [madewithml-baselines, d2l-multilayer-perceptrons, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# ReLU

Rectified Linear Unit: $\operatorname{ReLU}(x) = \max(0, x)$. Default [[ActivationFunction|activation]] for hidden layers in modern deep networks. Cheap, non-saturating for positive inputs, and one of the key empirical innovations behind the 2010s deep-learning revival ([[NairHinton2010|Nair & Hinton 2010]]; [[d2l-multilayer-perceptrons]] §ReLU Function).

## Derivative

$\operatorname{ReLU}'(x) = \mathbb{1}\{x>0\}$ — exactly 0 or 1. The discontinuity at $x=0$ is handled by convention (left-derivative = 0); inputs landing *exactly* on 0 have measure zero in practice.

## Why ReLU is the default

- **No saturation for $x>0$** → gradient just passes through; [[VanishingGradient|vanishing gradients]] are mitigated relative to [[Sigmoid|sigmoid]] / [[Tanh|tanh]].
- **Cheap** — one comparison, no exponentials.
- **Sparse activation** — half the units have zero output and zero gradient on a typical batch; that sparsity helps regularization and interpretability.
- **Composes with [[HeInitialization|He init]]** for stable variance through deep stacks.

## Variants

- **Leaky ReLU** $\max(0,x) + \alpha\min(0,x)$ with $\alpha \approx 0.01$ — small gradient for negatives.
- **pReLU** ([[KaimingHe|He]] et al. 2015) — same shape but $\alpha$ is *learned*.
- **GELU** $x\Phi(x)$ — smooth ReLU-ish curve; default in [[Transformer]]s.
- **Swish / SiLU** $x\sigma(\beta x)$ — smooth, non-monotonic; common in CV / RL.

## D2L's framing

> "The reason for using ReLU is that its derivatives are particularly well behaved: either they vanish or they just let the argument through. This makes optimization better behaved and it mitigated the well-documented problem of vanishing gradients that plagued previous versions of neural networks."

## Failure modes

- **Dying ReLU**: a unit can land in the $x<0$ regime *permanently* if a large gradient drives its pre-activation negative across all inputs — gradient is then always zero. Mitigated by Leaky / pReLU or careful learning rates. See [[DyingReLU]] for the dedicated treatment (10–40% of neurons can die per [[mlsysbook-ch05-neural-computation]]).

## Systems view (mlsysbook)

[[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]] frames ReLU's dominance as a hardware decision, not just a gradient one: the **[[TransistorTax|transistor tax]]** — ReLU = ~50 transistors / 1 cycle vs sigmoid's ~2,500 transistors / 20–40 cycles (~50×) — makes ReLU a density optimization that packs orders of magnitude more neurons into the same area/power budget, with ~5–10× faster activation per element.

## Connections

- [[d2l-multilayer-perceptrons]] — §ReLU Function (canonical reference).
- [[ActivationFunction]] — parent concept.
- [[Sigmoid]] / [[Tanh]] — the older saturating activations ReLU displaced.
- [[VanishingGradient]] — the problem ReLU mitigates.
- [[HeInitialization]] — the matched initialization scheme.
- [[NeuralNetwork]] / [[MultilayerPerceptron]] — where ReLU lives.
- [[Dropout]] — composed after ReLU in standard MLP layouts.
- [[TransistorTax]] / [[DyingReLU]] — the hardware-cost framing and failure mode (mlsysbook).
- [[mlsysbook-ch05-neural-computation]] — systems treatment of activation choice as a silicon decision.
