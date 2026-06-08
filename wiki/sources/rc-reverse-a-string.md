---
title: "Reverse a string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, unicode]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Reverse_a_string
---

## Summary
The task is to take a string and produce its reversal, so that "asdf" becomes "fdsa". The key subtlety, offered as extra credit, is that a naive reversal of code units or code points can corrupt Unicode combining characters: a base character followed by a combining mark must stay together rather than be split, so "as⃝df̅" should reverse to "f̅ds⃝a" instead of mangling the diacritics.

## Task Requirements
- Take an input string and reverse the order of its characters.
- For the extra credit, preserve Unicode combining characters by treating each base character plus its attached combining marks as a single grapheme cluster that moves as a unit.

## Language Coverage
276 languages implement this task, making it one of Rosetta Code's broadest entries since string reversal is a fundamental operation present in nearly every language. Representative implementations include C, Python, Haskell, Java, JavaScript, Rust, Perl, Ruby, Go, and APL.

## Connections
- [[StringProcessing]] — reversal is a canonical string-manipulation operation
- [[Unicode]] — correct reversal must respect encoding boundaries
- [[GraphemeClusters]] — combining characters require grapheme-aware handling
- [[InPlaceAlgorithms]] — many implementations use two-pointer swapping

## Contradictions
- None — reference task page.
