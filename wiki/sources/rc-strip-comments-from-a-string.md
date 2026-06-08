---
title: "Strip comments from a string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Strip_comments_from_a_string
---

## Summary
The task is to remove everything that follows any of a set of comment markers (the examples use a hash `#` and a semicolon `;`) from an input line, leaving only the code portion. The key subtlety is whitespace handling: per the task's evolving rules, both the comment marker and any surrounding leading/trailing whitespace should be trimmed, so a line like `apples, pears # and bananas` reduces to `apples, pears`. The page itself notes a long-running "whitespace debacle" where many implementations disagreed over whether to trim.

## Task Requirements
- Strip any text following one of a configurable set of comment markers (e.g. `#` or `;`).
- Remove the comment marker itself and the trailing comment text.
- Trim leading and trailing whitespace from the resulting line (a comment-free line should also be trimmed).
- Demonstrate on the example inputs, producing `apples, pears`.

## Language Coverage
101 languages implement this task, reflecting that it is an introductory string-manipulation exercise found across nearly every language family. Representative implementations include C, C++, Java, Python, Perl, Ruby, Haskell, Go, Rust, Lua, and AWK, plus assembly variants and esoteric or array languages like APL, BQN, and J.

## Connections
- [[StringProcessing]] — core operation of scanning and splitting on a delimiter
- [[RegularExpressions]] — many solutions match the comment marker via regex
- [[Tokenization]] — separating code text from trailing comment tokens
- [[Lexing]] — comment stripping is a primitive step in source-code lexers

## Contradictions
- None — reference task page.
