---
title: "The Fuzzing Book Ch 17 — Fuzzing with Constraints"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, semantic-fuzzing, constraints, isla, smt, grammar, declarative]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-17-fuzzing-with-constraints.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Fuzzing with Constraints

## Summary
This chapter opens **Part IV (Semantic Fuzzing)** of *The Fuzzing Book* by introducing **[[ISLa]]** (the **[[InputSpecificationLanguage|Input Specification Language]]**), a framework by [[DominicSteinhofel|Dominic Steinhöfel]] and [[AndreasZeller|Andreas Zeller]] that layers **declarative constraints** on top of a [[ContextFreeGrammar|context-free grammar]] to express the **[[SemanticConstraint|semantic input properties]]** a CFG cannot — "$X$ is the length of $Y$", "$X$ is an identifier previously declared", or "$X$ should be longer than 4,096 bytes." The core component is the `ISLaSolver`, which takes a [[Grammar|grammar]] plus a constraint string and `solve()`s it by reducing constraints to an [[SMTSolver|SMT problem]] (over the SMT-LIB theories, backed by Z3) to produce inputs that are both *syntactically* and *semantically* valid. This is the **declarative counterpart** to the *imperative* [[GeneratorGrammar|generator grammars]] of [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] — the same semantic properties, but specified as portable constraints rather than callback code, and usable as both a **fuzzer** *and* a **checker**. The running examples build from a `CONFIG_GRAMMAR` (page size / buffer size) through XML tag-matching to a programming-language define-before-use constraint; prerequisites are [[fuzzingbook-09-grammars|Ch 9 (grammars)]] and the related [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14 (generators)]], and it sets up [[fuzzingbook-21-symbolic-fuzzer|symbolic (Ch 21)]] and [[fuzzingbook-20-concolic-fuzzer|concolic (Ch 20)]] fuzzing, which also use constraint solvers.

## Key Concepts
- **[[ISLa]]** — the framework (`isla-solver` Python package; `isla` CLI). Three parts: the *specification language* (constraints over a grammar), the *solver* (`ISLaSolver.solve()`, produces satisfying inputs), and the *checker* (`ISLaSolver.check()`, tests whether an input satisfies the constraints). Other methods: `parse()`. CLI subcommands: `solve`, `fuzz`, `check`, `find`, `parse`, `repair`, `mutate`, `create`, `config`.
- **[[InputSpecificationLanguage]]** — the declarative constraint *language* itself: a grammar plus a string-valued constraint expression combining SMT-LIB functions, element references, and quantifiers.
- **[[ConstraintBasedFuzzing]]** — the technique: instead of writing a producer/checker in code, you *declare* what valid inputs look like and let a solver generate them. Purely declarative, language-independent, reversible (generate *and* check), and composable (multiple constraints with `and`).
- **[[SMTSolver]] / SMT-LIB** — constraints are reduced to **Satisfiability Modulo Theories** and discharged to an SMT solver (Z3). Functions like `str.len()`, `str.to.int()`, `str.to_code()`, and operators (`>`, `=`, `mod`, `+`) come straight from the SMT-LIB string/integer theories; ISLa supports both infix syntax and full LISP-like SMT-LIB prefix syntax (`(> (str.to.int <pagesize>) 1024)`).
- **[[SemanticConstraint|Semantic input properties]]** — properties that relate parts of an input to each other or to computed values; *cannot* be captured by a [[ContextFreeGrammar|CFG]]. The chapter contrasts CFGs with **unrestricted grammars** (Turing-universal but with no tooling and subject to the halting problem) to motivate a *dedicated* constraint language.
- **Element access** — XPath-like navigation of the [[DerivationTree|derivation tree]]: `<a>.<b>` = *immediate* subpart, `<a>..<b>` = *any* (transitive) subpart, `<a>[n]` = the *n*-th immediate child of that type (1-indexed, as in XPath).
- **Quantifiers** — `forall TYPE VAR in CONTEXT: (CONSTRAINT)` and `exists TYPE VAR in CONTEXT: (CONSTRAINT)` over derivation-tree nodes. By default every nonterminal used directly is **universally quantified within `<start>`**, so a bare `str.to.int(<int>) > 1000` is implicitly a `forall`.
- **Match expressions** — `forall <int>="<leaddigit><digits>" in <start>: ...` restricts a quantifier to a *specific expansion alternative*; the brace form `{<ID> VAR}` binds a named variable to a matched element for use in the constraint.
- **Predicates** — *structural* predicates over tree positions (`before(A, B)`, `after`, `inside`, `direct_child`, `nth`, `level`, `same_position`, …) and *semantic* predicates (`count(in_tree, NEEDLE, NUM)`). `before()` orders def/use; `count()` fixes the number of a nonterminal.
- **Solver configuration** — `ISLaSolver(grammar, constraint, max_number_smt_instantiations=10, max_number_free_instantiations=…, structural_predicates=…, semantic_predicates=…)`. `max_number_smt_instantiations` trades structurally-similar inputs for throughput; `max_number_free_instantiations` bounds random fills of unconstrained nonterminals; the predicate sets let you extend the language with custom predicates.

