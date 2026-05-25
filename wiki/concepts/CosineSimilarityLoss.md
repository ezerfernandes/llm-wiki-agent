---
title: "Cosine Similarity Loss"
type: concept
tags: [loss-function, contrastive-learning, embeddings, sbert, sts]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Cosine Similarity Loss

**Cosine similarity loss** — a contrastive loss for training [[SentenceTransformers|sentence-transformers]]-style embedding models on **graded similarity** data (pairs labeled with a continuous similarity score in `[0, 1]`).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"The cosine similarity loss is an intuitive and easy-to-use loss that works across many different use cases and datasets. It is typically used in semantic textual similarity tasks."*

## Mechanism

Per Ch 10: *"Cosine similarity loss is straightforward — it calculates the cosine similarity between the two embeddings of the two texts and compares that to the labeled similarity score. The model will learn to recognize the degree of similarity between sentences."*

For each `(sentence1, sentence2, similarity_label)` triple:

1. Encode both sentences with the (siamese) bi-encoder.
2. Compute the [[CosineSimilarity|cosine similarity]] of the two embeddings.
3. Compare to the labeled `similarity_label` (in `[0, 1]`).
4. Backprop the squared deviation (or similar).

## Data format

Per Ch 10: *"Cosine similarity loss intuitively works best using data where you have pairs of sentences and labels that indicate their similarity between 0 and 1."* This is the **[[SemanticTextualSimilarity|STS]]-style** data format — graded similarity scores rather than binary positive/negative or three-way NLI labels.

## Adapting NLI data to cosine loss

Ch 10's worked example uses [[MNLI]] for cosine loss by **relabeling the three NLI labels into two graded values**:

- Entailment (label 0) → **1.0** (high similarity)
- Neutral (label 1) → **0.0** (dissimilarity)
- Contradiction (label 2) → **0.0** (dissimilarity)

```python
mapping = {2: 0, 1: 0, 0: 1}
train_dataset = Dataset.from_dict({
    "sentence1": train_dataset["premise"],
    "sentence2": train_dataset["hypothesis"],
    "label": [float(mapping[label]) for label in train_dataset["label"]]
})
```

Per Ch 10: *"the entailment represents a high similarity between the sentences, so we give it a similarity score of 1. In contrast, since both neutral and contradiction represent dissimilarity, we give these labels a similarity score of 0."*

## Worked result in Ch 10

Trained on 50,000 [[MNLI]] pairs (with the entailment/neutral/contradiction → 1/0/0 mapping), starting from `bert-base-uncased`:

- Loss: `sentence_transformers.losses.CosineSimilarityLoss`
- Result: STS-B Pearson cosine = **0.72** (vs softmax loss 0.59 on the same data).
- *"A Pearson cosine score of 0.72 is a big improvement compared to the softmax loss example, which scored 0.59. This demonstrates the impact the loss function can have on performance."*

## Cosine vs MNR loss

Cosine loss is the **simpler, more general-purpose loss**; MNR loss is **more performant but requires (anchor, positive) or (anchor, positive, negative) data** rather than graded similarity. Ch 10's ladder positions cosine loss as the **between** option — better than softmax (0.59 → 0.72) but worse than MNR (0.72 → 0.80) on the same MNLI data. The right choice depends on what data you have:

- **Graded similarity scores in [0,1]** → cosine loss.
- **Positive pairs (or triplets)** → MNR loss.
- **3-way classification labels (entailment/neutral/contradiction)** → softmax loss (legacy; not recommended).

## Connections

- [[CosineSimilarity]] — the underlying similarity metric.
- [[MultipleNegativesRankingLoss]] — Ch 10's more performant alternative.
- [[SoftmaxLoss]] — Ch 10's less performant alternative.
- [[SemanticTextualSimilarity]] / [[STSB]] — the canonical data format for cosine loss.
- [[SBERTArchitecture]] / [[SentenceTransformers]] — the architecture and library.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
