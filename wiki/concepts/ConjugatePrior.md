---
title: "Conjugate Prior"
type: concept
tags: [probability, bayesian-inference, foundational]
sources: [mml-book, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
---

# Conjugate Prior

A prior $p(\boldsymbol\theta)$ is **conjugate** to a likelihood $p(\mathcal{D}\mid\boldsymbol\theta)$ if the posterior $p(\boldsymbol\theta\mid\mathcal{D})\propto p(\mathcal{D}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)$ stays in the **same family** as the prior ([[mml-book]] §6.6).

## Classical conjugate pairs

| Likelihood | Conjugate prior | Posterior |
|---|---|---|
| Bernoulli / Binomial | Beta | Beta |
| Multinomial / Categorical | Dirichlet | Dirichlet |
| Poisson | Gamma | Gamma |
| [[GaussianDistribution|Gaussian]] (known $\sigma^2$, unknown $\mu$) | Gaussian | Gaussian |
| Gaussian (known $\mu$, unknown $\sigma^2$) | Inverse-Gamma | Inverse-Gamma |
| Gaussian (both unknown) | Normal-Inverse-Wishart | Normal-Inverse-Wishart |
| Exponential | Gamma | Gamma |

Conjugate pairs *exist* because most useful likelihoods are members of the [[ExponentialFamily]] — and exponential-family likelihoods always have conjugate priors of a matching form.

## Why ML cares

- **Closed-form posterior updates** — no MCMC, no variational approximation. This is what makes [[BayesianLinearRegression]] tractable.
- **Sequential / online learning**: posterior at step $n$ becomes the prior at step $n+1$; conjugacy means the running representation stays compact.
- **Pedagogical scaffold**: conjugate cases give the analytical baseline against which approximate inference (MCMC, VI) is benchmarked.

## When conjugacy fails

For neural-network likelihoods or non-conjugate combinations (e.g., Bernoulli likelihood + Gaussian prior over logits → no closed-form posterior on the original probability), you fall back to **variational inference**, **MCMC**, or **Laplace approximation**.

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.6.1 (book pp. 208–210, Def. 6.13): a prior is *conjugate* for a likelihood if the **posterior is of the same form/type as the prior**. Since by [[BayesTheorem|Bayes' theorem]] the posterior $\propto$ prior · likelihood, conjugacy lets you "algebraically calculate the posterior distribution by **updating the parameters** of the prior" — no MCMC or variational approximation. Motivated by two difficulties in prior specification (p. 208): the prior should encode pre-data knowledge (hard to describe), and the posterior is often analytically intractable — conjugate priors resolve the second.

**Worked conjugacy.** Example 6.11 (Beta–Binomial) and Example 6.12 (Beta–Bernoulli) show the Beta is conjugate to the Bernoulli/Binomial parameter $\mu$: observing $h$ heads in $N$ flips updates a $\mathrm{Beta}(\alpha,\beta)$ prior to a $\mathrm{Beta}(h+\alpha,\,N-h+\beta)$ posterior (Eq. 6.104d) — you just add the counts to the hyperparameters.

**Table 6.2 (conjugate pairs).**

| Likelihood | Conjugate prior | Posterior |
|---|---|---|
| Bernoulli | Beta | Beta |
| Binomial | Beta | Beta |
| Gaussian (variance, univariate) | Gaussian / inverse-Gamma | Gaussian / inverse-Gamma |
| Gaussian (covariance, multivariate) | Gaussian / inverse-Wishart | Gaussian / inverse-Wishart |
| Multinomial | Dirichlet | Dirichlet |

The Gaussian appears twice because the univariate (scalar) variance uses an **inverse-Gamma** prior while the multivariate precision/covariance matrix uses an **inverse-Wishart**; the Dirichlet is conjugate to the Multinomial.

**Where conjugacy comes from.** Conjugate priors exist *systematically* because the listed likelihoods are members of the [[ExponentialFamily]]: **every exponential-family member has a conjugate prior** (Brown 1986; Eq. 6.120), whose sufficient statistics are $[\boldsymbol\theta,-A(\boldsymbol\theta)]^\top$. Example 6.15 *derives* the Beta as the canonical conjugate prior of the Bernoulli from its [[NaturalParameters|natural-parameter]] form. Geometrically, conjugate priors "retain the same distance structure as the likelihood" (Agarwal & Daumé III 2010).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.6.1 deep dive.
- [[mml-book]] — §6.6 canonical reference.
- [[ExponentialFamily]] — where conjugate priors come from systematically.
- [[NaturalParameters]] / [[SufficientStatistics]] — the exponential-family machinery behind conjugacy.
- [[GaussianDistribution]] — self-conjugate.
- [[BayesianLinearRegression]] — primary conjugate-prior application in [[mml-book]] Ch 9.
- [[BayesTheorem]] — the update rule conjugacy preserves form for.
