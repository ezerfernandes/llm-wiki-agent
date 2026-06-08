---
title: "Teacup rim text (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, word-puzzle]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Teacup_rim_text
---

## Summary
The task is inspired by the word TEA printed repeatedly around a teacup's rim, where starting at any letter and reading three letters yields a valid word (TEA, EAT, ATE). The challenge is to find all sets of words from the unixdict word list that share this cyclic property: each word is a rotation of the others, and every rotation must itself be a real word. The key insight is treating words as cyclic strings, where each member is produced by moving the first letter to the end.

## Task Requirements
- Use the unixdict.txt word list as the dictionary for English.
- Find sets of words all of the same length, with that length greater than two.
- Each word must be made of more than one distinct letter (excludes III, OOO, etc.).
- Words in a set are cyclic rotations of one another (first letter of one becomes the last letter of the next, e.g. ATE → TEA → EAT).
- All possible rotations produced by this first-to-last movement must exist in the list.
- Do not display permutations of an already-listed set (report each cyclic set only once).
- Display one line per qualifying set.

## Language Coverage
34 languages implement this task, showing broad coverage across mainstream and niche languages. Representative implementations include C, C++, Go, Rust, Java, JavaScript, Python, Haskell, Perl, Raku, Julia, and J.

## Connections
- [[StringRotation]] — the core operation is cyclically rotating a word's characters
- [[StringProcessing]] — reading, filtering, and comparing dictionary words
- [[SetMembership]] — fast lookup to verify each rotation exists in the word list
- [[Canonicalization]] — picking one representative per cyclic set to avoid duplicate output

## Contradictions
- None — reference task page.
