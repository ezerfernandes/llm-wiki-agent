---
title: "Click-Through Rate (CTR) Prediction"
type: concept
tags: [recommender-systems, advertising, classification]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Click-Through Rate (CTR) Prediction

The task of predicting **whether a user will click on a given ad / item / link given a set of features**. Defined per [[d2l-recommender-systems]] as:

$$\textrm{CTR} = \frac{\#\textrm{clicks}}{\#\textrm{impressions}}\times 100\%$$

Usually framed as **binary classification** with sigmoid output trained with [[BinaryCrossEntropy|BCE]] / sigmoid-cross-entropy loss.

## Characteristic input structure

Unlike pure-CF recommenders that take only `(user_id, item_id)`, CTR-prediction models consume **high-cardinality sparse categorical features** — ad id, site/app id, device id, time of day, user profile, page section, ad slot — typically 10s–100s of fields, each with vocabularies of $10^3$–$10^7$. The chapter's anonymized advertising dataset has **34 categorical fields** with the first column as the click label.

## Canonical models

- **[[LogisticRegression|Logistic regression]]** with hand-crafted feature crosses — the production baseline through the early 2010s (McMahan et al. 2013, *Google's FTRL CTR system*).
- **[[FactorizationMachines|Factorization Machines]]** ([[SteffenRendle|Rendle]] 2010) — automated bilinear feature interactions via low-rank embeddings; the $\mathcal{O}(kd)$ pairwise-interaction trick makes them tractable on sparse high-cardinality inputs.
- **[[WideAndDeep|Wide & Deep]]** (Cheng et al. 2016, Google) — parallel fusion of memorization (wide LR) and generalization (deep MLP).
- **[[DeepFM]]** ([[HuifengGuo|Guo]] et al. 2017) — FM + DNN parallel fusion that eliminates the wide-side feature-engineering effort.
- xDeepFM, AutoInt, DCN, DIN, DIEN — subsequent variants adding attention, sequential modeling, or explicit cross networks.

## Public benchmarks

- **[[CriteoDataset|Criteo display advertising challenge]]** — real CTR data with both numerical and categorical features.
- **[[AvazuDataset|Avazu CTR prediction]]** — Kaggle competition data.
- The D2L chapter's 15k-train / 3k-test anonymized advertising dataset — synthetic teaching dataset.

## Why it matters

CTR prediction underwrites *every monetized digital surface*: search ads, display ads, social-feed ads, app-store ads, video pre-rolls. Every Google / Meta / Bytedance / Amazon advertising query at runtime invokes a CTR model. Improvements measured in basis points translate to billions in revenue.

## Connections
- [[RecommenderSystems]] — parent application family.
- [[FactorizationMachines]], [[DeepFM]] — canonical models.
- [[Classification]], [[LogisticRegression]] — task framing.
- [[BinaryCrossEntropy]] — training loss.
- [[Embedding]] — required primitive for sparse-categorical inputs.
- [[CriteoDataset]], [[AvazuDataset]] — production benchmarks.
- [[d2l-recommender-systems]] — source §ctr.
