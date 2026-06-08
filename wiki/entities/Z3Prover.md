---
title: "Z3 (SMT Solver / Theorem Prover)"
type: entity
tags: [tool, smt-solver, theorem-prover, constraints, formal-methods, fuzzing, symbolic-execution, microsoft-research]
sources: [fuzzingbook-20-concolic-fuzzer, fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# Z3

**Z3** is a high-performance **Satisfiability Modulo Theories (SMT) solver** and automated theorem prover developed by [[microsoftresearch|Microsoft Research]] (Leonardo de Moura and Nikolaj Bjørner). Given logical formulas combining boolean structure with background *theories* — integers, reals, bit-vectors, arrays, and **strings** — Z3 decides satisfiability and, when satisfiable, returns a concrete **model** (an assignment of values to variables). It reads the [[SMTSolver|SMT-LIB]] standard format, exposes a Python API (`z3.Solver`, `z3.Int`, `z3.String`, `z3.solve`), and ships as a command-line `z3` binary. Z3 is the de-facto engine behind much of program analysis, verification, and test generation.

> **Naming note.** This entity is the Z3 *SMT solver/theorem prover*. It is unrelated to the wiki's `Z3` **concept** page, which documents Konrad Zuse's 1941 electromechanical Z3 *computer*. They share only a name.

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] uses Z3 as the constraint engine for [[ConcolicExecution|concolic execution]]. The `ConcolicTracer`'s symbolic proxy classes (`zbool`, `zint`, `zstr`, `zfloat`) build Z3 expressions (`z3.Int`, `z3.String`, `z3.SubString`, `z3.Length`, `z3.IndexOf`, `z3.And`, `z3.Not`) as a program runs; the resulting [[PathConstraint|path condition]] is solved two ways — `zeval_py()` via the `z3.Solver()` Python API, and `zeval_smt()` by shelling out to the `z3` binary on a generated SMT-LIB file. Z3's **theory of strings** is what lets the chapter solve constraints like `str.substr(s,0,1) == "+"` to synthesize CGI/SQL inputs. The chapter requires `z3-solver >= 4.8.13.0`, sets a 30-second timeout, and documents several Z3 string-solver bugs/limitations it works around (e.g. `str.to_code` handling, an `IndexOf` return-type quirk).

Z3 is reused across *The Fuzzing Book*'s semantic-fuzzing part: it is the hidden engine of [[ISLa]]'s solver in [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] and the constraint solver for [[fuzzingbook-21-symbolic-fuzzer|symbolic fuzzing in Ch 21]].

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] uses Z3 as the engine of *pure* [[SymbolicExecution|symbolic execution]]. [[SymbolicVariable|Symbolic variables]] are minted as `z3.Int`/`z3.Real`/`z3.String` from type annotations; each CFG path's [[PathConstraint|path condition]] is assembled as a Z3 conjunction and solved with `z3.solve()`/`z3.Solver()` (using `push`/`pop` checkpoints and `z3.Not(seen)` to enumerate distinct solutions). Z3 also *proves paths infeasible* by returning *unsat* and *simplifies* merged function summaries via `z3.simplify()`. The chapter notes z3py does **not** expose the SMT-LIB `define-fun` macro facility, so function summaries are namespaced with an AST `prefix_vars()` hack instead, and it asserts `z3.get_version() >= (4, 8, 6, 0)`. The Background credits Z3 to Leonardo de Moura and Nikolaj Bjørner at [[microsoftresearch|Microsoft Research]], "one of the most popular solvers."

## Connections
- [[microsoftresearch]] — the Microsoft Research lab that develops Z3.
- [[microsoft]] — parent company.
- [[SMTSolver]] — Z3 is the canonical implementation of the SMT-solver concept.
- [[ConcolicExecution]] / [[SymbolicExecution]] — use Z3 to solve and negate path conditions.
- [[PathConstraint]] — the formulas Z3 checks for satisfiability and solves.
- [[ConcolicFuzzing]] / [[PathExploration]] — Z3 synthesizes the path-reaching inputs.
- [[ISLa]] — Ch 17's constraint solver built on Z3.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] / [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] / [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]].

## Sources
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing" (Z3 as the SMT engine for concolic execution).
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (Z3 as the engine for pure symbolic execution; credited to de Moura & Bjørner at Microsoft Research).
