---
title: "History variables (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-feature, state-management]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/History_variables
---

## Summary
This task asks the programmer to demonstrate "history variables" — variables that retain not only their current value but every value they have previously held. The key insight is that few languages support this natively, so most solutions implement it by wrapping a value in a structure that appends each assignment to a log, allowing past states to be recalled non-destructively.

## Task Requirements
- Enable history variable support if the language requires it.
- Define a history variable.
- Assign three values to it in sequence.
- Non-destructively display the full history of values.
- Recall (read back) the three stored values.
- Extra credit: if the language lacks native history variables, show how the feature can be implemented.

## Language Coverage
56 languages implement this task, spanning systems and scripting languages alike, with most demonstrating a custom implementation since native support is rare. Representative entries include Ada, C, C++, C#, Haskell, Python, Ruby, Rust, Clojure, Common Lisp, Tcl, and 68000 Assembly.

## Connections
- [[StateManagement]] — tracking the evolving state of a variable over time
- [[ImmutableData]] — preserving past values rather than overwriting them
- [[ObserverPattern]] — assignment can be intercepted to record changes
- [[UndoHistory]] — recalling prior values resembles undo/redo stacks
- [[DataStructures]] — typically backed by a stack or list of prior values

## Contradictions
- None — reference task page.
