---
title: "Inner Product of Functions"
type: concept
tags: [analytic-geometry, functional-analysis, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Inner Product of Functions

The [[InnerProduct]] generalizes from finite vectors to **functions** by replacing the finite sum with an integral ([[mml-ch03-analytic-geometry|MML Ch 3]] §3.7). A finite vector $\mathbf{x}\in\mathbb{R}^n$ is a function with $n$ values; allowing countably or uncountably infinitely many "entries" turns $\sum_i x_iy_i$ into $\int u(x)v(x)\,dx$.

For functions $u,v:\mathbb{R}\to\mathbb{R}$ ([[mml-book]] Eq. 3.37):

$$\langle u,v\rangle := \int_a^b u(x)\,v(x)\,dx, \qquad a,b<\infty.$$

As with the usual inner product, this defines **norms** ($\|u\|=\sqrt{\langle u,u\rangle}$) and **[[Orthogonality|orthogonality]]**: if $\langle u,v\rangle=0$ the functions $u$ and $v$ are *orthogonal functions*.

## Caveats (functional analysis)

Making this precise requires measures and the definition of integrals, leading to the notion of a **Hilbert space**. Unlike finite-dimensional inner products, **inner products of functions may diverge** (have infinite value). The book defers these details to real/functional analysis ([[mml-book]] p. 81).

## Example: sin ⊥ cos

For $u=\sin(x)$, $v=\cos(x)$, the integrand $f(x)=\sin(x)\cos(x)$ is **odd** ($f(-x)=-f(x)$), so $\int_{-\pi}^{\pi}\sin(x)\cos(x)\,dx=0$ — sine and cosine are orthogonal functions ([[mml-book]] Example 3.9, Fig. 3.8).

## Fourier series

The collection $\{1,\cos(x),\cos(2x),\cos(3x),\ldots\}$ is **orthogonal** when integrated over $[-\pi,\pi]$ ([[mml-book]] Eq. 3.38). It spans a large subspace of the even, periodic functions, and **projecting functions onto this orthogonal subspace is the fundamental idea behind Fourier series** — i.e. [[OrthogonalProjection|orthogonal projection]] in an infinite-dimensional function space. (§6.4.6 covers a second unconventional inner product: the inner product of random variables.)

## ML uses

- **Gaussian processes / RKHS** — kernels are inner products in (possibly infinite-dim) function spaces; the [[KernelTrick]] computes them implicitly.
- **Fourier / spectral methods** — feature representations and positional encodings.
- **Functional data analysis** — treating curves as vectors in a function space.

## Connections

- [[mml-ch03-analytic-geometry]] — §3.7 canonical reference (Eq. 3.37).
- [[InnerProduct]] — the finite-dimensional analogue this generalizes.
- [[Orthogonality]] — orthogonal functions = zero integral inner product.
- [[OrthogonalProjection]] — projecting onto orthogonal function subspaces = Fourier series.
- [[KernelTrick]] — inner products in infinite-dimensional feature spaces.
