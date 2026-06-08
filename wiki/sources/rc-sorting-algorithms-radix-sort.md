---
title: "Sorting algorithms/Radix sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Radix_sort
---

## Summary
This task asks the programmer to sort an integer array using radix sort, a non-comparison sorting algorithm. Rather than comparing elements directly, radix sort distributes integers into buckets based on individual digits (or bits), processing one digit position at a time. The key insight is that by sorting on each digit from least significant to most significant (LSD variant) using a stable sub-sort, the array becomes fully ordered, achieving roughly linear time for fixed-width keys.

## Task Requirements
- Sort an integer array with the radix sort algorithm.
- Intended to complete the characterization of sort algorithms task (one of a family of comparable sorting implementations).

## Language Coverage
55 languages implement this task, spanning systems and scripting languages as well as several assembly dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, and ARM Assembly.

## Connections
- [[RadixSort]] — the algorithm this task implements
- [[SortingAlgorithms]] — the broader family of sorting tasks
- [[CountingSort]] — common stable sub-sort used per digit in LSD radix sort
- [[StableSort]] — stability is required for the per-digit passes to compose correctly
- [[NonComparisonSort]] — class of algorithms that avoid element-to-element comparisons

## Contradictions
- None — reference task page.
