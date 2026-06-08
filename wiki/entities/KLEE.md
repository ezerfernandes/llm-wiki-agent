---
title: "KLEE"
type: entity
tags: [tool, symbolic-execution, testing, security, program-analysis, llvm, smt]
sources: [fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# KLEE

**KLEE** is a landmark **symbolic execution** engine that operates over LLVM bitcode to automatically generate high-coverage test inputs and find bugs in real programs (notably the GNU Coreutils). It runs the program on [[SymbolicVariable|symbolic inputs]], forks at each branch, and uses an [[SMTSolver|SMT/constraint solver]] to decide path feasibility and synthesize concrete inputs — the canonical academic implementation of [[SymbolicExecution|symbolic execution]] (Cadar, Dunbar & Engler, OSDI 2008).

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] cites KLEE in its Background as one of the "well known symbolic execution tools," alongside [[angr]], Driller, and [[SAGE]]. The chapter's own [[SymbolicFuzzer|`SymbolicFuzzer`]] is a from-scratch, pedagogical Python analogue of what production tools like KLEE do at scale: statically enumerate [[ControlFlow|control-flow]] paths, build each [[PathConstraint|path condition]], and solve it with an SMT solver ([[Z3Prover|Z3]]).

## Connections
- [[SymbolicExecution]] — KLEE is the best-known implementation of the technique.
- [[SymbolicFuzzer]] — Ch 21's teaching engine that mirrors what KLEE does in production.
- [[SMTSolver]] / [[Z3Prover]] — the constraint-solving backend symbolic-execution tools rely on.
- [[angr]] / [[SAGE]] — fellow symbolic-execution tools cited in the same Background.
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] — where KLEE is referenced.

## Sources
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (Background: KLEE as a well-known symbolic-execution tool).
