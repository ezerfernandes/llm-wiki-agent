---
title: "Statistical Independence"
type: concept
tags: [probability, foundational]
sources: [d2l-preliminaries, mml-book, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
---

# Statistical Independence

Two random variables $A$ and $B$ are **independent** ($A \perp B$) iff conditioning on one tells us nothing about the other:

$$P(A \mid B) = P(A) \quad\Longleftrightarrow\quad P(A, B) = P(A)\,P(B).$$

The two formulations are equivalent via the product rule. Independence factorizes the [[JointProbability|joint]] into marginals — the cleanest possible probabilistic relationship ([[d2l-preliminaries]] §Multiple Random Variables; [[mml-book]] §6.4.5).

## Conditional independence

$A$ and $B$ are **conditionally independent given $C$** ($A \perp B \mid C$) iff

$$P(A, B \mid C) = P(A \mid C)\,P(B \mid C).$$

Marginal and conditional independence are distinct: each can hold without the other (see "explaining away" on [[ConditionalProbability]]).

## Two characteristic reversals

- **Independent → dependent under conditioning**: when $A$ and $B$ are independent causes of a common effect $C$, observing $C$ couples them. *Broken bones and lung cancer are independent in the general population but become correlated once you condition on hospitalization.*
- **Dependent → independent under conditioning**: when $A$ and $B$ are both effects of a common cause $C$, conditioning on $C$ decouples them. *Shoe size and reading level are correlated among children but become independent once you condition on age.*

## Why it matters

- **i.i.d. assumption**: training examples are typically assumed *independent and identically distributed*, allowing $P(\mathcal{D}\mid\boldsymbol\theta) = \prod_i P(\mathbf{x}_i\mid\boldsymbol\theta)$ and making [[MaximumLikelihoodEstimation|MLE]] tractable.
- **Naive Bayes** assumes features are conditionally independent given the label, factorizing $P(\mathbf{x}\mid y) = \prod_i P(x_i\mid y)$.
- **Bayes nets / [[ProbabilisticGraphicalModel|PGMs]]** encode a sparse pattern of conditional independencies via a DAG, making inference tractable.
- **Causal inference** turns on which conditional independencies a graph implies (d-separation).

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.4.5 (book pp. 194–195, Def. 6.10): $X\perp Y$ iff $p(\mathbf x,\mathbf y)=p(\mathbf x)p(\mathbf y)$ (Eq. 6.53) — "the value of $\mathbf y$ (once known) does not add any additional information about $\mathbf x$." When independent: $p(\mathbf y\mid\mathbf x)=p(\mathbf y)$, $p(\mathbf x\mid\mathbf y)=p(\mathbf x)$, $\mathbb{V}_{X,Y}[\mathbf x+\mathbf y]=\mathbb{V}_X[\mathbf x]+\mathbb{V}_Y[\mathbf y]$, and $\mathrm{Cov}_{X,Y}[\mathbf x,\mathbf y]=\mathbf 0$.

**Zero covariance does *not* imply independence** — a caveat the chapter pre-empts: [[Covariance|covariance]] measures only *linear* dependence, so nonlinearly dependent RVs can have zero covariance. **Example 6.5**: take $X$ zero-mean with $\mathbb{E}[x^3]=0$ and let $Y=x^2$ (clearly dependent on $X$); then $\mathrm{Cov}[x,y]=\mathbb{E}[xy]-\mathbb{E}[x]\mathbb{E}[y]=\mathbb{E}[x^3]=0$. The converse direction *does* hold: independence ⇒ zero covariance.

The chapter also defines **i.i.d.** (independent and identically distributed, p. 195): "independent" for $>2$ variables means *mutually* independent (all subsets independent); "identically distributed" means all from the same distribution — the standing assumption that factorizes the likelihood $\prod_i p(\mathbf x_i\mid\boldsymbol\theta)$ for [[MaximumLikelihoodEstimation|MLE]]. The geometric reading (§6.4.6): in the [[InnerProduct|inner-product space of random variables]], $X\perp Y$ (uncorrelated) iff $X,Y$ are *orthogonal vectors* ($\mathrm{Cov}[x,y]=0$). See [[ConditionalIndependence]] for $X\perp\!\!\!\perp Y\mid Z$.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.5 deep dive.
- [[d2l-preliminaries]] — definition + both reversal examples.
- [[mml-book]] — §6.4.5 canonical reference.
- [[JointProbability]] — factorization criterion.
- [[ConditionalProbability]] — alternate definition.
- [[ConditionalIndependence]] — conditioning on a third variable.
- [[Covariance]] — zero covariance ≠ independence (only linear dependence).
- [[InnerProduct]] — uncorrelated = orthogonal random variables.
- [[RandomVariable]] — the entities related.
- [[BayesTheorem]] — independence simplifies its denominator.
