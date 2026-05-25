---
title: "Token Classification"
type: concept
tags: [nlp, fine-tuning, sequence-labeling, token-level]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Token Classification

**Token classification** is the family of NLP tasks where the model predicts a label **per token** in a sequence — as opposed to *sequence* classification which predicts a single label per document. Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"Rather than relying on the aggregation or pooling of token embeddings, the model now makes predictions for individual tokens in a sequence."*

The most common token-classification task is **[[NamedEntityRecognition|named-entity recognition]] (NER)**; others include **part-of-speech tagging**, **chunking**, and **semantic role labeling**.

## Architectural change vs sequence classification

| Aspect | [[SequenceClassificationHead|Sequence classification]] | Token classification |
|---|---|---|
| Head | Linear on pooled `[CLS]` | Linear applied per-position |
| Output shape | `(batch, num_classes)` | `(batch, seq_len, num_classes)` |
| Model class | `AutoModelForSequenceClassification` | `AutoModelForTokenClassification` |
| Data collator | [[DataCollatorWithPadding]] | [[DataCollatorForTokenClassification]] |
| Labels | one int per document | one int per token |
| Loss ignored on | (typically none) | `-100` positions (special tokens, padding) |

## Subtoken alignment

Because [[bert|BERT]]-class models use [[WordPiece]] subword tokenization, a word may be split across multiple tokens. The supervision signal usually comes at the word level (from human annotators), so labels must be **aligned** to subtokens before training. The Ch 11 convention:

- First subtoken of each word inherits the word's label (with `B-` prefix for entity types in BIO tagging).
- Continuation subtokens get the `I-` prefix (computed via the `(label + 1) if label is odd` trick exploiting the B-=odd / I-=even ordering).
- `[CLS]`, `[SEP]`, and pad positions get `-100` so the loss function ignores them.

See [[LabelAlignment]] for the full code recipe.

## Evaluation

Token-level F1 is computed via [[seqeval|`seqeval`]] (Hugging Face `evaluate` package). `seqeval` is **span-aware** — it knows BIO-tag semantics and only counts a span as correct if both its start and end are predicted correctly. This is stricter than naive per-token F1.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[NamedEntityRecognition]] — the most common token-classification task.
- [[BIOTagging]] — the standard label scheme.
- [[LabelAlignment]] — the word-to-subtoken mapping step.
- [[DataCollatorForTokenClassification]] — the batch-building helper.
- [[TokenClassificationHead]] — the architectural head.
- [[seqeval]] — span-level evaluation.
- [[FineTuningBert]] — the broader fine-tuning template (Ch 11's *"token-level tagging"* row).
- [[CoNLL2003]] — canonical dataset.
