---
title: "Sequence-Aware Recommendation"
type: concept
tags: [recommender-systems, sequence-modeling]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Sequence-Aware Recommendation

Recommender-systems sub-family in which **the input is an ordered, timestamped sequence of user actions** rather than a static `(user, item, rating)` tuple. Surveyed by [[Quadrana]], [[Cremonesi]] & [[DietmarJannach|Jannach]] 2018 (*ACM Computing Surveys*).

## Why sequence

User interests *drift* over time (genres they like this week vs last year), and recent actions strongly predict the next action (a watch session, a shopping cart). Static CF on $(u,i,r)$ collapses this temporal structure into a bag-of-interactions and misses both **short-term intent** and **long-term-vs-recent decomposition**.

## Canonical models

- **[[CaserModel|Caser]]** ([[JiaxiTang|Tang]] & [[KeWang|Wang]] 2018) — CNN over the last $L$-item embedding matrix; the chapter's representative implementation.
- **GRU4Rec** ([[Hidasi]], [[Karatzoglou]], [[Baltrunas]] & Tikk 2015) — session-based recurrent recommender; flagged as the exercise alternative.
- **SASRec** (Kang & McAuley 2018), **BERT4Rec** (Sun et al. 2019) — self-attention / Transformer extensions (D2L doesn't implement these but they're the modern successors).

## Training-data construction

- `seq-aware` split: sort each user's interactions by timestamp, leave out the most-recent one for test.
- Window of length $L$ slides over the history; each window's last item is the target, the prior $L-1$ are the context.
- Negative samples drawn from the user's non-interacted items.

## Session-based vs sequence-aware

The chapter (exercise §seqrec) flags **session-based recommendation** as a related but distinct task — there the input is a short anonymous session (no persistent user identity); sequence-aware assumes a known user with long history. Same architectural primitives, different evaluation setup.

## Connections
- [[CaserModel]] — primary chapter implementation.
- [[RecommenderSystems]] — parent.
- [[CollaborativeFiltering]] — broader context.
- [[ImplicitFeedback]] — typical data regime.
- [[BPR]], [[HingeLossRanking]] — training losses.
- [[GRU]], [[ConvolutionalLayer]], [[SelfAttention]] — architectural primitives across the model family.
- [[d2l-recommender-systems]] — source §seqrec.
