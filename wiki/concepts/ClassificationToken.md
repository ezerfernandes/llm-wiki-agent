---
title: "Classification Token ([CLS])"
type: concept
tags: [nlp, bert, transformers, pretraining]
sources: [d2l-nlp-pretraining, 1810.04805-bert, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Classification Token ([CLS])

The special token prepended to every [[BERT]] input sequence. By convention, the **final hidden state at position 0** (the encoded `[CLS]` token) serves as the **aggregate sequence vector** used for any *sequence-level* classification head — including BERT's own [[NextSentencePrediction|NSP]] pretraining head, and any single-text / text-pair classification fine-tuning task (sentiment, NLI, paraphrase, etc.).

BERT input format:
- Single sequence: `[CLS] tok_1 ... tok_n [SEP]`
- Sentence pair: `[CLS] tok_1 ... tok_n [SEP] tok_1' ... tok_m' [SEP]`

The `[SEP]` token marks segment boundaries; a learned **segment embedding** $\mathbf{e}_A$ or $\mathbf{e}_B$ is added to every position to identify which sentence it belongs to. Per [[d2l-nlp-pretraining]] §bert: the `[CLS]` representation "encodes both the two sentences from the input" thanks to self-attention.

Carried forward into later encoder-only and encoder-decoder models — [[RoBERTa]], ALBERT, DistilBERT, and the [[VisionTransformer|ViT]] `<cls>` token all reuse this convention.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 names `[CLS]` in its BERT special-tokens enumeration: *"A special classification token for classification tasks, as we'll see in Chapter 4."* The chapter's [[deberta|DeBERTa v3]] worked example shows `[CLS]` as **token 0** of the tokenized `"Hello world"` input (`[CLS] Hello world [SEP]`), demonstrating that DeBERTa-family encoders inherit the BERT `[CLS]` / `[SEP]` wrapping convention.

The chapter forward-references **Chapter 4** for the practical fine-tuning recipe that uses the `[CLS]` representation as the classification-head input.
