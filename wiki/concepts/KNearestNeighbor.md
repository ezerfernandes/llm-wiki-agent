---
title: "k-Nearest Neighbor (kNN)"
type: concept
tags: [machine-learning, classification, lazy-learning, instance-based]
sources: [iir-ch14-vector-space-classification, islr-seventh-printing]
last_updated: 2026-05-23
---

Lazy / instance-based classifier: to classify a test point $x$, find the $k$ training points nearest to $x$ (under some distance — typically Euclidean or cosine), and predict the majority class among them. Optionally weight neighbors by inverse distance.

**Properties**:
- **No training phase** — training is just storing the training set. The classifier is fully *lazy*.
- **Decision boundary**: for $k = 1$, the partition of feature space by nearest-neighbor classification is the **[[VoronoiTessellation]]** of the training set.
- **Test-time complexity**: $O(|D| \cdot M_a)$ per test point ($|D|$ = training set size, $M_a$ = average non-zero features) — prohibitive at scale without spatial indexing (KD-trees, locality-sensitive hashing, [[ClusterPruning]]).
- **Bayes-optimal asymptotically**: as $|D| \to \infty$ and $k$ grows appropriately ($k \to \infty$, $k / |D| \to 0$), kNN's error rate is at most twice the Bayes error rate.

**Choosing $k$** is a [[BiasVarianceTradeoff|bias-variance tradeoff]]:
- Small $k$ (e.g. 1) → low bias, high variance (sensitive to training noise).
- Large $k$ → high bias, low variance (oversmooths the decision boundary).

Typically chosen by cross-validation.

**Contrast with [[RocchioClassification]]**: Rocchio summarizes each class as a single centroid (convex regions only); kNN keeps the entire training set and can represent arbitrarily complex decision boundaries — at the cost of test-time computation. Full treatment in [[iir-ch14-vector-space-classification]] and [[islr-seventh-printing]] chapter 2.
