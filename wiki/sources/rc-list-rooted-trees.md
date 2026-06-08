---
title: "List rooted trees (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, trees, enumeration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/List_rooted_trees
---

## Summary
The task asks the programmer to enumerate every distinct way of nesting *n* identical bags, which is equivalent to listing all unlabeled *n*-node rooted trees (the outermost bag is the root, each contained bag a subtree). A balanced-parenthesis string is the natural representation. The key insight is that "all bags are identical" means children of a node are unordered, so configurations that differ only by reordering siblings count as one — making the count match OEIS A000081 rather than the Catalan numbers.

## Task Requirements
- Given *n*, enumerate (not merely count) all ways of nesting *n* bags.
- Use balanced-parenthesis notation, or any unambiguous and intuitive tree representation.
- Treat all bags as identical, so sibling order is irrelevant and duplicates must be deduplicated.
- Counting via OEIS A000081 formulas is explicitly discouraged; the goal is enumeration.
- Demonstrate with *n* = 5, which should produce exactly 9 distinct trees.

## Language Coverage
33 languages implement this task, spanning high-level scripting, functional, systems, and even several hand-written assembly targets. Representative implementations include C, C++, Rust, Go, Haskell, Python, Java, JavaScript, Julia, Perl, and lower-level entries such as AArch64 Assembly and RISC-V Assembly.

## Connections
- [[RootedTree]] — the underlying combinatorial structure being enumerated
- [[Combinatorics]] — counting and listing distinct unlabeled structures
- [[BalancedParentheses]] — the canonical string encoding of each tree
- [[CanonicalForm]] — needed to deduplicate trees that differ only by sibling order
- [[IntegerPartition]] — child-subtree sizes are built from partitions of n-1

## Contradictions
- None — reference task page.
