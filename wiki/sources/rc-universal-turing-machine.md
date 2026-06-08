---
title: "Universal Turing machine (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, theory-of-computation, automata, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Universal_Turing_machine
---

## Summary
The task asks the programmer to build a simulator that can take the formal definition of any Turing machine — its states, alphabet, blank symbol, and transition rules — and execute it on a tape. The key insight is that implementing such a universal machine is itself a proof that the host language is Turing-complete. Because real memory is finite, the tape is emulated as a dynamically growing structure rather than a truly infinite one.

## Task Requirements
- Accept an arbitrary Turing machine definition: state set, initial state, terminating (halting) states, permissible symbols, and a blank symbol.
- Drive a tape supporting three head actions: "left", "right", and "stay".
- Apply transition rules of the form (current state, read symbol) → (write symbol, move, next state) until a terminating state is reached.
- Run two test machines: a "simple incrementer" (states q0/qf over symbols B,1, input tape `1 1 1`) and a "three-state busy beaver" (states a,b,c,halt over symbols 0,1, empty input tape).
- Bonus: run the 5-state, 2-symbol probable busy beaver from Wikipedia, which executes for over 47 million steps.

## Language Coverage
63 languages implement this task, spanning functional, imperative, logic, and array paradigms — a broad showing because the problem is a canonical Turing-completeness demonstration. Representative implementations include C, C++, Rust, Go, Python, Haskell, Prolog, Common Lisp, Java, and Mathematica.

## Connections
- [[TuringMachine]] — the abstract computation model being simulated
- [[TuringCompleteness]] — implementing this machine proves the host language is Turing-complete
- [[TheoryOfComputation]] — foundational area the task belongs to
- [[BusyBeaver]] — the test machines that maximize steps before halting
- [[FiniteStateAutomaton]] — the transition-rule control structure underlying the machine

## Contradictions
- None — reference task page.
