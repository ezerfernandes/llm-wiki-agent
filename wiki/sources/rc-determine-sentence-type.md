---
title: "Determine sentence type (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Determine_sentence_type
---

## Summary
This task asks the programmer to classify a sentence by examining its final punctuation mark and mapping it to one of four type codes. The key insight is to scan for the last *used* punctuation character (ignoring trailing whitespace or non-punctuation) and translate it: an exclamation mark yields "E", a question mark yields "Q", a period yields "S" (serious), and anything else is "N" (neutral). An extra credit variant requires handling a string containing multiple sentences and emitting one code per sentence.

## Task Requirements
- Search a sentence for its last used punctuation mark.
- Output a single letter based on that punctuation: "E" (exclamation `!`), "Q" (question `?`), "S" (serious `.`), or "N" (neutral, no terminal punctuation).
- Extra: extend the code to classify multiple sentences within a single input string.
- Handle the supplied test text gracefully without errors.

## Language Coverage
43 languages implement this task, spanning systems and scripting languages plus several assembly dialects. Representative implementations include Python, C++, Java, Rust, Go, Perl, Raku, Julia, AWK, and ARM Assembly.

## Connections
- [[StringProcessing]] — scanning and classifying characters within text
- [[TextParsing]] — segmenting input into sentences and inspecting delimiters
- [[FiniteStateMachine]] — punctuation-based classification can be modeled as a simple state mapping
- [[Tokenization]] — splitting a multi-sentence string on terminal punctuation

## Contradictions
- None — reference task page.
