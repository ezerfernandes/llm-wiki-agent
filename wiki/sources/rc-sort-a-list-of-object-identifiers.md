---
title: "Sort a list of object identifiers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sort_a_list_of_object_identifiers
---

## Summary
The task asks the programmer to sort a list of Object Identifiers (OIDs) — dot-separated strings of non-negative base-10 integers used to identify objects in network data — into their natural sort order. The key insight is that a plain string sort is wrong: each dot-separated field must be compared numerically, so the comparison is lexicographical over the sequence of fields but with integer (not character) comparison within each field.

## Task Requirements
- Sort a list of OID strings into natural order.
- An OID is one or more non-negative integers in base 10, separated by dots, starting and ending with a number.
- Order fields lexicographically, but compare each dot-separated field numerically rather than as text.
- Reproduce the given test case (e.g. `1.3.6.1.4.1.11.2.17.5.2.0.79` sorts before `1.3.6.1.4.1.11150.3.4.0`).

## Language Coverage
56 languages implement this task, spanning systems, functional, scripting, and array languages. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Ruby, J, and Raku.

## Connections
- [[Sorting]] — the task is a specialized sort with a custom key/comparator.
- [[NaturalSortOrder]] — numeric-aware ordering of strings containing digits.
- [[ObjectIdentifier]] — the dotted-integer OID notation being sorted.
- [[LexicographicalOrder]] — fields are ordered lexicographically as integer sequences.
- [[CustomComparator]] — sorting driven by a domain-specific comparison function.

## Contradictions
- None — reference task page.
