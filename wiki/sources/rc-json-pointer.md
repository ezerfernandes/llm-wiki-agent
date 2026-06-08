---
title: "JSON pointer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing, json]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/JSON_pointer
---

## Summary
The task asks the programmer to implement a JSON Pointer evaluator as defined in RFC 6901: parse a slash-separated string of tokens and walk a JSON document to resolve the value each pointer targets. The key insight is the token-decoding rule — `~1` decodes to a literal slash and `~0` to a literal tilde (in that order) — and the need to distinguish array-index navigation from object-property lookup, returning an error for out-of-range indices, missing properties, or pointers that don't begin with `/`.

## Task Requirements
- Parse a JSON Pointer string into slash-separated tokens, decoding `~1` → `/` and `~0` → `~`.
- Evaluate the pointer against a JSON document, descending into objects by property name and into arrays by numeric index.
- Treat the empty pointer `""` as referring to the entire document.
- Produce a helpful error for out-of-range indices, nonexistent properties, navigating into a non-container, or a malformed pointer (e.g. one not starting with `/`).
- Demonstrate the implementation against the provided example document and the full set of example pointers, displaying each resolved value or its error.

## Language Coverage
17 languages implement this task, a moderate spread reflecting that it relies on each language's JSON handling and string manipulation. Representative entries include Python, JavaScript, Go, Rust, Perl, Raku, Julia, Nim, Crystal, jq, and Prolog.

## Connections
- [[JSON]] — the data format whose documents these pointers navigate
- [[StringProcessing]] — token splitting and escape decoding drive the parser
- [[Parsing]] — pointers are parsed into a token sequence before evaluation
- [[TreeTraversal]] — evaluation walks the nested object/array tree node by node
- [[RFC6901]] — the standard that specifies the pointer syntax and semantics

## Contradictions
- None — reference task page.
