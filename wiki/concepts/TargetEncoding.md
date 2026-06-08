---
title: "Target Encoding"
type: concept
tags: [feature-engineering, categorical, encoding, leakage-risk]
sources: [mechanics-of-ml]
last_updated: 2026-06-04
---

# Target Encoding

Also called **mean encoding**: replace each category with the **average target value** for that category, turning a high-cardinality categorical column into one informative numeric feature. In [[mechanics-of-ml|*The Mechanics of Machine Learning*]] (Ch 6) the authors use the `category_encoders.TargetEncoder` and note it is "useful by ... competition winners," but warn it **risks [[Overfitting|overfitting]]** when the encoded feature gets over-weighted — validation scores can drop.

Because the encoding is derived from the target, it is a textbook [[DataLeakage|data-leakage]] hazard: the encoder must be **fit on training data only** and applied to validation/test via the stored mapping. "Transformations of validation and test sets can only use data derived from the training set."

## Connections
- [[mechanics-of-ml]] — Ch 6 *Categorically Speaking* (uses `category_encoders.TargetEncoder`).
- [[DataLeakage]] — target-derived features are the canonical leakage trap.
- [[FrequencyEncoding]] / [[LabelEncoding]] / [[OneHotEncoding]] — the other categorical encodings on the same menu.
- [[FeatureEngineering]] — parent activity.
- [[Overfitting]] — the failure mode target encoding invites.
