---
title: "CPython"
type: entity
tags: [interpreter, runtime, python, compiler-testing, reference-implementation]
sources: [fuzzingbook-26-python-fuzzer-testing-compilers]
last_updated: 2026-06-06
---

# CPython

**CPython** is the reference implementation of the Python programming language — the interpreter written in C that compiles Python source to bytecode and executes it on a virtual machine. It ships the standard library, including the `ast` module (`ast.parse`, `ast.dump`, `ast.unparse`, `ast.fix_missing_locations`) and the built-in `compile()`/`exec()` functions that turn source or AST trees into runnable code.

## Role in The Fuzzing Book — Testing Compilers (Python Fuzzer)
[[fuzzingbook-26-python-fuzzer-testing-compilers|Ch 26]] uses Python/CPython as its worked **[[CompilerTesting|compiler-testing]]** domain. The chapter's central design choice leans directly on CPython's infrastructure: rather than write a grammar of concrete Python source, it grammars over **[[AbstractSyntaxTree|abstract syntax trees]]** and relies on CPython's *parser* (`ast.parse`) and *unparser* (`ast.unparse`) to handle the concrete-syntax round-trip both ways, with `compile()`/`exec()` available to actually run the result. The [[PythonFuzzer]] feeds generated AST strings back through this machinery to produce valid Python programs that can be used to stress the interpreter. The chapter also flags version-specific AST differences (optional fields added in Python 3.12 / 3.13) that the grammar must guard against — a reminder that the implementation under test evolves.

## Connections
- [[CompilerTesting]] — CPython is the implementation under test in Ch 26.
- [[PythonFuzzer]] — generates code targeting CPython via its `ast`/`compile`/`exec` infrastructure.
- [[AbstractSyntaxTree]] — exposed by CPython's `ast` module; the chapter's grammar operates over it.
- [[PythonLanguage]] — CPython is Python's reference implementation.
- [[DifferentialTesting]] — comparing CPython across versions/alternative implementations (PyPy, etc.) is the natural compiler-testing oracle.

## Sources
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — *The Fuzzing Book* Ch 26, "Testing Compilers (Python Fuzzer)."
