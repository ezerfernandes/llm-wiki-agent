---
title: "Eertree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, data-structures, palindromes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Eertree
---

## Summary
The task is to implement an eertree (also called a palindromic tree), a data structure that efficiently processes palindrome-related queries such as counting or enumerating the sub-palindromes of a string. The structure shares traits with both tries and suffix trees, and the key insight is that any string contains at most n+2 distinct sub-palindromes, so they can be stored compactly in two roots (one for odd-length and one for even-length palindromes) with suffix links connecting nodes.

## Task Requirements
- Construct an eertree for the input string "eertree".
- Traverse the resulting tree and output all distinct sub-palindromes it contains.

## Language Coverage
28 languages implement this task, spanning systems and scripting languages alike. Representative implementations include C++, D, Rust, Zig, Go, Java, Python, Julia, Perl, Raku, Ruby, and Kotlin.

## Connections
- [[PalindromicTree]] — the formal name for the eertree data structure
- [[Trie]] — a related tree structure the eertree generalizes
- [[SuffixTree]] — another string-indexing structure it resembles
- [[Palindrome]] — the property each stored substring satisfies
- [[StringAlgorithms]] — the broader algorithmic domain of this task

## Contradictions
- None — reference task page.
