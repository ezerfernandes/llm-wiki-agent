---
title: "Derivatives"
type: concept
tags: [calculus, foundational]
sources: [d2l-preliminaries, mml-book]
last_updated: 2026-05-16
---

# Derivatives

The instantaneous rate of change of a function. For $f:\mathbb{R}\to\mathbb{R}$:

$$f'(x) = \lim_{h\to 0}\,\frac{f(x+h) - f(x)}{h}.$$

When $f'(x)$ exists, $f$ is **differentiable at $x$**; if so for every $x$ in an interval, $f$ is differentiable on that interval ([[d2l-preliminaries]] §Calculus).

Equivalent notational conventions: $f'(x) = y' = \frac{dy}{dx} = \frac{df}{dx} = \frac{d}{dx}f(x) = Df(x) = D_xf(x)$.

## Standard derivatives

$$\frac{d}{dx}\,C = 0;\quad \frac{d}{dx}\,x^n = n x^{n-1};\quad \frac{d}{dx}\,e^x = e^x;\quad \frac{d}{dx}\,\ln x = x^{-1}.$$

## Composition rules

For differentiable $f, g$ and constant $C$:

- **Constant multiple**: $\frac{d}{dx}[C f] = C f'$.
- **Sum**: $\frac{d}{dx}[f + g] = f' + g'$.
- **Product**: $\frac{d}{dx}[fg] = f g' + g f'$.
- **Quotient**: $\frac{d}{dx}[f/g] = (g f' - f g') / g^2$.
- **[[ChainRule|Chain rule]]**: $(g\circ f)' = g'(f)\,f'$.

## Why ML cares

- **Loss derivatives** tell us how to nudge each parameter to lower the loss — the engine of every gradient-based training algorithm.
- **Non-differentiable losses** (accuracy, AUC, BLEU) are optimized via differentiable **surrogates** (cross-entropy, smoothed metrics).
- Multivariate generalization → [[PartialDerivative]], [[Gradient]], [[Jacobian]], [[Hessian]].

## Connections

- [[d2l-preliminaries]] — definition + standard rules.
- [[mml-book]] — Ch 5 canonical reference.
- [[Calculus]] — parent topic.
- [[PartialDerivative]] / [[Gradient]] / [[Jacobian]] / [[Hessian]] — multivariate generalizations.
- [[ChainRule]] — composition.
- [[Autograd]] / [[Backpropagation]] — algorithmic computation.
