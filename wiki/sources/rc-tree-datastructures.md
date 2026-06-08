---
title: "Tree datastructures (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, trees, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tree_datastructures
---

## Summary
This task explores two contrasting in-memory representations of the same tree. The "nest form" models each node as a name plus a (possibly empty) ordered list of child nodes, capturing structure through actual nesting. The "indent form" flattens the tree into an ordered list of (indentation level, name) pairs, where depth is encoded by an integer rather than by containment. The key insight is that both representations are equivalent, and converting between them round-trips losslessly.

## Task Requirements
- Define a nest datastructure format and a textual representation for arbitrary trees.
- Define an indent datastructure format and a textual representation for arbitrary trees.
- Implement a routine to convert from nest form to indent form.
- Implement a routine to convert from indent form back to nest form.
- Encode the given RosettaCode example tree into nest form and display it.
- Transform that nest form into indent form and display it.
- Transform the indent form back into nest form and display it.
- Compare the initial and final nest forms, which should be identical (a formatted-string comparison is acceptable).

## Language Coverage
20 languages implement this task, spanning systems, functional, and scripting families. Representative implementations include C++, Go, Rust, Zig, Haskell, Java, Julia, Nim, Perl, Python, Raku, and Wren.

## Connections
- [[TreeDataStructure]] — the central abstraction being represented two ways
- [[Recursion]] — natural traversal strategy for the nested form
- [[TreeTraversal]] — flattening a tree to indent form is a depth-first walk
- [[Serialization]] — converting between in-memory and textual representations

## Contradictions
- None — reference task page.
