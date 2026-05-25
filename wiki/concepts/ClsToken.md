---
title: "`<cls>` Token"
type: concept
tags: [transformer, embedding]
sources: [d2l-attention-and-transformers, d2l-nlp-applications, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# `<cls>` Token

A special learnable token prepended to the input sequence whose final-layer representation serves as a **global / sequence-level summary**. Introduced by [[BERT]] for sentence classification and adopted by the [[VisionTransformer|Vision Transformer]] for image classification.

## Mechanism

The `<cls>` (class) token starts as a learnable embedding (no special semantic content). It participates in every self-attention layer like any other token — but because attention is all-to-all, after a few layers `<cls>` aggregates information from all other positions. Its final-layer representation is fed to a downstream classification head.

## Two canonical uses

- **[[BERT]]** — `<cls>` representation → linear head → sentiment / classification logits. Also used for the next-sentence-prediction pretraining objective. [[d2l-nlp-applications]] §`finetuning-bert` shows the `<cls>` hidden state is the **universal handle** for sequence-level fine-tuning ([[SentimentAnalysis]] / [[NaturalLanguageInference|NLI]] / [[SemanticTextualSimilarity|STS]]) — see [[FineTuningBert]].
- **[[VisionTransformer|ViT]]** — `<cls>` representation, after a final LayerNorm, → linear layer → image-class logits.

## Alternatives

- **Averaged patch / token representations.** Equivalent in some settings; the [[d2l-attention-and-transformers|D2L exercise]] suggests projecting the average instead of `<cls>`.
- **Learned pooling tokens.** Multiple cls-like tokens for multi-label or multi-task settings.

## See also

- [[VisionTransformer]] · [[BERT]] · [[Transformer]] · [[PatchEmbedding]] · [[SelfAttention]]
- [[ClassificationToken]] — the BERT-context-specific page on `[CLS]`.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 includes `[CLS]` in its BERT special-tokens enumeration; also appears in the [[deberta|DeBERTa v3]] `"Hello world"` worked example (tokenized as `[CLS] Hello world [SEP]`).

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 documents a **CLIP-specific override** of the BERT convention: *"In CLIP, the [CLS] token is actually used to represent the image embedding, not the text embedding."* — the inverse of [[BERT]]'s text-side-aggregator convention. The chapter's worked tokenization of *"a puppy playing in the snow"* via `CLIPTokenizerFast` returns `['<|startoftext|>', 'a</w>', 'puppy</w>', 'playing</w>', 'in</w>', 'the</w>', 'snow</w>', '<|endoftext|>']` — **without a `[CLS]` on the text side** — because in CLIP the `[CLS]` aggregator role has been **reassigned to the image branch** (the [[VisionTransformer|ViT]]). This is a wiki-novel observation; prior wiki coverage of `[CLS]` (BERT / ViT / DeBERTa) followed the standard text-side or image-side aggregator convention without flagging the cross-architecture role swap CLIP performs.
