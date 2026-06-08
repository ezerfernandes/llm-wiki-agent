---
title: "ISLa"
type: entity
tags: [tool, framework, fuzzing, constraints, smt, testing, security, python, isla]
sources: [fuzzingbook-17-fuzzing-with-constraints, fuzzingbook-26-python-fuzzer-testing-compilers]
last_updated: 2026-06-06
---

# ISLa

**ISLa** (the **[[InputSpecificationLanguage|Input Specification Language]]**) is a framework for **constraint-based input generation and checking** built by [[DominicSteinhofel|Dominic Steinhöfel]] and [[AndreasZeller|Andreas Zeller]] at [[CISPA]]. It pairs a standard [[ContextFreeGrammar|context-free grammar]] with **declarative semantic constraints** and automatically *solves* those constraints — via an underlying [[SMTSolver|SMT solver]] (Z3) over the SMT-LIB theories — to produce inputs that are simultaneously *syntactically* and *semantically* valid. ISLa is the centerpiece of [[fuzzingbook-17-fuzzing-with-constraints|Ch 17 of *The Fuzzing Book*]], which opens Part IV (Semantic Fuzzing).

## Components
ISLa consists of three parts:
- the **ISLa specification language** — adds [[SemanticConstraint|constraints]] to a grammar (see [[InputSpecificationLanguage]]);
- the **ISLa solver** — solves the constraints to produce satisfying inputs;
- the **ISLa checker** — checks whether a given input satisfies the constraints (much cheaper than solving, so ISLa constraints can serve as test *oracles*).

## Distribution and API
- Python package `isla-solver` (`pip install isla-solver`). Core class: `from isla.solver import ISLaSolver`.
- `ISLaSolver(grammar, constraint, ...)` — the constructor takes a [[Grammar|grammar]] and a constraint string, plus tuning parameters (`max_number_smt_instantiations`, `max_number_free_instantiations`, `structural_predicates`, `semantic_predicates`).
- Methods: `solve()` (returns a satisfying [[DerivationTree|derivation tree]]; call repeatedly for more solutions), `check(input)` (does the input satisfy the constraints?), `parse(...)`.
- The `isla` command-line tool ships with the package, with subcommands `solve`, `fuzz`, `check`, `find`, `parse`, `repair`, `mutate`, `create`, `config`. It accepts grammars in Fuzzingbook format (a Python file defining a `grammar` variable) and constraints inline (`--constraint`) or in constraint files.

## Background
ISLa is presented in the paper **"Input Invariants"** (Steinhöfel & Zeller) at **ESEC/FSE 2022** (CISPA publication 3596). Source and reference: the [ISLa project on GitHub](https://github.com/rindPHI/isla) and the [ISLa docs](https://rindphi.github.io/isla/).

## From The Fuzzing Book — Fuzzing with Constraints
[[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] introduces ISLa as the **declarative** route to [[SemanticConstraint|semantic validity]], explicitly contrasted with the **imperative** [[GeneratorGrammar|generator grammars]] of [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]]: where Ch 14 attaches Python `pre`/`post` code to expansions, ISLa declares constraints once and lets the solver produce *or* check inputs. The chapter walks `str.len`/`str.to.int`/`mod` constraints over a `CONFIG_GRAMMAR`, `<a>.<b>`/`<a>..<b>`/`<a>[n]` element access, `forall`/`exists` quantifiers (universal-in-`<start>` by default), match expressions, and the `before()`/`count()` predicates — culminating in matched-tag XML and a define-before-use programming-language constraint.

## From The Fuzzing Book — Testing Compilers (Python Fuzzer)
[[fuzzingbook-26-python-fuzzer-testing-compilers|Ch 26]] uses ISLa as the production engine for [[CompilerTesting|compiler testing]]: the [[PythonFuzzer]] class *subclasses* `ISLaSolver`, feeding it `convert_ebnf_grammar(PYTHON_AST_GRAMMAR)` to generate Python [[AbstractSyntaxTree|ASTs]]. The chapter exercises ISLa's full surface beyond `solve()`: `check()` to validate parsed code, `parse()` to obtain a [[DerivationTree|derivation tree]], and especially `mutate(input, min_mutations, max_mutations)` to re-expand random subtrees — the operator that powers Ch 26's [[EvolutionaryFuzzing|evolutionary fuzzing]]. It also shows ISLa `constraint=` strings shaping generated code (`str.len(<id>) = 10`, `count(def, "<stmt>", "3")`, `inside(...)`/`str.to.int(...)`, `<FunctionDef>..<expr_list> = "[]"`), and notes some constraints (e.g. `count`) "will not work with ISLa 2."

## Connections
- [[InputSpecificationLanguage]] — ISLa's constraint language (the syntax/semantics).
- [[PythonFuzzer]] / [[CompilerTesting]] — Ch 26's `PythonFuzzer` subclasses `ISLaSolver` to generate/mutate Python.
- [[EvolutionaryFuzzing]] — built on `ISLaSolver.mutate()` over derivation trees.
- [[ConstraintBasedFuzzing]] — the technique ISLa embodies.
- [[SMTSolver]] — the engine ISLa reduces constraints to (Z3 / SMT-LIB).
- [[SemanticConstraint]] — the validity-beyond-syntax properties ISLa specifies.
- [[GeneratorGrammar]] / [[GeneratorGrammarFuzzer]] — the imperative alternative ISLa is contrasted with.
- [[ContextFreeGrammar]] / [[Grammar]] / [[DerivationTree]] — the grammar ISLa constrains and the tree `solve()` returns.
- [[DominicSteinhofel]] / [[AndreasZeller]] / [[CISPA]] — ISLa's authors and host institution.
- [[fuzzingbook-17-fuzzing-with-constraints]] — the chapter that introduces ISLa.

## Sources
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints."
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — *The Fuzzing Book* Ch 26, "Testing Compilers" (`PythonFuzzer` subclasses `ISLaSolver`; uses `mutate()`/`parse()`/`check()` and constraints).
