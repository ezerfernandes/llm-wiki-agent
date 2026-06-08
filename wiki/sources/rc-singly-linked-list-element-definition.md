---
title: "Singly-linked list/Element definition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, linked-list]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Singly-linked_list/Element_definition
---

## Summary
This task asks the programmer to define the element (node) data structure used to build a singly-linked list. Each element must hold a numeric value and carry a mutable link pointing to the next element in the chain. The key insight is that a singly-linked list is a self-referential structure: each node references the same node type, with a null/empty link marking the end of the list.

## Task Requirements
- Define a data structure representing a single element (node) of a singly-linked list.
- The element must contain a data member capable of holding a numeric value.
- The element must contain a link to the next element, and that link must be mutable (re-assignable).

## Language Coverage
87 languages implement this task, spanning low-level assembly through high-level functional and dynamic languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, Ada, and several assembly variants such as x86 and ARM Assembly.

## Connections
- [[LinkedList]] — the element is the building block of this structure
- [[DataStructures]] — the broad category this task belongs to
- [[Pointers]] — the mutable "next" link is typically a pointer or reference
- [[RecursiveDataType]] — the element is self-referential, pointing to its own type

## Contradictions
- None — reference task page.
