---
title: "Doubly-linked list/Element insertion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, linked-list, pointers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Doubly-linked_list/Element_insertion
---

## Summary
The task asks the programmer to write a procedure that inserts a new node into a doubly-linked list, then to use it to insert element C between elements A and B in a list {A, B}. It builds on the linked-list element structure defined in a companion task. The key insight versus singly-linked insertion is that both the forward and backward pointers of the surrounding nodes must be updated so the bidirectional links stay consistent.

## Task Requirements
- Reuse the node/link structure from the companion "Doubly-Linked List (element)" task.
- Define a procedure that inserts a link into a doubly-linked list.
- Call that procedure to insert element C between A and B in the list {A, B}.
- Correctly maintain the backward-pointing links in addition to the forward ones.

## Language Coverage
56 languages implement this task, spanning systems languages, functional languages, and BASIC dialects. Representative implementations include C, C++, C#, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, and Ada.

## Connections
- [[DoublyLinkedList]] — the underlying data structure being mutated.
- [[LinkedList]] — the general family this task specializes.
- [[Pointers]] — the forward/backward references that must be rewired.
- [[DataStructures]] — broader category of the task.

## Contradictions
- None — reference task page.
