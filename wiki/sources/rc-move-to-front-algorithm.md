---
title: "Move-to-front algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-compression, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Move-to-front_algorithm
---

## Summary
The task asks the programmer to implement the move-to-front (MTF) transform, a reversible encoding that maps a sequence of input symbols to a sequence of integer indices. For each symbol, you output its current position in a symbol table (the lowercase alphabet a-z), then move that symbol to the front of the table. The key insight is that recently or frequently seen symbols drift toward index 0, producing many small numbers that downstream entropy coders can compress well.

## Task Requirements
- Use a zero-indexed symbol table of the lowercase characters a-z.
- Encode: for each input symbol, output its index in the table, then move it to the front.
- Decode: using the same starting table, for each index output the symbol at that position, then move it to the front.
- Encode and decode the three strings: `broood`, `bananaaa`, and `hiphophiphop`.
- Show each string and its encoding, and verify that the decoded string equals the original.

## Language Coverage
73 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, J, and APL.

## Connections
- [[MoveToFrontTransform]] — the underlying reversible transform being implemented
- [[DataCompression]] — MTF is a preprocessing stage that biases output toward small indices
- [[BurrowsWheelerTransform]] — MTF commonly follows BWT in compressors like bzip2
- [[EntropyCoding]] — the small-index distribution MTF produces is fed to Huffman/arithmetic coders

## Contradictions
- None — reference task page.
