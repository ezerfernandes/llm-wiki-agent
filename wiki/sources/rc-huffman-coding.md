---
title: "Huffman coding (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-compression, greedy-algorithm, binary-tree]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Huffman_coding
---

## Summary
The task asks the programmer to build a Huffman encoding for the characters of a given string based on their frequency of occurrence. Huffman coding assigns shorter bit strings to more frequent symbols and longer ones to rarer symbols, producing a prefix-free code where no symbol's code is a prefix of another's, which makes the variable-length stream uniquely decodable. The key insight is that repeatedly merging the two lowest-frequency nodes via a priority queue yields an optimal prefix code.

## Task Requirements
- Compute the character frequencies of the string `this is an example for huffman encoding`.
- Build a Huffman tree by creating a leaf node for each symbol, adding all to a priority queue, then repeatedly removing the two lowest-weight nodes and inserting a new internal node whose weight is their sum until one root node remains.
- Traverse the tree from root to leaves, accumulating a '0' for one branch and a '1' for the other, to derive each symbol's code.
- Output the resulting Huffman encoding for each character as a table.

## Language Coverage
66 languages implement this task, reflecting broad coverage across functional, imperative, and scripting paradigms. Representative implementations include C, C++, Java, Python, Haskell, OCaml, Go, Rust, Ruby, Scheme, and Common Lisp.

## Connections
- [[HuffmanCoding]] — the algorithm the task implements
- [[PriorityQueue]] — the data structure used to repeatedly select lowest-weight nodes
- [[GreedyAlgorithm]] — the optimization strategy that proves Huffman codes optimal
- [[BinaryTree]] — the tree traversed to assign codes
- [[DataCompression]] — the application domain (prefix-free, lossless encoding)

## Contradictions
- None — reference task page.
