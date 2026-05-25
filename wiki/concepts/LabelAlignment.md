---
title: "Label Alignment (Word → Subtoken)"
type: concept
tags: [preprocessing, ner, token-classification, tokenization]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Label Alignment (Word → Subtoken)

**Label alignment** is the preprocessing step that propagates **word-level labels** (the supervision signal in NER datasets like [[CoNLL2003|CoNLL-2003]]) to **subtoken-level labels** (what a [[bert|BERT]]-class encoder actually processes) for [[TokenClassification|token-classification]] training.

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"This creates a bit of a problem for us since we have labeled data at the word level but not at the token level. This can be resolved by aligning the labels with their subtoken counterparts during tokenization."*

## The alignment rules

For each word in a sentence:

1. **First subtoken** inherits the word's label as-is (typically `B-XXX`).
2. **Continuation subtokens** get the corresponding `I-XXX` label.
3. **`[CLS]`, `[SEP]`, and padding** get label **`-100`** so the loss function ignores them.

Example — *"Maarten"* labeled `B-PER`, tokenized into `Ma + ##arte + ##n`:

| Token | Label |
|---|---|
| `Ma` | `B-PER` (1) |
| `##arte` | `I-PER` (2) |
| `##n` | `I-PER` (2) |

## The `(label + 1) if odd` trick

Ch 11 exploits the [[BIOTagging|BIO label2id ordering]] convention (`B-*` at odd index 1/3/5/7, `I-*` at even index 2/4/6/8 = `B-*` + 1):

```python
def align_labels(examples):
    token_ids = tokenizer(
        examples["tokens"],
        truncation=True,
        is_split_into_words=True
    )
    labels = examples["ner_tags"]

    updated_labels = []
    for index, label in enumerate(labels):
        word_ids = token_ids.word_ids(batch_index=index)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            if word_idx != previous_word_idx:
                # Start of a new word — inherit label
                previous_word_idx = word_idx
                updated_label = -100 if word_idx is None else label[word_idx]
                label_ids.append(updated_label)
            elif word_idx is None:
                # Special token
                label_ids.append(-100)
            else:
                # Continuation subtoken — convert B-XXX → I-XXX
                updated_label = label[word_idx]
                if updated_label % 2 == 1:
                    updated_label += 1
                label_ids.append(updated_label)
        updated_labels.append(label_ids)

    token_ids["labels"] = updated_labels
    return token_ids

tokenized = dataset.map(align_labels, batched=True)
```

The `if updated_label % 2 == 1: updated_label += 1` does **all the B→I conversion at once** without a lookup table.

## Worked Ch 11 example

Original word-level labels for *"Dean Palmer hit his 30th homer for the Rangers ."*:

```
ner_tags: [1, 2, 0, 0, 0, 0, 0, 0, 3, 0]
```

After tokenization (`homer → home + ##r`) and alignment, labels become:

```
labels:   [-100, 1, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, -100]
```

The two `-100`s wrap the `[CLS]` and `[SEP]` special tokens; the extra `0` is for the `##r` continuation subtoken of `homer` (which inherits the `O` label of `homer`, since `O` is `0` regardless of B/I distinction).

## Use `is_split_into_words=True`

The trick that makes alignment possible is calling the tokenizer with `is_split_into_words=True` on a pre-tokenized word list, then reading back `token_ids.word_ids(batch_index=index)` — a mapping from subtoken index to original word index. The mapping returns `None` for special tokens.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[TokenClassification]] — the parent task family.
- [[NamedEntityRecognition]] — the canonical use case.
- [[BIOTagging]] — the label scheme whose B-=odd / I-=even ordering enables the trick.
- [[CoNLL2003]] — the dataset structure Ch 11 aligns.
- [[WordPiece]] — the subword tokenizer that necessitates the alignment.
- [[DataCollatorForTokenClassification]] — the downstream batch-builder.
