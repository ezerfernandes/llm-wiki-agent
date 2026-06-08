---
title: "Cumulative Distribution Function"
type: concept
tags: [probability, distributions, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book, d2l-appendix-mathematics]
last_updated: 2026-06-04
---

# Cumulative Distribution Function (CDF)

The **cumulative distribution function** of a multivariate real-valued [[RandomVariable]] $X=[X_1,\dots,X_D]^\top$ with states $\mathbf x\in\mathbb{R}^D$ is

$$F_X(\mathbf x)=P(X_1\le x_1,\dots,X_D\le x_D)$$

— the probability that every coordinate is at most its threshold ([[mml-book]] §6.2, Def. 6.2, Eq. 6.17). It is the natural way to express an **interval probability** for a continuous RV, where the point probability $P(X=x)=0$.

## Relation to the pdf

The cdf is the integral of the [[ProbabilityDensityFunction|pdf]]:

$$F_X(\mathbf x)=\int_{-\infty}^{x_1}\!\!\cdots\!\int_{-\infty}^{x_D} f(z_1,\dots,z_D)\,dz_1\cdots dz_D \quad(\text{Eq. 6.18}),$$

and in 1-D $F'(x)=f(x)$ (the fundamental theorem of calculus). [[mml-book]] stresses these are **two distinct concepts**: a pdf $f(x)$ is a nonnegative function integrating to 1, while the *law* of $X$ is the *association* of $X$ with $f$ (Def. 6.2 Remark). "There are cdfs which do not have corresponding pdfs" (margin, p. 181).

## Why it matters

- It exists for *every* RV (discrete and continuous), even when no density exists.
- It is the engine of the **[[ChangeOfVariables|change-of-variables / inverse-transform]]** machinery (§6.7): the *distribution-function technique* finds $F_Y(y)=P(Y\le y)$ and differentiates to get $f(y)$.
- The **probability integral transform** (Theorem 6.15, [[mml-book]] §6.7.1): if $X$ has a strictly monotonic cdf $F_X$, then $Y:=F_X(X)$ is **uniform** on $[0,1]$ — the basis of inverse-cdf sampling, hypothesis testing, and copulas.

## Nomenclature

[[mml-book]] mostly drops the $f(x)/F_X(x)$ distinction (it doesn't need it outside §6.7), but is "careful about pdfs and cdfs in Section 6.7" (p. 182). See Table 6.1 on [[ProbabilityMassFunction]].

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.2, §6.7 deep dive.
- [[mml-book]] — §6.2 canonical reference.
- [[ProbabilityDensityFunction]] — the cdf's derivative.
- [[ProbabilityMassFunction]] — discrete analogue.
- [[ChangeOfVariables]] — uses the cdf technique + probability integral transform.
- [[RandomVariable]] — the entity a cdf describes.
