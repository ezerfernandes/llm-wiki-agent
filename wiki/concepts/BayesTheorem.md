---
title: "Bayes' Theorem"
type: concept
tags: [probability, foundational]
sources: [mml-book, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-05-16
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

## Connections

- [[d2l-preliminaries]] — §Bayes' theorem + HIV example.
- [[mml-book]] — §6.3 canonical reference.
- [[JointProbability]] / [[ConditionalProbability]] — the rules used in the derivation.
- [[RandomVariable]] — the entities being updated.
- [[BayesianLinearRegression]] / [[MAPEstimation]] — ML uses.
