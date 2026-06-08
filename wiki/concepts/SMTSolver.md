---
title: "SMT Solver (Satisfiability Modulo Theories)"
type: concept
tags: [constraints, smt, solver, z3, smt-lib, formal-methods, fuzzing, symbolic-execution, testing]
sources: [fuzzingbook-17-fuzzing-with-constraints, fuzzingbook-20-concolic-fuzzer, fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# SMT Solver

An **SMT solver** decides **Satisfiability Modulo Theories (SMT)** — that is, the satisfiability of logical formulas combining boolean structure with *background theories* such as integers, reals, bit-vectors, arrays, and **strings**. Given a set of constraints over typed variables, an SMT solver either returns a **model** (concrete values satisfying all constraints) or reports *unsatisfiable*. SMT solvers generalize SAT (pure boolean satisfiability) by adding decision procedures for these theories. The de-facto standard input format is **SMT-LIB**, a LISP-like notation that names the available theory functions; the canonical solver is **Z3** (from [[microsoftresearch|Microsoft Research]]).

> **Naming note.** The "Z3" SMT solver here is *not* the same as the wiki's existing `Z3` concept page, which documents Konrad Zuse's 1941 Z3 *computer*. This page covers the constraint-solving engine.

## Role in fuzzing
SMT solvers are the engine behind two threads in *The Fuzzing Book*'s Part IV (Semantic Fuzzing):
- **Constraint-based input generation** — [[ConstraintBasedFuzzing|constraint-based fuzzing]] (e.g. [[ISLa]]) reduces declarative input constraints to an SMT problem and asks the solver for a model, yielding semantically valid inputs.
- **Symbolic/concolic execution** — [[fuzzingbook-21-symbolic-fuzzer|symbolic fuzzing (Ch 21)]] and [[fuzzingbook-20-concolic-fuzzer|concolic fuzzing (Ch 20)]] collect path conditions over the program and solve them to derive inputs that reach a target location.

## From The Fuzzing Book — Fuzzing with Constraints
[[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] uses an SMT solver as the hidden engine of [[ISLa]]'s `ISLaSolver`. The constraint functions ISLa exposes — `str.len()`, `str.to.int()`, `str.to_code()`, and operators `>`, `=`, `mod`, `+` — "actually stem from the SMT-LIB library for satisfiability modulo theories," and the full SMT-LIB theory catalog is available inside ISLa constraints. ISLa accepts both programmer-style infix and raw SMT-LIB prefix syntax (`(> (str.to.int <pagesize>) 1024)`), though it keeps boolean operators like `and` in its own layer (cheaper than passing them to the solver). The solver parameter `max_number_smt_instantiations` directly bounds how many times ISLa calls the underlying SMT solver, trading structurally-similar inputs for throughput.

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] uses [[Z3Prover|Z3]] as the engine for [[ConcolicExecution|concolic execution]]. The `ConcolicTracer`'s symbolic proxies (`zbool`/`zint`/`zstr`/`zfloat`) build Z3 terms over the *theory of integers* and *theory of strings* (`z3.SubString`, `z3.Length`, `z3.IndexOf`) as the program runs, accumulating a [[PathConstraint|path condition]]. That condition is solved two ways — `zeval_py()` via the `z3.Solver()` Python API and `zeval_smt()` by shelling out to the `z3` binary on a generated SMT-LIB file (parsed back with `parse_sexp()`). Solving the unmodified condition reproduces a path; solving it with one predicate *negated* yields an input on a different path — the core move of [[ConcolicFuzzing|concolic fuzzing]] and [[PathExploration|path exploration]]. The chapter notes practical SMT limits: Z3's string solver had several bugs it works around, and a soft timeout is set to bound solver time.

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] uses [[Z3Prover|Z3]] as the engine of *pure* [[SymbolicExecution|symbolic execution]]. It builds [[SymbolicVariable|symbolic variables]] from type annotations via the `SYM_VARS` map (`int → z3.Int`, `float → z3.Real`, `str → z3.String`), assembles each CFG path's [[PathConstraint|path condition]] as a Z3 conjunction, and solves it with `z3.solve()` / `z3.Solver()` (using `push`/`pop` checkpoints and `z3.Not(seen)` to enumerate distinct solutions). The solver does double duty: it *proves paths infeasible* by returning *unsat* (e.g. `check_triangle`'s `a==b ∧ a==c ∧ b≠c`) and it *simplifies* merged function summaries via `z3.simplify()`. The chapter notes z3py does **not** expose SMT-LIB's `define-fun` macro facility, so function summaries are namespaced with the `prefix_vars()` AST hack instead. Solutions come back as Z3 values (`as_long()`, numerator/denominator) needing conversion to Python numbers.

## Connections
- [[ISLa]] / [[InputSpecificationLanguage]] / [[ConstraintBasedFuzzing]] — reduce input constraints to SMT and solve them.
- [[Z3Prover]] — the concrete Z3 SMT solver/theorem prover (Microsoft Research) used by Ch 17/20/21.
- [[ConcolicExecution]] / [[SymbolicExecution]] / [[PathConstraint]] — collect path conditions and solve them with an SMT solver.
- [[SemanticConstraint]] — the properties expressed as SMT formulas.
- [[microsoftresearch]] — origin of the Z3 SMT solver.
- [[ConstraintStore]] / [[ConstraintPropagationPrinciple]] — related constraint-solving machinery.
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] / [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — symbolic/concolic fuzzing that solve path conditions with an SMT solver.
- [[fuzzingbook-17-fuzzing-with-constraints]] — the chapter that introduces SMT solving for input generation.

## Sources
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints."
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing" (Z3 as the engine for solving/negating path conditions in concolic execution).
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (Z3 as the engine for pure symbolic execution: solving CFG path conditions, proving infeasibility, simplifying function summaries).
