---
name: HashingTrick
title: "Hashing Trick"
type: concept
tags: [feature-engineering, categorical-encoding, online-learning]
sources: [dmls-ch05-feature-engineering]
last_updated: 2026-05-23
---

# Hashing Trick

Technique for encoding **categorical features with unbounded or dynamic vocabularies** by hashing each category into a fixed-size integer space, then one-hot-encoding the hash. Popularized by [[VowpalWabbit]] (Microsoft); ships in [[sklearn]] / [[TensorFlow]] / [[Gensim]]. Per [[ChipHuyen|Huyen]]'s [[dmls-ch05-feature-engineering|DMLS Ch 5]] the canonical fix for the production failure mode of [[OneHotEncoding|one-hot encoding]] (unseen categories at inference time).

## How
Choose a hash space size `N` (typically a power of 2). For each raw category `c`, compute `index = hash(c) % N`. Use `index` as the dense or one-hot vector position.

## Why it works in production
- **Constant-time lookup** — no vocabulary table to grow or sync.
- **Open vocabulary** — unseen categories at inference time hash to *some* bucket (vs. [[OneHotEncoding|one-hot]]'s "unknown" bucket or crash).
- **Fixed memory** — vector dimension is `N`, regardless of how many distinct categories the production stream has ever seen.
- **Collision tolerance is high**: Lucas Bernardi at [[Booking|Booking.com]] (2018) found ~50% collisions degrade [[CTRPrediction]] log-loss by <0.5%.

## Special value in continual learning
For [[ContinualLearning|continually-trained]] models the hash trick is doubly useful: the model never has to be re-architected when a new category appears in production, because the input space is fixed by the hash function.

## Trade-offs
- **Information loss** under collisions — two distinct categories share one bucket.
- **Not interpretable** — hash buckets are opaque vs. labeled one-hot positions.
- **Hash-function choice matters** — bad hash → uneven bucket utilization → wasted parameters.

## Connections
- [[FeatureEngineering]] — Ch 5 categorical-encoding section.
- [[OneHotEncoding]] — the brittle production-failure-mode it replaces.
- [[LabelEncoding]] — sibling categorical-encoding scheme with different brittleness profile.
- [[VowpalWabbit]] — the implementation that popularized the technique.
- [[CTRPrediction]] / [[RecommenderSystems]] — the canonical applications.
