---
title: "RMSLE (Root Mean Squared Log Error)"
type: concept
tags: [metric, regression, evaluation]
sources: [mechanics-of-ml]
last_updated: 2026-06-04
---

# RMSLE (Root Mean Squared Log Error)

Root mean squared error computed in **log space**: $\sqrt{\frac{1}{n}\sum_i (\log(\hat y_i + 1) - \log(y_i + 1))^2}$. Because it penalizes *ratio* error rather than absolute error, RMSLE is the natural metric for **skewed, multiplicative targets** like prices — under-prediction and over-prediction are weighted by relative size, and a $1,000 miss on a $5,000 item counts far more than on a $500,000 item. It pairs naturally with the [[LogInExpOut|log-target]] training trick.

The [[Kaggle]] "Blue Book for Bulldozers" competition in [[mechanics-of-ml|*The Mechanics of Machine Learning*]] (Ch 9) scores on RMSLE: the authors' tuned [[RandomForests|Random Forest]] reaches validation RMSLE 0.2469 → 0.2327 (after tuning) and a final **test RMSLE 0.2396** (≈ top 5% of competitors). Close validation/test RMSLE is the book's evidence the model "doesn't fall apart" off the training distribution.

## Connections
- [[mechanics-of-ml]] — Ch 9 *Train, Validate, Test* (bulldozer scoring metric).
- [[LogInExpOut]] — log-space training, the metric's natural companion.
- [[Kaggle]] — RMSLE is a common Kaggle regression metric.
- [[RandomForests]] — the model scored against it in the book.
