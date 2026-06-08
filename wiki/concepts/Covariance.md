---
title: "Covariance"
type: concept
tags: [probability, statistics, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Covariance

The **covariance** measures how *dependent* two random variables are on one another ([[mml-book]] §6.4.1, Def. 6.5) — the [[ExpectedValue|expected]] product of their deviations from their respective [[Mean|means]]:

$$\mathrm{Cov}_{X,Y}[x,y]:=\mathbb{E}_{X,Y}\big[(x-\mathbb{E}_X[x])(y-\mathbb{E}_Y[y])\big]\qquad(\text{Eq. 6.35}).$$

By linearity of [[ExpectedValue|expectation]] this rewrites to the convenient **raw-score** form

$$\mathrm{Cov}[x,y]=\mathbb{E}[xy]-\mathbb{E}[x]\,\mathbb{E}[y]\qquad(\text{Eq. 6.36}).$$

## Variance is self-covariance

The covariance of a variable with itself, $\mathrm{Cov}[x,x]$, **is** the [[Variance|variance]] $\mathbb{V}_X[x]$, whose square root is the standard deviation $\sigma(x)$ ([[mml-book]] p. 190).

## Multivariate (cross-covariance)

For multivariate $X\in\mathbb{R}^D$, $Y\in\mathbb{R}^E$ (Def. 6.6, Eq. 6.37):

$$\mathrm{Cov}[\mathbf x,\mathbf y]=\mathbb{E}[\mathbf x\mathbf y^\top]-\mathbb{E}[\mathbf x]\,\mathbb{E}[\mathbf y]^\top=\mathrm{Cov}[\mathbf y,\mathbf x]^\top\in\mathbb{R}^{D\times E}.$$

[[mml-book]] notes a terminology fork (margin, p. 190): the multivariate $\mathrm{Cov}[\mathbf x,\mathbf y]$ "is sometimes referred to as **cross-covariance**, with covariance referring to $\mathrm{Cov}[\mathbf x,\mathbf x]$" (the variance). Collecting all pairwise covariances of a vector's coordinates yields the **[[CovarianceMatrix|covariance matrix]]**.

## Covariance measures only *linear* dependence

A crucial caveat ([[mml-book]] §6.4.5, Example 6.5): **zero covariance does not imply [[StatisticalIndependence|independence]]**. Covariance only captures *linear* dependence, so nonlinearly dependent variables can have zero covariance. Example: $X$ zero-mean with $\mathbb{E}[x^3]=0$ and $Y=x^2$ (dependent on $X$) gives $\mathrm{Cov}[x,y]=\mathbb{E}[x^3]=0$. The converse *does* hold: independence ⇒ zero covariance.

## Geometric view

For zero-mean RVs, $\langle X,Y\rangle:=\mathrm{Cov}[x,y]$ is a valid [[InnerProduct|inner product]] (§6.4.6, Eq. 6.59): symmetric, positive definite, bilinear. Then $X\perp Y$ (orthogonal) iff $\mathrm{Cov}[x,y]=0$, and the **[[Correlation|correlation]] is the cosine of the angle** between $X$ and $Y$ (Eq. 6.61).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.1/§6.4.5/§6.4.6 deep dive.
- [[mml-book]] — §6.4 canonical reference.
- [[Variance]] — self-covariance.
- [[CovarianceMatrix]] — the matrix of all pairwise covariances.
- [[Correlation]] — normalized covariance / cosine of angle.
- [[StatisticalIndependence]] — independence ⇒ zero covariance (not conversely).
- [[InnerProduct]] — covariance as an inner product on RVs.
- [[DataCovarianceMatrix]] — the empirical version used in PCA.
