---
title: "Predictor"
type: concept
tags: [machine-learning, foundations, mml]
sources: [mml-ch01-introduction-and-motivation, mml-ch08-when-models-meet-data]
last_updated: 2026-06-04
---

# Predictor

A **predictor** is a machine-learning system that **makes predictions based on input data** — the trained artifact that maps an input to an output. *[[mml-book|Mathematics for Machine Learning]]* introduces the term in Chapter 1 (§1.1, p. 12) to disambiguate the overloaded phrase "machine learning algorithm," which is used in *two distinct senses*:

1. **The predictor** — *"a system that makes predictions based on input data."* This is the model-as-deployed: input in, prediction out.
2. **The training procedure** — *"a system that adapts some internal parameters of the predictor so that it performs well on future unseen input data."* That adaptation is **[[Training|training]]** the system.

Chapter 1 deliberately does not resolve this ambiguity but flags it up front, so that "predictor" can be used unambiguously to mean the prediction-making artifact, distinct from the learning process that produces it.

## Two views of a predictor

[[mml-book|MML]] frames the model behind a predictor in two interchangeable ways (§1.1 summary, p. 13):

- **As a function** — e.g., in a [[Regression|regression]] setting the predictor is a function $f$ that maps inputs $\boldsymbol{x} \in \mathbb{R}^D$ to outputs (real-valued for regression, integer labels for [[Classification|classification]]). This is the **optimization view**.
- **As a probabilistic model** — the predictor describes a probability distribution over outputs, which lets it express *uncertainty* (confidence about a prediction at a particular test point). This is the **probabilistic view**, and it is what motivates [[ProbabilityAndDistributions|probability theory]] (Ch 6) and [[BayesianLinearRegression|Bayesian]] methods.

A central design property the book wants from a predictor is the ability to handle **noisy** data — to identify the underlying signal from noise and quantify the associated uncertainty (§1.2, Part I motivation, p. 14).

## Similarity drives prediction

The book motivates [[AnalyticGeometry|analytic geometry]] (Ch 3) via the predictor: *"vectors that are similar should be predicted to have similar outputs by our machine learning algorithm (our predictor)"* (§1.2, p. 14). Formalizing similarity between input vectors requires inner products, norms, and distances.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

Chapter 8 makes the §1.1 "model as a function" view precise (§8.1.2, p. 255): a predictor is a function that, given a feature vector, produces an output — for a real-valued scalar, $f:\mathbb{R}^D\to\mathbb{R}$ (Eq. 8.1). The book restricts to **linear (affine) predictors** $f(\mathbf{x})=\boldsymbol\theta^\top\mathbf{x}+\theta_0$ (Eq. 8.2), since "linear functions strike a good balance between the generality of the problems that can be solved and the amount of background mathematics that is needed." The probabilistic view becomes the [[ProbabilisticModel|probabilistic model]] of §8.1.3. The set of admissible predictors is the [[HypothesisClass|hypothesis class]] (§8.2.1), and the predictor is what the three learning phases — **prediction/inference**, **training**, **model selection** — operate on (§8.1.4); for a probabilistic model the prediction phase is called **inference**.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.1.2 makes the function-view of the predictor precise (Eqs. 8.1–8.2).
- [[mml-ch01-introduction-and-motivation]] — where the predictor / training disambiguation is introduced.
- [[HypothesisClass]] — the set of predictors a learner searches over.
- [[ProbabilisticModel]] — the §8.1.3 distribution-valued view of a model.
- [[Training]] — the *other* sense of "ML algorithm"; the procedure that produces a predictor by optimizing its [[Parameter|parameters]].
- [[MachineLearning]] — the predictor is the *model* component of the data / model / learning trichotomy.
- [[Generalization]] — a good predictor performs well on *unseen* data, not just training data.
- [[Regression]] / [[Classification]] — supervised settings where the predictor maps inputs to real-valued (regression) or integer (classification) outputs.
- [[ProbabilityAndDistributions]] — the probabilistic view of a predictor; how it expresses uncertainty.
- [[AnalyticGeometry]] — similarity between input vectors underpins similar predictions.
