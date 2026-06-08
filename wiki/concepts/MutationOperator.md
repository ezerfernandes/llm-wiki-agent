---
title: "Mutation Operator"
type: concept
tags: [testing, mutation-testing, ast, program-transformation, software-engineering]
sources: [fuzzingbook-08-mutation-analysis]
last_updated: 2026-06-06
---

# Mutation Operator

A **mutation operator** is a rule that transforms a program into a [[Mutant|mutant]] by applying one small, syntactically valid change. Operators encode the kinds of "probable faults" a programmer might make. Classic families include **statement deletion** (replace a statement with a no-op), **arithmetic/relational operator replacement** (`+`↔`-`, `==`↔`!=`), **constant mutation**, and **branch/condition negation**. The set of operators defines the space of mutants — and hence what a [[MutationScore|mutation score]] actually measures.

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] implements operators as subclasses of an [[AbstractSyntaxTree|AST]] `Mutator` (itself an `ast.NodeTransformer`). The base `Mutator.mutable_visit()` either *counts* a candidate location or, when a target location is selected, calls `mutation_visit()` to perform the change. The chapter's primary operator is `StmtDeletionMutator`, which hooks `visit_Return`, `visit_Assign`, `visit_Assert`, `visit_Raise`, `visit_Break`, etc., and replaces each visited statement with `ast.Pass()` — yielding 5 mutants for `triangle()`. Exercise 1 adds a `BinOpMutator` that visits `BinOp` nodes and swaps `op` via a replacement map (`Add→Sub`, `Sub→Add`, `Mult→Div`, `Div→Mult`), wired into a `MuBinOpAnalyzer`. Exercise 3 proposes a *bytecode* mutator for cases where source is unavailable. A single location can legitimately produce multiple mutants (hence the count/index bookkeeping).

## Connections
- [[Mutant]] — the output of applying an operator.
- [[MutationAnalysis]] — orchestrates operators over a program.
- [[AbstractSyntaxTree]] — the structure operators rewrite (via `ast.NodeTransformer`).
- [[MutationScore]] — the operator set determines what the score reflects.
- [[Mutator]] — note the *fuzzing* `Mutator` of [[MutationBasedFuzzing|Ch 5]] mutates inputs, not program ASTs; different concept, similar name.

## Sources
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
