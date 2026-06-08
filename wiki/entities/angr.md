---
title: "angr"
type: entity
tags: [tool, symbolic-execution, concolic-execution, binary-analysis, reverse-engineering, security, testing]
sources: [fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# angr

**angr** is an open-source **binary analysis** framework that combines [[SymbolicExecution|symbolic]] and [[ConcolicExecution|concolic]] execution with static analysis to reason about compiled programs (no source needed). Widely used in vulnerability research, reverse engineering, and CTF automation, it builds a [[ControlFlow|control-flow graph]] of a binary, executes paths over [[SymbolicVariable|symbolic inputs]], and solves the resulting [[PathConstraint|path conditions]] with an [[SMTSolver|SMT solver]] to reach target states (Wang et al., "angr").

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] cites angr in its Background as one of the "well known symbolic execution tools" applied to vulnerability analysis of binary programs, alongside [[KLEE]], Driller (an angr-based concolic/fuzzing hybrid), and [[SAGE]]. It is a production-scale instance of the same enumerate-paths-and-solve-constraints approach the chapter's [[SymbolicFuzzer|`SymbolicFuzzer`]] implements pedagogically in Python.

## Connections
- [[SymbolicExecution]] / [[ConcolicExecution]] — angr's core analysis engines.
- [[SymbolicFuzzer]] — Ch 21's teaching analogue of binary symbolic-execution tools like angr.
- [[ControlFlow]] / [[PathConstraint]] — angr builds a binary's CFG and solves path conditions.
- [[SMTSolver]] / [[Z3Prover]] — the constraint-solving backend.
- [[KLEE]] / [[SAGE]] — fellow symbolic-execution tools cited in the same Background.
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] — where angr is referenced.

## Sources
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (Background: angr as a well-known symbolic-execution tool).
