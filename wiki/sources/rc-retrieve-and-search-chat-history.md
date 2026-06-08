---
title: "Retrieve and search chat history (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, text-processing, date-time]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Retrieve_and_search_chat_history
---

## Summary
The task asks the programmer to download the Tcl Chatroom's daily log files for the last 10 days over HTTP, search each line for a substring supplied as a command-line argument, and print every matching line grouped under its log file URL. The key wrinkle is time-zone correctness: log files are named `YYYY-MM-DD.tcl` in Germany's `Europe/Berlin` zone, so a naive client-local date can miss the most recent file — solved either by generating dates in Berlin time or by widening the range an extra day while suppressing "not found" pages. The implementation must be a single-file script using only the standard library.

## Task Requirements
- Retrieve chat logs for the last 10 days via HTTP from `http://tclers.tk/conferences/tcl/`, with files named `YYYY-MM-DD.tcl`.
- Take the search substring as a command-line argument (or from stdin if argument parsing isn't available).
- Print matching lines in the format: log file URL, a `------` separator, the matching lines, then a closing `------`.
- Account for the client-vs-server time-zone difference by using `Europe/Berlin` dates or by checking one extra day (today + 1) without printing the contents of a missing-file error page.
- Use only the language's standard library; no third-party dependencies or project/dependency files.
- If the standard library lacks an HTTP client, speak raw HTTP 1.0 to the server.

## Language Coverage
21 languages implement this task, spanning systems, scripting, functional, and JVM languages — including C, Go, Java, Python, Perl, Ruby, Raku, Julia, F#, Racket, Tcl, and Wren.

## Connections
- [[HypertextTransferProtocol]] — fetching log files over HTTP, possibly raw HTTP 1.0
- [[TimeZoneHandling]] — generating correct dates in the Europe/Berlin zone
- [[SubstringSearch]] — matching the query string within each log line
- [[StandardLibrary]] — constraint to use only built-in facilities
- [[TextProcessing]] — line-oriented parsing and filtering of log output

## Contradictions
- None — reference task page.
