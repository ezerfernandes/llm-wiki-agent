---
title: "Snorkel"
type: entity
tags: [tool, weak-supervision, data-labeling]
sources: [madewithml-mlops-evaluation, mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Snorkel

Programmatic weak-supervision framework for labeling training data with labeling functions. Mentioned alongside [[Cleanlab]] for improving training-set quality in [[madewithml-mlops-evaluation]].

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) cites Snorkel as the canonical **[[WeakSupervision|weak-supervision]]** framework: it automatically generates initial labels at scale through rule-based heuristics, knowledge bases, and existing model outputs, exchanging manual annotation labor for the upfront effort of writing programmatic labeling functions (each then labeling millions of points at near-zero marginal cost).

## Connections

- [[WeakSupervision]] — the paradigm Snorkel implements.
- [[AIAssistedLabeling]] / [[DataLabeling]] — the labeling-scalability hierarchy.
- [[Cleanlab]] — adjacent training-set-quality tool.
- [[madewithml-mlops-evaluation]] / [[mlsysbook-ch04-data-engineering]] — sources.
