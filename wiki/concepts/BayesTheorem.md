---
title: "Bayes' Theorem"
type: concept
tags: [probability, foundational]
sources: [mml-book, d2l-preliminaries, d2l-appendix-mathematics, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
---

# Bayes' Theorem

The rule that updates beliefs in light of evidence. Derived directly from the product rule for [[JointProbability|joint probabilities]] ([[d2l-preliminaries]] §Multiple Random Variables): $P(A, B) = P(B \mid A)\,P(A) = P(A \mid B)\,P(B)$, hence

$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}.$$

In Bayesian inference, with hypothesis $H$ and evidence $E$:

$$\underbrace{P(H \mid E)}_{\text{posterior}} = \frac{\overbrace{P(E \mid H)}^{\text{likelihood}}\;\overbrace{P(H)}^{\text{prior}}}{\underbrace{P(E)}_{\text{evidence}}}.$$

"Posterior equals prior times likelihood, divided by evidence."

## When you don't have $P(B)$

If the evidence term is unavailable, use the **proportional form** $P(A \mid B) \propto P(B \mid A)\,P(A)$ and normalize:

$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{\sum_a P(B \mid A=a)\,P(A=a)}.$$

The denominator is **marginalization over $A$**.

## HIV-test example

[[d2l-preliminaries]] §An Example walks through the canonical update. With $P(D=1\mid H=1)=1$, $P(D=1\mid H=0)=0.01$, prevalence $P(H=1)=0.0015$:

$$P(D=1) = 0.01\cdot 0.9985 + 1\cdot 0.0015 = 0.011485,$$
$$P(H=1\mid D=1) = \frac{1\cdot 0.0015}{0.011485} \approx 0.1306.$$

A second independent positive test pushes the posterior to ~0.99 — Bayes' theorem chained.

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.3 (book pp. 184–186) derives Bayes' theorem directly from the [[ProductRule|product rule]] (the joint factorizes two ways, Eqs. 6.24–6.26) and presents it with the standard Bayesian labels (Eq. 6.23):

$$\underbrace{p(\mathbf x\mid\mathbf y)}_{\text{posterior}}=\frac{\overbrace{p(\mathbf y\mid\mathbf x)}^{\text{likelihood}}\;\overbrace{p(\mathbf x)}^{\text{prior}}}{\underbrace{p(\mathbf y)}_{\text{evidence}}}.$$

- **Prior** $p(\mathbf x)$ — subjective knowledge of the latent $\mathbf x$ *before* observing data; "it is critical to ensure that the prior has a nonzero pdf (or pmf) on all plausible $\mathbf x$, even if they are very rare."
- **Likelihood** $p(\mathbf y\mid\mathbf x)$ — "sometimes also called the **measurement model**" (MacKay 2003); it is a distribution in $\mathbf y$ **only**, *not* in $\mathbf x$. *"We call $p(\mathbf y\mid\mathbf x)$ either the 'likelihood of $\mathbf x$ (given $\mathbf y$)' or the 'probability of $\mathbf y$ given $\mathbf x$' but never the likelihood of $\mathbf y$."*
- **Posterior** $p(\mathbf x\mid\mathbf y)$ — "the quantity of interest in Bayesian statistics," encoding all available information from prior + data.
- **Evidence / marginal likelihood** $p(\mathbf y)=\int p(\mathbf y\mid\mathbf x)p(\mathbf x)\,d\mathbf x=\mathbb{E}_X[p(\mathbf y\mid\mathbf x)]$ (Eq. 6.27) — the [[Marginalization|marginalization]] of the numerator over $\mathbf x$; it normalizes the posterior and drives Bayesian **model selection** (§8.6), but the integral is "often hard to compute."

Bayes' theorem "allows us to invert the relationship between $\mathbf x$ and $\mathbf y$ given by the likelihood," so it is called the **probabilistic inverse** ([[mml-book]] p. 186). The chapter notes that collapsing the full posterior to a single statistic (e.g. its [[Mode|mode]], the [[MAPEstimation|MAP]] estimate) **loses information**, and that carrying the full posterior can yield far more data-efficient downstream decisions (model-based RL example, Deisenroth et al. 2015). The "closure" of Bayes updates within a distribution family is exactly what [[ConjugatePrior|conjugacy]] (§6.6) provides.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.3 deep dive.
- [[d2l-preliminaries]] — §Bayes' theorem + HIV example.
- [[mml-book]] — §6.3 canonical reference.
- [[ProductRule]] / [[SumRule]] — Bayes is derived from these.
- [[JointProbability]] / [[ConditionalProbability]] — the rules used in the derivation.
- [[Marginalization]] — the evidence term is a marginalization.
- [[ConjugatePrior]] — preserves the posterior's family across updates.
- [[RandomVariable]] — the entities being updated.
- [[BayesianLinearRegression]] / [[MAPEstimation]] — ML uses.
