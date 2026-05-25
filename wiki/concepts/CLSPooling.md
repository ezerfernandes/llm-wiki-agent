---
title: "CLS Pooling"
type: concept
tags: [pooling, embeddings, sentence-embeddings, bert, tsdae]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# CLS Pooling

**[CLS]-token pooling** — for [[bert|BERT]]-family encoders, the strategy of producing a single fixed-dim sentence vector by **taking the final-layer hidden state of the special `[CLS]` token** (position 0). The BERT-paper default for sentence-level downstream tasks (classification, NLI), and the [[TSDAE]]-recommended pooling for unsupervised denoising auto-encoder training.

## In [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 introduces [CLS]-pooling **only in the [[TSDAE]] section**, as the **one regime where [CLS]-pooling outperforms [[MeanPooling|mean-pooling]]**:

> *"We run the training as before but with the [CLS] token as the pooling strategy instead of the mean pooling of the token embeddings. In the TSDAE paper, this was shown to be more effective since mean pooling loses the position information, which is not the case when using the [CLS] token."* — Ch 10 on TSDAE pooling.

The rationale Ch 10 gives is **position information**: mean-pooling averages across all positions and discards positional order; the [CLS] token, having attended to every other position through self-attention, retains a position-aware summary. For the denoising-auto-encoder reconstruction objective — where reproducing the original sentence requires getting positions right — [CLS]-pooling beats mean-pooling.

## In the broader Sentence-BERT literature

For the **supervised contrastive** regime (the main SBERT use case), Ch 10 cites Reimers & Gurevych's Sentence-BERT paper finding the opposite: *"A solution to this overhead is to generate embeddings from a BERT model by averaging its output layer or using the [CLS] token. This, however, has shown to be worse than simply averaging word vectors, like GloVe."* In the supervised contrastive regime, **mean-pooling wins**; in TSDAE's unsupervised denoising regime, **[CLS]-pooling wins**. The choice is regime-specific.

## In CLIP

In [[CLIP]] (per [[hands-on-llm-ch09-multimodal-llms|Ch 9]]), *"the [CLS] token is actually used to represent the image embedding"* — the inverse of BERT's text-side convention. So [CLS]-pooling has at least three distinct uses in the wiki: BERT classification head, TSDAE sentence embedding, and CLIP image embedding.

## Implementation

In sentence-transformers:

```python
from sentence_transformers import models, SentenceTransformer

word_embedding_model = models.Transformer("bert-base-uncased")
pooling_model = models.Pooling(
    word_embedding_model.get_word_embedding_dimension(),
    "cls",  # vs the default "mean"
)
embedding_model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
```

## Connections

- [[MeanPooling]] — the default; [CLS]-pooling is the regime-specific exception.
- [[TSDAE]] — the unsupervised regime where [CLS]-pooling is preferred.
- [[ClsToken]] — the BERT special token this pooling extracts.
- [[SBERTArchitecture]] — the broader pooling-layer context.
- [[Pooling]] — the parent concept.
- [[CLIP]] — the multimodal model where `[CLS]` represents the **image** embedding (Ch 9).
- [[bert|BERT]] — the encoder that defines the [CLS] token convention.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
