---
title: "Recommender Systems"
type: concept
tags: [supervised-learning, ml-application]
sources: [d2l-introduction, d2l-recommender-systems]
last_updated: 2026-05-16
---

# Recommender Systems

[[SupervisedLearning|Supervised-learning]] application that displays items relevant to a *specific* user — related to search/ranking but emphasizing **personalization**. Movies, retail products, music, news. Per [[d2l-introduction]]: "the results page for a science fiction fan and the results page for a connoisseur of Peter Sellers comedies might differ significantly."

## Feedback signals

- **[[ExplicitFeedback]]** — star ratings, written reviews (Amazon / IMDb / Goodreads).
- **[[ImplicitFeedback]]** — skipping playlist tracks, purchase history, dwell time. Noisier but vastly more abundant.

A simple objective is to estimate the expected user rating or the probability of purchase, then retrieve the top-scoring items.

## Pathologies — the chapter explicitly flags these

[[d2l-introduction]] devotes a paragraph to "serious conceptual flaws" of naive predictive-model-based recommenders:

1. **Censored feedback** — users preferentially rate items they feel strongly about, producing a bimodal one-star / five-star distribution with few three-star ratings; the unobserved distribution is *not* missing-at-random.
2. **Feedback loops** — current purchase habits are *caused by* the current recommender. If the loop is ignored during training, items the system has historically pushed get more purchases, look "better," and get pushed even more — a self-reinforcing distribution shift.
3. **Exposure bias / incentives** — related; the user can only rate what they've seen.

The chapter labels handling these "important open research questions."

## Task taxonomy ([[d2l-recommender-systems]])

D2L's dedicated recommender-systems chapter elaborates a three-way task split:

- **Rating prediction** — regression on explicit feedback. RMSE. Canonical models: [[MatrixFactorization]], [[AutoRec]].
- **Top-$n$ ranking** — retrieval on implicit feedback. Hit@k / AUC / NDCG. Canonical models: [[NeuMF]], [[CaserModel]].
- **[[CTRPrediction|Click-through-rate prediction]]** — binary classification with high-cardinality sparse categorical features. Canonical models: [[FactorizationMachines]], [[DeepFM]].

Each requires different objectives ([[MeanSquaredError|MSE]] / [[BPR]] / [[BinaryCrossEntropy|BCE]]) and different data structures.

## Sub-paradigms

- **[[CollaborativeFiltering]]** — uses only the user-item [[InteractionMatrix|interaction matrix]] (no side info). Splits into [[MemoryBasedCF|memory-based]] (nearest-neighbor) and [[ModelBasedCF|model-based]] (latent-factor) families.
- **Content-based** — item-content-driven (NLP / CV features over descriptions, images, metadata).
- **Context-based** — incorporates timestamps, location, device.
- **Feature-rich / hybrid** — incorporates everything via [[FactorizationMachines]] / [[DeepFM]].
- **[[SequenceAwareRecommendation|Sequence-aware]]** — input is ordered, timestamped action history; captures user-interest drift and short-term intent.
- **Cold-start** — recommending for new users / new items lacking interaction history (Schein, Popescul, Ungar et al. 2002).

## Connections

- [[SupervisedLearning]] — parent paradigm.
- [[Classification]], [[Regression]] — depending on whether the score is a rating (regression) or a click probability (classification).
- [[DataDrift]], [[ConceptDrift]] — distribution shifts induced by feedback loops.
- [[CapabilityVsAlignment]] — value-alignment concerns (engagement vs user welfare) the chapter's "feedback loop" framing previews.
- [[CollaborativeFiltering]], [[MatrixFactorization]], [[AutoRec]], [[NeuMF]], [[CaserModel]], [[FactorizationMachines]], [[DeepFM]], [[BPR]], [[CTRPrediction]], [[ImplicitFeedback]], [[ExplicitFeedback]] — sub-concepts.
- [[MovieLens]] — canonical benchmark dataset.
- [[NetflixPrize]] — historical anchor.
- [[d2l-introduction]], [[d2l-recommender-systems]] — corpus anchors.
