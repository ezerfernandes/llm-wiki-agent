---
title: "Compiler Testing"
type: concept
tags: [fuzzing, testing, compiler-testing, security, grammar-based-fuzzing, program-generation]
sources: [fuzzingbook-26-python-fuzzer-testing-compilers]
last_updated: 2026-06-06
---

# Compiler Testing

**Compiler testing** (compiler/interpreter fuzzing) is the practice of automatically generating — and mutating — *programs* in some source language to stress-test the tool that processes them: a parser, compiler, or runtime/interpreter. The goal is to expose crashes, hangs, **miscompilations** (wrong output for valid code), and unwarranted rejections (valid code reported as invalid). Because the inputs are themselves programs, the generator must produce *syntactically* well-formed code (and ideally *semantically* well-formed code) — making compiler testing one of the most demanding applications of [[GrammarBasedFuzzing|grammar-based fuzzing]].

## From The Fuzzing Book — Testing Compilers (Python Fuzzer)
[[fuzzingbook-26-python-fuzzer-testing-compilers|Ch 26]] develops compiler testing for **Python / CPython** as the worked domain ([[CPython]]). Its key design lesson: do *not* grammar over concrete source text. A concrete grammar can easily *produce* code but is brittle when you also need to *parse and mutate* it — whitespace, comments, continuation lines, C type identifiers, and Python indentation defeat a plain [[ContextFreeGrammar|context-free grammar]]. Instead the chapter writes `PYTHON_AST_GRAMMAR`, a grammar over **[[AbstractSyntaxTree|abstract syntax tree]]** constructor calls, and lets Python's own `ast.parse()`/`ast.unparse()` (and `compile()`/`exec()`) handle the concrete-syntax round-trip both ways. From this it builds the [[PythonFuzzer]] class, shows how to steer output (grammar editing and [[ISLa]] constraints), how to mutate parsed code (`ISLaSolver.mutate()` over [[DerivationTree|derivation trees]]), and an [[EvolutionaryFuzzing|evolutionary fuzzing]] loop using [[Coverage|coverage]] as a [[FitnessFunction|fitness function]] to reach a planted bug. The chapter notes generated programs are valid only *syntactically* — most fail with `TypeError` at runtime — and warns against blindly executing them (`os.remove("/")`). It cites **[[CSmith]]** (Yang et al., 2011), the C-program generator that found 400+ Clang/GCC bugs, as the seminal prior work and the bar for *semantic* validity.

## The two core requirements
- **Generate well-formed programs** — at minimum syntactically valid; CSmith and serious compiler fuzzers also enforce *semantic* validity (type correctness, definition-before-use, no undefined/unspecified behavior) so failures are unambiguously compiler bugs.
- **An oracle** — for crashes the oracle is trivial (the compiler segfaults/throws). For miscompilations the standard oracle is **[[DifferentialTesting|differential testing]]**: run the same program through multiple compilers/optimization levels/versions and flag disagreement.

## Connections
- [[PythonFuzzer]] — the concrete Python compiler-testing fuzzer this chapter builds.
- [[DifferentialTesting]] — the canonical oracle for miscompilation bugs.
- [[CSmith]] — the seminal C-compiler fuzzer; the prototype of the field.
- [[AbstractSyntaxTree]] — the abstraction the chapter grammars over instead of source text.
- [[GrammarBasedFuzzing]] / [[ContextFreeGrammar]] — the underlying generation technique and its expressiveness limits for code.
- [[EvolutionaryFuzzing]] / [[Coverage]] — coverage-guided evolution toward bug-triggering programs.
- [[ISLa]] — the generator/solver backend (`PythonFuzzer` subclasses `ISLaSolver`).
- [[CPython]] — the reference implementation under test in the chapter.
- [[Fuzzing]] / [[Testing]] — the broader field and discipline.

## Sources
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — *The Fuzzing Book* Ch 26, "Testing Compilers (Python Fuzzer)."
