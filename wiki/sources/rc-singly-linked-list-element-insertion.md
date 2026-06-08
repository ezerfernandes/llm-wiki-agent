---
title: "Singly-linked list/Element insertion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, linked-list, pointers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Singly-linked_list/Element_insertion
---

## Summary
This task asks the programmer to define a method that inserts a new element into a singly-linked list immediately after a given existing element. The key insight is the standard pointer-splice: point the new node's `next` to the current node's successor, then point the current node's `next` to the new node — order matters to avoid losing the rest of the list. The concrete demonstration inserts element C after element A in a list A->B, yielding A->C->B.

## Task Requirements
- Reuse the link/node element defined in the companion task "Singly-Linked List (element)".
- Define a method that inserts a new element after a given element in the list.
- Demonstrate it by inserting C after A in the list A->B, producing A->C->B.

## Language Coverage
76 languages implement this task, spanning low-level assembly (360 Assembly, ARM/AArch64/x86/RISC-V Assembly) up through systems, functional, and scripting languages. Representative implementations include C, C++, Rust, Go, Ada, Haskell, OCaml, Python, Ruby, and Java.

## Connections
- [[LinkedList]] — the underlying data structure being mutated
- [[SinglyLinkedList]] — the specific single-pointer-per-node variant
- [[Pointers]] — the `next` reference manipulation at the core of the splice
- [[DataStructures]] — the broader task category

## Contradictions
- None — reference task page.
