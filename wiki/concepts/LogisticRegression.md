---
title: "Logistic Regression"
type: concept
tags: [classical-ml, classification]
sources: [islr-seventh-printing, d2l-linear-classification, hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Logistic Regression

A linear classifier that maps features through a sigmoid (or softmax for multiclass) and is trained with [[CrossEntropyLoss]]. Interpretable baseline for binary classification and the conceptual single-neuron unit underlying all deep classifiers; trained via [[GradientDescent]]. Covered alongside [[LinearDiscriminantAnalysis]], [[QuadraticDiscriminantAnalysis]], and [[KNearestNeighbors]] in [[islr-seventh-printing|ISLR]] Ch.4; a special case of [[GeneralizedLinearModels]] with the logit link.

## Binary special case of softmax regression

Per [[d2l-linear-classification]]: logistic regression is exactly **softmax regression with $q=2$** — the sigmoid $\sigma(z) = 1/(1+e^{-z})$ is the 2-category softmax $\exp(z)/(\exp(z) + \exp(0))$. Both share the same exponential-family structure and the same gradient form $\partial_{o_j} l = \hat p_j - y_j$.

## Workhorse for distribution-shift correction

[[d2l-linear-classification]] uses logistic regression as the **importance-weight estimator** in [[CovariateShift|covariate-shift correction]]: train a binary classifier to distinguish source-distribution inputs from target-distribution inputs, then recover the density ratio $p(\mathbf x)/q(\mathbf x) = \exp(h(\mathbf x))$ for use in weighted [[EmpiricalRiskMinimization|ERM]]. The recursion is clean: logistic regression (binary softmax) is used to repair softmax regression's shift bias.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 elevates logistic regression to **the canonical classification head on top of pretrained-LLM embeddings** — *"we can train a classifier, like a logistic regression, on the CPU instead."* The chapter's two roles for logistic regression:

1. **Classification head over frozen embeddings.** Train `sklearn.linear_model.LogisticRegression(random_state=42)` on the `(8530, 768)` feature matrix produced by [[AllMPNetBaseV2|`all-mpnet-base-v2`]]; predict on test embeddings. **F1 = 0.85 on [[RottenTomatoes|Rotten Tomatoes]]** — the best of the four representation-model regimes in Ch 4.
2. **Classical-baseline floor.** Ch 4's pedagogical opener: *"it is highly advised to compare these examples against classic, but strong baselines such as representing text with [[TFIDF|TF-IDF]] and training a logistic regression classifier on top of that."* The recipe **every LLM-based classifier must beat to justify itself**.

The chapter's framing — embeddings as features, logistic regression as the head — generalizes to any classifier: *"the classifier is trainable and not limited to logistic regression and can take on any form as long as it performs classification."* Logistic regression is preferred for **CPU-trainable interpretability** and as a strong-but-not-cheating baseline.

## Connections

- [[EmbeddingModel]] — Ch 4's frozen-embedding regime where logistic regression is the head.
- [[ClassificationHead]] — the role logistic regression plays in Ch 4.
- [[sklearn]] — the library Ch 4 uses.
- [[TFIDF]] — the classical-baseline upstream featurizer.
- [[hands-on-llm-ch04-text-classification]] — wiki source.
