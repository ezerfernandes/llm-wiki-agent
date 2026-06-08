---
title: "Yahoo! search interface (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, web-scraping, http, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Yahoo!_search_interface
---

## Summary
This task asks the programmer to build a class that queries Yahoo!'s web search and extracts structured results. Each result must expose its URL, title, and content snippet, and the class must offer a "Next Page" method to paginate through additional results. The core challenge is issuing an HTTP request and parsing the returned HTML (typically with regular expressions or a markup parser) to recover the relevant fields, plus tracking pagination state to fetch subsequent pages.

## Task Requirements
- Create a class that searches Yahoo! results.
- Implement a "Next Page" method to advance to subsequent result pages.
- For each result, read and expose the URL, Title, and Content.

## Language Coverage
30 languages implement this task, spanning systems languages, scripting languages, and functional languages. Representative implementations include Python, Ruby, Perl, Raku, Haskell, Java, C#, Go, Racket, and Tcl.

## Connections
- [[WebScraping]] — extracting structured data from a search results page
- [[HTTPRequests]] — issuing the query to the Yahoo! endpoint
- [[RegularExpressions]] — common technique for pulling URL/title/content fields from HTML
- [[Pagination]] — the "Next Page" method tracks offset/state across requests
- [[ObjectOrientedProgramming]] — the task is specified as a reusable class

## Contradictions
- None — reference task page.
