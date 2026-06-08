---
title: "Joint Probability"
type: concept
tags: [probability, foundational]
sources: [d2l-preliminaries, mml-book, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
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

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.2.1 (book pp. 178–180) defines the discrete joint via counts: with $n_{ij}$ events in state $(x_i,y_j)$ out of $N$ total,

$$P(X=x_i,Y=y_j)=\frac{n_{ij}}{N}=P(X=x_i\cap Y=y_j)\qquad(\text{Eq. 6.9}),$$

visualized as a 2-D table / grid (Fig. 6.2, adapted from Bishop 2006). From the joint:

- **[[Marginalization|Marginals]]** are row/column sums: $p(x_i)=c_i/N$ (Eq. 6.10), $p(y_j)=r_j/N$ (Eq. 6.11) — the [[SumRule|sum rule]].
- **[[ConditionalProbability|Conditionals]]** are a cell divided by its row/column total: $p(y_j\mid x_i)=n_{ij}/c_i$ (Eq. 6.13) — the [[ProductRule|product rule]] rearranged.

The joint is the master object: "one can think of a probability as a function that takes state $x$ and $y$ and returns a real number, which is the reason we write $p(x,y)$" (p. 179). [[mml-book]] flags that ML literature writes the joint *lazily* as $p(x,y)$ (§6.2.1). The [[ProductRule|product rule]] $p(\mathbf x,\mathbf y)=p(\mathbf y\mid\mathbf x)p(\mathbf x)$ (Eq. 6.22) shows every joint factorizes — and equating its two orderings yields [[BayesTheorem|Bayes' theorem]].

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.2–6.3 deep dive.
- [[d2l-preliminaries]] — derives the upper bound, marginalization, and product rule.
- [[mml-book]] — §6.2 canonical reference.
- [[ProbabilitySpace]] — the underlying $(\Omega, \mathcal{A}, P)$.
- [[RandomVariable]] — components of the joint.
- [[SumRule]] / [[Marginalization]] — recover marginals from the joint.
- [[ProductRule]] / [[ConditionalProbability]] — joint ÷ marginal.
- [[StatisticalIndependence]] — when the joint factorizes.
- [[BayesTheorem]] — derived from two expansions of the joint.
