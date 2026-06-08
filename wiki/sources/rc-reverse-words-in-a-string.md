---
title: "Reverse words in a string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Reverse_words_in_a_string
---

## Summary
The task asks the programmer to reverse the order of the whitespace-separated tokens (words) within each of a set of input strings, while leaving the characters inside each token untouched. For example, "Hey you, Bub!" becomes "Bub! you, Hey". The key insight is that this is a token-level reversal, not a character-level one, so punctuation travels with its surrounding word.

## Task Requirements
- Split each input string into tokens delimited by whitespace, treating attached punctuation as part of the token.
- Reverse the order of the tokens but preserve the internal character order of each token.
- Collapse multiple or superfluous spaces into a single space.
- Strings with no tokens (empty or all-space) should yield an empty result.
- Display the strings in their original order, one per line, over the supplied ten-line "Ice and Fire" input data.

## Language Coverage
129 languages implement this task, reflecting how widely supported basic string splitting and list reversal are. Representative implementations include Python, C, C++, Java, JavaScript, Haskell, Ruby, Rust, Go, Perl, and APL-family languages like J and BQN.

## Connections
- [[StringProcessing]] — core domain of the task
- [[Tokenization]] — splitting input on whitespace into words
- [[ListReversal]] — reversing the resulting sequence of tokens
- [[WhitespaceNormalization]] — collapsing superfluous spaces into one

## Contradictions
- None — reference task page.
