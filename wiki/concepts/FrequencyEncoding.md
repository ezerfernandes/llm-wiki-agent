---
title: "Frequency Encoding"
type: concept
tags: [feature-engineering, categorical, encoding]
sources: [mechanics-of-ml]
last_updated: 2026-06-04
---

# Frequency Encoding

Replace each category with **how often it appears** in the training data (`df['col'].value_counts()` then `.map`). The premise, from [[mechanics-of-ml|*The Mechanics of Machine Learning*]] (Ch 6): "there might be predictive power in the number of apartments managed by a particular manager" — i.e. category prevalence may correlate with the target. Cheap and leakage-free (counts come from features, not the target), but it conflates distinct categories that happen to share a count, and in the book's apartment example it did **not** improve accuracy.

## Connections
- [[mechanics-of-ml]] — Ch 6 *Categorically Speaking*.
- [[TargetEncoding]] / [[LabelEncoding]] / [[OneHotEncoding]] — sibling categorical encodings.
- [[FeatureEngineering]] — parent activity.
