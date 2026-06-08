---
title: "Directed Graphical Model"
type: concept
tags: [probabilistic-modeling, graphical-models, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Directed Graphical Model (Bayesian Network)

A graphical language for specifying a probabilistic model that **visually captures how the joint distribution factorizes** ([[mml-book]] §8.5, p. 278). Also known as a **[[BayesianNetwork|Bayesian network]]**; it is the directed member of the three graphical-model families (the others: undirected / Markov random fields, and factor graphs — Fig. 8.12).

## Semantics

- **Nodes are random variables.**
- **Directed edges (arrows) indicate conditional probabilities** — an arrow $a\to b$ encodes $p(b\,|\,a)$ ([[mml-book]] §8.5.1, p. 279).
- With additional assumptions, arrows can be read as **causal** (Pearl 2009).

The joint distribution by itself (e.g. $p(a,b,c)$) tells us nothing about independence relations; the *graph* does — which is the entire point.

## Graph ↔ factorization (a two-way street)

**Joint → graph** (Example 8.7): $p(a,b,c)=p(c\,|\,a,b)\,p(b\,|\,a)\,p(a)$ (Eq. 8.29) yields the DAG where $c$ has parents $a,b$, $b$ has parent $a$, and $a$ has none. Recipe: (1) one node per variable; (2) for each conditional, draw arrows from the conditioning nodes.

**Graph → joint** (Example 8.8): the joint is a product of one conditional per node, each conditioned only on its **parents** — in general (Eq. 8.31):

$$p(\mathbf{x})=\prod_{k=1}^{K}p(x_k\,|\,\mathrm{Pa}_k),$$

where $\mathrm{Pa}_k$ denotes the parents of $x_k$ (nodes with arrows pointing into $x_k$).

## Why graphical models are useful

- A simple way to **visualize** a probabilistic model's structure.
- Can **design / motivate** new statistical models.
- Inspection of the graph alone reveals properties — notably [[ConditionalIndependence|conditional independence]] via [[DSeparation|d-separation]] (§8.5.2).
- Complex inference/learning becomes **graphical manipulation** (local message passing).

**Caveat:** not every distribution can be represented by a given graphical model (Bishop 2006).

## Shading, plates, and hyperpriors

[[PlateNotation|Plate notation]] compactly repeats i.i.d. structure; **shaded nodes are observed variables**; a **hyperprior** adds a second layer of priors (§8.5.1, Fig. 8.10).

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.5 canonical reference.
- [[mml-book]] — §8.5.
- [[BayesianNetwork]] — the synonym.
- [[ProbabilisticGraphicalModel]] — the umbrella over directed / undirected / factor-graph families.
- [[PlateNotation]] — compact repeated structure.
- [[DSeparation]] — reading conditional independence off the graph.
- [[ConditionalIndependence]] — what the graph topology encodes.
- [[LatentVariable]] — unshaded (unobserved) nodes.
- [[GaussianMixtureModel]] / [[PrincipalComponentAnalysis]] — drawn as DGMs in Chs 10–11.
