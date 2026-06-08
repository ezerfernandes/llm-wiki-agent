---
title: "Search a list of records (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, list-processing, higher-order-functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Search_a_list_of_records
---

## Summary
This task asks the programmer to find the first element in a list of compound records (objects/structs) that satisfies an arbitrary search condition, rather than a simple equality test against scalars. The key insight is to write a generic, reusable search routine — ideally one that accepts a predicate function (a closure returning a boolean) applied to each element in order.

## Task Requirements
- Build a native ordered collection of 10 associative records, each mapping `name` (string) to `population` (number), holding Africa's 10 largest metropolitan areas — without parsing JSON.
- Write a generic `find_index`-style function: given a list and a predicate, return the first matching element/index.
- Run three test cases: find the zero-based index where name is "Dar Es Salaam" (expect 6); find the name of the first city with population < 5 million (expect Khartoum-Omdurman); find the population of the first city whose name starts with "A" (expect 4.58).
- If higher-order programming is unavailable or unidiomatic, explain why and show the natural alternative.

## Language Coverage
66 languages implement this task, spanning functional, imperative, scripting, and query-oriented styles. Representative entries include Haskell, OCaml, Scheme, Common Lisp, Python, Ruby, Rust, Go, Java, JavaScript, jq, and SQL/DuckDB.

## Connections
- [[HigherOrderFunctions]] — the predicate-based `find_index` is the idiomatic generic solution
- [[Predicate]] — a boolean-returning function defining the match condition
- [[Closure]] — predicates are commonly expressed as lambdas/closures capturing context
- [[LinearSearch]] — first-match scanning over an ordered collection
- [[AssociativeArray]] — each record is a key-to-value map

## Contradictions
- None — reference task page.
