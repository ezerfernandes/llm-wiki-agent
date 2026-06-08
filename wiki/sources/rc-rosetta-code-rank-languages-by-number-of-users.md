---
title: "Rosetta Code/Rank languages by number of users (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, web-scraping, text-processing, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rosetta_Code/Rank_languages_by_number_of_users
---

## Summary
The task asks the programmer to rank programming languages by their number of declared users on Rosetta Code itself, showing only those with at least 100 users. The key insight is that this is a self-referential web-scraping exercise: a language X's users are listed on its `Category:X_User` page, so a solution must crawl Rosetta Code's MediaWiki pages, enumerate the user categories, count members of each, and sort the results descending.

## Task Requirements
- Determine the popularity of each programming language by counting its users on Rosetta Code.
- Discover the per-language user categories, e.g. by parsing `Special:Categories` (limit 5000), then querying each `Category:X_User` page.
- Prefer the `redirect=no` form of the category URL to avoid following redirects.
- Count the members of each language's user category (a user declares a language via the `mylang` template, normally on their User page).
- Sort languages by user count in descending order and display only those with 100+ users in a two-column table.

## Language Coverage
13 languages implement this task — a modest count, since solutions require live HTTP access and MediaWiki/HTML parsing. Representative implementations include Go, Julia, Nim, Perl, Python, Racket, Raku, REXX, Wren, and zkl.

## Connections
- [[WebScraping]] — fetching and parsing remote MediaWiki category pages
- [[HttpClient]] — downloading pages from the Rosetta Code API/site
- [[Sorting]] — ranking languages by descending user count
- [[TextProcessing]] — extracting category names and member counts from page markup
- [[RegularExpressions]] — common technique for pulling user counts out of HTML

## Contradictions
- None — reference task page.
