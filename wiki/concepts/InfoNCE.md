---
title: "InfoNCE"
type: concept
tags: [loss-function, contrastive-learning, mutual-information, representation-learning]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# InfoNCE

**InfoNCE** — *"Information Noise-Contrastive Estimation,"* the contrastive loss introduced by van den Oord, Li & Vinyals in *"Representation Learning with Contrastive Predictive Coding"* (arXiv:1807.03748, 2018). The same loss as **[[NTXentLoss|NT-Xent]]** (Chen et al. 2020 SimCLR) and **[[MultipleNegativesRankingLoss|Multiple Negatives Ranking (MNR) loss]]** (Henderson et al. 2017 / sentence-transformers).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"Multiple negatives ranking (MNR) loss, often referred to as InfoNCE or NTXentLoss, is a loss that uses either positive pairs of sentences or triplets."*

## The loss form

For an anchor $z_i$ with positive $z_j$ and negatives $\{z_k\}_{k \neq j}$:

$$\mathcal{L}_{\text{InfoNCE}} = -\log \frac{\exp(\text{sim}(z_i, z_j) / \tau)}{\sum_k \exp(\text{sim}(z_i, z_k) / \tau)}$$

where $\text{sim}(\cdot, \cdot)$ is typically [[CosineSimilarity|cosine similarity]] and $\tau$ is a temperature hyperparameter. This is **cross-entropy of an in-batch classification** — pick the right positive out of all candidates.

## Why the name "InfoNCE"

InfoNCE is a lower-bound estimator of the **mutual information** between the anchor and its positive: maximizing the InfoNCE objective maximizes a tractable lower bound on $I(z_i; z_j)$. This is the theoretical justification for contrastive representation learning — the learned embeddings preserve the most information shared between paired views of the same underlying object.

## Three names, one loss

The same mathematical loss is known by three names in three communities:

- **InfoNCE** — representation-learning / contrastive predictive coding community (Oord et al. 2018).
- **NT-Xent** (Normalized Temperature-scaled Cross Entropy) — vision contrastive learning community (Chen et al. 2020 SimCLR).
- **MNR loss** (Multiple Negatives Ranking) — sentence-embeddings community (Henderson et al. 2017, used as `MultipleNegativesRankingLoss` in sentence-transformers).

Ch 10 names all three explicitly: *"Multiple negatives ranking (MNR) loss, often referred to as InfoNCE or NTXentLoss."*

## Connections

- [[MultipleNegativesRankingLoss]] — the sentence-transformers name.
- [[NTXentLoss]] — the SimCLR / vision name.
- [[ContrastiveLearning]] — the paradigm InfoNCE instantiates.
- [[InBatchNegatives]] — the negative-sampling mechanism most commonly used with InfoNCE.
- [[MutualInformation]] — the information-theoretic quantity InfoNCE lower-bounds.
- [[NoiseContrastiveEstimation]] — the historical predecessor.
- [[CrossEntropy]] / [[Softmax]] — the underlying classification mechanic.
- [[Word2Vec]] — historical predecessor that used noise-contrastive estimation.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
