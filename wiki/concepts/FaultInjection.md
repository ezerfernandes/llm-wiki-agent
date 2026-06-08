---
title: "Fault Injection"
type: concept
tags: [testing, fault-injection, mutation-testing, reliability, software-engineering]
sources: [fuzzingbook-08-mutation-analysis]
last_updated: 2026-06-06
---

# Fault Injection

**Fault injection** is the practice of deliberately introducing faults into a program (or its environment) to measure how well a test suite — or a system's fault tolerance — detects or withstands them. In the test-quality context it is the *manual* precursor to [[MutationAnalysis|mutation analysis]]: a developer hand-writes a buggy variant of the program and checks whether the tests catch it. The frequency with which injected faults are detected estimates the suite's real bug-finding likelihood.

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] introduces fault injection as the intuition behind mutation analysis, then explains why it is insufficient on its own. Its example `triangle_m1()` returns `None` where `triangle()` would return `'Isosceles'`; the chapter shows the `weak_oracle()` *fails to detect* this injected fault while the `strong_oracle()` catches it — evidence the strong suite is better. But hand-curated faults are **manual, expensive, biased** by the developer's preconceptions, and **non-exhaustive** (likely to miss whole classes of bugs). [[MutationAnalysis|Mutation analysis]] automates and de-biases fault injection by mechanically enumerating *all* small valid program variants ([[Mutant|mutants]]) via [[MutationOperator|mutation operators]] over the [[AbstractSyntaxTree|AST]], replacing a curated fault list with a systematic one.

## Connections
- [[MutationAnalysis]] — the automated, systematic generalization of fault injection.
- [[Mutant]] — a mechanically generated injected fault.
- [[TestAdequacy]] — fault detection rate is an adequacy signal.
- [[TestOracle]] / [[Assertion]] — determine whether an injected fault is caught.

## Sources
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
