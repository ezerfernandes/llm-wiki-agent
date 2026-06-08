---
title: "I before E except after C (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-analysis]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/I_before_E_except_after_C
---

## Summary
The task tests the well-known English spelling mnemonic "I before E, except after C" against a real word list (unixdict.txt). The program must check two sub-clauses statistically and decide if each is "plausible." The key insight is treating a folk rule as an empirical hypothesis: a clause is plausible only if the supporting words outnumber the contradicting words by more than 2-to-1.

## Task Requirements
- Read the unixdict.txt word list.
- Check sub-clause 1: "I before E when not preceded by C" (count "ie" not after "c" vs "ei" not after "c").
- Check sub-clause 2: "E before I when preceded by C" (count "cei" vs "cie").
- A sub-clause is plausible if its feature count exceeds twice the opposite-feature count.
- The whole phrase is plausible only if both sub-clauses are plausible.
- Stretch goal: repeat the analysis weighting words by frequency from the British National Corpus list.
- Show both the program and its output.

## Language Coverage
86 languages implement this task, spanning systems languages, scripting languages, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Ruby, Perl, Raku, and AWK.

## Connections
- [[StringProcessing]] — core substring counting over a word list
- [[FrequencyAnalysis]] — tallying occurrences of "ie"/"ei" patterns
- [[StatisticalHypothesisTesting]] — plausibility decided by a count-ratio threshold
- [[TextCorpusAnalysis]] — stretch goal weights words by corpus frequency

## Contradictions
- None — reference task page.
