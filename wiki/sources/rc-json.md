---
title: "JSON (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, serialization, data-interchange, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/JSON
---

## Summary
This task asks the programmer to round-trip JSON data: parse (deserialize) a JSON string into a native data structure, then build a fresh data structure and serialize it back into a valid JSON string. The key insight is that JSON maps cleanly onto two ubiquitous container types — ordered arrays and key/value objects — so most languages handle it with a standard library or a single popular package rather than hand-rolled parsing.

## Task Requirements
- Load a JSON string into a native data structure (deserialize/parse).
- Create a new data structure and serialize it into JSON.
- Use the language's appropriate object/map and array/list types.
- Ensure the produced JSON is valid (per a validator such as jsonformatter.org).

## Language Coverage
103 languages implement this task, reflecting JSON's status as a near-universal data-interchange format with first-class or library support almost everywhere. Representative implementations include Python, JavaScript, Java, C#, Go, Rust, Ruby, Haskell, Clojure, jq, and Raku.

## Connections
- [[JSON]] — the data-interchange format being parsed and produced
- [[Serialization]] — converting in-memory structures to a portable string form
- [[Parsing]] — reading the textual format back into structured data
- [[DataInterchange]] — the broader problem class JSON addresses
- [[AssociativeArray]] — JSON objects map to key/value containers in each language

## Contradictions
- None — reference task page.
