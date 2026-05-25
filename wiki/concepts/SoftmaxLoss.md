---
title: "Softmax Loss (Sentence-BERT)"
type: concept
tags: [loss-function, contrastive-learning, embeddings, sbert, legacy]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Softmax Loss (Sentence-BERT)

**Softmax loss** — the original training loss for [[SBERT|Sentence-BERT]] in the Reimers & Gurevych 2019 paper. A **3-way classification loss** over [[NLI]] labels (entailment / neutral / contradiction), implemented by concatenating the two sentence embeddings with their element-wise difference and feeding the result into a softmax classifier head.

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"One of the first instances of sentence-transformers uses softmax loss. ... During training, the embeddings for each sentence are concatenated together with the difference between the embeddings. Then, this resulting embedding is optimized through a softmax classifier."*

## Why it is included in Ch 10

For pedagogical / historical reasons only: *"We trained our model using softmax loss to illustrate how one of the first sentence-transformers models was trained. However, not only is there a large variety of loss functions to choose from, but softmax loss is generally not advised as there are more performant losses."*

## Mechanism

For each `(sentence1, sentence2, nli_label)` triple where `nli_label ∈ {0=entailment, 1=neutral, 2=contradiction}`:

1. Encode both sentences with the (siamese) bi-encoder → embeddings `u`, `v`.
2. Concatenate `[u; v; |u - v|]` into a feature vector.
3. Pass through a linear softmax classifier head with `num_labels=3`.
4. Cross-entropy loss against the NLI label.

In sentence-transformers:

```python
train_loss = losses.SoftmaxLoss(
    model=embedding_model,
    sentence_embedding_dimension=embedding_model.get_sentence_embedding_dimension(),
    num_labels=3,
)
```

The chapter notes: *"in softmax loss, we will also need to explicitly set the number of labels"* — unlike the other losses which infer their output shape.

## Worked result in Ch 10

Trained on 50,000 [[MNLI]] pairs (with original 3-way labels), starting from `bert-base-uncased` with [[MeanPooling|mean-pooling]]:

- Loss: `sentence_transformers.losses.SoftmaxLoss(num_labels=3)`
- Result: STS-B Pearson cosine = **0.59** — *"a value of 0.59, which we consider a baseline throughout this chapter."*

This is the **floor** of Ch 10's loss-function ladder. Cosine similarity loss on the same data hits 0.72; MNR loss hits 0.80.

## Why softmax loss underperforms

The structural problem: softmax loss optimizes the **classification head**, not the **embedding geometry**. The embeddings learn to produce features the classifier can separate by NLI label, but those features may not be optimal under [[CosineSimilarity|cosine similarity]] at inference time. The newer losses ([[CosineSimilarityLoss]], [[MultipleNegativesRankingLoss|MNR]]) optimize the embedding geometry directly.

## Connections

- [[CosineSimilarityLoss]] / [[MultipleNegativesRankingLoss]] — the more performant alternatives Ch 10 recommends.
- [[SBERTArchitecture]] / [[SBERT]] — the architecture; softmax was the original training loss.
- [[NaturalLanguageInference]] / [[MNLI]] — the data format softmax loss consumes.
- [[CrossEntropy]] / [[Softmax]] — the underlying classification mechanic.
- [[NilsReimers]] / [[IrynaGurevych]] — Sentence-BERT authors who used softmax loss in the original paper.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
