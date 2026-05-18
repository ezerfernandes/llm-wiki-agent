---
title: "Dive into Deep Learning — Notation"
type: source
tags: [textbook, d2l, notation, math]
date: 2026-05-16
source_file: raw/d2l-en/chapter_notation/
---

# Dive into Deep Learning — Notation

## Summary

Short front-matter chapter of *Dive into Deep Learning* (D2L) by [[AstonZhang]], [[ZacharyLipton]], [[MuLi]] & [[AlexanderSmola]] that fixes the book's mathematical symbol conventions across five domains: numerical objects (scalars / vectors / matrices / tensors), set theory, functions and operators, calculus, and probability / information theory. The chapter is reference material — it does not introduce concepts, only the typographic conventions used to denote them in every later chapter. The convention follows the standard ML-textbook style: lowercase italics for scalars, lowercase boldface for vectors, uppercase boldface for matrices, sans-serif uppercase for general tensors, calligraphic uppercase for sets, blackboard-bold for number systems. Notational "rule of thumb": indefinite-article entries ("$x$: a scalar") are placeholders for a family of symbols; definite-article entries ("$\mathbb{Z}$: the set of integers") are reserved literals.

## Key Claims

- **Typographic rule of thumb**: indefinite article in the gloss ("a scalar", "a vector") means the symbol is a *placeholder* — any similarly-formatted symbol denotes the same kind of object. Definite article ("the set of integers") means the symbol is *reserved*.

- **Numerical objects** (font discriminates rank):
  - $x$ scalar (lowercase italic) · $\mathbf{x}$ vector (lowercase bold) · $\mathbf{X}$ matrix (uppercase bold) · $\mathsf{X}$ general [[Tensor]] (sans-serif uppercase).
  - $\mathbf{I}$ identity matrix (square, $1$ on diagonal, $0$ elsewhere).
  - Indexing: $x_i \equiv [\mathbf{x}]_i$ for vector entries; $x_{ij} \equiv x_{i,j} \equiv [\mathbf{X}]_{ij} \equiv [\mathbf{X}]_{i,j}$ for matrix entries at row $i$, column $j$.

- **Set theory** (blackboard-bold for number systems, calligraphic for generic sets):
  - $\mathcal{X}$ a set · $\mathbb{Z}$ integers · $\mathbb{Z}^+$ positive integers · $\mathbb{R}$ reals · $\mathbb{R}^n$ real $n$-vectors · $\mathbb{R}^{a\times b}$ real $a\times b$ matrices.
  - $|\mathcal{X}|$ cardinality · $\cup$ union · $\cap$ intersection · $\setminus$ set difference.

- **Functions and operators**:
  - $f(\cdot)$ a function · $\log$ natural log (base $e$) · $\log_2$ base-2 log · $\exp$ exponential.
  - $\mathbf{1}(\cdot)$ indicator function; $\mathbf{1}_{\mathcal{X}}(z)$ set-membership indicator.
  - $(\cdot)^\top$ transpose · $\mathbf{X}^{-1}$ matrix inverse · $\odot$ Hadamard (elementwise) product · $[\cdot,\cdot]$ concatenation.
  - $\|\cdot\|_p$ $\ell_p$ [[Norm|norm]]; bare $\|\cdot\|$ defaults to $\ell_2$ · $\langle \mathbf{x},\mathbf{y}\rangle$ [[InnerProduct|inner / dot product]].
  - $\sum, \prod$ collection sum / product · $\stackrel{\textrm{def}}{=}$ definition.

- **Calculus** ([[MML-Book|MML]] uses similar but row-vector convention; D2L is silent on layout):
  - $\frac{dy}{dx}$ derivative · $\frac{\partial y}{\partial x}$ [[PartialDerivative|partial derivative]] · $\nabla_{\mathbf{x}} y$ [[Gradient|gradient]] of $y$ w.r.t. vector $\mathbf{x}$.
  - $\int_a^b f(x)\,dx$ definite integral · $\int f(x)\,dx$ indefinite integral.

- **Probability and information theory**:
  - $X$ random variable · $P$ probability distribution · $X \sim P$ "X follows P" · $P(X=x)$ point probability · $P(X\mid Y)$ conditional distribution · $p(\cdot)$ PDF associated with $P$.
  - ${E}[X]$ expectation · $X \perp Y$ independence · $X \perp Y \mid Z$ conditional independence.
  - $\sigma_X$ std dev · $\textrm{Var}(X)=\sigma^2_X$ variance · $\textrm{Cov}(X,Y)$ covariance · $\rho(X,Y) = \textrm{Cov}(X,Y)/(\sigma_X \sigma_Y)$ Pearson correlation.
  - $H(X)$ entropy · $D_{\textrm{KL}}(P\|Q)$ KL-divergence (relative entropy from $Q$ to $P$).

- **Notational silences**: D2L's notation chapter does not commit to a gradient layout convention (row-vector vs column-vector), does not introduce expectation w.r.t. a specific distribution ($\mathbb{E}_{x\sim P}[\cdot]$), and does not define the Jacobian, Hessian, or trace symbols here — those are presumably introduced just-in-time in later chapters per the [[JustInTimeTeaching]] pedagogical principle.

## Key Quotes

> "As a general rule of thumb, the indefinite article 'a' often indicates that the symbol is a placeholder and that similarly formatted symbols can denote other objects of the same type. For example, '$x$: a scalar' means that lowercased letters generally represent scalar values, but '$\mathbb{Z}$: the set of integers' refers specifically to the symbol $\mathbb{Z}$." — the meta-convention that governs every other entry in the chapter.

> "$\|\cdot\|$: $\ell_2$ norm" — D2L's default norm is $\ell_2$; an explicit subscript ($\|\cdot\|_p$) is required for any other $\ell_p$.

## Connections

- [[d2l-preface]] — preceding chapter; same authors, same book.
- [[d2l-installation]] — sibling front-matter chapter.
- [[AstonZhang]] / [[ZacharyLipton]] / [[MuLi]] / [[AlexanderSmola]] — co-authors.
- [[Tensor]] — D2L's $\mathsf{X}$ symbol matches this concept's "multidimensional array generalizing scalars / vectors / matrices" definition.
- [[Gradient]] — $\nabla_{\mathbf{x}} y$ here is the symbol D2L uses for the same object [[mml-book]] defines (with a different row-vector layout).
- [[Norm]] — $\|\cdot\|_p$ / $\|\cdot\|$ notation; D2L defaults bare $\|\cdot\|$ to $\ell_2$.
- [[InnerProduct]] — $\langle \mathbf{x},\mathbf{y}\rangle$ symbol.
- [[PartialDerivative]] — $\partial$ symbol.
- [[RandomVariable]] — capital-$X$ convention for r.v.s.
- [[ProbabilitySpace]] — backdrop for $P$, $p(\cdot)$, $\mathbb{E}[\cdot]$.
- [[mml-book]] — parallel symbol table at the front of *Mathematics for Machine Learning*; same overall conventions but row-vector gradient layout differs.
- [[JustInTimeTeaching]] — explains why this chapter is so short: notation introduced *here* is only what is shared across the whole book; chapter-specific notation is introduced when first used.

## Contradictions

- No direct contradictions with existing wiki content. **Notational caveat** vs [[mml-book]]: MML uses a **row-vector** convention for the gradient (flagged on the [[Gradient]] and [[Jacobian]] pages); D2L's notation chapter does not commit to a layout, so the two are not yet in conflict — to be revisited once a later D2L chapter (likely the linear-algebra or calculus preliminaries) makes a layout choice explicit.
