---
title: "Out-of-Bag (OOB) Score"
type: concept
tags: [random-forest, evaluation, ensemble]
sources: [mechanics-of-ml]
last_updated: 2026-06-04
---

# Out-of-Bag (OOB) Score

A "free" validation estimate built into [[RandomForests|Random Forests]]. Each tree trains on a [[Bootstrap|bootstrap]] sample, so roughly a third of records are **out of the bag** (not used by that tree); predicting each record using only the trees that *didn't* see it yields a held-out accuracy estimate with no separate validation set. In scikit-learn: `RandomForestRegressor(..., oob_score=True).oob_score_`.

[[mechanics-of-ml|*The Mechanics of Machine Learning*]] uses OOB R² as the working metric on the (time-insensitive) apartment data — raw OOB R² −0.0076 → 0.8677 after [[Denoising|denoising]] → 0.8767 with a [[LogInExpOut|log target]]. But the book's key **caveat**: for time-sensitive data, OOB is "overly optimistic about the generality of a model" because "OOB samples are within the same date range as the training samples." Use a true time-based [[TrainValTestSplit|validation split]] for time-series problems.

## Connections
- [[mechanics-of-ml]] — Ch 5 (uses OOB) and Ch 9 (time-series caveat).
- [[RandomForests]] / [[Bagging]] / [[Bootstrap]] — OOB is a property of bootstrap-aggregated ensembles.
- [[TrainValTestSplit]] — what OOB substitutes for, except on time-series data.
- [[CrossValidation]] — the alternative held-out-estimate technique.
