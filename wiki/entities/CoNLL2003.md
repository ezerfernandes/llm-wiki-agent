---
title: "CoNLL-2003 dataset"
type: entity
tags: [dataset, ner, nlp, benchmark, sequence-labeling]
sources: [hands-on-llm-ch11-fine-tuning-representation-models, dspy-entity-extraction-tutorial]
last_updated: 2026-05-24
---

# CoNLL-2003 dataset

**CoNLL-2003** is the canonical English **[[NamedEntityRecognition|named-entity recognition]]** benchmark — introduced as a shared task at the seventh CoNLL conference. Reference: Erik F. Sang & Fien De Meulder, *"Introduction to the CoNLL-2003 shared task: Language-independent named entity recognition,"* arXiv:cs/0306050 (2003).

Distributed on the Hugging Face Hub as `conll2003`. Loaded via:

```python
dataset = load_dataset("conll2003", trust_remote_code=True)
```

## Size (per Ch 11)

- *"roughly 14,000 training samples"*
- Four entity classes: **PER** (person), **ORG** (organization), **LOC** (location), **MISC** (miscellaneous), plus **O** (outside any entity)

## Data structure

Each example contains:

| Field | Type | Description |
|---|---|---|
| `id` | string | Example identifier |
| `tokens` | list[str] | Pre-tokenized words (NOT subtokens) |
| `pos_tags` | list[int] | Part-of-speech tags |
| `chunk_tags` | list[int] | Chunking tags |
| `ner_tags` | list[int] | The NER labels in [[BIOTagging|BIO format]] |

## Label scheme

Nine labels in the BIO scheme:

```python
label2id = {
    "O": 0, "B-PER": 1, "I-PER": 2, "B-ORG": 3, "I-ORG": 4,
    "B-LOC": 5, "I-LOC": 6, "B-MISC": 7, "I-MISC": 8
}
```

## Worked Ch 11 example

```python
example = dataset["train"][848]
# {
#   'tokens': ['Dean','Palmer','hit','his','30th','homer','for','the','Rangers','.'],
#   'ner_tags': [1, 2, 0, 0, 0, 0, 0, 0, 3, 0]
# }
```

The labels mean: *"Dean Palmer"* = `B-PER I-PER` (one person), *"Rangers"* = `B-ORG` (organization), rest = `O`.

## Why it's the canonical benchmark

- **Standard evaluation** via [[seqeval|`seqeval`]] / the CoNLL eval script.
- **Span-level F1** is the headline metric.
- The **four-class PER/ORG/LOC/MISC ontology** is widely adopted across NER datasets and tools, making cross-dataset transfer reasonable.

## Use as a DSPy benchmark

The [[dspy-entity-extraction-tutorial|DSPy Entity Extraction tutorial]] (2024) uses CoNLL-2003 as the eval surface for **decoder-LM prompt optimization** — orthogonal to the [[FineTuningBert|encoder-fine-tuning]] use the dataset historically supported. The tutorial scopes a narrower task — **persons only** (`ner_tag ∈ {1, 2}` — `B-PER` + `I-PER`) — and trains/evals on small slices (50-example train, 200-example test). Result: **86.0% exact-list-match zero-shot → 93.0% after [[MIPROv2|MIPROv2]]** (`gpt-4o-mini`, $0.26 USD total). This makes CoNLL-2003 the **first dataset in the wiki where both encoder-fine-tuning and decoder-LLM prompt-optimization receipts coexist**.

Note: the DSPy tutorial's metric is **strict ordered-list equality**, not span-level [[seqeval]] F1 — the 93.0% number is **not directly comparable** to encoder-NER F1 results on the same dataset.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — encoder-fine-tuning primary source.
- [[dspy-entity-extraction-tutorial]] — decoder-LM prompt-optimization receipt.
- [[NamedEntityRecognition]] / [[TokenClassification]] — task family.
- [[EntityExtraction]] — the umbrella for the DSPy framing.
- [[BIOTagging]] — the label scheme.
- [[seqeval]] — the canonical evaluation tool.
- [[WNUT17]] — harder NER benchmark targeting emerging entities.
- [[HuggingFace]] — distribution channel.
- [[LabelAlignment]] — the preprocessing step needed before fine-tuning.
