---
title: "Negative Log-Likelihood"
type: concept
tags: [statistics, estimation, optimization, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Negative Log-Likelihood (NLL)

The quantity minimized by [[MaximumLikelihoodEstimation|maximum likelihood estimation]] ([[mml-book]] §8.3.1, Eq. 8.14):

$$\mathcal{L}_{\mathbf{x}}(\boldsymbol\theta)=-\log p(\mathbf{x}\,|\,\boldsymbol\theta).$$

The subscript $\mathbf{x}$ emphasizes that **the data $\mathbf{x}$ are fixed (observed) and the parameter $\boldsymbol\theta$ varies** — it is usually dropped, written $\mathcal{L}(\boldsymbol\theta)$. Two readings of $p(\mathbf{x}\,|\,\boldsymbol\theta)$: with $\boldsymbol\theta$ fixed it models the uncertainty of the data; with the data fixed and $\boldsymbol\theta$ varying, $\mathcal{L}(\boldsymbol\theta)$ tells us *"how likely a particular setting of $\boldsymbol\theta$ is for the observations."*

## Why a sum, not a product

Under the [[IID|i.i.d.]] assumption, the data likelihood factorizes into a product (Eq. 8.16), so the NLL becomes a **sum** (Eq. 8.17):

$$\mathcal{L}(\boldsymbol\theta)=-\log p(\mathcal{Y}\,|\,\mathcal{X},\boldsymbol\theta)=-\sum_{n=1}^N\log p(y_n\,|\,\mathbf{x}_n,\boldsymbol\theta).$$

A sum of simpler functions is far easier to optimize than a product (and numerically more stable) — this is the whole point of taking the logarithm.

## Why *negative*

[[mml-book]] §8.3.1 (Remark, p. 267): *"The negative sign … is a historical artifact that is due to the convention that we want to maximize likelihood, but numerical optimization literature tends to study minimization of functions."* This negative sign is exactly what makes MLE an instance of [[EmpiricalRiskMinimization|ERM]] with the NLL as its [[LossFunction|loss function]].

## NLL = least squares for Gaussian noise

With a Gaussian likelihood $p(y_n\,|\,\mathbf{x}_n,\boldsymbol\theta)=\mathcal{N}(y_n\,|\,\mathbf{x}_n^\top\boldsymbol\theta,\sigma^2)$ (Example 8.5, Eqs. 8.18a–d):

$$\mathcal{L}(\boldsymbol\theta)=\frac{1}{2\sigma^2}\sum_{n=1}^N(y_n-\mathbf{x}_n^\top\boldsymbol\theta)^2-\sum_{n=1}^N\log\frac{1}{\sqrt{2\pi\sigma^2}}.$$

With $\sigma$ given, the second term is constant, so **minimizing the NLL is exactly the least-squares problem** (compare Eq. 8.8).

## Caveat

Although $\boldsymbol\theta$ sits to the right of the conditioning bar in $p(y_n\,|\,\mathbf{x}_n,\boldsymbol\theta)$, it must **not** be read as observed/fixed — $\mathcal{L}(\boldsymbol\theta)$ is a function *of* $\boldsymbol\theta$, minimized w.r.t. $\boldsymbol\theta$ (§8.3.1, p. 267).

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.3.1 canonical reference (Eqs. 8.14–8.18).
- [[mml-book]] — §8.3.1.
- [[MaximumLikelihoodEstimation]] — minimizes the NLL.
- [[MAPEstimation]] — adds a negative-log-prior term to the NLL.
- [[LossFunction]] — the NLL *is* the loss in the probabilistic view of ERM.
- [[EmpiricalRiskMinimization]] — MLE is ERM with the NLL loss.
- [[GaussianDistribution]] — the likelihood whose NLL is least squares.
