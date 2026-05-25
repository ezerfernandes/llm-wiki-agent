---
title: "BIO Tagging"
type: concept
tags: [nlp, sequence-labeling, ner, token-classification, tagging-scheme]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# BIO Tagging

**BIO (Beginning / Inside / Outside)** is the canonical token-level label scheme for marking entity spans in [[NamedEntityRecognition|NER]] and other [[TokenClassification|token-classification]] tasks. Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"These entities are prefixed with either a B (beginning) or an I (inside). If two tokens that follow each other are part of the same phrase, then the start of that phrase is indicated with B, which is followed by an I to show that they belong to each other and are not independent entities."*

## Why prefixes are needed

Without B/I prefixes, adjacent same-class tokens would be ambiguous. Example: *"Dean Palmer"* could mean:

- **One** person named Dean Palmer → `B-PER I-PER`
- **Two** people named Dean and Palmer → `B-PER B-PER`

The B-vs-I prefix resolves this.

## CoNLL-2003's nine labels

The canonical four-entity-class instantiation Ch 11 uses:

```python
label2id = {
    "O":     0,
    "B-PER": 1, "I-PER": 2,    # person
    "B-ORG": 3, "I-ORG": 4,    # organization
    "B-LOC": 5, "I-LOC": 6,    # location
    "B-MISC": 7, "I-MISC": 8   # miscellaneous
}
```

The **ordering convention** (B-* at odd index, I-* at even index = next odd + 1) is load-bearing: Ch 11's [[LabelAlignment|`align_labels`]] code uses `if updated_label % 2 == 1: updated_label += 1` to convert beginning labels to inside labels on subtoken continuations.

## BIO vs related schemes

- **IOB1** — original Ramshaw & Marcus 1995; `B-` only used to separate adjacent same-class entities. **Less common.**
- **IOB2 / BIO** — every entity starts with `B-`. **Ch 11's scheme and the modern default.**
- **BIOES** (a.k.a. BILOU) — adds `E-` (end) and `S-` (singleton); strictly more expressive but rarely worth the complexity for transformer-based taggers.

## Span-aware evaluation

[[seqeval|`seqeval`]] is BIO-tag-aware: it counts a predicted span as correct only when both its start (`B-XXX`) and end (last `I-XXX` before transition) are correctly predicted. This is stricter than naive per-token F1 and is the standard CoNLL-2003 metric.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[NamedEntityRecognition]] — primary use case.
- [[TokenClassification]] — the broader task family.
- [[LabelAlignment]] — uses the odd/even B-/I- ordering to assign continuation labels to subtokens.
- [[CoNLL2003]] — the dataset that codified the four-class BIO scheme used in Ch 11.
- [[seqeval]] — the span-aware evaluation tool.
