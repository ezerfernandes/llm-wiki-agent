---
title: "The Fuzzing Book Ch 9 — Fuzzing with Grammars"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, grammar, context-free-grammar, ebnf, bnf, formal-languages]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-09-grammars.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Fuzzing with Grammars

## Summary
Chapter 9 opens **Part III — Syntactic Fuzzing** and is the foundational grammar chapter that Chapters 10–18 build on. Whereas [[fuzzingbook-03-fuzzer|Ch 3]]'s random fuzzer and [[fuzzingbook-05-mutation-fuzzer|Ch 5]]'s mutation fuzzer produce mostly *invalid* inputs that bounce off a parser, this chapter shows how to feed a program *syntactically valid* inputs by supplying a [[ContextFreeGrammar|context-free grammar]] that specifies the program's input *language*. It defines the book's reusable [[Grammar|`Grammar`]] data structure (a Python `dict` mapping [[Nonterminal|nonterminal]] symbols in `<angle brackets>` to lists of alternative expansions), introduces the running `EXPR_GRAMMAR`, `CGI_GRAMMAR`, and `URL_GRAMMAR` examples, and implements `simple_grammar_fuzzer()` — a naive string-rewriting expander capped by `max_nonterminals`. It also builds a *grammar toolbox* (`srange()`/`crange()` character classes, `extend_grammar()`, an [[EBNF]]→[[BNF]] converter `convert_ebnf_grammar()`, the `opts()` annotation mechanism, and the `is_valid_grammar()` checker). The chapter is explicit that its naive fuzzer is inefficient and can grow without bound, deferring an efficient, growth-bounded producer to [[fuzzingbook-10-grammar-fuzzer|Ch 10]].

## Key Concepts
- **[[ContextFreeGrammar|Context-free grammar (CFG)]]** — a [[GrammarBasedFuzzing|grammar formalism]] sitting between regular expressions ([[FiniteStateMachine|finite-state machines]]) and Turing machines on the language spectrum. A grammar is a *start symbol* plus a set of *expansion rules* of the form `<A> ::= <B>`; "context-free" means the left-hand side of every rule is exactly one symbol. Rules may be *recursive* (e.g. `<integer> ::= <digit> | <digit><integer>`), which is what lets grammars express nested/arbitrarily-deep inputs like arithmetic expressions.
- **[[Grammar|The `Grammar` data structure]]** — the chapter's central reusable type: `Grammar = Dict[str, List[Expansion]]`, where each key is a [[Nonterminal|nonterminal]] string and each value is a list of [[ProductionRule|expansion alternatives]]. An `Expansion` is either a string or a `(string, opts)` pair (`Expansion = Union[str, Tuple[str, Option]]`) to carry annotations. `START_SYMBOL = "<start>"` is the canonical entry point. The running examples are `EXPR_GRAMMAR` (arithmetic expressions), `CGI_GRAMMAR` (CGI-encoded strings, for `cgi_decode()` from [[fuzzingbook-04-coverage|Ch 4]]), `URL_GRAMMAR`, `TITLE_GRAMMAR`, and `US_PHONE_GRAMMAR`.
- **[[Nonterminal|Nonterminals]] vs [[Terminal|terminals]]** — nonterminals are symbols enclosed in `<...>` (matched by `RE_NONTERMINAL = r'(<[^<> ]*>)'`) that get further expanded; terminals are the literal characters that survive into the final output. Helpers: `nonterminals(expansion)` extracts the nonterminals in an expansion, and `is_nonterminal(s)` tests a symbol.
- **`simple_grammar_fuzzer()`** — the chapter's naive *producer*: start from the start symbol, repeatedly pick a random nonterminal in the current string and replace it (via `str.replace(..., 1)`) with a random expansion alternative, stopping when no nonterminals remain. A `max_nonterminals` limit avoids unbounded growth and `max_expansion_trials` bounds retries (raising `ExpansionError` on failure).
- **[[EBNF]] extensions and `convert_ebnf_grammar()`** — *Extended BNF* adds the operators `?` (0–1), `+` (1+), `*` (0+), and parenthesized groups `(...)` as shortcuts. `convert_ebnf_grammar()` mechanically desugars EBNF into plain [[BNF]] in two passes — `convert_ebnf_parentheses()` (rule 1: a parenthesized group becomes a fresh symbol via `new_symbol()`) then `convert_ebnf_operators()` (rules 2–4: `?`/`+`/`*` become fresh recursive symbols with an `<empty>`/epsilon alternative as needed). `EXPR_EBNF_GRAMMAR` is the worked example.
- **Grammar toolbox** — `srange(chars)` and `crange(start, end)` build character-class expansion lists programmatically (e.g. `srange(string.ascii_letters)`); `extend_grammar(g, ext)` deep-copies a grammar and `dict.update()`s it (grammar extension as a kind of subclassing); `trim_grammar()` removes unused/unreachable nonterminals.
- **Annotation mechanism (`opts()`)** — expansions can be `(string, opts(...))` pairs carrying per-expansion attributes (e.g. `min_depth`, `max_depth`), accessed via `exp_string()`, `exp_opts()`, `exp_opt()`, `set_opts()`. This is the hook later chapters use to attach [[fuzzingbook-13-probabilistic-grammar-fuzzer|probabilities (Ch 13)]] and [[fuzzingbook-14-generator-grammar-fuzzer|generator constraints (Ch 14)]].
- **`is_valid_grammar()`** — a consistency checker that verifies every used nonterminal is defined (and vice versa) and that all symbols are reachable from the start symbol, using `def_used_nonterminals()` and `reachable_nonterminals()`/`unreachable_nonterminals()`.
- **Grammars as mutation seeds** — grammar-produced (always syntactically valid) inputs can be fed as seeds into the [[MutationBasedFuzzing|mutation fuzzer]] (`MutationFuzzer`) from [[fuzzingbook-05-mutation-fuzzer|Ch 5]] to also explore the *boundaries* between valid and invalid inputs, where parser bugs hide.

