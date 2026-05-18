---
title: "Logistic Regression"
type: concept
tags: [classical-ml, classification]
sources: [islr-seventh-printing, d2l-linear-classification]
last_updated: 2026-05-16
---

# Logistic Regression

A linear classifier that maps features through a sigmoid (or softmax for multiclass) and is trained with [[CrossEntropyLoss]]. Interpretable baseline for binary classification and the conceptual single-neuron unit underlying all deep classifiers; trained via [[GradientDescent]]. Covered alongside [[LinearDiscriminantAnalysis]], [[QuadraticDiscriminantAnalysis]], and [[KNearestNeighbors]] in [[islr-seventh-printing|ISLR]] Ch.4; a special case of [[GeneralizedLinearModels]] with the logit link.

## Binary special case of softmax regression

Per [[d2l-linear-classification]]: logistic regression is exactly **softmax regression with $q=2$** — the sigmoid $\sigma(z) = 1/(1+e^{-z})$ is the 2-category softmax $\exp(z)/(\exp(z) + \exp(0))$. Both share the same exponential-family structure and the same gradient form $\partial_{o_j} l = \hat p_j - y_j$.

## Workhorse for distribution-shift correction

[[d2l-linear-classification]] uses logistic regression as the **importance-weight estimator** in [[CovariateShift|covariate-shift correction]]: train a binary classifier to distinguish source-distribution inputs from target-distribution inputs, then recover the density ratio $p(\mathbf x)/q(\mathbf x) = \exp(h(\mathbf x))$ for use in weighted [[EmpiricalRiskMinimization|ERM]]. The recursion is clean: logistic regression (binary softmax) is used to repair softmax regression's shift bias.
