---
title: "Rosetta Code/Rank languages by popularity (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, web-scraping, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rosetta_Code/Rank_languages_by_popularity
---

## Summary
This task asks the programmer to rank programming languages by their popularity on Rosetta Code itself, measured by the number of task entries (category members) per language. The data is obtained either by scraping the Special:Categories page or by querying the MediaWiki API, then sorted in descending order by member count. The key insight is combining live data retrieval (HTTP fetch plus parsing) with a numeric sort and formatted ranked output.

## Task Requirements
- Retrieve the membership counts of Rosetta Code programming-language categories.
- Use web scraping (the Special:Categories page) and/or the MediaWiki API to get the data.
- Sort languages in descending order by number of category members.
- Print a ranked list showing rank, entry count, and language name.
- Filtering out non-language or spurious results is optional (can be cross-checked against Special:MostLinkedCategories or the full language list).

## Language Coverage
63 languages implement this task, spanning scripting, functional, BASIC-family, and systems languages. Representative implementations include Python, Perl, Ruby, Go, Haskell, Java, C, Tcl, AWK, and Raku.

## Connections
- [[WebScraping]] — fetching the Special:Categories HTML page to extract counts
- [[MediaWikiAPI]] — the structured alternative data source for category membership
- [[Sorting]] — ordering languages in descending order by entry count
- [[StringProcessing]] — parsing the retrieved markup or JSON to extract names and numbers
- [[HTTPRequests]] — the networking step that retrieves the live data

## Contradictions
- None — reference task page.
