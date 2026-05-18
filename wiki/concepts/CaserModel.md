---
title: "Caser (Convolutional Sequence Embedding Recommendation)"
type: concept
tags: [recommender-systems, cnn, sequence-aware, deep-learning]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Caser — Convolutional Sequence Embedding Recommendation

**Sequence-aware recommender using CNN over recent item history** ([[JiaxiTang|Tang]] & [[KeWang|Wang]] 2018, *WSDM*). Captures users' *short-term* intent while preserving a separate *long-term* (general-taste) embedding.

## Setup

For user $u$ at time $t$, take the previous $L$ interacted items and look up their embeddings:

$$\mathbf{E}^{(u,t)} = [\mathbf{q}_{S_{t-L}^u}, \ldots, \mathbf{q}_{S_{t-1}^u}]^\top \in \mathbb{R}^{L\times k}$$

Treat $\mathbf{E}^{(u,t)}$ as an "image" of shape $L\times k$ and apply two parallel convolutional networks:

- **Horizontal convolutions** with filters $\mathbf{F}^j\in\mathbb{R}^{h\times k}$ for $h\in\{1,\ldots,L\}$ capture **union-level patterns** — *"buying both milk and butter together leads to higher probability of buying flour than just buying one of them."*
- **Vertical convolutions** with filters $\mathbf{G}^j\in\mathbb{R}^{L\times 1}$ capture **point-level patterns** — single-item-to-target influences.

After convolution + max-pooling, concatenate the two outputs:

$$\mathbf{z} = \phi(\mathbf{W}[\mathbf{o}, \mathbf{o}']^\top + \mathbf{b}) \in \mathbb{R}^k$$

representing the user's short-term intent.

## Prediction

Combine short-term $\mathbf{z}$ with a separately-learned long-term user embedding $\mathbf{p}_u$, and score against item $i$:

$$\hat{y}_{uit} = \mathbf{v}_i\cdot[\mathbf{z}, \mathbf{p}_u]^\top + b'_i$$

## Training

- Sequential dataset with negative sampling — for each $(u, \text{history}, i^+)$ training sample, sample $j^-$ from unobserved items.
- [[BPR]] or [[HingeLossRanking|Hinge]] loss.
- `seq-aware` MovieLens split.

## Alternatives flagged

- **GRU4Rec** ([[Hidasi]] et al. 2015) — session-based RNN approach, the canonical pre-Caser sequence-aware model.
- Session-based recommendation in general is flagged as a sibling task in the chapter exercises.

## Connections
- [[SequenceAwareRecommendation]] — parent task.
- [[ConvolutionalLayer]] — primitive.
- [[BPR]], [[HingeLossRanking]] — training losses.
- [[NeuMF]] — non-sequence-aware sibling.
- [[d2l-recommender-systems]] — source §seqrec.
