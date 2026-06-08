---
title: "Parsing Expression Grammar"
type: concept
tags: [parsing, grammar, peg, ordered-choice, recursive-descent, fuzzing, python]
sources: [fuzzingbook-12-parser]
last_updated: 2026-06-06
---

# Parsing Expression Grammar

A **Parsing Expression Grammar (PEG)** is a *recognition-based* formal grammar that specifies the exact sequence of steps to take to parse a string. Syntactically a PEG looks almost identical to a [[ContextFreeGrammar|context-free grammar]] — nonterminals with alternative expansions — but its alternatives mean **ordered choice**, not unordered alternation. Rather than considering *all* rules that could match (as a CFG does), a PEG tries its choices left-to-right and **commits to the first that succeeds**. This single change eliminates ambiguity by construction: a PEG always yields at most one parse. PEGs were introduced by [[BryanFord|Bryan Ford]] (2004) and model the typical practice of hand-written recursive-descent parsers, which makes them intuitive to read.

## The Fuzzing Book's treatment
[[fuzzingbook-12-parser|Ch 12]] introduces PEGs and implements them with the [[PackratParsing|`PEGParser`]] (a packrat parser). Worked illustration of ordered choice: the PEG `{'<start>': ['ab', 'abc']}` matches `ab` but **not** `abc` — having matched the first choice `ab`, it never backtracks to try `abc`, whereas a CFG would match both.

Key cautions the chapter raises:

- **PEG ≠ CFG in expressiveness.** Although a PEG *looks* like a CFG, the language it describes can differ. Only `LL(1)` grammars are guaranteed to denote the same language under both interpretations.
- **Counter-intuitive behavior.** The chapter's `PEG_SURPRISE` example `{'<A>': ['a<A>a', 'aa']}`, read as a CFG generator, produces strings with `2n` a's; but the PEG *parser* only recognizes strings of length `2^n`.
- **Recognition vs. generation mismatch.** PEGs are oriented toward *recognizing* a language, and there is no clean general translation from an arbitrary PEG to a CFG — a problem because the book's main goal is *generation*. This deficiency motivates moving on to the [[EarleyParser|Earley parser]] for arbitrary CFGs.
- **PEG extras.** Exercises cover regex-like conveniences (`T?`, `T*`, `T+`) desugared to basic rules, and lookahead **and-/not-predicates** (`&`, `!`) that match without consuming input.

The chapter's `Background` notes the exact class of languages expressible by PEGs is still unknown — no CFL is currently known to be inexpressible as a PEG, and since a PEG parses any string in `O(n)` time (see [[PackratParsing]]), PEGs are a strong practical choice for writing parsers.

## Connections
- [[PackratParsing]] — the memoized recursive-descent algorithm that parses PEGs (`PEGParser`).
- [[ContextFreeGrammar]] — the grammar class PEGs resemble but differ from; *ordered* vs *unordered* choice.
- [[EarleyParser]] — the general CFG parser the chapter turns to because PEGs can't express arbitrary CFGs.
- [[Ambiguity]] — PEGs eliminate it by ordered choice (at most one parse).
- [[Parser]] — `PEGParser` is a subclass of the book's `Parser` base.
- [[BryanFord]] — introduced PEGs and packrat parsing.
- [[fuzzingbook-12-parser]] — the chapter that introduces PEGs.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
