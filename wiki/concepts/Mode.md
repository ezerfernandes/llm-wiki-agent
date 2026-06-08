---
title: "Mode"
type: concept
tags: [probability, statistics, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book, prealgebra-2e-ch05-decimals]
last_updated: 2026-06-07
---

# Mode

The **mode** is the most frequently occurring value of a [[RandomVariable]] ([[mml-book]] §6.4.1, p. 188) — one of three notions of "average," with the [[Mean|mean]] and [[Median|median]].

In introductory arithmetic (OpenStax [[Prealgebra]] 2e Ch 5.5, [[prealgebra-2e-ch05-decimals]]) the mode of a small data set is found by ordering the values, counting how often each occurs, and picking the value with the highest frequency (a data set can have more than one mode, or none).

- **Discrete RV**: the value of $x$ with the highest frequency / pmf.
- **Continuous RV**: a **peak** of the density $p(\mathbf x)$.

## Multimodality

A density may have **more than one mode** (it is then *multimodal*), and high-dimensional densities can have a very large number of modes ([[mml-book]] p. 188). Example 6.4 (Fig. 6.4) is a **bimodal** Gaussian mixture $0.4\,\mathcal{N}(\cdot)+0.6\,\mathcal{N}(\cdot)$ whose 2-D distribution has two modes while one of its marginals is unimodal. Consequently, **finding all the modes of a distribution can be computationally challenging**.

## Relation to inference

The **mode of the posterior** is the [[MAPEstimation|MAP estimate]] ([[mml-book]] §8.3); the mode of the likelihood is the [[MaximumLikelihoodEstimation|MLE]]. Focusing on a single mode of the posterior "leads to loss of information" versus carrying the full posterior (§6.3 Remark, p. 186).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.1 deep dive.
- [[mml-book]] — §6.4.1 canonical reference.
- [[Mean]] / [[Median]] — the other two "averages".
- [[GaussianMixtureModel]] — multimodal densities.
- [[MAPEstimation]] — the posterior mode.
- [[prealgebra-2e-ch05-decimals]] — elementary most-frequent-value procedure (Ch 5.5).
