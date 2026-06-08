---
title: "Bayesian Network"
type: concept
tags: [probabilistic-modeling, graphical-models, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Bayesian Network

Synonym for a **[[DirectedGraphicalModel|directed graphical model]]** — the canonical content lives there. [[mml-book]] §8.5 (p. 278) states plainly: *"Directed graphical models are also known as Bayesian networks."* §8.5.1 (p. 278) defines them as "a method for representing conditional dependencies in a probabilistic model," providing a visual description of the conditional probabilities and hence a simple language for complex interdependence.

A directed acyclic graph (DAG) whose nodes are random variables and whose arrows encode conditional probabilities ($a\to b$ ⇒ $p(b\,|\,a)$); the joint factorizes as a product of one conditional per node, conditioned only on its parents (Eq. 8.31). With extra assumptions the arrows admit a **causal** reading (Pearl 2009), the basis of the renewed interest in graphical models for causal inference (Pearl 2009; Imbens & Rubin 2015; Peters et al. 2017).

## Connections

- [[DirectedGraphicalModel]] — the canonical page (full semantics, graph↔factorization, examples).
- [[mml-ch08-when-models-meet-data]] — §8.5 canonical reference.
- [[mml-book]] — §8.5.
- [[ProbabilisticGraphicalModel]] — the family umbrella.
- [[DSeparation]] — conditional-independence reading.
- [[ConditionalIndependence]] — what the network encodes.
