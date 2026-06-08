---
title: "Comma quibbling (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Comma_quibbling
---

## Summary
Write a function that joins a list of words into a single braced string, using ", " between all words except the last pair, which is joined with " and ". Originating from an Eric Lippert blog post, the task's insight is handling the four arity cases (zero, one, two, and three-or-more words) cleanly without special-casing every count.

## Task Requirements
- Empty input produces `"{}"`.
- One word `["ABC"]` produces `"{ABC}"`.
- Two words produce the words separated by `" and "`, e.g. `"{ABC and DEF}"`.
- Three or more words separate all but the last with `", "` and join the final word with `" and "`, e.g. `"{ABC, DEF, G and H}"`.
- Demonstrate the function against the four sample inputs: `[]`, `["ABC"]`, `["ABC","DEF"]`, `["ABC","DEF","G","H"]`.

## Language Coverage
130 languages implement this task, spanning systems, scripting, functional, and assembly languages. Representative entries include Python, Haskell, C, C++, Java, JavaScript, Perl, Raku, Rust, Go, and Common Lisp.

## Connections
- [[StringProcessing]] — core operation is conditional string concatenation
- [[StringJoining]] — generalizes the join-with-separator pattern with a special final delimiter
- [[ListProcessing]] — operates over a sequence, partitioning head from last element
- [[ConditionalLogic]] — branches on the cardinality of the input

## Contradictions
- None — reference task page.
