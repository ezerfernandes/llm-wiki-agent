---
title: "Hard Negatives"
type: concept
tags: [contrastive-learning, negative-mining, embeddings, sbert]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Hard Negatives

**Hard negatives** — for contrastive embedding-model training, **negatives that are semantically related to the anchor but are NOT the right positive**. The kind of negatives production embedding models actually need to learn nuanced representations.

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"We would like to have negatives that are very related to the question but not the right answer. These negatives are called hard negatives. Since this would make the task more difficult for the embedding model as it has to learn more nuanced representations, the embedding model's performance generally improves quite a bit."*

## Canonical example (Ch 10)

- **Question**: *"How many people live in Amsterdam?"*
- **Positive**: *"Almost a million people live in Amsterdam."*
- **Easy negative**: random unrelated sentence (e.g., *"The cat sat on the mat."*).
- **Semi-hard negative**: related to Amsterdam OR to population, but not both.
- **Hard negative**: *"More than a million people live in Utrecht, which is more than Amsterdam."* — Related to Amsterdam, related to population, but **wrong city / wrong answer**.

The hard negative pushes the model to learn the fine distinction (which city is the subject of the question) rather than relying on topical overlap.

## The three-tier taxonomy

Ch 10 codifies the **easy / semi-hard / hard** mining hierarchy:

| Tier | Definition | How to mine | Cost |
|---|---|---|---|
| **[[EasyNegatives|Easy]]** | Random, unrelated | Random sampling (free, via [[InBatchNegatives|in-batch negatives]]) | Free |
| **[[SemiHardNegatives|Semi-hard]]** | Cosine-similar but not the right pair | Pretrained embedding model + nearest neighbors | Cheap |
| **Hard** | Related but wrong | Manual labeling or generative-model labeling | Expensive |

Per Ch 10: *"Hard negatives often need to be either manually labeled (for instance, by generating semi-hard negatives) or you can use a generative model to either judge or generate sentence pairs."*

## Why hard negatives are expensive

Random sampling produces easy negatives; cosine-similarity mining produces semi-hard negatives — both are cheap. True hard negatives require either:

1. **Manual labeling** — human annotators identify related-but-wrong sentences.
2. **Generative-model labeling** — prompt an LLM to generate plausible-but-wrong answers to a question, or to judge whether a candidate negative is "hard enough."

This is the **bottleneck on production embedding-model quality**: in-batch negatives are free, but the model plateaus quickly; hard negatives unlock higher-quality embeddings but require expensive labeling.

## Connection to AugmentedSBERT

[[AugmentedSBERT]] is one way to **automate hard-negative labeling**: a fine-tuned [[CrossEncoder|cross-encoder]] (trained on a small gold dataset) labels a larger pool of candidate pairs, producing a silver dataset that includes both new positives and new negatives. The cross-encoder's joint-encoding accuracy lets it identify whether a candidate is a hard negative rather than just topically similar.

## Connections

- [[EasyNegatives]] / [[SemiHardNegatives]] — the other tiers.
- [[InBatchNegatives]] — the easy-negative default in MNR loss.
- [[MultipleNegativesRankingLoss]] — the loss function negatives feed.
- [[ContrastiveLearning]] — the paradigm.
- [[AugmentedSBERT]] — one mechanism for cheaper hard-negative labeling.
- [[CrossEncoder]] — the architecture used to label hard negatives in Augmented SBERT.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
