---
title: "Scoped Rules (Anchors)"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/anchors.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
*Authors: Tobias Goerke & Magdalena Lang (with later edits from Christoph Molnar)*

## Key Claims
- **Finding anchors** — Although anchors’ mathematical description may seem clear and straightforward, constructing particular rules is infeasible.
- **Complexity and runtime** — Knowing the anchors approach’s asymptotic runtime behavior helps to evaluate how well it is expected to perform on specific problems.
- **Tabular data example** — Tabular data is structured data represented by tables, wherein columns embody features and rows instances.
- **Strengths** — The anchors approach offers multiple advantages over LIME.
- **Limitations** — The algorithm suffers from a **highly configurable** and impactful setup, just like most perturbation-based explainers.
- **Software and alternatives** — Currently, there are two implementations available: [anchor, a Python package](https://github.com/marcotcr/anchor) (also integrated by [Alibi](https://github.com/SeldonIO/alibi)), and a [Java…

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-lime]] — referenced via @sec or [text](#lime).
- **Cited works** (sample): `kaufmann2013information`, `ribeiro2018anchors`.

## Contradictions
None noted in this chapter.
