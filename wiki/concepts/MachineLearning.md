---
title: "Machine Learning"
type: concept
tags: [foundational, paradigm]
sources: [d2l-introduction, d2l-preface, islr-seventh-printing, mml-book, mml-ch01-introduction-and-motivation, mml-ch08-when-models-meet-data, pml1-murphy]
last_updated: 2026-06-04
---

# Machine Learning

The study of algorithms that **learn from experience** — typically observational data or environment interactions — and whose performance improves as that experience accumulates ([[d2l-introduction]] Ch 1). Contrasted with deterministic rule-based software whose behavior is fixed by the developer until manually updated.

[[d2l-introduction]] organizes any ML system around **four core components**:

1. The **data** that we can learn from — examples (data points / instances / samples) characterized by **features** ([[FeatureEngineering|covariates]] / inputs) and, in supervised problems, **labels** (targets).
2. A **model** of how to transform the data — a parametric family of input→output mappings (a *statistical model* "estimated from data").
3. An **[[CrossEntropyLoss|objective function]]** quantifying model performance — by convention *lower is better*, hence *loss function*. Surrogate objectives are used when the natural metric is non-differentiable.
4. An **optimization algorithm** to adjust parameters — almost always a variant of [[GradientDescent|gradient descent]].

## Taxonomy of problem types

| Paradigm | Defining feature | Examples |
|---|---|---|
| [[SupervisedLearning]] | Labeled $(x, y)$ pairs; predict $y$ given $x$ | [[Regression]], [[Classification]], tagging, search/ranking, [[RecommenderSystems]], sequence learning |
| [[UnsupervisedLearning]] | No labels; discover structure in $x$ | [[KMeansClustering|clustering]], [[PrincipalComponentAnalysis|PCA]], generative modeling |
| [[SelfSupervisedLearning]] | Fabricated supervision from structure in $x$ | Masked LM ([[bert]]), context-prediction, contrastive |
| [[reinforcementlearning]] | Agent ↔ environment over time; reward signal | Atari DQN, [[alphazero|AlphaGo]], robotics |

Special RL cases: fully-observed = [[MarkovDecisionProcess|MDP]]; state-independent-of-action = contextual bandit; no state = [[MultiArmedBandits|multi-armed bandit]].

## Sister-corpus framings

- **[[islr-seventh-printing|ISLR]]** calls the umbrella *[[StatisticalLearning|statistical learning]]* and emphasizes the inference/prediction distinction.
- **[[pml1-murphy|Murphy]]** unifies the field under the [[ProbabilisticPerspective|probabilistic perspective]] (every unknown is a random variable; predictions are distributions).
- **[[mml-book|MML]]** structures it as four pillars (regression / PCA / GMM / SVM) on six mathematical foundations.
- **[[d2l-introduction|D2L]]** uses ML as the lead-in to [[DeepLearning|deep learning]] specifically, anchored by the four-components-plus-four-paradigms framing above.

## From [[mml-ch01-introduction-and-motivation|MML Ch 1]]

*[[mml-book|Mathematics for Machine Learning]]* opens with its own definition: "Machine learning is about designing algorithms that automatically extract valuable information from data" (§1, p. 11), stressing the word *automatic* — general-purpose methodologies applicable to many datasets while still producing something meaningful. It organizes the field around **three core concepts** rather than D2L's four components:

1. **Data** — ML is inherently data-driven; the goal is to extract patterns *ideally without much domain-specific expertise* (§1, p. 11). Data is assumed already converted to a numerical representation and is thought of as **vectors** (§1.1, p. 12).
2. **Model** — a simplified version of the (unknown) data-generating process, captured either as a **function** (the optimization view) or as a **probabilistic model** (§1.1, pp. 12–13). See [[Predictor]].
3. **Learning** — "a way to automatically find patterns and structure in data by optimizing the parameters of the model" (§1, p. 11). See [[Training]].

MML also disambiguates the overloaded phrase "machine learning algorithm" into a **[[Predictor|predictor]]** (makes predictions) versus the **[[Training|training]]** procedure (adapts the predictor's parameters) (§1.1, p. 12). Structurally the book frames the field as the **[[FourPillarsOfMachineLearning|four pillars × six mathematical foundations]]** of Figure 1.1, and emphasizes that the goal is [[Generalization|generalization]] to unseen data, not memorization of the training set (§1.1, p. 13).

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] (*When Models Meet Data*, opening Part II) operationalizes the three concepts. **Data** are vectors $\mathbf{x}_n\in\mathbb{R}^D$ in the [[DesignMatrix|example matrix]] $\mathbf{X}\in\mathbb{R}^{N\times D}$ (§8.1.1). A **model** is precisely either a [[Predictor|predictor function]] $f:\mathbb{R}^D\to\mathbb{R}$ (§8.1.2) or a [[ProbabilisticModel|probability distribution]] (§8.1.3). **Learning is finding parameters**, with three conceptually distinct algorithmic phases (§8.1.4): **(1) prediction/inference**, **(2) training/parameter estimation**, **(3) hyperparameter tuning / [[ModelSelection|model selection]]**. The chapter then gives three "flavors" of the *training* phase — **[[EmpiricalRiskMinimization|empirical risk minimization]]** (§8.2, non-probabilistic), **[[MaximumLikelihoodEstimation|maximum likelihood]]** / [[MAPEstimation|MAP]] (§8.3, point estimates of a probabilistic model), and full **[[BayesianInference|Bayesian inference]]** (§8.4, integrate over parameters) — all unified by the goal of [[Generalization|generalization]], framed philosophically as [[Abduction|abduction]] (§8.1.4).

## Connections

- [[mml-ch01-introduction-and-motivation]] — MML's data / model / learning trichotomy and the predictor/training disambiguation.
- [[DeepLearning]] — the [[NeuralNetwork|multi-layer]] subfield D2L focuses on.
- [[Generalization]], [[Overfitting]], [[BiasVarianceTradeoff]] — the central tension all four corpora share.
- [[StatisticalLearning]] — sibling umbrella term.
- [[ProbabilisticPerspective]] — Murphy's unifying lens.
- [[ArtificialGeneralIntelligence|AGI]] — [[d2l-introduction]] explicitly contrasts present-day specialized ML with hypothetical general-purpose self-improving AI.
