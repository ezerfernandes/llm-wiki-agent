---
title: "NT-Xent Loss"
type: concept
tags: [loss-function, contrastive-learning, simclr, vision]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# NT-Xent Loss

**NT-Xent** — *"Normalized Temperature-scaled Cross Entropy"* — the contrastive loss introduced by Chen, Kornblith, Norouzi & Hinton in *"A Simple Framework for Contrastive Learning of Visual Representations"* (SimCLR, ICML 2020). Mathematically identical to **[[InfoNCE]]** (Oord et al. 2018) and to **[[MultipleNegativesRankingLoss|MNR loss]]** (Henderson et al. 2017 / sentence-transformers).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"Multiple negatives ranking (MNR) loss, often referred to as InfoNCE or NTXentLoss."*

## The loss form

For an anchor $z_i$ with positive $z_j$ and negatives $\{z_k\}_{k \neq j}$:

$$\mathcal{L}_{\text{NT-Xent}} = -\log \frac{\exp(\text{sim}(z_i, z_j) / \tau)}{\sum_{k \neq i} \exp(\text{sim}(z_i, z_k) / \tau)}$$

where $\text{sim}(\cdot, \cdot)$ is L2-normalized cosine similarity and $\tau$ is the temperature.

## Naming breakdown

- **N**ormalized — both vectors are L2-normalized before the dot product, so the similarity score is exactly the cosine similarity.
- **T**emperature-scaled — divide by $\tau$ before the softmax, sharpening or smoothing the distribution.
- **X**ent — Cross-Entropy.

## Position in SimCLR

In Chen et al. 2020, NT-Xent is the loss for the **simple contrastive framework for visual representations**: augment each image into two views, encode both, and use NT-Xent with the two augmented views as the positive pair and all other images in the batch as negatives. This is the **vision-side analog** of what sentence-transformers does with MNR loss for text.

## Connections

- [[InfoNCE]] — the same loss under the representation-learning name.
- [[MultipleNegativesRankingLoss]] — the same loss under the sentence-transformers name.
- [[ContrastiveLearning]] — the paradigm.
- [[SimCLR]] — the vision contrastive framework that introduced the NT-Xent name.
- [[InBatchNegatives]] — the sampling mechanism.
- [[CrossEntropy]] / [[Softmax]] — the underlying mechanic.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
