---
title: "XML/Output (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, xml, string-processing, serialization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/XML/Output
---

## Summary
The task asks the programmer to write a function that takes a list of character names and a parallel list of remarks and serializes them into an XML document. Each name/remark pair becomes a `<Character>` element with a `name` attribute holding the name and the remark as its text content, all wrapped in an outer `<CharacterRemarks>` element. The key insight is correct XML entity escaping: special characters in the data (`<`, `>`, `&`, quotes) must be substituted with their entity references (`&lt;`, `&gt;`, `&amp;`, etc.) so the output is well-formed.

## Task Requirements
- Accept a list of names and a corresponding list of remarks (a name-to-remark map is also acceptable).
- Emit a `<Character name="...">remark</Character>` element for each pair.
- Enclose all `<Character>` elements within a single outer `<CharacterRemarks>` element.
- Perform proper XML entity substitution on the data if building output via direct string manipulation (the example deliberately includes `<`, `>`, `&`, and quote characters to test escaping).
- The `<?xml?>` declaration and document type declaration are optional; indentation is not significant.

## Language Coverage
70 languages implement this task, showing broad coverage across systems, scripting, functional, and assembly languages. Representative implementations include C, C++, C#, Java, Python, Ruby, Perl, Haskell, Go, Rust, Common Lisp, and even AArch64 and ARM Assembly, with several using dedicated DOM/XML libraries and others doing manual string building with escaping.

## Connections
- [[XML]] — the document format being generated
- [[Serialization]] — converting in-memory data into a textual XML representation
- [[EntityEscaping]] — substituting reserved characters with XML entity references
- [[DocumentObjectModel]] — many solutions build the output via a DOM/tree API rather than raw strings

## Contradictions
- None — reference task page.
