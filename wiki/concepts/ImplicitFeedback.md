---
title: "Implicit Feedback"
type: concept
tags: [recommender-systems, data]
sources: [d2l-recommender-systems, d2l-introduction]
last_updated: 2026-05-16
---

# Implicit Feedback

User preference signals **inferred from observable behavior** rather than proactively stated — clicks, purchases, watches, dwell time, plays, mouse movements. Canonicalized as a feedback-type distinct from [[ExplicitFeedback|explicit feedback]] by [[YifanHu|Hu]], [[YehudaKoren|Koren]] & Volinsky 2008.

## Defining traits

- **Abundant** — implicit signals are emitted continuously by every user action; explicit ratings require active user effort and are scarce.
- **Noisy** — *"we can only guess their preferences and true motives"*: a user watching a movie does not imply they liked it. ([[d2l-recommender-systems]])
- **Positive-only by default** — observation = positive signal; absence = ambiguous (real negative OR untracked OR future interaction). The defining modeling challenge.
- **Heteroscedastic confidence** — repeated interaction implies stronger preference than a single click; Hu-Koren-Volinsky introduce confidence weights for this.

## Modeling consequences

- **Pure rating-prediction methods break** — MF and AutoRec ignore unobserved entries; on implicit-only data this means *every prediction is positive*. [[d2l-recommender-systems]] §ranking opens with this critique.
- **Negative sampling becomes mandatory** — unobserved pairs must be sampled as candidate negatives during training ([[NegativeSampling]]). Random per-step sampling is the chapter's default in `PRDataset`.
- **Evaluation switches** from RMSE to ranking metrics — [[HitRate|Hit@k]], [[AUC]], [[NDCG]], MRR.
- **Pairwise / listwise losses replace pointwise MSE** — [[BPR]], [[HingeLossRanking|Hinge]] target relative order across `(positive, negative)` pairs rather than absolute scores.

## Connections
- [[ExplicitFeedback]] — sibling category.
- [[YehudaKoren]] — co-author of the canonical 2008 paper.
- [[NeuMF]], [[CaserModel]], [[BPR]], [[NegativeSampling]] — modeling consequences.
- [[CTRPrediction]] — implicit-feedback's most monetized incarnation.
- [[InteractionMatrix]] — typical data structure.
- [[d2l-recommender-systems]], [[d2l-introduction]] — sources.
