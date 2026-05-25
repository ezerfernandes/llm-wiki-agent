---
title: "Fuzzy Matching"
type: concept
tags: [evaluation, similarity, nlp]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Fuzzy Matching

The colloquial name for **approximate string matching** based on [[EditDistance|edit distance]]. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "It measures the similarity between two texts by counting how many edits it'd need to convert from one text to another, a number called edit distance."

## When to reach for fuzzy matching

- **Short strings with typos** — name matching, address matching, search-bar autocorrection.
- **Schema-level comparison** — does the model's generated SQL column name approximately match the reference column name?
- **Code-character-level similarity** — not common for evaluation but used in some [[bleu|BLEU]] alternatives.

## Limitations

Like other [[LexicalSimilarity|lexical-similarity]] methods, fuzzy matching is **blind to meaning**: *"Let's eat, grandma"* and *"Let's eat grandma"* are nearly identical by edit distance and opposite in meaning.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[EditDistance]] — the operationalization.
- [[LexicalSimilarity]] — parent family.
- [[ExactMatch]] — the strict (zero-edit) special case.
- [[SemanticSimilarity]] — what fuzzy matching is blind to.
