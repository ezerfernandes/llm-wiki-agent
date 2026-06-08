---
title: "Doubly-linked list/Definition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, linked-list]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Doubly-linked_list/Definition
---

## Summary
This task asks the programmer to define the data structure for a complete doubly-linked list. Unlike a singly-linked list, each node holds references to both its predecessor and its successor, enabling traversal in both directions. The key design constraint is that the structure must support insertion at the head, tail, and middle while never forming a circular loop (the head's previous pointer and the tail's next pointer remain null).

## Task Requirements
- Define the data structure for a complete doubly-linked list (a node with forward and backward links plus the list container).
- Support adding elements at the head of the list.
- Support adding elements at the tail of the list.
- Support adding elements in the middle of the list.
- Ensure the structure does not allow circular loops (it must be a proper linear, non-cyclic list).

## Language Coverage
56 languages implement this task, spanning systems languages, functional languages, assembly, and scripting languages. Representative implementations include C, C++, C#, Rust, Go, Java, Haskell, Common Lisp, Python, and ARM Assembly.

## Connections
- [[DoublyLinkedList]] — the data structure being defined
- [[LinkedList]] — the broader family of node-and-pointer structures
- [[Pointer]] — the prev/next references that wire nodes together
- [[DataStructures]] — the general category this task belongs to

## Contradictions
- None — reference task page.
