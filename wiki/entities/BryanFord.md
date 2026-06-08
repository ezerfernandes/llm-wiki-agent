---
title: "Bryan Ford"
type: entity
tags: [person, parsing, computer-science, peg]
sources: [fuzzingbook-12-parser]
last_updated: 2026-06-06
---

# Bryan Ford

**Bryan Ford** is the computer scientist who introduced **[[ParsingExpressionGrammar|Parsing Expression Grammars]]** (PEGs) and **[[PackratParsing|packrat parsing]]** (2004). PEGs reformulate grammar alternatives as *ordered choice*, eliminating [[Ambiguity|ambiguity]] by construction, and packrat parsing parses them in linear time via [[Memoization|memoization]].

## From The Fuzzing Book — Parsing Inputs
[[fuzzingbook-12-parser|Ch 12]] presents Ford's PEG formalism (citing his 2004 work) and implements packrat parsing as the `PEGParser`, using `functools.lru_cache` for the memoization that gives the technique its name. The chapter highlights both PEGs' practical appeal (intuitive, top-down, `O(n)`) and their subtleties (a PEG can denote a different language than the same rules read as a CFG).

## Connections
- [[ParsingExpressionGrammar]] — the grammar formalism he introduced.
- [[PackratParsing]] — the linear-time PEG parsing technique he introduced.
- [[Memoization]] — the caching that makes packrat parsing linear-time.
- [[fuzzingbook-12-parser]] — the chapter that presents his work.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
