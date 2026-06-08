---
title: "Compiler/code generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, compilers, code-generation, virtual-machine]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compiler/code_generator
---

## Summary
This task is the back-end stage of a multi-part compiler exercise: it takes the flattened Abstract Syntax Tree produced by the syntax analyzer and emits virtual-machine assembly code that a companion stack-based VM can execute. The key insight is that walking the AST recursively and emitting stack-machine instructions (push/fetch/store, arithmetic, comparisons, and relative jumps) is enough to lower a structured program into linear bytecode, with branch targets resolved as offsets relative to the current code address.

## Task Requirements
- Read a flattened AST (one node per line; two-token lines are leaf nodes for Identifier, Integer, String) from a file and/or stdin and rebuild it as an internal parse tree.
- Emit output in text form representing virtual assembly: a header line giving the data size (count of unique 32-bit variables) and number of constant strings, then the constant strings, then the code.
- Generate instructions for a stack machine with `sp` and `pc` registers: `fetch [index]`, `store [index]`, `push n`, relative `jmp (n) addr` and `jz (n) addr`, binary ops (add, sub, mul, div, mod, lt, gt, le, ge, eq, ne, and, or), unary ops (neg, not), `prtc`/`prti`/`prts` for output, and `halt`.
- Pass the provided `while.t` example plus the additional sample programs; the C and Python versions are the reference implementations.

## Language Coverage
28 languages implement this task, a moderate breadth typical of these multi-stage compiler exercises, spanning systems and functional styles. Representative implementations include C, Python, Go, Rust, Java, JavaScript, Forth, Scheme, ALGOL 68, and Nim.

## Connections
- [[AbstractSyntaxTree]] — the input data structure this stage consumes
- [[CodeGeneration]] — the compiler back-end phase this task implements
- [[StackMachine]] — the target execution model for the emitted bytecode
- [[Bytecode]] — the linear virtual assembly produced as output
- [[CompilerPipeline]] — follows lexical and syntax analysis, feeds the virtual machine interpreter

## Contradictions
- None — reference task page.
