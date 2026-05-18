---
title: "Joint Probability"
type: concept
tags: [probability, foundational]
sources: [d2l-preliminaries, mml-book]
last_updated: 2026-05-16
---

# Joint Probability

For random variables $A$ and $B$, the **joint probability** $P(A=a, B=b)$ is the probability that both events $A=a$ *and* $B=b$ occur simultaneously — i.e., the probability assigned to the intersection of the corresponding subsets of the sample space ([[d2l-preliminaries]] §Multiple Random Variables; [[mml-book]] §6.2).

## Key identities

- **Upper bound**: $P(A=a, B=b) \leq \min(P(A=a),\, P(B=b))$ — joint never exceeds the marginal of either component.
- **Marginalization** ("summing out"): $P(A=a) = \sum_v P(A=a, B=v)$ recovers the marginal from the joint.
- **Product rule (definition of [[ConditionalProbability|conditional probability]])**: $P(A,B) = P(B \mid A)\,P(A) = P(A \mid B)\,P(B)$. This is the engine that produces [[BayesTheorem|Bayes' theorem]].
- **Under [[StatisticalIndependence|independence]]**: $P(A, B) = P(A)\,P(B)$ — the factorization that makes naive Bayes work.

## Why it matters

The joint distribution tells us *everything* there is to know probabilistically about a set of random variables: marginals are recovered by summing/integrating, conditionals by ratios, and any expectation $\mathbb{E}[f(X,Y)] = \sum_{x,y} f(x,y)P(x,y)$ is a sum against the joint. Most ML models are *factorizations* of an intractable joint into tractable pieces — naive Bayes ($P(\mathbf{x},y) = P(y)\prod_i P(x_i\mid y)$), Bayes nets / [[ProbabilisticGraphicalModel|PGMs]] (DAG-structured factorization), autoregressive language models ($P(x_1,\ldots,x_T) = \prod_t P(x_t \mid x_{<t})$).

## Connections

- [[d2l-preliminaries]] — derives the upper bound, marginalization, and product rule.
- [[mml-book]] — §6.2 canonical reference.
- [[ProbabilitySpace]] — the underlying $(\Omega, \mathcal{A}, P)$.
- [[RandomVariable]] — components of the joint.
- [[ConditionalProbability]] — joint ÷ marginal.
- [[StatisticalIndependence]] — when the joint factorizes.
- [[BayesTheorem]] — derived from two expansions of the joint.
