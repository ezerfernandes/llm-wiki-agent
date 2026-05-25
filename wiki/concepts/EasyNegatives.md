---
title: "Easy Negatives"
type: concept
tags: [contrastive-learning, negative-mining, embeddings, in-batch-negatives]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Easy Negatives

**Easy negatives** — for contrastive embedding-model training, negatives that are **completely unrelated** to the anchor. The cheapest, default tier of the [[HardNegatives|negative mining hierarchy]] [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]] codifies. The kind of negatives [[InBatchNegatives|in-batch negatives]] produce by default in [[MultipleNegativesRankingLoss|MNR loss]] training.

Per Ch 10: *"Easy negatives [are produced] through randomly sampling documents."*

## Why "easy"

Easy negatives are topically unrelated to the anchor — a question about Amsterdam might get a randomly-sampled negative about quantum mechanics, or French cuisine, or sports. The model can discriminate the right positive from these distractors almost trivially via cosine similarity on broad topical features.

This is why MNR loss training with in-batch negatives **plateaus** without further intervention: the model learns to separate topics but doesn't learn the fine-grained distinctions (which city, which person, which date) that production retrieval needs. Ch 10's central observation: *"these in-batch or 'easy' negatives that we used could potentially be completely unrelated to the question. As a result, the embedding model's task of then finding the right answer to a question becomes quite easy."*

## When easy negatives are sufficient

For broad-topic retrieval (cluster-level discrimination), easy negatives suffice. The Ch 10 MNR-on-MNLI worked example reaches **STS-B = 0.80** using only easy in-batch negatives — already a strong score. The case for [[HardNegatives|hard negatives]] is for the **fine-grained, production-retrieval** regime where the model needs to distinguish *"Amsterdam"* from *"Utrecht"* and not just *"Amsterdam"* from *"Eiffel Tower."*

## Connections

- [[HardNegatives]] / [[SemiHardNegatives]] — the other tiers.
- [[InBatchNegatives]] — the default sampling mechanism that produces easy negatives.
- [[ContrastiveLearning]] — the paradigm.
- [[MultipleNegativesRankingLoss]] — the loss function that consumes them.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
