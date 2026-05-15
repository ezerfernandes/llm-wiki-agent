---
title: "Counterfactual Explanations"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/counterfactual.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
*Authors: Susanne Dandl & Christoph Molnar*

## Key Claims
- **Generating counterfactual explanations** — A simple and naive approach to generating counterfactual explanations is searching by trial and error.
- **Example** — The following example is based on the credit dataset example in Dandl et al.
- **Strengths** — **The interpretation of counterfactual explanations is very clear**.
- **Limitations** — **For each instance, you will usually find multiple counterfactual explanations (Rashomon effect).** This is inconvenient --  most people prefer simple explanations over the complexity of the real world.
- **Software and alternatives** — The multi-objective counterfactual explanation method by Dandl et al.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-anchors]] — referenced via @sec or [text](#anchors).
- [[imlbook-lime]] — referenced via @sec or [text](#lime).
- [[2605.03808-agentic-imodels]] — modern interpretability work uses LLM-graded counterfactual probes (testing whether an LLM can predict the model's behavior under perturbation) as one component of its simulatability suite.
- **Cited works** (sample): `dandl2020multiobjective`, `deb2002fast`, `karimi2020modelagnostic`, `laugel2017inverse`, `mothilal2020explaining`, `ribeiro2018anchors`, `vanlooveren2021interpretable`, `wachter2018counterfactual`.

## Contradictions
None noted in this chapter.
