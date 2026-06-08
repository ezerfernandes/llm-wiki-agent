---
title: "Singly-linked list/Traversal (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, linked-list, iteration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Singly-linked_list/Traversal
---

## Summary
This task asks the programmer to walk a singly-linked list from its head node to its tail, visiting each element exactly once. The core idea is to start at the head pointer and repeatedly follow each node's "next" reference until a null/empty link signals the end of the list. It is a foundational data-structures exercise that pairs with the related list creation and element-definition tasks.

## Task Requirements
- Traverse a singly-linked list starting from its beginning (head node).
- Continue following the chain of next-pointers until reaching the end of the list.
- Visit (e.g. print or process) each node along the way.

## Language Coverage
89 languages implement this task, spanning low-level assembly, functional, and high-level scripting paradigms. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, Scheme, and several assembly variants (6502, ARM, AArch64, RISC-V).

## Connections
- [[LinkedList]] — the underlying data structure being traversed
- [[Iteration]] — the control pattern used to walk node-by-node
- [[Pointers]] — following next-references is the mechanism of traversal
- [[Recursion]] — many functional implementations traverse recursively instead of with a loop

## Contradictions
- None — reference task page.
