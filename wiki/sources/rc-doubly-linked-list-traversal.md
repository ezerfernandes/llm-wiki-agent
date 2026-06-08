---
title: "Doubly-linked list/Traversal (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, linked-list, iteration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Doubly-linked_list/Traversal
---

## Summary
This task asks the programmer to walk a doubly-linked list in both directions: from the head node to the tail (following each node's "next" pointer) and from the tail back to the head (following each node's "previous" pointer). The key insight is that the bidirectional links of a doubly-linked list make reverse traversal a constant-overhead operation, unlike a singly-linked list which would require auxiliary structure or recursion to iterate backward.

## Task Requirements
- Traverse from the beginning of a doubly-linked list to the end.
- Traverse from the end of the list back to the beginning.
- Build on the list defined in the companion Doubly-linked list/Definition task.

## Language Coverage
56 languages implement this task, spanning systems languages, functional languages, scripting languages, and several assembly/BASIC dialects. Representative implementations include C, C++, C#, Rust, Go, Java, Haskell, Python, Ruby, ALGOL 68, and ARM Assembly.

## Connections
- [[DoublyLinkedList]] — the data structure being traversed
- [[Iteration]] — forward and backward looping over the nodes
- [[Pointer]] — next/previous references that enable bidirectional walking
- [[DataStructures]] — the broader category this task belongs to

## Contradictions
- None — reference task page.
