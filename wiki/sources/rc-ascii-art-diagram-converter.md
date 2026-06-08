---
title: "ASCII art diagram converter (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing, code-generation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/ASCII_art_diagram_converter
---

## Summary
The task takes the ASCII art "wire diagram" of the RFC 1035 DNS message header (Section 4.1.1) — a grid of `+--+` bit-boxes with named fields spanning multiple columns — and asks the programmer to parse it into a usable data structure or header decoder. The key insight is treating the diagram as a compact field-layout DSL: each column is one bit, each `+--+` box marks a bit boundary, and labels centered across spans define field names and bit widths. Languages with macros or strong templates are encouraged to consume the string at compile time and generate the header type statically.

## Task Requirements
- Accept a similar multi-line ASCII diagram string as input to a function, member function, class, or template.
- Produce a data structure (or equivalent) able to decode/store a header with the specified bit layout.
- Support tables with 8, 16, 32, or 64 columns and any number of rows; every column is one bit and each bit box is the four characters `+--+`.
- Only `+`, `-`, `|`, and whitespace are valid table symbols; whitespace-only lines are ignored.
- Strip leading/trailing whitespace of the whole string and around each row.
- Perform light input validation (full validation is optional bonus).
- Bonus: compile-time generation via macros/introspection/code generation, plus thorough validation.

## Language Coverage
35 languages implement this task, spanning assembly, systems, functional, and scripting families. Representative entries include AArch64 Assembly, C, C++, C#, Rust, Go, Haskell, Java, JavaScript, Python, Perl, Raku, Ruby, and Wolfram Language.

## Connections
- [[StringParsing]] — interpreting the structured ASCII grid into tokens and field spans
- [[BitFields]] — fields are defined by their bit offsets and widths within the header
- [[CodeGeneration]] — bonus path generates the header type from the diagram, ideally at compile time
- [[DomainSpecificLanguage]] — the diagram acts as a small declarative layout language
- [[DNS]] — the concrete example is the RFC 1035 DNS message header

## Contradictions
- None — reference task page.
