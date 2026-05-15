---
title: "Decision Rules"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/rules.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
A decision rule is a simple IF-THEN statement consisting of a condition (also called antecedent) and a prediction. For example: IF it rains today AND if it is April (condition), THEN it will rain tomorrow (prediction). A single decision rule or a combination of several rules can be used to make predictions.

## Key Claims
- **Learn rules from a single feature (OneR)** — The OneR algorithm [@holte1993very] is one of the simplest rule induction algorithms.
- **Use OneR as baseline** — OneR makes for a great baseline to compare more complex models against.
- **Use validation data** — Always validate your chosen model with a separate validation set to ensure that it performs well on unseen data, even if it's a simple "one-rule" model.
- **Sequential covering** — Sequential covering is a general procedure that repeatedly learns a single rule to create a decision list (or set) that covers the entire dataset rule by rule.
- **Bayesian Rule Lists** — In this section, I'll show you another approach to learning a decision list, which follows this rough recipe:
- **Strengths** — This section discusses the benefits of IF-THEN rules in general.
- **Limitations** — This section deals with the disadvantages of IF-THEN rules in general.
- **Software and alternatives** — OneR is implemented in the [R package OneR](https://cran.r-project.org/web/packages/OneR/), which was used for the examples in this book.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-rulefit]] — referenced via @sec or [text](#rulefit).
- **Cited works** (sample): `borgelt2005implementation`, `cohen1995fast`, `furnkranz2012foundations`, `holte1993very`, `letham2015interpretable`, `yang2017scalable`.

## Contradictions
None noted in this chapter.
