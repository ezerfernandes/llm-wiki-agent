---
title: "Machine Learning"
type: concept
tags: [foundational, paradigm]
sources: [d2l-introduction, d2l-preface, islr-seventh-printing, mml-book, pml1-murphy]
last_updated: 2026-05-16
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

## Connections

- [[DeepLearning]] — the [[NeuralNetwork|multi-layer]] subfield D2L focuses on.
- [[Generalization]], [[Overfitting]], [[BiasVarianceTradeoff]] — the central tension all four corpora share.
- [[StatisticalLearning]] — sibling umbrella term.
- [[ProbabilisticPerspective]] — Murphy's unifying lens.
- [[ArtificialGeneralIntelligence|AGI]] — [[d2l-introduction]] explicitly contrasts present-day specialized ML with hypothetical general-purpose self-improving AI.
