---
title: "Information Seeking"
type: concept
tags: [framing, hci, information-retrieval]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Information Seeking

**Information seeking** — the user-facing task of *finding* and *making sense of* information across multiple sources. [[Pirolli2009|Pirolli (2009)]] frames it as part of the broader **sensemaking** process: collecting, sifting, understanding, and organizing information from large collections to generate a knowledge product.

## Properties of *complex* information seeking

Per [[2408.15232-co-storm|Jiang et al. 2024 §2.1]], **complex information seeking** has three properties:

1. **Multiple sources** — addressing different facets of a topic, rather than retrieving a single best-matching document.
2. **Ongoing user interaction** — not a one-shot query but an evolving dialogue.
3. **Report-like curated information product** — the output is a structured artifact, not a short-form answer.

Co-STORM's [[2408.15232-co-storm|Table 1]] taxonomy of existing systems:

| System type | Multiple Sources | Ongoing Interaction | Curated Report |
|---|---|---|---|
| [[InformationRetrieval]] (e.g., [[Robertson1977]]) | ✗ | ✗ | ✗ |
| Single-Turn [[QASystem\|QA]] | ✓ | ✗ | ✗ |
| Conversational QA (e.g., [[Reddy2019\|CoQA]]) | ✓ | ✓ | ✗ |
| Report Generation (e.g., [[STORM]]) | ✓ | ✗ | ✓ |
| **[[CoSTORM]]** | **✓** | **✓** | **✓** |

## Two distinct epistemic modes

[[Kirzner1997|Kirzner 1997]] separates:

- **Successful search** — *"the deliberate production of information which one knew one had lacked"* — addresses **known unknowns**.
- **Discovery** — *"the realization that one had overlooked something in fact readily available"* — addresses [[UnknownUnknowns|unknown unknowns]].

LM-based QA/RAG systems are strong at the first mode and weak at the second. Co-STORM targets the second.

## See also
- [[CoSTORM]] · [[UnknownUnknowns]] · [[CollaborativeDiscourse]] · [[QASystem]] · [[rag]]
