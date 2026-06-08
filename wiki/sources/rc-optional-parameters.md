---
title: "Optional parameters (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-features, function-parameters]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Optional_parameters
---

## Summary
This task asks the programmer to define a function that sorts a table (a sequence of rows, where each row is a sequence of string cells) by one of its columns, exposing three optional parameters: a custom ordering function (lexicographic by default), a column index to compare on (the first by default), and a reverse flag. The key insight is that the task is about the *calling interface* for optional parameters, not the sort itself — implementations are encouraged to show whatever mechanism is most natural to the language (named/keyword arguments, default values, overloading on arity, distinct function names, or selector-based dispatch).

## Task Requirements
- Define a function/method that sorts a sequence of rows of string cells.
- Support an optional `ordering` parameter: a function defining string order, defaulting to lexicographic.
- Support an optional `column` parameter: an integer choosing which cell of each row to compare, defaulting to the first.
- Support an optional `reverse` parameter that reverses the ordering.
- Demonstrate positional and named optional parameters, and where natural, overloading on argument count (Java) or selector name (Smalltalk).
- Do not implement a sorting algorithm — rely on a built-in sort, or omit the implementation with a comment; the focus is the interface.

## Language Coverage
69 languages implement this task, spanning a broad mix of paradigms that surface optional parameters in different idiomatic ways. Representative examples include Python and Ruby (keyword/default arguments), Java (method overloading), Common Lisp and Racket (lambda lists / keyword args), Haskell and OCaml (higher-order functions, labeled args), Smalltalk-style selectors in Slate, plus C, C++, Go, Perl, and Tcl.

## Connections
- [[OptionalParameters]] — the named language feature this task showcases
- [[NamedArguments]] — the directly cross-referenced related task
- [[Sorting]] — the underlying operation being parameterized
- [[HigherOrderFunctions]] — passing the ordering comparator as an argument
- [[FunctionOverloading]] — one idiomatic way to express optional arguments

## Contradictions
- None — reference task page.
