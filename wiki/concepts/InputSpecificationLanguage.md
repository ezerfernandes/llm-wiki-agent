---
title: "Input Specification Language (ISLa)"
type: concept
tags: [fuzzing, constraints, grammar, smt, declarative, semantic-fuzzing, testing, isla, dsl]
sources: [fuzzingbook-17-fuzzing-with-constraints]
last_updated: 2026-06-06
---

# Input Specification Language

The **Input Specification Language (ISLa)** is a **declarative constraint language** layered on top of a [[ContextFreeGrammar|context-free grammar]] for specifying the [[SemanticConstraint|semantic properties]] of valid inputs — the properties a grammar alone cannot express. An ISLa specification is a grammar *plus* a string-valued **constraint** combining SMT-LIB functions/predicates, element references into the [[DerivationTree|derivation tree]], and quantifiers over tree nodes. It is the language half of the [[ISLa]] framework (the solver/checker is the engine half). ISLa is the *declarative* counterpart to the *imperative* [[GeneratorGrammar|generator-grammar]] callbacks of [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]].

## Language surface (from Ch 17)
- **SMT-LIB functions** drawn from the SMT-LIB theories: `str.len(<x>)` (length), `str.to.int(<x>)` (string→int), `str.to_code(<c>)` (char→ordinal), with operators `>`, `<`, `=`, `mod`, `+`. Equality uses a *single* `=` (there is no assignment to confuse it with). Two syntaxes are accepted: programmer-friendly **infix** (`str.to.int(<pagesize>) > 1024`) and full LISP-like **SMT-LIB prefix** (`(> (str.to.int <pagesize>) 1024)`); boolean operators like `and` stay in ISLa infix even in prefix mode (more efficient than passing them to the solver).
- **Element access (XPath-like):** `<a>.<b>` = *immediate* subpart, `<a>..<b>` = *any* (transitive) subpart, `<a>[n]` = the *n*-th immediate child of type `<a>` (**1-indexed**, as in XPath abbreviated syntax).
- **Quantifiers:** `forall TYPE VAR in CONTEXT: (CONSTRAINT)` and `exists TYPE VAR in CONTEXT: (CONSTRAINT)`. Variable names are optional (you may reuse the nonterminal). By default every nonterminal used directly is **universally quantified within `<start>`**, so a bare `str.to.int(<int>) > 1000` is an implicit `forall`.
- **Match expressions:** `forall <int>="<leaddigit><digits>" in <start>: ...` restricts a quantifier to a *specific expansion alternative*; the brace form `{<ID> VAR}` binds `VAR` to the value matched by `<ID>` for use in the body.
- **Predicates:** *structural* — `before`, `after`, `consecutive`, `direct_child`, `inside`, `different_position`, `same_position`, `nth`, `level`; *semantic* — `count(in_tree, NEEDLE, NUM)`. These can be extended via the solver's `structural_predicates`/`semantic_predicates` parameters.

## From The Fuzzing Book — Fuzzing with Constraints
[[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] mints ISLa as a *dedicated language* preferable to either context-sensitive/unrestricted grammars (Turing-universal but tooling-less and halting-prone) or imperative generator code. It demonstrates the language incrementally — numeric constraints (`mod`, ranges, equality between elements), dot/double-dot navigation, quantifier defaults, match expressions, the `before()` def/use ordering, and `count()` for input size — ending with matched-tag XML and a programming-language define-before-use specification. Because the language is *declarative*, the same specification serves both [[ConstraintBasedFuzzing|generation]] and checking.

## Connections
- [[ISLa]] — the framework that hosts this language (solver + checker + CLI).
- [[ConstraintBasedFuzzing]] — the fuzzing technique the language enables.
- [[SMTSolver]] — the engine that discharges ISLa constraints; supplies the SMT-LIB functions.
- [[SemanticConstraint]] — the validity-beyond-syntax properties ISLa expresses.
- [[ContextFreeGrammar]] / [[Grammar]] / [[DerivationTree]] — the grammar ISLa augments and the tree its operators navigate.
- [[GeneratorGrammar]] — the imperative alternative this language is contrasted with.
- [[DominicSteinhofel]] / [[AndreasZeller]] — the language's designers.
- [[fuzzingbook-17-fuzzing-with-constraints]] — the chapter that introduces ISLa.

## Sources
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints."
