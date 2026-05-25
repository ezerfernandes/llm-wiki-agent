---
title: "Semi-Hard Negatives"
type: concept
tags: [contrastive-learning, negative-mining, embeddings]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Semi-Hard Negatives

**Semi-hard negatives** — the middle tier of the [[HardNegatives|negatives mining hierarchy]] [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]] codifies: sentences that are **cosine-similar to the anchor but are not the right positive**, typically mined via a pretrained embedding model's nearest-neighbor search.

Per Ch 10's mining recipe: *"using a pretrained embedding model, we can apply cosine similarity on all sentence embeddings to find those that are highly related. Generally, this does not lead to hard negatives since this method merely finds similar sentences, not question/answer pairs."*

## Why "semi-hard"

Semi-hard negatives are **topically similar** to the anchor (they share words / domain / theme) but are not the right answer — they're harder than [[EasyNegatives|easy negatives]] (random documents) but easier than true [[HardNegatives|hard negatives]] (related-but-wrong answers). The cosine-similarity mining catches topical overlap but cannot reliably distinguish between *"this sentence is related to the question's topic"* and *"this sentence is the right answer to the question."*

## Use as a labeling-pipeline stepping stone

Per Ch 10: *"Hard negatives often need to be either manually labeled (for instance, by generating semi-hard negatives) or you can use a generative model to either judge or generate sentence pairs."*

The pattern: **mine semi-hard negatives cheaply, then upgrade them to hard negatives via human or LLM judgment**. The semi-hard pool is the candidate set for the more expensive hard-negative labeling pass.

## Connections

- [[HardNegatives]] / [[EasyNegatives]] — the other tiers in the hierarchy.
- [[InBatchNegatives]] — the easy-negative default.
- [[ContrastiveLearning]] — the paradigm.
- [[MultipleNegativesRankingLoss]] — the loss function negatives feed.
- [[AugmentedSBERT]] — the cross-encoder-labeling approach that automates the semi-hard → hard upgrade.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
