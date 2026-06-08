---
title: "Input loop (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, io, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Input_loop
---

## Summary
This task asks the programmer to read from a text stream of unknown length, consuming it either word-by-word or line-by-line until the stream is exhausted. The key insight is detecting end-of-stream gracefully and looping until that condition is met, rather than assuming a fixed input size.

## Task Requirements
- Read from a text stream (e.g., standard input or a file).
- Process the data either word-by-word or line-by-line.
- Continue reading until the stream runs out of data (EOF).
- Handle an unknown, arbitrary amount of input data.

## Language Coverage
129 languages implement this task, reflecting how fundamental stream reading is across nearly every language. Representative implementations include C, C++, Python, Java, Go, Rust, Haskell, Perl, Ruby, AWK, and several assembly variants such as ARM Assembly.

## Connections
- [[StandardInput]] — the common source for the text stream
- [[EndOfFile]] — the termination condition the loop detects
- [[StreamProcessing]] — the general pattern of consuming sequential data
- [[Tokenization]] — splitting input into words during word-by-word reads

## Contradictions
- None — reference task page.
