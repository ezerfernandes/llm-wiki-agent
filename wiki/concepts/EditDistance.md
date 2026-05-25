---
title: "Edit Distance"
type: concept
tags: [evaluation, metric, similarity, nlp]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Edit Distance

The **minimum number of edit operations** needed to convert one string into another. The basis for [[FuzzyMatching|fuzzy matching]] — *"approximate string matching, known colloquially as fuzzy matching"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]).

## Three primary operations

1. **Deletion**: *"brad"* → *"bad"*
2. **Insertion**: *"bad"* → *"bard"*
3. **Substitution**: *"bad"* → *"bed"*

Some fuzzy matchers also count **transposition** (swapping two adjacent letters: *"mats"* → *"mast"*) as one edit; others count it as two (one deletion + one insertion).

## Distance as similarity

Lower edit distance → higher similarity. Ch 3's example:
- *"bad"* → *"bard"* = 1 edit.
- *"bad"* → *"cash"* = 3 edits.
- ⇒ *"bad"* is more similar to *"bard"* than to *"cash"*.

## The Levenshtein link

The classical realization is **Levenshtein distance** (1965) with operations {insert, delete, substitute}. Damerau-Levenshtein adds transposition. Real-world fuzzy-matching libraries (e.g., `rapidfuzz`, `fuzzywuzzy`) typically use a normalized variant.

## Position in the [[LexicalSimilarity]] family

Edit distance is the **character-level** branch of lexical similarity, complementary to the **n-gram** branch ([[bleu|BLEU]] / [[ROUGE]] / [[METEOR]] / [[TER]] / [[CIDEr]]). The Ch 3 framing: lexical similarity can be computed either way.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[FuzzyMatching]] — the colloquial name for edit-distance-based matching.
- [[LexicalSimilarity]] — parent family.
- [[NGramSimilarity]] — sibling lexical-similarity method.
- [[SimilarityMeasurement]] — grandparent.
