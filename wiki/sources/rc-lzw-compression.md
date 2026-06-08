---
title: "LZW compression (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-compression, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/LZW_compression
---

## Summary
The task asks the programmer to implement the Lempel-Ziv-Welch (LZW) algorithm, a lossless data-compression scheme. The key insight is that LZW builds a dictionary of substrings on the fly: it starts with all single characters and progressively adds longer sequences as they are encountered, emitting integer codes in place of repeated patterns. Both encoder and decoder reconstruct the same dictionary independently, so no dictionary needs to be transmitted.

## Task Requirements
- Implement loss-less LZW compression (and typically the matching decompression).
- Initialize the dictionary with the base set of single-character entries.
- Read input, finding the longest current string already in the dictionary, emit its code, then add that string plus the next character as a new dictionary entry.
- Reproduce behavior consistent with the standard algorithm described in the Wikipedia article on Lempel-Ziv-Welch.

## Language Coverage
70 languages implement this task, showing very broad coverage across imperative, functional, and scripting paradigms. Representative implementations include C, C++, C#, Java, Python, Haskell, OCaml, Go, Rust, Ruby, JavaScript, and Common Lisp.

## Connections
- [[DataCompression]] — LZW is a lossless compression algorithm
- [[LempelZivWelch]] — the specific dictionary-based technique implemented
- [[DictionaryCoding]] — the general class of substitutional compression methods
- [[StringProcessing]] — relies on incremental substring matching
- [[HashTable]] — dictionaries are commonly backed by hash maps for fast lookup

## Contradictions
- None — reference task page.
