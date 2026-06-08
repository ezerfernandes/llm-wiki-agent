---
title: "Nested function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, closures, scope]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Nested_function
---

## Summary
This task asks the programmer to define an inner function nested inside an outer function, where the inner function reads and mutates variables belonging to the enclosing outer function. The concrete demonstration builds a numbered list ("1. first", "2. second", "3. third"): the outer function holds a separator and a counter, and the inner function consumes both to format each item. The key insight is lexical scoping — the inner function closes over the outer function's local state rather than receiving it as parameters.

## Task Requirements
- Write a program with two nested functions that prints the lines "1. first", "2. second", "3. third".
- The outer function (`MakeList` or equivalent) creates the whole list, takes the separator `". "` as an argument, and defines a counter variable tracking the item number.
- The inner function (`MakeItem` or equivalent) creates a single list item, reading the separator from the outer scope and modifying the outer counter.
- The example must show the inner function influencing variables defined in the outer function.

## Language Coverage
84 languages implement this task, spanning functional, procedural, object-oriented, and assembly traditions — closures and lexical nesting are nearly universal but expressed very differently across them. Representative implementations include Python, JavaScript, Haskell, Lua, C, Rust, Scheme, Common Lisp, Java, and OCaml.

## Connections
- [[Closure]] — the inner function captures and retains access to the outer function's variables.
- [[LexicalScoping]] — name resolution follows the static nesting structure that makes the outer counter visible inside.
- [[FirstClassFunctions]] — defining functions within functions relies on functions being ordinary, locally-definable values.
- [[MutableState]] — the inner function mutates the shared counter held by the outer function.

## Contradictions
- None — reference task page.
