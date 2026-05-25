---
title: "Named-Entity Recognition (NER)"
type: concept
tags: [nlp, token-classification, fine-tuning, ner, sequence-labeling]
sources: [hands-on-llm-ch11-fine-tuning-representation-models, dspy-entity-extraction-tutorial]
last_updated: 2026-05-24
---

# Named-Entity Recognition (NER)

**Named-entity recognition (NER)** is the [[TokenClassification|token-classification]] task of labeling each token in a sequence with an entity tag — typically PERSON, ORGANIZATION, LOCATION, MISCELLANEOUS, or O (outside any entity). Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"Instead of classifying entire documents, this procedure allows for the classification of individual tokens and/or words, including people and locations. This is especially helpful for de-identification and anonymization tasks when there is sensitive data."*

NER is the **canonical sequence-labeling task** in NLP — it dates back to the [[CoNLL2003|CoNLL-2003 shared task]] (Sang & De Meulder 2003).

## Tokens vs words

Ch 11 emphasizes: *"Our word-level classification task does not entail classifying entire words, but rather the tokens that collectively constitute those words."* [[bert|BERT]]-class encoders use [[WordPiece]] subword tokenization, so a word like `homer` becomes `home + ##r` and a word like `Maarten` becomes `Ma + ##arte + ##n`. The model labels each subtoken; word-level labels must be **aligned** to subtokens before training (see [[LabelAlignment]]).

## The architecture

Same backbone as document classification (e.g., `bert-base-cased`), but:

- Head: per-token classification (linear layer applied to each position's final hidden state), not pooled-CLS classification.
- Model class: `AutoModelForTokenClassification`, not `AutoModelForSequenceClassification`.
- Data collator: [[DataCollatorForTokenClassification]], not [[DataCollatorWithPadding]].
- Evaluation: span-level F1 via [[seqeval|`seqeval`]], not per-document F1.

## Standard label scheme: BIO tagging

NER labels follow the **[[BIOTagging|BIO scheme]]**: `B-XXX` (beginning of an XXX entity), `I-XXX` (inside / continuation of an XXX entity), `O` (outside any entity). CoNLL-2003's nine labels:

```python
label2id = {
    "O": 0, "B-PER": 1, "I-PER": 2, "B-ORG": 3, "I-ORG": 4,
    "B-LOC": 5, "I-LOC": 6, "B-MISC": 7, "I-MISC": 8
}
```

Without the B/I distinction, two adjacent same-class tokens would be ambiguous — `Dean Palmer` (one person) vs `Dean Palmer` (two unrelated people).

## Use cases

- **De-identification and anonymization** of sensitive documents (medical records, legal filings).
- **Knowledge-graph construction** — extract entity mentions to populate graph nodes.
- **Search and indexing** — facet results by recognized entities.
- **Information extraction** — first step in a relation-extraction or event-extraction pipeline.

## Datasets named in Ch 11

- **[[CoNLL2003|CoNLL-2003]]** — the canonical English NER benchmark (~14k training samples; PER/ORG/LOC/MISC entities).
- **[[WNUT17|`wnut_17`]]** — emerging and rare entities, harder to spot.
- **`tner/mit_movie_trivia`** — detects actor, plot, soundtrack entities.
- **`tner/mit_restaurant`** — detects amenity, dish, cuisine entities (Liu et al., ICASSP 2013).

## Worked Ch 11 inference

`pipeline("token-classification")` on *"My name is Maarten."*:

```python
[{'entity': 'B-PER', 'score': 0.995, 'index': 4, 'word': 'Ma',    'start': 11, 'end': 13},
 {'entity': 'I-PER', 'score': 0.993, 'index': 5, 'word': '##arte','start': 13, 'end': 17},
 {'entity': 'I-PER', 'score': 0.995, 'index': 6, 'word': '##n',   'start': 17, 'end': 18}]
```

*"In the sentence 'My name is Maarten', the word 'Maarten' and its subtokens were correctly identified as a person!"*

## Decoder-LLM alternative (DSPy)

The [[dspy-entity-extraction-tutorial|DSPy Entity Extraction tutorial]] (2024) supplies the wiki's canonical **decoder-LLM** alternative to encoder-fine-tuning NER on the same [[CoNLL2003|CoNLL-2003]] dataset. Instead of per-token BIO classification with a [[BERT|BERT]]-class encoder, the tutorial wraps a `list[str] -> list[str]` [[DSPySignatures|Signature]] in [[ChainOfThought|`dspy.ChainOfThought`]] over `gpt-4o-mini` — bypassing the [[BIOTagging|BIO]] surface entirely and emitting the **token subset** directly. Result: **86.0% exact-match zero-shot → 93.0% after [[MIPROv2|MIPROv2]] optimization** (200-example test slice, $0.26 USD total). See [[EntityExtraction]] for the broader operational template and a side-by-side comparison of when to use each.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — encoder-fine-tuning primary source.
- [[dspy-entity-extraction-tutorial]] — decoder-LLM alternative on the same dataset.
- [[EntityExtraction]] — broader umbrella for the *return-the-subset* task framing.
- [[TokenClassification]] — the parent task family.
- [[BIOTagging]] — the standard label scheme.
- [[LabelAlignment]] — the word-to-subtoken label-mapping step.
- [[CoNLL2003]] — the canonical dataset.
- [[WNUT17]] — the harder emerging-entities sibling.
- [[seqeval]] — span-level F1 evaluation.
- [[FineTuningBert]] — the broader fine-tuning template.
- [[bert]] — the representative backbone.
