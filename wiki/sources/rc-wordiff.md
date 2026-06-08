---
title: "Wordiff (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, game]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Wordiff
---

## Summary
Wordiff is a turn-based word game where each contestant must produce a new dictionary word of three or more letters that differs from the previous word by exactly one edit. The single allowed difference is a deletion of one letter, an addition of one letter, or the substitution of one letter — effectively requiring the two words to be at edit distance one. The task is to build a program that runs the game and validates each move against the dictionary, against past words, and against the one-letter-difference rule.

## Task Requirements
- Ask for the contestants' names.
- Choose an initial random three- or four-letter word from the dictionary.
- Prompt each contestant in turn for a wordiff word.
- Validate each submitted word: it must be in the dictionary, must not repeat any prior word, and must differ from the last word by exactly one deletion, addition, or substitution.
- Optional stretch goals: track per-player response timing, allow a maximum game time, halt play when exceeded, and on timeout declare the loser as the player with the longest average response time.

## Language Coverage
21 languages implement this task, a moderate-breadth spread covering systems, scripting, functional, and BASIC-family languages. Representative implementations include C++, Rust, Java, JavaScript, Python, Perl, Raku, Julia, Nim, Phix, J, jq, and Wren.

## Connections
- [[EditDistance]] — the one-letter-difference rule is exactly Levenshtein distance one.
- [[StringProcessing]] — words are compared and mutated character by character.
- [[DictionaryLookup]] — every move is validated against a word list.
- [[TurnBasedGames]] — alternating-player game loop with state tracking.

## Contradictions
- None — reference task page.
