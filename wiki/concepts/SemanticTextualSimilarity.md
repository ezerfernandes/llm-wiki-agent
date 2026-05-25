---
title: "Semantic Textual Similarity"
type: concept
tags: [nlp, text-pair-regression, application]
sources: [d2l-nlp-applications, hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Semantic Textual Similarity

**Semantic textual similarity (STS)** measures the meaning-similarity of a pair of sentences as a continuous value — a canonical *text-pair regression* task. Per [[d2l-nlp-applications]] §`finetuning-bert`: "in the Semantic Textual Similarity Benchmark dataset, the similarity score of a pair of sentences is an ordinal scale ranging from 0 (no meaning overlap) to 5 (meaning equivalence)" (Cer, Diab, Agirre et al. 2017).

## Examples (STS-B)

| Sentence 1 | Sentence 2 | Score |
|---|---|---|
| "A plane is taking off." | "An air plane is taking off." | 5.000 |
| "A woman is eating something." | "A woman is eating meat." | 3.000 |
| "A woman is dancing." | "A man is talking." | 0.000 |

## Fine-tuning [[BERT]]

Same input template as [[NaturalLanguageInference|NLI]] — `[CLS] A [SEP] B [SEP]` with segment ids — but the head outputs a single continuous value (regression), trained with mean squared error instead of cross-entropy.

## Connections

- [[NaturalLanguageInference]] — the closely-related *classification* twin task.
- [[BERT]] / [[FineTuningBert]] — the canonical model template.
- [[d2l-nlp-applications]] §`finetuning-bert`.

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 uses STS-B as **the evaluator for every embedding-model training regime** in the chapter's loss-function ladder. The framing differs from D2L's BERT-fine-tune-as-regression approach: Ch 10 evaluates by computing the **cosine similarity of two embeddings** (one per sentence, produced by the [[BiEncoder|bi-encoder]] under test) and correlating against the human-labeled similarity score — no regression head.

> *"We can perform evaluation of the performance of our model using the Semantic Textual Similarity Benchmark (STSB). It is a collection of human-labeled sentence pairs, with similarity scores between 1 and 5. ... We process the STSB data to make sure all values are between 0 and 1."* — Ch 10

The Ch 10 evaluator is `sentence_transformers.evaluation.EmbeddingSimilarityEvaluator` with `main_similarity="cosine"`, returning Pearson and Spearman correlations under cosine / manhattan / euclidean / dot-product. *"The one we are interested in most is 'pearson_cosine', which is the cosine similarity between centered vectors."*

The full evaluator output also includes other distance metrics:

```
{'pearson_cosine': 0.8093892326162132,
 'spearman_cosine': 0.8121064796503025,
 'pearson_manhattan': 0.8215001523827565,
 ...}
```

Ch 10's loss-function ladder is benchmarked against STS-B Pearson cosine: softmax loss 0.59 → cosine loss 0.72 → MNR loss 0.80 → fine-tune MiniLM-L6-v2 with MNR 0.85. The **STS-B-as-fast-evaluator role** for embedding-model training is the [[hands-on-llm-ch10-creating-text-embedding-models|Ch 10]] contribution to this page — vs the D2L-source-page framing of STS-B as a BERT fine-tuning task.

See [[STSB]] for the dataset-level page.
