---
title: "Probabilistic Graphical Model"
type: concept
tags: [probabilistic-modeling, graphical-models, foundational]
sources: [mml-book, mml-ch08-when-models-meet-data]
last_updated: 2026-06-04
---

# Probabilistic Graphical Model (PGM)

A compact **graphical representation of a joint probability distribution** over many variables, in which inspection of the graph reveals structural properties — above all [[ConditionalIndependence|conditional independence]] ([[mml-book]] §8.5). A PGM "visually captures the way in which the joint distribution over all random variables can be decomposed into a product of factors depending only on a subset of these variables."

## The three families ([[mml-book]] §8.5.3, Fig. 8.12)

- **[[DirectedGraphicalModel|Directed graphical models]] / [[BayesianNetwork|Bayesian networks]]** — arrows encode conditional probabilities; the joint factorizes as a product of one conditional per node given its parents (Eq. 8.31). Conditional independence is read off via [[DSeparation|d-separation]].
- **Undirected graphical models / Markov random fields** — symmetric pairwise/clique potentials.
- **Factor graphs** — explicit factor nodes between variable nodes.

## Why they matter

[[mml-book]] §8.5 lists the convenient properties:

- A simple way to **visualize** a probabilistic model's structure.
- They can **design or motivate** new statistical models.
- **Inspection of the graph alone** yields insight (e.g. conditional independence).
- Complex inference/learning computations can be expressed as **graphical manipulations** (local message passing — ranking, computer vision, coding theory, signal processing).

**Caveat:** not every distribution can be represented by a given graphical model (Bishop 2006). Introductions: Bishop (2006, ch. 8); Koller & Friedman (2009).

## In ML

- **Naive Bayes** is the simplest directed model: features conditionally independent given the label.
- [[GaussianMixtureModel|GMMs]] (Ch 11) and [[PrincipalComponentAnalysis|PCA]] (Ch 10) are drawn as directed models with [[LatentVariable|latent variables]].
- Renewed interest for **causal inference** (Pearl 2009; Imbens & Rubin 2015; Peters et al. 2017).

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.5 canonical reference.
- [[mml-book]] — §8.5.
- [[DirectedGraphicalModel]] / [[BayesianNetwork]] — the directed family (the chapter's focus).
- [[PlateNotation]] — compact repeated-structure notation.
- [[DSeparation]] — conditional-independence reading.
- [[ConditionalIndependence]] — the property the graph encodes.
- [[LatentVariable]] — unobserved nodes in the graph.
