---
title: "Visualize a tree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, tree, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Visualize_a_tree
---

## Summary
The task asks the programmer to produce a human-friendly visual representation of a tree structure (a rooted, connected, acyclic graph). Neither the tree's content nor the output format is fixed — common approaches include indented text (like the Unix `tree` command), nested HTML tables, hierarchical GUI widgets, or 2D/3D images. The deliberately vague requirement of "friendly" output makes this an open-ended rendering exercise rather than an algorithmic one.

## Task Requirements
- Write a program that produces a visual representation of some tree.
- The tree's content is arbitrary and chosen by the implementer.
- The output format is free; the sole constraint is that it be human friendly.
- "Friendly" is intentionally undefined — interpret it reasonably.

## Language Coverage
55 languages implement this task, spanning systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Java, Python, Haskell, Go, Rust, Ruby, Perl, and even AArch64/ARM/RISC-V Assembly, reflecting how each ecosystem handles recursive traversal and text formatting.

## Connections
- [[TreeDataStructure]] — the rooted acyclic graph being rendered
- [[TreeTraversal]] — depth-first walking to emit each node at its level
- [[Recursion]] — the natural technique for descending the hierarchy
- [[PrettyPrinting]] — formatting indented, human-readable output

## Contradictions
- None — reference task page.
