---
title: "Random sentence from book (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, markov-chain, text-generation, nlp]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Random_sentence_from_book
---

## Summary
This task asks the programmer to build a Markov-chain text generator trained on the public-domain text of H. G. Wells' "The War of the Worlds". After cleaning punctuation (keeping sentence terminators `.`, `!`, `?`), the program tabulates how often each word follows a given pair of preceding words. New sentences are then produced by starting from a virtual full-stop and repeatedly making weighted random choices of the next word until a terminator is reached. The key insight is that a second-order (bigram-context) Markov model yields far more coherent output than a first-order one.

## Task Requirements
- Read the book text (Project Gutenberg "The War of the Worlds") and skip the preamble to the start of the book proper.
- Strip extraneous punctuation but preserve sentence-ending characters `.`, `!`, and `?`, treating those terminators as words.
- Record counts of which single word follows each word.
- Record counts of which word follows each pair of two words (treating terminators as words).
- Begin a sentence at an implicit, unprinted full-stop and use a weighted random choice over candidate following words.
- Extend the sentence by weighted random choices conditioned on the previous two words.
- Stop after emitting a sentence-ending punctuation character, then tidy and print the result.

## Language Coverage
14 languages implement this task, a modest but varied spread covering systems, scripting, and functional styles. Representative implementations include Ada, ALGOL 68, Crystal, Dart, Julia, Nim, Perl, Python, Raku, and Wren.

## Connections
- [[MarkovChain]] — the core probabilistic model driving word-by-word generation
- [[TextGeneration]] — the broader natural-language synthesis task
- [[WeightedRandomChoice]] — selecting next words proportional to observed frequencies
- [[NGramModel]] — counting word pairs/triples is an n-gram language model
- [[FrequencyCounting]] — tabulating how often words follow other words

## Contradictions
- None — reference task page.
