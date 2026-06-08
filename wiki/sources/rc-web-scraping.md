---
title: "Web scraping (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, string-processing, http]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Web_scraping
---

## Summary
This task asks the programmer to download a web page over HTTP and extract a specific piece of data from its HTML — specifically the current UTC time from the US Naval Observatory's clock page (or, since that URL went offline in 2011, the first date/time on the task's talk page). The key insight is the two-step pattern of web scraping: fetch the raw HTML, then parse/pattern-match to pull out the wanted substring, ideally using only free, widely available standard libraries.

## Task Requirements
- Download the page at http://tycho.usno.navy.mil/cgi-bin/timer.pl over HTTP.
- Extract just the UTC time from the returned HTML.
- Print the current UTC time.
- Use only libraries that come at no extra monetary cost and are widely available (e.g. CPAN for Perl, Boost for C++).
- Fallback: if the URL is dead, scrape the first date/time from the task's talk page.

## Language Coverage
86 languages implement this task, reflecting broad support across scripting, functional, and systems languages since HTTP fetching plus text extraction is nearly universal. Representative implementations include Python, Perl, Ruby, Go, Rust, Haskell, JavaScript, Java, C#, PowerShell, and Tcl.

## Connections
- [[HypertextTransferProtocol]] — the underlying protocol used to fetch the page
- [[HTMLParsing]] — interpreting the markup to locate the target data
- [[RegularExpressions]] — common technique for extracting the time substring
- [[StringProcessing]] — general text manipulation involved in pulling out the value
- [[WebScraping]] — the named technique this task demonstrates

## Contradictions
- None — reference task page.
