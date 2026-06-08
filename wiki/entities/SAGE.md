---
title: "SAGE"
type: entity
tags: [tool, symbolic-execution, concolic-execution, whitebox-fuzzing, testing, security, microsoft]
sources: [fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# SAGE

**SAGE** (Scalable Automated Guided Execution) is Microsoft's production **whitebox fuzzing** tool, built on dynamic symbolic / [[ConcolicExecution|concolic execution]]. It traces a program on a concrete input, collects the [[PathConstraint|path condition]], systematically negates branch constraints, and solves them with an [[SMTSolver|SMT solver]] to generate new inputs that drive execution down un-taken paths — applied at scale to find security bugs in large Windows binaries (Godefroid, Levin & Molnar). It is one of the most influential industrial applications of [[SymbolicExecution|symbolic execution]].

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] lists SAGE (citing Godefroid et al. 2012) in its Background among the "well known symbolic execution tools" used "extensively in vulnerability analysis of software, especially binary programs," alongside [[KLEE]], [[angr]], and Driller. SAGE's negate-a-branch-and-resolve loop is exactly the [[PathExploration|path-exploration]] strategy the chapter's [[SymbolicFuzzer|`SymbolicFuzzer`]] and its Exercise-3 concolic variant demonstrate on small Python functions.

## Connections
- [[SymbolicExecution]] / [[ConcolicExecution]] — SAGE is a large-scale (concolic) whitebox-fuzzing application of these techniques.
- [[PathExploration]] / [[PathConstraint]] — SAGE negates branch constraints and re-solves to reach new paths.
- [[SymbolicFuzzer]] — Ch 21's pedagogical analogue of SAGE-style exploration.
- [[SMTSolver]] / [[Z3Prover]] — the constraint solver behind SAGE-style tools (Microsoft's Z3 originated to serve exactly this need).
- [[microsoft]] — SAGE's origin.
- [[KLEE]] / [[angr]] — fellow symbolic-execution tools cited in the same Background.
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] — where SAGE is referenced.

## Sources
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (Background: SAGE as a well-known symbolic-execution tool).
