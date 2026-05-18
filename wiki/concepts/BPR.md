---
title: "BPR (Bayesian Personalized Ranking)"
type: concept
tags: [recommender-systems, ranking, loss-function, implicit-feedback]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# BPR — Bayesian Personalized Ranking

**Pairwise ranking loss for implicit-feedback recommenders**, proposed by [[SteffenRendle|Rendle]], Freudenthaler, Gantner & Schmidt-Thieme 2009 (*UAI*) — *the* canonical ranking loss in the field. Derived from MAP estimation of the personalized ranking $\succ_u$.

## Objective

Training data: triples $(u, i, j)\in D$ where $i\in I_u^+$ (item the user interacted with) and $j\in I\setminus I_u^+$ (unobserved item). The model learns scores $\hat{y}_{ui}$, $\hat{y}_{uj}$ and minimizes:

$$\textrm{BPR-OPT} = -\sum_{(u,i,j)\in D}\ln\sigma(\hat{y}_{ui}-\hat{y}_{uj}) + \lambda_\Theta\|\Theta\|^2$$

with $\sigma$ the logistic sigmoid. Derivation: $p(\Theta\mid\succ_u)\propto p(\succ_u\mid\Theta)p(\Theta)$ with a zero-mean Gaussian prior $p(\Theta)$ giving the $\ell_2$ regularization term.

## Training mechanics

- Negatives sampled at every step from the user's complement of positives ([[NegativeSampling]]). The chapter implements this in `PRDataset.__getitem__` for [[NeuMF]] training.
- Compared with [[HingeLossRanking|Hinge loss]] ($\sum\max(m-\hat{y}_{ui}+\hat{y}_{uj},0)$), which the chapter notes is *interchangeable* for personalized ranking — both target relative-order, not absolute scores.
- Strictly *pairwise* (not pointwise like MF/MSE; not listwise like NDCG); the chapter argues pairwise is the practical sweet spot for ranking.

## Connections
- [[SteffenRendle]] — author.
- [[PersonalizedRanking]] — task this loss targets.
- [[ImplicitFeedback]] — feedback type BPR was designed for.
- [[NegativeSampling]] — required training-time mechanic.
- [[HingeLossRanking]] — interchangeable pairwise alternative.
- [[NeuMF]], [[CaserModel]] — D2L models trained with BPR.
- [[FactorizationMachines]] — also commonly trained with BPR for ranking.
- [[d2l-recommender-systems]] — source §ranking.
