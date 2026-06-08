---
title: "S-expressions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, parsing, data-structures, serialization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/S-expressions
---

## Summary
The task asks the programmer to build a simple reader and writer for S-expressions, the nested parenthesized notation popularized by Lisp. The reader must parse a single (possibly deeply nested) S-expression from a string into a native data structure such as a list or array, distinguishing quoted strings, unquoted strings/symbols, integers, and floats. The writer must serialize that structure back into valid S-expression text, quoting only strings that contain whitespace or parentheses.

## Task Requirements
- Read one nested S-expression from a string into a native structure (list, array, etc.).
- Recognize quoted strings, unquoted strings (treated as symbols where supported), integers, and floats.
- Ignore newlines and other whitespace except inside quoted strings.
- Treat `()` inside quoted strings as literal characters, not structure.
- Handling escaped quotes (`\`) is optional; the only special characters are `()"`, the optional `\`, and whitespace.
- Parse the given sample input `((data "quoted data" 123 4.5) (data (!@# (4.5) "(more" "data)")))` correctly.
- Write the structure back out, quoting only strings needing it (any string may be quoted as a simplification).
- Extra credit: pretty-print the output with indentation and line breaks.

## Language Coverage
46 languages implement this task, spanning Lisp-family dialects, functional, systems, and scripting languages. Representative examples include Common Lisp, Scheme, Racket, Haskell, OCaml, F#, C, C++, Rust, Go, Java, Python, Ruby, Perl, and Raku.

## Connections
- [[Parsing]] — the reader is a small recursive-descent parser/tokenizer
- [[RecursiveDescentParsing]] — natural fit for the nested grammar
- [[AbstractSyntaxTree]] — the parsed nested lists form a tree representation
- [[Serialization]] — the writer serializes the structure back to text
- [[Lisp]] — S-expressions originate from the Lisp language family

## Contradictions
- None — reference task page.
