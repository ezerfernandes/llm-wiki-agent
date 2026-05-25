---
title: "STS-B (Semantic Textual Similarity Benchmark)"
type: concept
tags: [benchmark, dataset, evaluation, sts, embeddings, glue]
sources: [hands-on-llm-ch10-creating-text-embedding-models, d2l-nlp-applications]
last_updated: 2026-05-23
---

# STS-B (Semantic Textual Similarity Benchmark)

**STS-B** — the **Semantic Textual Similarity Benchmark** dataset, the canonical evaluation suite for sentence-embedding models. Part of the [[GLUE]] benchmark. Per Cer, Diab, Agirre, Lopez-Gazpio & Specia 2017.

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"We can perform evaluation of the performance of our model using the Semantic Textual Similarity Benchmark (STSB). It is a collection of human-labeled sentence pairs, with similarity scores between 1 and 5."*

## Structure

- **Pairs**: ~8,628 human-labeled sentence pairs across the train / validation / test splits.
- **Score range**: 0 to 5 (continuous), where 0 = no meaning overlap and 5 = full meaning equivalence.
- **Sources**: image captions, news headlines, forum discussions.
- **Annotation**: each pair scored by multiple human annotators; the published score is the mean.

## Sample annotations

| Sentence 1 | Sentence 2 | Score |
|---|---|---|
| *"A plane is taking off."* | *"An air plane is taking off."* | **5.000** |
| *"A woman is eating something."* | *"A woman is eating meat."* | **3.000** |
| *"A woman is dancing."* | *"A man is talking."* | **0.000** |

## Use in Ch 10

Ch 10 uses STS-B as the **evaluator for every training run**: load `glue/stsb/validation`, rescale labels from `[0, 5]` to `[0, 1]` by dividing by 5, then evaluate via `sentence_transformers.evaluation.EmbeddingSimilarityEvaluator` with `main_similarity="cosine"`.

```python
val_sts = load_dataset("glue", "stsb", split="validation")
evaluator = EmbeddingSimilarityEvaluator(
    sentences1=val_sts["sentence1"],
    sentences2=val_sts["sentence2"],
    scores=[score/5 for score in val_sts["label"]],
    main_similarity="cosine",
)
```

The evaluator returns Pearson and Spearman correlations under cosine, manhattan, euclidean, and dot-product distance — Ch 10 reports **Pearson cosine** as the headline metric. *"The one we are interested in most is 'pearson_cosine', which is the cosine similarity between centered vectors. It is a value between 0 and 1 where a higher value indicates higher degrees of similarity."*

## Why STS-B (not MTEB) in Ch 10

Per Ch 10: *"Since testing your model on the entire [[MTEB]] can take a couple of hours depending on your GPU, we will use the STSB benchmark throughout this chapter instead for illustration purposes."*

STS-B is the **single-task quick evaluator**; [[MTEB]] is the **multi-task production rubric**.

## Position in the wiki

STS-B is also covered in [[SemanticTextualSimilarity]] (the D2L-source page on the task) — that page treats STS-B in the BERT fine-tuning context where the regression head outputs a similarity score. Ch 10 uses STS-B from the **cosine-similarity-of-embeddings** angle instead: no regression head, just `cos_sim(emb(s1), emb(s2))` compared to the human label.

## Connections

- [[GLUE]] — the parent benchmark suite STS-B belongs to.
- [[SemanticTextualSimilarity]] — the task STS-B benchmarks.
- [[MTEB]] — the broader multi-task evaluator.
- [[CosineSimilarity]] — the distance metric Ch 10 evaluates against.
- [[CosineSimilarityLoss]] — the loss function directly aligned with STS-B-style scoring.
- [[SBERTArchitecture]] / [[SBERT]] — the model family STS-B evaluates.
- [[SentenceTransformers]] — implements `EmbeddingSimilarityEvaluator`.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
- [[d2l-nlp-applications]] — covers STS-B in the BERT-regression framing.
