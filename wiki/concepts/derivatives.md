---
title: "Derivatives"
type: concept
tags: [calculus, foundational]
sources: [mml-ch05-vector-calculus, d2l-preliminaries, mml-book]
last_updated: 2026-06-04
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

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.1 Def 5.2 (Eq. 5.4) defines the derivative as the limit of the [[DifferenceQuotient|difference quotient]] $\frac{\mathrm{d}f}{\mathrm{d}x}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$ — the secant rotating into the tangent — and notes it *"points in the direction of steepest ascent."* MML Example 5.2 derives $\frac{\mathrm{d}}{\mathrm{d}x}x^n=nx^{n-1}$ directly from this limit (binomial expansion; the $x^n$ term cancels, $i\geq 2$ terms vanish). The univariate [[DifferentiationRules|product/quotient/sum/chain rules]] follow (§5.1.2); the multivariate generalization is the [[PartialDerivative|partial derivative]] (§5.2).

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.1 Def 5.2 canonical reference.
- [[DifferenceQuotient]] — the limit that defines the derivative.
- [[DifferentiationRules]] — composition rules.
- [[d2l-preliminaries]] — definition + standard rules.
- [[mml-book]] — umbrella source.
- [[Calculus]] — parent topic.
- [[PartialDerivative]] / [[Gradient]] / [[Jacobian]] / [[Hessian]] — multivariate generalizations.
- [[ChainRule]] — composition.
- [[Autograd]] / [[Backpropagation]] — algorithmic computation.
