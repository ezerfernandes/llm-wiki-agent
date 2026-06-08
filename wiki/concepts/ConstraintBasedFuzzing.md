---
title: "Constraint-Based Fuzzing"
type: concept
tags: [fuzzing, constraints, grammar, smt, declarative, semantic-fuzzing, testing, security, isla]
sources: [fuzzingbook-17-fuzzing-with-constraints]
last_updated: 2026-06-06
---

# Constraint-Based Fuzzing

**Constraint-based fuzzing** generates test inputs by **declaring** the properties valid inputs must satisfy and letting a **solver** produce inputs that meet them — rather than writing a producer or filter in code. Concretely, it combines a [[ContextFreeGrammar|context-free grammar]] (for *syntactic* validity) with declarative [[SemanticConstraint|semantic constraints]] (for *semantic* validity such as lengths, checksums, value ranges, matched tags, and define-before-use dependencies), then reduces the constraints to a solving problem — in [[ISLa]]'s case, an [[SMTSolver|SMT]] problem over the SMT-LIB theories (Z3). It is the opening technique of **Part IV (Semantic Fuzzing)** in *The Fuzzing Book*.

## Declarative vs. imperative semantic fuzzing
Constraint-based fuzzing is the **declarative** sibling of the **imperative** [[GeneratorGrammar|generator-grammar]] approach of [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]], which attaches Python `pre`/`post` callbacks to grammar expansions. The chapter argues the declarative form is superior on three axes:
- **Multi-constraint composition** — satisfying several constraints at once is hard to hand-code (you end up writing a bespoke generation *strategy*); a solver composes them with `and` automatically.
- **Portability** — a grammar + constraints is language-independent and adaptable to any constraint-aware fuzzer, whereas attached Python code ties you to Python forever.
- **Bidirectionality** — code can *produce* or *check* inputs but not both; a constraint can do both, and *checking* is far cheaper than *solving* (no search), so constraints double as test *oracles*.

## From The Fuzzing Book — Fuzzing with Constraints
[[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] realizes constraint-based fuzzing with [[ISLa]] and its `ISLaSolver`. The running examples scale from a single numeric constraint (`str.to.int(<pagesize>) >= 100000`), through ranges (`>= 100 and <= 200`), modular arithmetic (`mod 7 = 0`), and cross-element relations (`<pagesize> = <bufsize>`), to genuinely context-sensitive properties — matched infinite-tag XML and a programming-language define-before-use rule using the `before()` predicate. Tuning parameters (`max_number_smt_instantiations`, `max_number_free_instantiations`) trade input diversity against throughput. The chapter positions this as the foundation for the rest of Part IV, where [[fuzzingbook-20-concolic-fuzzer|concolic]] and [[fuzzingbook-21-symbolic-fuzzer|symbolic]] fuzzing also lean on constraint solvers.

## Connections
- [[ISLa]] / [[InputSpecificationLanguage]] — the framework and language realizing this technique.
- [[SMTSolver]] — the engine that solves the declared constraints.
- [[SemanticConstraint]] — the validity-beyond-syntax properties being declared.
- [[GeneratorGrammar]] / [[GeneratorGrammarFuzzer]] — the imperative (code-based) alternative.
- [[GrammarBasedFuzzing]] / [[ContextFreeGrammar]] — supplies the syntactic backbone constraints sit on top of.
- [[DerivationTree]] — solutions are returned as derivation trees.
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] / [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — later Part IV chapters that also solve constraints (to reach code, not shape inputs).
- [[fuzzingbook-17-fuzzing-with-constraints]] — the chapter that introduces this technique.

## Sources
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints."
