---
title: "MovieLens"
type: entity
tags: [dataset, recommender-systems, benchmark]
sources: [d2l-recommender-systems, pydata-data-analysis-examples]
last_updated: 2026-05-16
---

# MovieLens

The canonical academic recommender-systems dataset, hosted by [[GroupLens]] at the University of Minnesota since 1997. Multiple sizes released over the years (100K / 1M / 10M / 20M / 25M ratings). [[d2l-recommender-systems]] uses **MovieLens 100K** (943 users × 1682 movies × 100,000 1–5-star ratings) — cleaned so every user has rated ≥20 movies; sparsity is **93.695%** of the user × item matrix; ratings distribution is roughly Gaussian centered at 3–4.

Each record is `(user_id, item_id, rating, timestamp)` — the timestamp field enables the `seq-aware` split mode used in [[SequenceAwareRecommendation]] and [[NeuMF]] (leave-out-last-item-per-user evaluation), distinct from the `random` 90/10 split used for [[MatrixFactorization]] and [[AutoRec]] rating-prediction experiments.

## Connections
- [[GroupLens]] — institutional host.
- [[d2l-recommender-systems]] — running benchmark across all 8 sub-chapters.
- [[pydata-data-analysis-examples]] — uses MovieLens 1M for a separate analytics example.
- [[MatrixFactorization]], [[AutoRec]], [[NeuMF]], [[CaserModel]] — all evaluated on MovieLens in the D2L chapter.
- [[RMSE]] — primary evaluation metric for rating prediction.
- [[HitRate]], [[AUC]] — primary evaluation metrics for ranking.
