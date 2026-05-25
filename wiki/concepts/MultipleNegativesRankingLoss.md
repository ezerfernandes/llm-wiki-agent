---
title: "Multiple Negatives Ranking Loss (MNR Loss)"
type: concept
tags: [loss-function, contrastive-learning, embeddings, sbert, infonce, ntxent]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Multiple Negatives Ranking Loss (MNR Loss)

**Multiple Negatives Ranking (MNR) loss** — the contrastive loss function that became the production default for training [[SentenceTransformers|sentence-transformers]]-style [[BiEncoder|bi-encoder]] embedding models. Also known as **[[InfoNCE]]** and **[[NTXentLoss|NT-Xent]]** loss in adjacent literatures.

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"Multiple negatives ranking (MNR) loss, often referred to as InfoNCE or NTXentLoss, is a loss that uses either positive pairs of sentences or triplets that contain a pair of positive sentences and an additional unrelated sentence."*

## References

- Matthew Henderson et al. *"Efficient natural language response suggestion for smart reply."* arXiv:1705.00652 (2017). (The original MNR formulation.)
- Aaron van den Oord, Yazhe Li, and Oriol Vinyals. *"Representation learning with contrastive predictive coding."* arXiv:1807.03748 (2018). (InfoNCE.)
- Ting Chen et al. *"A simple framework for contrastive learning of visual representations."* ICML 2020 (PMLR). (SimCLR's NT-Xent.)

## Data format

- **Positive pairs**: `(anchor, positive)` — *"question/answer, image/image caption, paper title/paper abstract, etc."* — pairs known to be related.
- **Triplets**: `(anchor, positive, negative)` — adds an explicitly unrelated sentence.

## Mechanism — in-batch negatives

Per Ch 10: *"In MNR loss, negative pairs are constructed by mixing a positive pair with another positive pair. In the example of a paper title and abstract, you would generate a negative pair by combining the title of a paper with a completely different abstract. These negatives are called **in-batch negatives** and can also be used to generate the triplets."*

The training step:

1. Embed all anchors and all positives (and negatives if triplets) in the batch.
2. For each anchor, compute its [[CosineSimilarity|cosine similarity]] to every other positive/negative in the batch.
3. Treat it as a **classification problem**: which of the in-batch items is the right pair for this anchor? Optimize with [[CrossEntropy|cross-entropy loss]].

Per Ch 10: *"After having generated these positive and negative pairs, we calculate their embeddings and apply cosine similarity. These similarity scores are then used to answer the question, are these pairs negative or positive? In other words, it is treated as a classification task and we can use cross-entropy loss to optimize the model."*

## Batch size matters

Ch 10's mechanical observation appears twice in the chapter: *"Larger batch sizes tend to work better with multiple negative rankings (MNR) loss as a larger batch makes the task more difficult. The reason for this is that the model needs to find the best matching sentence from a larger set of potential pairs of sentences."*

The bigger the batch, the more "distractor" negatives the model has to compete against, and the harder/better the learned representation becomes. This is **the structural reason MNR loss training tends to run at the largest batch size that fits in GPU memory** (compare to softmax loss / cosine loss, which are batch-size-agnostic to first order).

## Easy / semi-hard / hard negatives

The default in-batch negatives are **[[EasyNegatives|easy negatives]]**: random other positives in the batch, usually completely unrelated to the anchor. Per Ch 10: *"these in-batch or 'easy' negatives that we used could potentially be completely unrelated to the question. As a result, the embedding model's task of then finding the right answer to a question becomes quite easy."*

Production embedding models supplement in-batch negatives with **[[HardNegatives|hard negatives]]** (related-but-wrong) via either manual labeling or generative-model labeling.

## Worked result in Ch 10

Trained on 16,875 [[MNLI]] entailment triplets (50k pairs filtered to entailment-only, with shuffled hypotheses as easy negatives), starting from `bert-base-uncased` with [[MeanPooling|mean-pooling]]:

- Loss: `sentence_transformers.losses.MultipleNegativesRankingLoss`
- Result: STS-B Pearson cosine = **0.80** (vs softmax loss 0.59, cosine loss 0.72).
- *"Compared to our previously trained model with softmax loss (0.72), our model with MNR loss (0.80) seems to be much more accurate!"*

## Connections

- [[InfoNCE]] / [[NTXentLoss]] — alternative names from adjacent literatures.
- [[ContrastiveLearning]] — the training paradigm MNR loss instantiates.
- [[InBatchNegatives]] — the negative-mining mechanism.
- [[HardNegatives]] / [[SemiHardNegatives]] / [[EasyNegatives]] — the negative-quality hierarchy.
- [[CosineSimilarityLoss]] / [[SoftmaxLoss]] — the alternative losses in Ch 10's worked ladder.
- [[CrossEntropy]] / [[CrossEntropyLoss]] — the underlying optimization mechanic.
- [[SentenceTransformers]] — the library implementing it as `losses.MultipleNegativesRankingLoss`.
- [[SBERTArchitecture]] — the architecture this loss trains.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
