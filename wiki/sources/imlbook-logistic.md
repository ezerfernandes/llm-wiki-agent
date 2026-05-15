---
title: "Logistic Regression"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/logistic.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Logistic regression models the probabilities for classification problems with two possible outcomes. It's an extension of the linear regression model for class outcomes.[^actually-probabilities]

## Key Claims
- **Don't use linear regression for classification** — The linear regression model can work well for regression, but fails for classification.
- **Theory** — A solution for classification is logistic regression.
- **Interpretation** — The interpretation of the weights in logistic regression differs from the interpretation of the weights in linear regression since the outcome in logistic regression is a value between 0 and 1.
- **Logistic regression is multiplicative** — On the level of probabilities, logistic regression is not linear in the features.
- **Enhance interpretation with model-agnostic methods** — If you want to interpret the outcome on the level of probabilities, then you have to use model-agnostic methods, such as the [partial dependence plot](#pdp).
- **Example** — We use logistic regression to predict [whether a penguin is female](#penguins) for Chinstrap penguins based on body measurements.
- **Strengths** — Many of the pros and cons of the [linear regression model](#limo) also apply to the logistic regression model.
- **Limitations** — Logistic regression has been widely used by many different people, but it struggles with its restrictive expressiveness (e.g., interactions must be added manually), and other models may have better predictive performance.
- **Software** — I used the `glm` function in R for all examples.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-limo]] — referenced via @sec or [text](#limo).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).

## Contradictions
None noted in this chapter.