## Key Claims
- There exist input properties — lengths, checksums, value ranges, def-before-use, matched tags — that are **provably inexpressible in a context-free grammar** because the CFG's single-symbol left-hand side cannot relate one input part to another.
- ISLa's `ISLaSolver` produces inputs that satisfy a declared constraint by solving it; e.g. `str.to.int(<area>) > 900` over `US_PHONE_GRAMMAR` yields phone numbers whose area code is always > 900.
- The constraint functions (`str.len`, `str.to.int`, `str.to_code`, …) are **SMT-LIB theory functions**, not ISLa-specific; the full SMT-LIB theory catalog is available inside constraints.
- A constraint can express an **infinite-tag** XML well-formedness rule (`<xml-tree>.<open-tag>.<id> = <xml-tree>.<close-tag>.<id>`) that is impossible in a CFG with an unbounded tag set.
- A **define-before-use** rule is expressible as `forall <rhs>: exists <assgn> declaration: (before(declaration, <assgn>) and <rhs>.<var> = declaration.<lhs>.<var>)`.
- **Checking** a constraint is much cheaper than **solving** it, because checking needs no search — making ISLa constraints usable as test *oracles* on outputs, not just input generators.
- Declarative constraints are **more versatile and language-independent** than the imperative generator/filter code of [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]]: portable across fuzzers and usable for both producing and checking, where attached code is Python-bound and one-directional.

## Key Quotes
> "there are *semantic* input features that cannot be expressed in a context-free grammar, such as '$X$ is the length of $Y$'; '$X$ is an identifier previously declared'; or '$X$ should be longer than 4,096 bytes'." — the chapter's motivating gap.

> "Declaring constraints (and have a solver solve them) is much more versatile than adding generator code, and language-independent, too." — Lessons Learned, on declarative vs. imperative semantic fuzzing.

> "By default, all nonterminals in ISLa constraints are *universally* quantified ... so the above can actually be simplified to `str.to.int(<int>) > 1000` ... in all our initial constraints, we always had an implicit universal quantification." — on the default quantifier semantics.

## Connections
- [[ISLa]] — the framework this chapter introduces (entity: tool/package/CLI by [[DominicSteinhofel]] & [[AndreasZeller]]).
- [[InputSpecificationLanguage]] / [[ConstraintBasedFuzzing]] / [[SMTSolver]] — the language, the technique, and the solving substrate minted here.
- [[SemanticConstraint]] — the validity-beyond-syntax notion; this chapter is the *declarative* way to specify it.
- [[GeneratorGrammar]] / [[GeneratorGrammarFuzzer]] / [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] — the *imperative* counterpart (attached Python `pre`/`post` code); this chapter is explicitly contrasted with it.
- [[ContextFreeGrammar]] / [[Grammar]] — the syntactic backbone ISLa constrains; its expressive limit is the chapter's motivation.
- [[DerivationTree]] — what `solve()` returns and what element-access operators (`.`/`..`/`[n]`) and quantifiers navigate.
- [[EarleyParser]] — used to parse example inputs into trees for visualization (`display_tree`).
- [[GrammarBasedFuzzing]] / [[fuzzingbook-09-grammars|Ch 9]] — the prerequisite producing syntactically valid inputs; constraints make them semantically valid too.
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21 (symbolic)]] / [[fuzzingbook-20-concolic-fuzzer|Ch 20 (concolic)]] — later Part IV chapters that also use constraint solvers, but to reach code locations rather than shape inputs.
- [[fuzzingbook-18-grammar-miner|Ch 18 (grammar mining)]] — the next semantics chapter (mining grammars from inputs).
- [[DominicSteinhofel]] / [[AndreasZeller]] / [[CISPA]] — ISLa's authors and host institution.

## Contradictions
- None identified. (Note: the wiki's existing `Z3` concept page documents the 1941 *Zuse Z3 computer*, not the Z3 SMT solver referenced by ISLa; this chapter's Z3 is the SMT solver — captured under [[SMTSolver]] to avoid the name collision.)
