---
title: "Cosine Similarity"
type: concept
tags: [analytic-geometry, similarity, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Cosine Similarity

The cosine of the angle between two vectors — a magnitude-invariant similarity measure ([[d2l-appendix-mathematics]] §geometry-linear-algebraic-ops):

$$\cos(\theta) = \frac{\mathbf{v}\cdot\mathbf{w}}{\|\mathbf{v}\|\,\|\mathbf{w}\|}.$$

Maximum value $+1$ when $\mathbf{v}$ and $\mathbf{w}$ point in the same direction, minimum $-1$ when they point opposite, and $0$ when they are orthogonal.

## Why magnitude-invariant matters

[[d2l-appendix-mathematics]] §geometry-linear-algebraic-ops motivates cosine similarity via image brightness: an image and its $0.1\times$-brightness duplicate sit at very different Euclidean distances but at *zero* angle to each other — *"the angle between $\mathbf{v}$ and $0.1\mathbf{v}$ is zero."* For most ML applications (image content, document topic, semantic similarity) we want similarity to ignore overall magnitude.

For text counts, doubling the document length doubles the word-count vector but leaves cosine similarity unchanged — exactly the desired behavior.

## Caveat in high dimensions

[[d2l-appendix-mathematics]] flags: *"if the components of high-dimensional vectors are sampled randomly with mean 0, their cosine will nearly always be close to 0."* In $d$ dimensions, two random Gaussian vectors are nearly orthogonal with high probability — so cosine similarity needs to be calibrated against this baseline when used at scale.

## ML uses

- **Embedding similarity**: word / sentence / image embeddings ([[Word2Vec]] / [[GloVe]] / [[BERT]] [CLS] / [[CLIP]] image-text) routinely use cosine similarity for retrieval, clustering, and analogy tasks.
- **[[ContrastiveLearning|Contrastive learning]]** (SimCLR, CLIP, [[InfoNCE]]): the temperature-scaled cosine similarity $\text{sim}(\mathbf{z}_i, \mathbf{z}_j)/\tau$ is the standard score function.
- **[[Attention]]**: scaled dot-product attention $\mathbf{q}^\top\mathbf{k}/\sqrt{d}$ is unnormalized cosine similarity times the magnitudes.
- **[[VectorDatabase|Vector databases]]** ([[Pinecone]], [[Weaviate]], [[Faiss]]) use cosine similarity / inner-product as the primary distance metric.
- **Document retrieval / TF-IDF**: classical pre-neural document search.

## Relation to other distances

| Measure | Formula | Invariance |
|---|---|---|
| Euclidean | $\|\mathbf{v}-\mathbf{w}\|_2$ | none |
| Cosine similarity | $\langle\mathbf{v},\mathbf{w}\rangle/(\|\mathbf{v}\|\|\mathbf{w}\|)$ | magnitude |
| Cosine distance | $1 - \cos\theta$ | magnitude |
| Inner product | $\langle\mathbf{v},\mathbf{w}\rangle$ | none (depends on both magnitude and angle) |

For **unit-norm vectors**, cosine similarity, inner product, and (a monotonic transform of) Euclidean distance all coincide.

## Connections

- [[d2l-appendix-mathematics]] — §geometry-linear-algebraic-ops canonical reference.
- [[InnerProduct]] / [[DotProduct]] — numerator of the cosine.
- [[Norm]] — denominator factors.
- [[Attention]] / [[ScaledDotProductAttention]] — uses unnormalized cosine.
- [[ContrastiveLearning]] / [[InfoNCE]] — modern primary use.
- [[Word2Vec]] / [[GloVe]] / [[CLIP]] — embedding spaces designed for cosine retrieval.
