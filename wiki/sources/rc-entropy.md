---
title: "Entropy (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, information-theory, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Entropy
---

## Summary
The task asks the programmer to calculate the Shannon entropy H of a given input string, measured in bits per symbol. The core method is to count the frequency of each distinct character, convert counts to probabilities (count/N), and sum -p·log₂(p) over all distinct symbols. The key insight is that this "specific" (intensive) entropy measures information per symbol and ignores any patterns or order in the data, so two strings with identical symbol frequencies yield identical entropy regardless of arrangement.

## Task Requirements
- Compute the Shannon entropy H₂(X) = -Σ (countᵢ/N) · log₂(countᵢ/N) over the n distinct characters.
- Treat the input string as a discrete random variable of N total characters drawn from n distinct symbols.
- Use the example input X = "1223334444", which should produce a result of approximately 1.84644 bits/symbol.
- Report the result in bits per symbol.

## Language Coverage
110 languages implement this task, reflecting very broad coverage since it relies only on character counting and a base-2 logarithm available almost everywhere. Representative implementations include C, C++, Python, Haskell, Java, JavaScript, Ruby, Rust, Go, Perl, and Mathematica.

## Connections
- [[ShannonEntropy]] — the information-theoretic measure being computed
- [[InformationTheory]] — the field that defines entropy as average information per symbol
- [[Logarithm]] — base-2 log is central to the bits/symbol formula
- [[FrequencyAnalysis]] — counting character occurrences underpins the probability estimates

## Contradictions
- None — reference task page.
