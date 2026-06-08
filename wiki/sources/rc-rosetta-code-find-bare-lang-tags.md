---
title: "Rosetta Code/Find bare lang tags (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, text-processing, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rosetta_Code/Find_bare_lang_tags
---

## Summary
This Rosetta Code task asks the programmer to scan the MediaWiki source of a page and find all `<lang>` tags that omit a language attribute (i.e. bare tags), then report counts. The key insight is associating each bare tag with the language section (`{{header|...}}`) it falls under, classifying tags with no enclosing header as "no language". It is a domain-specific text-processing exercise rooted in the Rosetta Code wiki's own markup conventions.

## Task Requirements
- Parse the wikitext of a page for `<lang>` opening tags that have no language specified.
- Track the current language section, determined by `=={{header|Language}}==` markers.
- Print the total count of bare tags, then a per-section breakdown including a "no language" bucket.
- Extra credit: process multiple files/pages and aggregate results by language, listing the page names where each bare tag appears.
- Extra extra credit: use the MediaWiki API to fetch and test real Rosetta Code task pages.

## Language Coverage
27 languages implement this task, a moderate breadth typical of niche meta/text-processing tasks. Representative implementations include Haskell, Go, Python, Perl, Raku, Ruby, Rust, Java, Tcl, and jq.

## Connections
- [[TextProcessing]] — the core activity is scanning and matching markup
- [[RegularExpressions]] — a natural tool for detecting bare `<lang>` tags and `{{header}}` markers
- [[Parsing]] — interpreting MediaWiki source structure
- [[MediaWikiAPI]] — used to retrieve live page content for the extra credit
- [[StateMachine]] — tracking the active language section while scanning

## Contradictions
- None — reference task page.
