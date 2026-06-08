---
title: "Bilinear Form"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Bilinear Form

A **bilinear mapping** (bilinear form) $\Omega:V\times V\to\mathbb{R}$ is a mapping of two vector arguments that is **linear in each argument separately** ([[mml-ch03-analytic-geometry|MML Ch 3]] §3.2.2, Eqs. 3.6–3.7):

$$\Omega(\lambda\mathbf{x}+\psi\mathbf{y},\,\mathbf{z}) = \lambda\,\Omega(\mathbf{x},\mathbf{z})+\psi\,\Omega(\mathbf{y},\mathbf{z}) \quad\text{(linear in the 1st argument)}$$
$$\Omega(\mathbf{x},\,\lambda\mathbf{y}+\psi\mathbf{z}) = \lambda\,\Omega(\mathbf{x},\mathbf{y})+\psi\,\Omega(\mathbf{x},\mathbf{z}) \quad\text{(linear in the 2nd argument)}$$

for all $\mathbf{x},\mathbf{y},\mathbf{z}\in V$ and $\lambda,\psi\in\mathbb{R}$.

## Special bilinear forms

[[mml-book]] Definition 3.2 (p. 73) refines a bilinear $\Omega$:

- **Symmetric**: $\Omega(\mathbf{x},\mathbf{y})=\Omega(\mathbf{y},\mathbf{x})$ for all $\mathbf{x},\mathbf{y}$ — the order of arguments does not matter.
- **Positive definite**: $\forall\mathbf{x}\in V\setminus\{\mathbf{0}\}:\Omega(\mathbf{x},\mathbf{x})>0$, and $\Omega(\mathbf{0},\mathbf{0})=0$ (Eq. 3.8).

## The key specialization: inner product

An **[[InnerProduct]] is exactly a positive definite, symmetric bilinear form** ([[mml-book]] Def. 3.3). Drop positive definiteness and you have a general (possibly indefinite) bilinear form; this is why **[[Orthogonality|orthogonality]] generalizes perpendicularity to bilinear forms that need not be the dot product** ([[mml-book]] Remark, p. 77).

## Matrix representation

In coordinates w.r.t. an ordered basis $B$, every bilinear form is $\Omega(\mathbf{x},\mathbf{y})=\hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$ for some matrix $\mathbf{A}$ with $A_{ij}=\Omega(\mathbf{b}_i,\mathbf{b}_j)$ ([[mml-book]] Eq. 3.10). It is symmetric iff $\mathbf{A}=\mathbf{A}^\top$, positive definite iff $\mathbf{A}$ is a [[SymmetricPositiveDefiniteMatrix|symmetric positive definite matrix]]. Thus inner products correspond exactly to SPD matrices ([[mml-book]] Thm 3.5).

## Connections

- [[mml-ch03-analytic-geometry]] — §3.2.2 canonical reference (Eqs. 3.6–3.8).
- [[InnerProduct]] — the symmetric + positive-definite bilinear form.
- [[SymmetricPositiveDefiniteMatrix]] — the matrix of a symmetric positive-definite bilinear form.
- [[Orthogonality]] — generalizes perpendicularity to any bilinear form.
- [[LinearMapping]] — the one-argument analogue; bilinear = linear in each argument.
