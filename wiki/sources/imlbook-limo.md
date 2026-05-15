---
title: "Linear Regression"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/limo.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
get_reference_dataset = function(dat){   df = lapply(dat, function(feature){     if(class(feature) == 'factor'){       factor(levels(feature)[1], levels = levels(feature))     } else {       0     }   })   data.frame(df) }

## Key Claims
- **Interpretation** — The interpretation of a weight in the linear regression model depends on the type of the corresponding feature.
- **Example** — In this example, we use the linear regression model to predict the [number of rented bikes](#bike-data) on a particular day, given weather and calendar information.
- **Weight and effect plot** — Visualizations like the weight and the effect plot make the linear regression model easy and quick to grasp for humans.
- **Encoding categorical features** — There are several ways to encode a categorical feature, and the choice influences the interpretation of the weights.
- **Sparse linear models** — The examples of the linear models that I've chosen all look nice and neat, don't they?
- **Strengths** — The modeling of the predictions as a **weighted sum** makes it transparent how predictions are produced.
- **Limitations** — Linear regression models can only represent linear relationships, i.e., a weighted sum of the input features.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-extend-lm]] — referenced via @sec or [text](#extend-lm).
- [[imlbook-logistic]] — referenced via @sec or [text](#logistic).
- **Cited works** (sample): `hastie2009elements`.

## Contradictions
None noted in this chapter.
