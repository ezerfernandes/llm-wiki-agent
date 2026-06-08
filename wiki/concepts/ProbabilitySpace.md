---
title: "Probability Space"
type: concept
tags: [probability, foundational, measure-theory]
sources: [mml-book, d2l-preliminaries, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
---

# Probability Space

The triple $(\Omega, \mathcal{A}, P)$ ([[mml-book]] §6.1.2):

- **Sample space $\Omega$**: set of all possible outcomes of the experiment (e.g., $\Omega=\{hh, ht, th, tt\}$ for two coin tosses).
- **Event space $\mathcal{A}$**: collection of subsets of $\Omega$ — the "observable events." For discrete $\Omega$, $\mathcal{A}$ is usually the power set $2^\Omega$.
- **Probability measure $P:\mathcal{A}\to[0,1]$**: assigns each event $A\in\mathcal{A}$ a number $P(A)\in[0,1]$ with $P(\Omega)=1$.

## Why this construction matters

[[mml-book]] §6.1.1 frames probability via **Cox-Jaynes**: any consistent quantification of plausibility *must* obey the axioms of probability ($P\in[0,1]$, sum rule, product rule). Probability is "a generalization of Boolean logic" (citing Jaynes 2003) — when premises don't entail conclusions, you fall back from $\{0,1\}$ truth values to plausibilities in $[0,1]$.

This grounds the **Bayesian** interpretation of probability as degree of belief, but the same axioms also support the **frequentist** interpretation as the limiting relative frequency (§6.1, Remark). MML is deliberately agnostic about which interpretation to commit to.

## The target space

In ML we rarely work with $\Omega$ directly. Instead a [[RandomVariable]] $X:\Omega\to\mathcal{T}$ pushes the probability measure onto a more convenient target space $\mathcal{T}$ (typically $\mathbb{R}$ or $\mathbb{R}^D$), giving the *distribution* $P_X(S) := P(X^{-1}(S))$ (Eq. 6.8, [[mml-book]] §6.1.2).

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.1.2 (book pp. 174–177) presents the triple "deliberately slightly hand-wavy" — it avoids measure theory to keep intuition visible. Modern probability is axiomatized by **Kolmogorov** (Grinstead & Snell 1997, Jaynes 2003), with three concepts:

- **Sample space $\Omega$** — the set of all outcomes of an experiment (e.g. two coin tosses → $\{hh, tt, ht, th\}$). The chapter notes $\Omega$ goes by *many* names across textbooks: "state space" (Jacod & Protter 2004 — though that term is also used for dynamical systems), "sample description space," "possibility space," or even "event space" (§6.1.2 Remark, p. 175–176).
- **Event space $\mathcal{A}$** — the subsets of $\Omega$ we can *observe* the outcome to be in; for discrete $\Omega$ usually the power set $2^\Omega$. For **continuous** spaces the set of all subsets is not well-behaved (it must close under complements/intersections/unions and admit a well-defined *measure*); the well-behaved object is a **Borel $\sigma$-algebra** (§6.2.2 Remark, p. 180). MML sidesteps the measure-theoretic construction.
- **Probability $P:\mathcal{A}\to[0,1]$** — assigns each event a number in $[0,1]$ with $P(\Omega)=1$.

We rarely work with $\Omega$ directly; instead a [[RandomVariable]] $X:\Omega\to\mathcal{T}$ pushes the measure onto a convenient **target space** $\mathcal{T}$ (whose elements MML calls *states*), giving the **law / distribution** $P_X(S)=P(X\in S)=P(X^{-1}(S))$ (Eq. 6.8) — equivalently $P_X=P\circ X^{-1}$.

There are "three distinct ideas often confused" (§6.1.2, p. 174): (1) the probability space, (2) the random variable that transfers probability to a numerical space, and (3) the *distribution/law* associated with the random variable (expanded in §6.2).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.1.2 deep dive.
- [[mml-book]] — §6.1 canonical reference.
- [[RandomVariable]] — the function that pushes probability onto $\mathcal{T}$.
- [[CoxJaynesTheorem]] — the justification for the probability axioms.
- [[BayesTheorem]] — the consistent updating rule on a probability space.
- [[ProbabilityMassFunction]] / [[ProbabilityDensityFunction]] / [[CumulativeDistributionFunction]] — how the distribution on $\mathcal{T}$ is specified.
