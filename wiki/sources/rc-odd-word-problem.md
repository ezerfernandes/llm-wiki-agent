---
title: "Odd word problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Odd_word_problem
---

## Summary
The task is to read a stream of letters and punctuation, where single punctuation marks delimit words and a period ends the input, and reverse the letters of every other word while leaving the punctuation in place. The catch is that I/O is restricted to one character at a time with no buffering, peeking, push-back, or explicit storage of characters in a collection. The key insight is that the reversal must instead exploit the implicit storage afforded by recursion, closures, continuations, threads, or coroutines — the call stack effectively becomes the buffer.

## Task Requirements
- Process an input stream of English letters and punctuation; words are delimited by exactly one punctuation char, the stream starts with a word, and a full stop (.) marks the end.
- Print words at even positions unchanged and reverse the letters of every other (odd) word, keeping punctuation intact.
- I/O only one character at a time: no string reads, no peeking ahead, no pushing chars back, no stashing chars in a global variable.
- No explicit storage of characters in arrays, strings, hash tables, or similar collections for later reversal.
- Recursion, closures, continuations, threads, and coroutines are permitted even though they implicitly hold multiple characters.
- Handle both `what,is,the;meaning,of:life.` and `we,are;not,in,kansas;any,more.`

## Language Coverage
65 languages implement this task, a broad spread across functional, imperative, stack-based, and esoteric languages. Representative examples include C, C++, Java, Python, Haskell, Racket, Scheme, Common Lisp, Forth, FALSE, Prolog, and Raku.

## Connections
- [[Recursion]] — the canonical trick: recurse on each character so the call stack reverses letters on the way back out
- [[Continuations]] — continuation-passing style and call/cc offer an alternative to plain recursion for odd words
- [[Coroutines]] — generators/coroutines satisfy the implicit-storage allowance without explicit buffers
- [[StringProcessing]] — character-stream parsing and selective word reversal
- [[CallStack]] — the implicit data structure standing in for a forbidden explicit buffer

## Contradictions
- None — reference task page.
