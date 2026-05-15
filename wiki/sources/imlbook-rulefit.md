---
title: "RuleFit"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/rulefit.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
The RuleFit algorithm [@friedman2008predictive] learns sparse linear models that include automatically detected interaction effects in the form of decision rules.

## Key Claims
- **Interpretation and example** — Since RuleFit estimates a linear model in the end, the interpretation is the same as for "normal" [linear models](#limo).
- **Theory** — Let's dive deeper into the technical details of the RuleFit algorithm.
- **Strengths** — RuleFit automatically adds **feature interactions** to linear models.
- **Limitations** — Sometimes RuleFit creates many rules that get a non-zero weight in the Lasso model.
- **Software and alternatives** — The RuleFit algorithm is [implemented in R](https://CRAN.R-project.org/package=pre) by @fokkema2020fitting, and you can find a [Python version on GitHub](https://github.com/christophM/rulefit).

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-feature-importance]] — referenced via @sec or [text](#feature-importance).
- [[imlbook-interaction]] — referenced via @sec or [text](#interaction).
- [[imlbook-limo]] — referenced via @sec or [text](#limo).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- **Cited works** (sample): `buhlmann2007boosting`, `fokkema2020fitting`, `friedman2008predictive`.

## Contradictions
None noted in this chapter.
