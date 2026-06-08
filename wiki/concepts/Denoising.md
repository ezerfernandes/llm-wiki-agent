---
title: "Denoising (Data Cleaning)"
type: concept
tags: [data-cleaning, preprocessing, tabular]
sources: [mechanics-of-ml]
last_updated: 2026-06-04
---

# Denoising (Data Cleaning)

Removing out-of-scope or corrupted records so a model learns the real signal rather than artifacts. In [[mechanics-of-ml|*The Mechanics of Machine Learning*]] (Ch 5) the discipline is: **decide the valid bounds *before* looking at the data** — "It's critical that we decide what these bounds are before looking at the data" — otherwise you fit your filters to the noise (a subtle form of [[DataLeakage|leakage]]). On the NYC apartment data the authors set a price floor/ceiling ($1,000–$10,000) and an NYC lat/long bounding box, catching $4.49M/mo prices, (0,0) coordinates, and Boston listings.

Impact is dramatic and model-independent: the *same* `RandomForestRegressor` jumps from OOB R² **−0.0076** (raw) to **0.8677** (denoised). The book offers [[LogInExpOut|"log in, exp out"]] as a no-domain-knowledge alternative that matches on R² but not [[RMSLE|MAE]].

## Connections
- [[mechanics-of-ml]] — Ch 5 *Exploring and Denoising Your Data Set*.
- [[LogInExpOut]] — transformation-based alternative to manual cleaning.
- [[DataLeakage]] — setting bounds *after* peeking is a leakage risk.
- [[FeatureEngineering]] — the broader data-preparation phase.
- [[OutOfBagScore]] — the metric the book uses to show denoising's effect.
