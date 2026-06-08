---
title: "Rosetta Code/Count examples (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, web-scraping, api-client]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rosetta_Code/Count_examples
---

## Summary
This task asks the programmer to count the number of language examples present on each Rosetta Code task page and produce a grand total across all tasks. The key insight is that each language section on a task page begins with the marker `=={{header|...}}==`, so counting these markers per page yields the example count. The data must be gathered programmatically through the MediaWiki API rather than by hand.

## Task Requirements
- For each task in the Programming Tasks category, count its programming examples (occurrences of the `=={{header|` header marker on the page).
- Output each task name followed by its example count.
- Output a single grand total of examples across all tasks.
- Retrieve the task list and page contents via the MediaWiki API.

## Language Coverage
49 languages implement this task, a moderate breadth reflecting that it requires HTTP requests and JSON/XML parsing rather than pure computation. Representative implementations include Python, Go, Rust, Haskell, Ruby, Perl, Raku, Java, C#, and Tcl.

## Connections
- [[MediaWikiAPI]] — the task is built around querying this web API
- [[HTTPRequests]] — fetching category listings and page wikitext over HTTP
- [[StringMatching]] — counting occurrences of the header marker substring
- [[WebScraping]] — programmatic extraction of structured data from a wiki
- [[JSONParsing]] — decoding the API's structured responses

## Contradictions
- None — reference task page.
