---
title: "Decision Tree"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/tree.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Plain linear regression and logistic regression models fail in situations where the relationship between features and outcome is nonlinear or where features interact with each other. Time to shine for the decision tree! Tree-based models split the data multiple times according to certain cutoff values in the features. Through splitting, different subsets of the dataset are created, with each instance belonging to one subset. The final subsets are called terminal or leaf nodes, and the intermediate subsets are called internal nodes or split nodes. To predict the outcome in each leaf node, the…

## Key Claims
- **Interpretation** — The interpretation is simple: Starting from the root node, you go to the next nodes, and the edges tell you which subsets you are looking at.
- **Interpretation Template** — If feature $x_j$ is [smaller/bigger] than threshold c AND ...
- **Example** — Let's have another look at the [bike rental data](#bike-data).
- **Decrease depth and number of nodes** — Trees with lower depths and fewer nodes are easier to interpret.
- **Strengths** — The tree structure is ideal for **capturing interactions** between features in the data.
- **Limitations** — **Trees fail to deal with linear relationships**.
- **Software** — For the examples in this chapter, I used the `rpart` R package that implements CART (classification and regression trees).

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-feature-importance]] — referenced via @sec or [text](#feature-importance).
- **Cited works** (sample): `hastie2009elements`, `strobl2008conditional`.
- [[imlbook-limo]] — linear regression, the canonical interpretable baseline.
- [[imlbook-logistic]] — logistic regression, the classification analogue.

## Contradictions
None noted in this chapter.
