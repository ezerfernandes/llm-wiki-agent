---
title: "Jay Earley"
type: entity
tags: [person, parsing, computer-science, computational-linguistics]
sources: [fuzzingbook-12-parser]
last_updated: 2026-06-06
---

# Jay Earley

**Jay Earley** is the computer scientist who invented the **[[EarleyParser|Earley parser]]** (1970), a general algorithm — originally devised for computational linguistics — that can parse *any* [[ContextFreeGrammar|context-free grammar]], including ambiguous and recursive ones, using [[ChartParsing|chart parsing]] / [[DynamicProgramming|dynamic programming]].

## From The Fuzzing Book — Parsing Inputs
[[fuzzingbook-12-parser|Ch 12]] adopts Earley's algorithm as its general-purpose parser for arbitrary CFGs, implementing it as the `EarleyParser` with `predict`/`scan`/`complete` operations over a column-indexed chart. The chapter cites Earley's complexity bounds (`O(n^3)` arbitrary, `O(n^2)` unambiguous) and the later refinements that build on his work — the Aycock et al. epsilon fix and Joop Leo's `O(n)` right-recursion optimization.

## Connections
- [[EarleyParser]] — the parsing algorithm he invented.
- [[ChartParsing]] / [[DynamicProgramming]] — the techniques underlying it.
- [[ContextFreeGrammar]] — the grammar class his parser fully handles.
- [[fuzzingbook-12-parser]] — the chapter that implements his algorithm.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
