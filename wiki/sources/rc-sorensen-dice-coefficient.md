---
title: "Sorensen–Dice coefficient (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, similarity-metrics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorensen–Dice_coefficient
---

## Summary
The task asks the programmer to implement the Sørensen–Dice coefficient, a similarity statistic that measures how alike two samples are by computing twice the size of their intersection divided by the sum of their sizes (SDC = 2·|A∩B| / (|A| + |B|)), yielding a ratio between 0.0 and 1.0. For text, the typical approach tokenizes words into bi-grams (overlapping pairs of consecutive letters) and treats the token groups as multisets, where the intersection takes the minimum multiplicity of each shared token. The key insight is that this metric excels at fuzzy matching of misspelled or reordered short phrases where Levenshtein edit distance would be too slow or too strict.

## Task Requirements
- Use the list of Rosetta Code task and draft task names as the "dictionary" to search against.
- Tokenize by folding case, splitting words, ignoring whitespace but keeping punctuation, and forming bi-grams (e.g. "differ" → di if ff fe er).
- Treat token groups as multisets when computing the intersection (item with multiplicity a in A and b in B has multiplicity min(a,b) in A∩B).
- Search for the four mangled task names: "Primordial primes", "Sunkist-Giuliani formula", "Sieve of Euripides", "Chowder numbers".
- For each search term, show the coefficient and the five closest matching task names.
- A built-in or freely available library implementation may be used with a pointer to its source.

## Language Coverage
14 languages implement this task, a moderate spread covering systems, functional, scripting, and BASIC-family languages. Representative implementations include ALGOL 68, C++, Java, Julia, Nim, Perl, Python, Raku, jq, J, Phix, and Wren.

## Connections
- [[StringSimilarity]] — Sørensen–Dice is a string/set similarity measure
- [[LevenshteinDistance]] — contrasted alternative for measuring word/phrase closeness
- [[NGram]] — bi-gram tokenization underlies the text-based comparison
- [[Multiset]] — token groups are compared as multisets using min multiplicity
- [[FuzzyMatching]] — primary practical application of the coefficient

## Contradictions
- None — reference task page.
