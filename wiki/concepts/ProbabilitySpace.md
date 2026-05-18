---
title: "Probability Space"
type: concept
tags: [probability, foundational, measure-theory]
sources: [mml-book, d2l-preliminaries]
last_updated: 2026-05-16
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

## Connections

- [[mml-book]] — §6.1 canonical reference.
- [[RandomVariable]] — the function that pushes probability onto $\mathcal{T}$.
- [[CoxJaynesTheorem]] — the justification for the probability axioms.
- [[BayesTheorem]] — the consistent updating rule on a probability space.
