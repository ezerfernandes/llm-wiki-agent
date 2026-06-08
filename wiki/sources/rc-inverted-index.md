---
title: "Inverted index (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, information-retrieval, data-structures, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Inverted_index
---

## Summary
This task asks the programmer to build an inverted index, the core data structure behind full-text search. Given a set of text files, the program maps each distinct term to the list of files containing it, then exposes a search interface that returns the files matching one or more query terms. The key insight is inverting the natural document-to-words mapping into a word-to-documents mapping so lookups become fast set operations rather than scans.

## Task Requirements
- Given a set of text files, build an inverted index from them.
- Provide a user interface that performs a search over the index.
- A search returns the list of files containing the query term or terms.
- The index may be held entirely in memory.

## Language Coverage
47 languages implement this task, spanning systems and functional languages as well as scripting and BASIC dialects. Representative implementations include C, C++, C#, Java, Python, Haskell, Go, Rust, Ruby, Perl, Clojure, and Common Lisp.

## Connections
- [[InvertedIndex]] — the data structure the task is named for
- [[FullTextSearch]] — the application domain that motivates the structure
- [[InformationRetrieval]] — the field studying document indexing and querying
- [[HashTable]] — the typical underlying map from terms to document lists
- [[Tokenization]] — splitting file contents into the terms that key the index

## Contradictions
- None — reference task page.
