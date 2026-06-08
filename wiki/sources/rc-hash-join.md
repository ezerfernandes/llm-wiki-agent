---
title: "Hash join (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, algorithms, data-structures, databases]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hash_join
---

## Summary
The task asks the programmer to implement the hash join algorithm, a scalable way to perform an inner join between two tables on matching column values. The key insight is that instead of an O(n*m) nested-loop comparison, you build a hash-based multimap from one table (ideally the smaller one) keyed on its join column, then scan the other table doing constant-time lookups, reducing the cost toward O(n+m).

## Task Requirements
- Implement the hash join algorithm and pass the given test case.
- Represent the two input tables using data structures natural to the language.
- Phase 1 (hash): build a multimap from one table, mapping each join-column value to all rows holding it (use the smaller table to minimize memory/time).
- Phase 2 (join): scan the other table and find matches via hash lookup in the multimap.
- For each matched pair, emit the concatenation of the two rows into the output table.
- Output row order is not significant.

## Language Coverage
66 languages implement this task, showing broad coverage across functional, imperative, scripting, and database-oriented languages. Representative implementations include Python, Java, C++, C#, Go, Rust, Haskell, Clojure, Perl, Ruby, and SQL/DuckDB.

## Connections
- [[HashTable]] — the multimap backing the hash phase relies on hash-based lookup
- [[InnerJoin]] — hash join is one algorithm for computing a relational inner join
- [[Multimap]] — the join-column-to-rows mapping is a multimap
- [[AlgorithmComplexity]] — improves on nested-loop join's quadratic cost
- [[RelationalAlgebra]] — joins are a core relational-algebra operation

## Contradictions
- None — reference task page.
