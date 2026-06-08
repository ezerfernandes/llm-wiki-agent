---
title: "Change of Variables"
type: concept
tags: [probability, distributions, calculus, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book, d2l-appendix-mathematics]
last_updated: 2026-06-04
---

# Change of Variables / Inverse Transform

Because the set of *named* distributions is small, ML constantly needs to know how a **transformed** random variable is distributed — e.g. the distribution of $X^2$ or $\frac12(X_1+X_2)$ when $X, X_1, X_2$ are standard normal ([[mml-book]] §6.7). Two techniques answer this; both ultimately rest on the [[CumulativeDistributionFunction|cdf]] and the calculus [[ChainRule|substitution rule]].

## Discrete case

For a discrete RV $X$ with pmf $P(X=x)$ and an invertible $U$, the transformed $Y:=U(X)$ has

$$P(Y=y)=P(U(X)=y)=P(X=U^{-1}(y))\qquad(\text{Eq. 6.125}).$$

Transformations simply relabel events; probabilities move with them.

## Distribution-function (cdf) technique

Find the cdf of $Y=U(X)$ then differentiate ([[mml-book]] §6.7.1):

$$F_Y(y)=P(Y\le y),\qquad f(y)=\frac{d}{dy}F_Y(y)\qquad(\text{Eqs. 6.126–6.127}).$$

Example 6.16 finds the pdf of $Y=X^2$ for $f(x)=3x^2$ on $[0,1]$, obtaining $f(y)=\tfrac32 y^{1/2}$.

### Probability integral transform

A key special case (Theorem 6.15, Casella & Berger 2002): if $X$ has a **strictly monotonic** cdf $F_X$, then

$$Y:=F_X(X) \text{ is uniformly distributed on } [0,1].$$

This **probability integral transform** is the basis of **inverse-cdf sampling** (sample $u\sim\mathcal{U}[0,1]$, return $F_X^{-1}(u)$), of hypothesis testing, and of copulas (Nelsen 2006).

## Change-of-variables technique

Built on the calculus substitution rule $\int f(g(x))g'(x)\,dx=\int f(u)\,du$ with $u=g(x)$ (Eq. 6.133). For a univariate **invertible** $U$ with $Y=U(X)$ ([[mml-book]] §6.7.2):

$$f(y)=f_x(U^{-1}(y))\cdot\left|\frac{d}{dy}U^{-1}(y)\right|\qquad(\text{Eq. 6.143}).$$

The **absolute value** of the differential handles both increasing and decreasing $U$. Compared with the discrete case, the extra factor $|dU^{-1}/dy|$ appears because $P(Y=y)=0$ for continuous RVs ([[mml-book]] §6.7.2 Remark, p. 219) — the density has no event-probability interpretation.

## Multivariate: the Jacobian determinant

For a differentiable, invertible vector transform $\mathbf y=U(\mathbf x)$ (Theorem 6.16, Billingsley 1995):

$$f(\mathbf y)=f_{\mathbf x}(U^{-1}(\mathbf y))\cdot\left|\det\!\left(\frac{\partial}{\partial\mathbf y}U^{-1}(\mathbf y)\right)\right|\qquad(\text{Eq. 6.144}).$$

The **absolute value of the [[Jacobian]] [[Determinant|determinant]]** replaces $|dU^{-1}/dy|$. This is the volume-scaling reading of the determinant from §4.1 / §5.3: differentials (cubes of volume) are mapped to parallelepipeds by the Jacobian, and the determinant measures how a unit volume changes. Example 6.17 transforms a standard bivariate Gaussian by $\mathbf y=\mathbf A\mathbf x$ and recovers a Gaussian with covariance $\boldsymbol\Sigma=\mathbf A\mathbf A^\top$.

## ML payoff: normalizing flows

The modern application is **[[NormalizingFlow|normalizing flows]]** (Jimenez Rezende & Mohamed 2015; cited in §6.8): chains of invertible neural transforms whose exact density is tracked through the change-of-variables Jacobian-determinant formula — enabling exact likelihood training of deep generative models.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.7 deep dive.
- [[mml-book]] — §6.7 canonical reference.
- [[CumulativeDistributionFunction]] — the cdf technique + probability integral transform.
- [[ProbabilityDensityFunction]] — the density being transformed.
- [[Jacobian]] / [[Determinant]] — volume scaling under the transform.
- [[ChainRule]] — the substitution rule underpinning the method.
- [[GaussianDistribution]] — closed under linear transforms (Example 6.17).
- [[NormalizingFlow]] — the deep-generative-model application.
