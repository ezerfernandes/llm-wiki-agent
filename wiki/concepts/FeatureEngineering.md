---
title: "Feature Engineering"
type: concept
tags: [data, ml-engineering]
sources: [mechanics-of-ml, mlsysbook-ch04-data-engineering, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Feature Engineering

Crafting model inputs from raw data — aggregations, joins, time windows, transformations — to expose signal the model can exploit. Often the largest lever on tabular performance; outputs live in a [[FeatureStore]] and must respect [[DataSplitting]] boundaries to avoid [[DataLeakage]].

## From *The Mechanics of Machine Learning*

[[mechanics-of-ml|Parr & Howard]] make feature engineering the dominant lever on tabular data — bigger than algorithm choice. Their concrete catalog: categorical encodings ([[LabelEncoding|label]] / [[FrequencyEncoding|frequency]] / [[OneHotEncoding|one-hot]] / [[TargetEncoding|target]]), **synthesizing numeric features** (ratios, string-derived booleans/counts), target transforms ([[LogInExpOut|"log in, exp out"]]), and **injecting external info** — Manhattan distance to desirable neighborhood centers moved apartment OOB 0.868 → 0.872 ("definitely worth trying as a general rule"). Two disciplines: (1) RFs are forgiving — "RFs simply ignore features without much predictive power," so you can stack features freely; (2) never build a feature from the target without fitting on training data only — that is [[DataLeakage|data leakage]].

## In ML systems (mlsysbook)

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) calls feature engineering "frequently the single highest-leverage activity in the ML pipeline, precisely because it changes what signal the model can see" — the *distance to nearest hospital* example reveals a pattern invisible in raw GPS coordinates. The systems constraint: every engineered feature must be computed **identically** in training and serving (the [[TrainingServingConsistency|consistency imperative]]), which is why production systems implement feature logic in shared libraries and adopt [[FeatureStore|feature stores]].

## Connections

- [[FeatureStore]] — materializes feature logic consistently across train/serve.
- [[TrainingServingConsistency]] / [[TrainingServingSkew]] — why feature computation must match.
- [[DataLeakage]] / [[DataSplitting]] — the leakage discipline.
- [[DeepLearning]] / [[Compositionality]] / [[mlsysbook-ch05-neural-computation]] — Ch 5 frames deep learning as eliminating the *feature-engineering bottleneck* via automatic [[RepresentationLearning|representation learning]]: the [[HOG]]/SIFT/Gabor handcrafted descriptors gave way to learned hierarchical features (a network's first conv layers rediscover Gabor-like filters), trading expert tuning for GPU-hours.
- [[mechanics-of-ml]] / [[mlsysbook-ch04-data-engineering]] — sources.
