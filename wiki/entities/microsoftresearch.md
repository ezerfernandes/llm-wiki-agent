---
title: "Microsoft Research"
type: entity
tags: [organization, ai-lab]
sources: [2605.02572-long-horizon-llm-training, 2605.03808-agentic-imodels, fuzzingbook-20-concolic-fuzzer, fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# Microsoft Research

Microsoft's central research arm. In the corpus, MSR co-authors two ICML 2026 papers: the long-horizon training study with Yonsei (horizon reduction → horizon generalization) and AGENTIC-IMODELS with NUS (autoresearch loop discovering models interpretable to coding agents).

## From The Fuzzing Book — Concolic Fuzzing
Microsoft Research is the origin of the [[Z3Prover|Z3]] SMT solver / theorem prover (Leonardo de Moura, Nikolaj Bjørner), the constraint engine used throughout *The Fuzzing Book*'s semantic-fuzzing part. [[fuzzingbook-20-concolic-fuzzer|Ch 20]] solves and negates [[PathConstraint|path conditions]] with Z3 to drive [[ConcolicExecution|concolic execution]]; Z3 also powers [[ISLa]] in [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] and the [[fuzzingbook-21-symbolic-fuzzer|symbolic fuzzing of Ch 21]].

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] uses MSR's [[Z3Prover|Z3]] as the engine of pure [[SymbolicExecution|symbolic execution]], crediting it in the Background to de Moura and Bjørner as "one of the most popular solvers." The chapter also cites Microsoft's [[SAGE]] whitebox-fuzzing tool — itself an industrial application of (concolic) symbolic execution that motivated Z3 — among the well-known symbolic-execution tools.

## Connections
- [[Z3Prover]] — the Z3 SMT solver/theorem prover developed at Microsoft Research.
- [[SAGE]] — Microsoft's whitebox-fuzzing tool built on symbolic/concolic execution, cited in Ch 21.
- [[SMTSolver]] — Z3 is its canonical implementation.
- [[2605.02572-long-horizon-llm-training]]
- [[2605.03808-agentic-imodels]]
- [[autoresearch|Autoresearch]]
