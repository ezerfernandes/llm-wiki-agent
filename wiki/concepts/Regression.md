---
title: "Regression"
type: concept
tags: [supervised-learning, ml-task]
sources: [d2l-introduction, islr-seventh-printing, mml-book]
last_updated: 2026-05-16
---

# Regression

[[SupervisedLearning|Supervised-learning]] task where the **label takes arbitrary numerical values** (continuous or interval-valued). Rule of thumb from [[d2l-introduction]]: any *how much?* or *how many?* problem is regression — house prices, length of stay, hours-to-complete, rainfall forecast.

The goal is a model whose predictions approximate the observed targets. The dominant loss is **squared error**, which under a Gaussian-noise assumption is the negative log-likelihood ([[mml-book]] §9.2; see [[LinearRegression]] for the linear case). When the noise has a different form, the loss changes accordingly ([[GeneralizedLinearModels|GLMs]]).

## Worked example (the contractor pricing problem)

[[d2l-introduction]] introduces the linear case via a contractor charging 350 dollars for 3 hours and 250 dollars for 2 hours. Assuming a base fee plus per-hour rate gives **100 dollars per hour + 50 dollars to show up** — a two-parameter linear regression solved by inspection. Sometimes a perfect fit is not possible (variation from omitted features); then we **minimize squared error** as a fallback.

## Connections

- [[SupervisedLearning]] — parent paradigm.
- [[Classification]] — sibling supervised task (discrete labels).
- [[LinearRegression]] — simplest model class.
- [[MeanSquaredError]] — canonical loss.
- [[GaussianDistribution]] — noise model the MSE corresponds to.
- [[RegressionSplines]], [[BasisFunctions]], [[GeneralizedAdditiveModels|GAMs]] — non-linear regressor families.
- [[d2l-introduction]] — corpus-anchor introduction.
- [[islr-seventh-printing|ISLR]] — Ch 3 develops linear regression at length.
