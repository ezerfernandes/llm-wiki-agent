---
title: "Catamorphism (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functional-programming, higher-order-functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Catamorphism
---

## Summary
This task asks the programmer to show how a *reduce* operation (also known as *fold*, *foldl*, or *foldr*) works or would be implemented in their language. A reduce takes a list or array and a binary function, then applies that function across successive elements to collapse the whole collection down to a single accumulated value. The key insight is that this single primitive — a catamorphism — generalizes many aggregate operations such as sum, product, maximum, and concatenation.

## Task Requirements
- Demonstrate the *reduce* / *fold* operation in the chosen language.
- Either use the language's built-in reduce/foldl/foldr facility or implement one if none exists.
- Show how successive members of a list are combined via a function into one final value.

## Language Coverage
111 languages implement this task, spanning the full spectrum from functional languages where fold is a native idiom to assembly and BASIC dialects where it must be hand-rolled. Representative implementations include Haskell, OCaml, Scheme, Clojure, Python, JavaScript, Rust, Java, Erlang, and APL.

## Connections
- [[FoldHigherOrderFunction]] — the generalized fold/reduce operation this task is built on
- [[Catamorphism]] — the category-theory concept that names this task
- [[HigherOrderFunctions]] — reduce takes a function as an argument
- [[FunctionalProgramming]] — folds are a core idiom of the paradigm
- [[Recursion]] — foldl/foldr are naturally expressed recursively

## Contradictions
- None — reference task page.
