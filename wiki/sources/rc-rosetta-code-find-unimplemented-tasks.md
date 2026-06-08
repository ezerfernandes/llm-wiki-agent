---
title: "Rosetta Code/Find unimplemented tasks (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, web-api, set-operations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rosetta_Code/Find_unimplemented_tasks
---

## Summary
Given the name of a programming language on Rosetta Code, this task asks the programmer to find every task that is NOT yet implemented in that language. The core insight is a set difference: compute all tasks, subtract the tasks that already have an implementation in the target language. Both lists come from the MediaWiki API by querying category membership.

## Task Requirements
- Accept the name of a language on Rosetta Code as input.
- Use the MediaWiki API (the local Rosetta Code wiki API) to retrieve the relevant page lists.
- Compute the set of all tasks minus the set of tasks already implemented in the given language.
- Handle pagination/continuation: implementations must fetch more data than a single API request can return in one batch.

## Language Coverage
43 languages implement this task, a moderate breadth reflecting the need for HTTP/API access and JSON or XML parsing. Representative implementations include Python, Go, Rust, Haskell, Ruby, Perl, Raku, JavaScript, Tcl, and Julia.

## Connections
- [[MediaWikiAPI]] — the data source queried for category membership and task lists
- [[SetDifference]] — the underlying operation: all tasks minus implemented tasks
- [[HTTPRequest]] — implementations must call a remote web API
- [[Pagination]] — continuation tokens are required to fetch the full result set
- [[RESTfulQuery]] — interacting with a paginated query interface

## Contradictions
- None — reference task page.
