---
title: "Chain Rule"
type: concept
tags: [calculus, foundational]
sources: [mml-ch05-vector-calculus, mml-book, d2l-preliminaries, d2l-multilayer-perceptrons, d2l-appendix-mathematics, matrix-calculus-for-deep-learning]
last_updated: 2026-06-04
---

# Chain Rule

The derivative of a composition. For scalar functions $y = f(g(x))$ with $y = f(u)$ and $u = g(x)$:

$$\frac{dy}{dx} = \frac{dy}{du}\,\frac{du}{dx}.$$

Multivariate version ([[d2l-preliminaries]] §Calculus): if $y = f(\mathbf{u})$ with $\mathbf{u} = g(\mathbf{x})$, then

$$\nabla_\mathbf{x} y = \mathbf{A}\,\nabla_\mathbf{u} y,$$

where $\mathbf{A} \in \mathbb{R}^{n\times m}$ is the [[Jacobian]] $\partial\mathbf{u}/\partial\mathbf{x}$. Evaluating gradients of composed functions is therefore a **vector–matrix product** — which is why [[LinearAlgebra]] is structurally inseparable from deep learning.

## Why deep learning depends on it

> "Functions composed from differentiable functions are often themselves differentiable. […] This is one of the key reasons why linear algebra is such an integral building block in building deep learning systems."
> — [[d2l-preliminaries]] §Calculus

A neural network of depth $L$ is exactly a composition $f_L \circ f_{L-1} \circ \cdots \circ f_1$. Gradients of the loss with respect to layer-1 parameters require composing $L$ Jacobians — efficiently done by reverse-mode [[Backpropagation]] over the [[ComputationalGraph]].

## Three variants (Parr & Howard)

[[matrix-calculus-for-deep-learning|Parr & Howard]] decompose the chain rule into three forms:

1. **Single-variable** — $\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}$ for one dataflow path (e.g. $y=\sin(x^2)$).
2. **Single-variable total-derivative** — when a variable reaches the output along *multiple* paths, *sum* the contributions: $\frac{\partial f}{\partial x}=\sum_j\frac{\partial f}{\partial u_j}\frac{\partial u_j}{\partial x}$. The summation (not multiplication alone) is the key correction the naive rule misses.
3. **Vector chain rule** — $\frac{\partial\mathbf{f}(g(\mathbf{x}))}{\partial\mathbf{x}}=\frac{\partial\mathbf{f}}{\partial g}\frac{\partial g}{\partial\mathbf{x}}$, a product of [[Jacobian|Jacobians]] that "automatically takes into consideration the total derivative" while staying notationally simple. For element-wise inner functions it collapses to $\operatorname{diag}(\partial f_i/\partial g_i)\cdot(\partial\mathbf{g}/\partial\mathbf{x})$.

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.1.2 states the univariate rule $(g\circ f)'(x)=g'(f(x))f'(x)$ (Eq. 5.32, one of the four [[DifferentiationRules|differentiation rules]]); §5.2.1–5.2.2 generalize it to vectors as $\frac{\partial}{\partial\mathbf{x}}(g\circ f)=\frac{\partial g}{\partial f}\frac{\partial f}{\partial\mathbf{x}}$ (Eq. 5.48). MML's dimension-matching intuition (p. 148, flagged as *"only an intuition, not mathematically correct since the partial derivative is not a fraction"*): reading left-to-right, $\partial f$ sits in the "denominator" of the first factor and the "numerator" of the second, so it "cancels" — mirroring matrix-multiplication's neighboring-dimension rule.

**The chain rule is a matrix product — clean only with the row-vector gradient.** For $f$ of $x_1(s,t),x_2(s,t)$, MML writes $\frac{\mathrm{d}f}{\mathrm{d}(s,t)}=\frac{\partial f}{\partial\mathbf{x}}\frac{\partial\mathbf{x}}{\partial(s,t)}$ (Eq. 5.53) — a $1\times 2$ row vector times a $2\times 2$ [[Jacobian]]. MML §5.2.2 (p. 149): *"This compact way of writing the chain rule as a matrix multiplication only makes sense if the gradient is defined as a row vector. Otherwise, we will need to start transposing gradients."* This is the chapter's chief justification for the [[Gradient|row-vector convention]]. Worked composition: Example 5.10, $h(t)=f(g(t))$ with $f(\mathbf{x})=\exp(x_1x_2^2)$, $g(t)=[t\cos t, t\sin t]^\top$, gives $\frac{\mathrm{d}h}{\mathrm{d}t}=\frac{\partial f}{\partial\mathbf{x}}\frac{\partial\mathbf{x}}{\partial t}$ ($1\times 2$ times $2\times 1$).

**Chain rule at the heart of deep learning (§5.6).** A depth-$K$ net is the composition $\mathbf{y}=(f_K\circ\cdots\circ f_1)(\mathbf{x})$ (Eq. 5.111); the chain rule for $\frac{\partial L}{\partial\boldsymbol\theta_i}$ (Eqs. 5.115–5.118) reuses already-computed upstream partials, which is exactly [[Backpropagation|backprop]] = [[ReverseModeAutodiff|reverse-mode]] [[AutomaticDifferentiation|autodiff]] over the [[ComputationalGraph|computation graph]] (Eq. 5.145).

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.1.2 / §5.2.2 / §5.6 canonical reference.
- [[mml-book]] — umbrella source.
- [[DifferentiationRules]] — the chain rule is one of the four.
- [[d2l-preliminaries]] — multivariate version stated explicitly.
- [[derivatives]] / [[PartialDerivative]] / [[Gradient]] / [[Jacobian]] — operands.
- [[Backpropagation]] — algorithmic application across a computational graph.
- [[Autograd]] / [[ComputationalGraph]] — frameworks that automate it.
- [[matrix-calculus-for-deep-learning]] — single-variable / total-derivative / vector variants.
- [[HadamardProduct]] — element-wise case that diagonalizes the vector chain rule.
