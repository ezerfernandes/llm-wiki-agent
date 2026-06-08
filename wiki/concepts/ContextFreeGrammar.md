---
title: "Context-Free Grammar"
type: concept
tags: [grammar, context-free-grammar, formal-languages, fuzzing, parsing, testing]
sources: [fuzzingbook-09-grammars, fuzzingbook-12-parser, fuzzingbook-14-generator-grammar-fuzzer, fuzzingbook-17-fuzzing-with-constraints, fuzzingbook-18-grammar-miner]
last_updated: 2026-06-06
---

# Context-Free Grammar

A **context-free grammar (CFG)** is a formalism for specifying a *language* — the set of strings that are syntactically valid for some program or format. A CFG consists of a *start symbol* and a set of *expansion rules* (or [[ProductionRule|production rules]]) of the form `<A> ::= <B>`, meaning the [[Nonterminal|nonterminal]] on the left may be replaced by the string on the right; the `|` operator separates alternative expansions. The defining property is that the **left-hand side of every rule is exactly one symbol** — the rule applies regardless of surrounding "context," hence *context-free*. Rules may be **recursive** (e.g. `<integer> ::= <digit> | <digit><integer>`), which is what lets a CFG describe nested and arbitrarily deep inputs such as arithmetic expressions.

On the language spectrum, CFGs sit between [[FiniteStateMachine|regular expressions/finite-state automata]] (too weak to capture nesting and balanced structure) and Turing-complete generators (maximally expressive but requiring a bespoke program per target). This middle ground makes CFGs "among the most popular (and best understood) formalisms to formally specify input languages," and the formalism of choice for nested/recursive structure.

## From The Fuzzing Book — Fuzzing with Grammars
[[fuzzingbook-09-grammars|Ch 9]] adopts CFGs as the basis for [[GrammarBasedFuzzing|grammar-based fuzzing]] and encodes them in the [[Grammar|`Grammar`]] Python data structure (a `dict` of nonterminal → expansion list). It explains *rules and expansions*, *alternatives*, and *recursion* via worked grammars for digits, integers, and full arithmetic expressions (`EXPR_GRAMMAR`), and notes that the single-symbol-LHS restriction is precisely what makes the grammars context-free. The chapter's `Background` credits the modern grammar hierarchy (regular, context-free, context-sensitive, universal) to Noam Chomsky (1956), with grammars produced in the [[BNF|Backus–Naur form]] (and its [[EBNF|extended]] form). CFGs are the foundation the entire [[fuzzingbook-10-grammar-fuzzer|syntactic-fuzzing]] part of the book rests on.

## From The Fuzzing Book — Parsing Inputs
[[fuzzingbook-12-parser|Ch 12]] uses CFGs in *reverse* — parsing a given string back into the [[DerivationTree|derivation tree]] the CFG would have produced. It introduces a *canonical* CFG representation (each symbol an explicit token, `Dict[str, List[List[str]]]`) for parsing, and the [[EarleyParser|`EarleyParser`]] that handles **any** CFG, including left-/right-recursive and [[Ambiguity|ambiguous]] ones (returning a [[ParseForest|parse forest]]). It contrasts CFGs with [[ParsingExpressionGrammar|Parsing Expression Grammars]] (which use *ordered* rather than unordered choice), and its `Background` surveys CFG parser classes — `LL`/`LR`, `LL(k)`/`LR(k)` (linear-time), plus GLL, GLR, CYK, and ANTLR's `ALL(*)`. It notes worst-case arbitrary-CFG parsing is `O(n^3)` (reducible to boolean matrix multiplication) and that some CFLs are inherently ambiguous (no `LR(1)` grammar).

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] turns the CFG's defining *limitation* into its central motivation: a context-free grammar **cannot express [[SemanticConstraint|semantic constraints]]** that relate parts of the input to each other or to computed values — a checksum (the [[LuhnAlgorithm|Luhn]] check digit is an arithmetic function of the other digits), a matched XML closing tag, or a define-before-use dependency. The chapter notes one *could* in principle use a context-*sensitive* grammar (and that a *reversed* closing tag `</gnorts>` would actually be context-free), but instead supplies the missing power imperatively by attaching Python functions to expansions ([[GeneratorGrammar|generator grammars]]). This positions the CFG as the *syntactic* backbone whose *semantic* gaps are filled by code.

## From The Fuzzing Book — Fuzzing with Constraints
[[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] keeps the CFG as the *syntactic* layer but supplies the missing *semantic* power **declaratively**: [[ISLa]] pairs a CFG with constraints that an [[SMTSolver|SMT solver]] satisfies, so the generated inputs are both syntactically and semantically valid. The chapter motivates this against two alternatives — adding more grammar rules (works for finite cases, e.g. a fixed HTML tag set, but cannot match an *infinite* set of XML tags) and **unrestricted grammars** (multiple symbols on the left-hand side make them Turing-universal, but they have no tooling and inherit the halting problem). ISLa's element-access operators (`<a>.<b>` immediate, `<a>..<b>` any descendant, `<a>[n]` nth child) navigate the CFG's [[DerivationTree|derivation tree]], confirming that the CFG remains the structural backbone the constraints reason over.

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] *recovers* a CFG rather than assuming one: program-guided [[GrammarInference|grammar inference]] observes how a program decomposes its input and abstracts the result into a context-free [[Grammar|grammar]] (the chapter says the technique can "produce the **Context Free Grammar** of the input"). The recovered CFG is necessarily an *approximation* — the substring/scope heuristics, and the inability to capture context-sensitive relationships, mean it describes the input's syntax but not all semantic constraints (the same gap Ch 14/17 fill). It is nonetheless a real CFG that the book's standard CFG tooling (parsers, grammar fuzzers) can consume.

## Connections
- [[GrammarInference]] / [[GrammarMiner]] — Ch 18 recovers an (approximate) CFG from a program + samples.
- [[ISLa]] / [[InputSpecificationLanguage]] / [[SMTSolver]] — Ch 17's declarative constraints layered on top of a CFG.
- [[Grammar]] — the Python data structure that encodes a CFG in the book.
- [[SemanticConstraint]] / [[GeneratorGrammar]] — the validity conditions a CFG can't express, and the function-annotation mechanism that supplies them.
- [[Parser]] / [[EarleyParser]] — parse strings *against* a CFG (the inverse of production).
- [[ParsingExpressionGrammar]] — PEGs resemble CFGs but use ordered choice and can denote a different language.
- [[Ambiguity]] / [[ParseForest]] — ambiguous CFGs admit multiple parse trees.
- [[ProductionRule]] / [[Nonterminal]] / [[Terminal]] — the parts a CFG is built from.
- [[BNF]] / [[EBNF]] — the textual notations for writing CFG rules.
- [[FiniteStateMachine]] — regular languages, the weaker formalism CFGs subsume.
- [[GrammarBasedFuzzing]] — the testing technique built on CFGs.
- [[fuzzingbook-09-grammars]] — the chapter that introduces CFGs for fuzzing.
- [[fuzzingbook-12-parser|Ch 12]] — parsing inputs *against* a CFG (the inverse of production).

## Sources
- [[fuzzingbook-09-grammars]] — *The Fuzzing Book* Ch 9, "Fuzzing with Grammars."
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs" (parsing strings against a CFG).
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators" (the CFG limitation that motivates attaching functions).
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints" (declarative ISLa constraints layered on a CFG to supply semantic validity).
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars" (recovering an approximate CFG from a program).
