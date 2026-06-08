---
title: "Bayes Factor"
type: concept
tags: [bayesian-inference, model-selection, statistics]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Bayes Factor

The **ratio of [[MarginalLikelihood|marginal likelihoods]]** of two probabilistic models, used to compare them for [[ModelSelection|model selection]] ([[mml-book]] §8.6.3, p. 287). For models $M_1,M_2$ and data $\mathcal{D}$, the **posterior odds** decompose (Eq. 8.46):

$$\underbrace{\frac{p(M_1\,|\,\mathcal{D})}{p(M_2\,|\,\mathcal{D})}}_{\text{posterior odds}}=\underbrace{\frac{p(M_1)}{p(M_2)}}_{\text{prior odds}}\cdot\underbrace{\frac{p(\mathcal{D}\,|\,M_1)}{p(\mathcal{D}\,|\,M_2)}}_{\text{Bayes factor}}.$$

The **prior odds** measures how much the prior favors $M_1$ over $M_2$; the **Bayes factor** is the ratio of [[MarginalLikelihood|marginal likelihoods]] (evidences), measuring **how well $\mathcal{D}$ is predicted by $M_1$ compared to $M_2$**.

## Decision rule

Under a **uniform model prior** the prior odds is 1, so the posterior odds equals the Bayes factor (Eq. 8.47):

$$\frac{p(\mathcal{D}\,|\,M_1)}{p(\mathcal{D}\,|\,M_2)}.$$

A Bayes factor $> 1$ ⇒ choose $M_1$, otherwise $M_2$. As in frequentist statistics, there are guidelines on the ratio size required before "significance" (Jeffreys 1961).

## The Jeffreys–Lindley paradox

[[mml-book]] §8.6.3 (Remark, p. 287): *"the Bayes factor always favors the simpler model since the probability of the data under a complex model with a diffuse prior will be very small"* (Murphy 2012). A **diffuse** prior — one that does not favor specific parameter values, making many models a priori plausible — spreads the complex model's evidence thin, so the Bayes factor systematically prefers the simpler model. A cautionary note on naive use of Bayes factors.

## Computing it requires the marginal likelihood

Both numerator and denominator are marginal likelihoods $p(\mathcal{D}\,|\,M_i)=\int p(\mathcal{D}\,|\,\boldsymbol\theta_i)p(\boldsymbol\theta_i\,|\,M_i)\,d\boldsymbol\theta_i$ (Eq. 8.44) — generally an intractable integral, so the Bayes factor inherits the marginal likelihood's reliance on numerical/Monte-Carlo integration (closed-form only for conjugate priors).

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.6.3 canonical reference (Eqs. 8.46–8.47).
- [[mml-book]] — §8.6.3.
- [[MarginalLikelihood]] — the numerator/denominator.
- [[ModelSelection]] — what the Bayes factor serves.
- [[OccamsRazor]] — the automatic complexity penalty inside each marginal likelihood.
- [[BayesianInference]] — the posterior-odds framing.
