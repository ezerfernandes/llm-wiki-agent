---
title: "In-Batch Negatives"
type: concept
tags: [contrastive-learning, negative-mining, mnr-loss, embeddings]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# In-Batch Negatives

**In-batch negatives** — the default negative-mining strategy in [[MultipleNegativesRankingLoss|MNR loss]] (and most contrastive losses for text embeddings). Inside a training batch of $n$ positive pairs, treat **the other positives in the batch as negatives** for each anchor.

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"In MNR loss, negative pairs are constructed by mixing a positive pair with another positive pair. In the example of a paper title and abstract, you would generate a negative pair by combining the title of a paper with a completely different abstract. These negatives are called in-batch negatives and can also be used to generate the triplets."*

## Mechanism

Given a batch of $n$ positive pairs $(a_1, p_1), (a_2, p_2), \ldots, (a_n, p_n)$:

- For anchor $a_i$, its **positive** is $p_i$.
- Its **negatives** are $p_j$ for all $j \neq i$ — the **other** positives in the batch, re-purposed as distractor negatives for this particular anchor.

The training step: for each anchor, the model must pick its true positive out of the $n$ candidates ($1$ positive + $n-1$ in-batch negatives) by cosine similarity. This is treated as a classification problem with cross-entropy loss (see [[MultipleNegativesRankingLoss]]).

## Why batch size matters

Per Ch 10: *"Larger batch sizes tend to work better with multiple negative rankings (MNR) loss as a larger batch makes the task more difficult. The reason for this is that the model needs to find the best matching sentence from a larger set of potential pairs of sentences."*

The bigger the batch, the more in-batch negatives per anchor, the harder the discrimination task, the richer the representation. This is the **structural reason** MNR-loss training typically runs at the largest batch size that fits in GPU memory.

## Limitation — easy negatives

In-batch negatives are **[[EasyNegatives|easy negatives]]** by default: randomly-sampled positives from the same batch are usually completely unrelated to the anchor. Per Ch 10: *"there is a downside to how we used this loss function. Since negatives are sampled from other question/answer pairs, these in-batch or 'easy' negatives that we used could potentially be completely unrelated to the question. As a result, the embedding model's task of then finding the right answer to a question becomes quite easy. Instead, we would like to have negatives that are very related to the question but not the right answer. These negatives are called [[HardNegatives|hard negatives]]."*

Production embedding models therefore **supplement in-batch negatives with explicit hard negatives** to push the model harder.

## Connections

- [[MultipleNegativesRankingLoss]] — the loss function in-batch negatives serve.
- [[HardNegatives]] / [[SemiHardNegatives]] / [[EasyNegatives]] — the broader negatives taxonomy.
- [[ContrastiveLearning]] — the paradigm.
- [[SentenceTransformers]] — the library that defaults to in-batch negatives.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
