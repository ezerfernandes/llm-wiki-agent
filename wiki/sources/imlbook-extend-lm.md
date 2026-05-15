---
title: "GLM, GAM and more"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/extend-lm.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
The biggest strength, but also the biggest weakness, of the [linear regression model](#limo) is that the prediction is modeled as a weighted sum of the features. In addition, the linear model comes with many other assumptions. The bad news is (well, not really news) that all those assumptions are often violated in reality: The outcome given the features might have a non-Gaussian distribution, the features might interact, and the relationship between the features and the outcome might be nonlinear. The good news is that the statistics community has developed a variety of modifications that…

## Key Claims
- **For the GLM** — n = 30000 df = data.frame(x = c(rnorm(n), rexp(n, rate = 0.5)), dist = rep(c("Gaussian", "Definitely Not Gaussian"), each = n)) df$dist  = relevel(factor(df$dist), "Gaussian") p.glm = ggplot(df) + geom_density(aes(x = x)) + facet_grid(.
- **Non-Gaussian outcomes - GLMs** — The linear regression model assumes that the outcome given the input features follows a Gaussian distribution.
- **Interactions** — The linear regression model assumes that the effect of one feature is the same regardless of the values of the other features (= no interactions).
- **Nonlinear effects - GAMs** — **The world is not linear.** Linearity in linear models means that no matter what value an instance has in a particular feature, increasing the value by one unit always has the same effect on the predicted outcome.
- **Strengths** — All these extensions of the linear model are a bit of a universe in themselves.
- **Limitations** — As an advantage, I've said that linear models live in their own universe.
- **Use model-agnostic methods** — The more you move away from the pure linear regression by using transformations, interactions, and smooth effects, the more you may need model-agnostic tools like the [partial dependence plot](#pdp) to analyze the model.
- **Software** — All examples in this chapter were created using the R language.
- **Further extensions** — As promised, here is a list of problems you might encounter with linear models, along with the name of a solution for this problem that you can copy and paste into your favorite search engine.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-limo]] — referenced via @sec or [text](#limo).
- [[imlbook-logistic]] — referenced via @sec or [text](#logistic).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- [[imlbook-rulefit]] — referenced via @sec or [text](#rulefit).
- **Cited works** (sample): `caruana2015intelligible`.

## Contradictions
None noted in this chapter.
