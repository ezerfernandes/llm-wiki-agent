---
title: "Exponential Family"
type: concept
tags: [probability, distributions, foundational]
sources: [mml-book, d2l-linear-classification, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
---

# Exponential Family

A parametric family of distributions whose density factors as

$$p(\mathbf{x}\mid\boldsymbol\theta) = h(\mathbf{x})\,\exp\!\left(\langle\boldsymbol\eta(\boldsymbol\theta), \mathbf{T}(\mathbf{x})\rangle - A(\boldsymbol\theta)\right)$$

where $\mathbf{T}(\mathbf{x})$ is the **sufficient statistic**, $\boldsymbol\eta(\boldsymbol\theta)$ the natural parameter, $A(\boldsymbol\theta)$ the log-partition function, and $h(\mathbf{x})$ the base measure ([[mml-book]] §6.6).

## Members

[[GaussianDistribution|Gaussian]], Bernoulli, Binomial, Multinomial, Poisson, Exponential, Gamma, Beta, Dirichlet, Wishart — essentially every distribution in standard probabilistic ML.

## Why exponential families are special

- **Sufficient statistics summarize data**: for an i.i.d. sample, the log-likelihood depends on the data *only through* the sum $\sum_n \mathbf{T}(\mathbf{x}_n)$. This is the Fisher-Pitman-Koopman-Darmois result and is why empirical-mean / empirical-variance update rules exist for [[GaussianMixtureModel|GMM]] EM (Ch 11).
- **Conjugate priors always exist** ([[mml-book]] §6.6): for any exponential-family likelihood, there is an exponential-family prior such that the posterior stays in the same family. See [[ConjugatePrior]].
- **MLE = method of moments**: setting $\nabla A(\boldsymbol\theta) = \frac{1}{N}\sum_n\mathbf{T}(\mathbf{x}_n)$ gives the MLE for natural parameters.
- **Maximum entropy**: each exponential family is the *maximum-entropy* distribution consistent with the constraints $\mathbb{E}[\mathbf{T}(\mathbf{X})]=\boldsymbol\mu$.

## Connection to GLMs

[[GeneralizedLinearModels|Generalized linear models]] use an exponential-family conditional likelihood $p(y\mid\mathbf{x})$ with the natural parameter $\boldsymbol\eta = \mathbf{w}^\top\mathbf{x}$. Logistic regression is exponential-family + Bernoulli; Poisson regression is exponential-family + Poisson; linear regression is exponential-family + Gaussian. This is why [[CrossEntropyLoss]] (the NLL of an exponential-family Bernoulli/Categorical) appears uniformly across classification ML.

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.6.3 (book pp. 210–214) frames the exponential family as the class hitting all three ML desiderata for distributions (§6.6, p. 205): a *closure property* under probability operations, no growth in parameter count as data accumulates, and well-behaved parameter estimation. There are **three levels of abstraction** (p. 211): a named distribution with fixed params; a fixed parametric form with params to be learned; and a *family* of distributions (the exponential family). MML's canonical form (Eq. 6.107):

$$p(\mathbf x\mid\boldsymbol\theta)=h(\mathbf x)\exp\big(\langle\boldsymbol\theta,\boldsymbol\phi(\mathbf x)\rangle - A(\boldsymbol\theta)\big),$$

with $\boldsymbol\phi(\mathbf x)$ the [[SufficientStatistics|sufficient statistics]], $\boldsymbol\theta$ the [[NaturalParameters|natural parameters]], $A(\boldsymbol\theta)$ the log-partition function, $h(\mathbf x)$ the base measure (absorbable into the dot product). This is a particular expression of $g_\theta(\boldsymbol\phi(x))$ in the **Fisher–Neyman** factorization (Theorem 6.14).

**Worked members.** Gaussian (Example 6.13): $\boldsymbol\phi(x)=[x,x^2]^\top$, $\boldsymbol\theta=[\mu/\sigma^2,-1/(2\sigma^2)]^\top$. Bernoulli (Example 6.14): natural parameter $\theta=\log\frac{\mu}{1-\mu}$ (log-odds), with inverse $\mu=\frac{1}{1+\exp(-\theta)}$ = the **sigmoid / logistic function** (Eq. 6.118) — the same nonlinearity used in logistic regression and neural-net activations.

**Why it is the answer to a deep question** (§6.6.2): as more data arrives, do we need more parameters? In general yes — *except* for exponential families, the only families with **finite-dimensional sufficient statistics** under repeated i.i.d. sampling. Historical note (p. 211): independently discovered 1935–1936 by Edwin Pitman (Tasmania), Georges Darmois (Paris), and Bernard Koopman (New York).

**Payoffs** (p. 214): finite-dimensional sufficient statistics; conjugate priors are easy to write and themselves come from an exponential family (**every member has a conjugate prior**, Eq. 6.120 — Example 6.15 derives the Beta as the Bernoulli's conjugate); empirical estimates of sufficient statistics are optimal estimates of the population values; and the log-likelihood is **concave** → efficient optimization (Ch 7).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.6.3 deep dive.
- [[mml-book]] — §6.6 canonical reference.
- [[GaussianDistribution]] — exponential-family prototype.
- [[NaturalParameters]] — the parameters $\boldsymbol\theta$ in the canonical form.
- [[SufficientStatistics]] — $\boldsymbol\phi(\mathbf x)$; the Fisher–Neyman connection.
- [[ConjugatePrior]] — conjugate to every exponential-family likelihood.
- [[MaximumLikelihoodEstimation]] — has a particularly clean form on the family.
- [[GeneralizedLinearModels]] — exponential-family + linear-in-parameters predictor.
- [[CrossEntropyLoss]] — exponential-family NLL.
