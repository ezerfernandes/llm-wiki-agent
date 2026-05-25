---
title: "WNUT-17 (wnut_17) dataset"
type: entity
tags: [dataset, ner, nlp, benchmark, emerging-entities, sequence-labeling]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# WNUT-17 (wnut_17) dataset

**WNUT-17** is a [[NamedEntityRecognition|named-entity recognition]] dataset targeting **emerging and rare entities** — names that are not in standard NER training data and are difficult to recognize without world knowledge. From the 3rd Workshop on Noisy User-generated Text (W-NUT 2017). Distributed on Hugging Face as `wnut_17`.

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]] (named in a sidebar):

> *"wnut_17 is a task that focuses on emerging and rare entities, those that are more difficult to spot."*

## Why it matters

CoNLL-2003 covers entities common in 1990s news (Bill Clinton, Microsoft, Berlin) — entities the model has seen many times during pretraining. WNUT-17 deliberately targets the **long tail**: people, products, and places that appeared after model pretraining or that are obscure enough that pretraining didn't memorize them. A reasonable proxy for **real-world NER deployment** where the entities of interest are often emergent (a new product launch, a niche scientific compound, a small company).

## Related dataset family Ch 11 names

In the same sidebar:

- **`tner/mit_movie_trivia`** — detects entities like actor, plot, soundtrack.
- **`tner/mit_restaurant`** — detects entities such as amenity, dish, cuisine.

Reference: Jingjing Liu et al. *"Asgard: A portable architecture for multilingual dialogue systems,"* ICASSP 2013.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source (sidebar mention).
- [[NamedEntityRecognition]] — task family.
- [[CoNLL2003]] — the standard NER benchmark; WNUT-17 is the harder sibling.
- [[BIOTagging]] — the label scheme.
- [[HuggingFace]] — distribution channel.