## Key Claims
- Specifying inputs via a grammar enables "very systematic and efficient test generation, in particular for complex input formats," and grammars are the base for configuration, API, and GUI fuzzing later in the book.
- A program's set of valid inputs is its *language*; grammars occupy the expressive middle ground between regular expressions (too weak for nested structure) and Turing-complete generators (too unautomatable, requiring a bespoke program per target).
- "Context-free" is precisely the property that each rule's left-hand side is a single symbol (`<A> ::= ...`).
- `simple_grammar_fuzzer()` is deliberately simple and has three drawbacks (the quiz answer is "all of the above"): many string search/replace operations, it may fail to produce a string (`ExpansionError`), and it often picks a symbol to expand that no longer occurs in the string.
- Because it expands to the maximum nonterminal count first and then refuses any expansion that would (transiently) raise the count, `simple_grammar_fuzzer()` can fail on grammars like the JSON or `expr_grammar` examples and can even loop into infinite expansion — issues fixed by the [[DerivationTree|derivation-tree]]-based `GrammarFuzzer` of [[fuzzingbook-10-grammar-fuzzer|Ch 10]].
- Any basic regular expression can be converted into a grammar using the EBNF-desugaring rules plus `crange()` character classes.
- Grammars produce *always* syntactically valid inputs but cannot easily express *semantic* constraints (e.g. "port between 1024 and 2048") — motivating constraint-based fuzzing in [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]].
- Grammar-based testing has a long pedigree: the first formalization of generative grammars is attributed to Pāṇini (~350 BC), the modern hierarchy to Chomsky (1956), and grammar-based input generation to Burkhardt/Hanford/Purdom; production tools include CSmith, LangFuzz, Grammarinator, and Domato, which have collectively found thousands of compiler and browser bugs.

## Key Quotes
> "Specifying inputs via a _grammar_ allows for very systematic and efficient test generation, in particular for complex input formats. Grammars also serve as the base for configuration fuzzing, API fuzzing, GUI fuzzing, and many more." — chapter introduction.

> "Note that we assume that on the left-hand side of a rule (i.e., the key in the mapping) is always a single symbol. This is the property that gives our grammars the characterization of _context-free_." — on the Python `Grammar` representation.

> "The seminal work by Chomsky introduced the central models of regular languages, context-free grammars, context-sensitive grammars, and universal grammars as they are used (and taught) in computer science as a means to specify input and programming languages ever since." — Background.

## Connections
- [[ContextFreeGrammar]] — the formalism this chapter adopts; the central idea.
- [[Grammar]] — the concrete Python data structure (`dict` of nonterminal → expansion list) the chapter mints and the rest of Part III reuses.
- [[Nonterminal]] / [[Terminal]] — the two symbol kinds; `<angle-bracket>` symbols vs literal characters.
- [[ProductionRule]] — the `<A> ::= <B> | <C>` expansion rules a grammar is built from.
- [[GrammarBasedFuzzing]] — the technique family this chapter founds: produce inputs by expanding a grammar.
- [[EBNF]] / [[BNF]] — the notation; the chapter desugars EBNF (`?`/`+`/`*`/`(...)`) into BNF via `convert_ebnf_grammar()`.
- [[Fuzzing]] / [[Testing]] — the broader subject and discipline; grammar fuzzing is the structured-input branch.
- [[FiniteStateMachine]] — regular expressions/automata, the weaker end of the language spectrum the chapter contrasts grammars against.
- [[MutationBasedFuzzing]] — grammar outputs are used as seeds for the Ch 5 `MutationFuzzer`.
- [[AndreasZeller]] — lead author; co-author Christian Holler is behind the LangFuzz tool cited in the Background.
- [[CSmith]] — grammar-based C-compiler fuzzer cited as a flagship application.
- [[fuzzingbook-10-grammar-fuzzer|Ch 10]] — the immediate sequel: an efficient, growth-bounded `GrammarFuzzer` using derivation trees, fixing this chapter's naive producer.
- [[fuzzingbook-03-fuzzer|Ch 3]] — the random-fuzzer baseline whose invalid-input weakness grammar fuzzing addresses.
- [[fuzzingbook-04-coverage|Ch 4]] — source of the `cgi_decode()` example behind `CGI_GRAMMAR`.
- [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] / [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] / [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] / [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] / [[fuzzingbook-18-grammar-miner|Ch 18]] — downstream chapters that extend this grammar foundation with coverage, probabilities, generators, constraints, and mining.

## Contradictions
- None identified.
