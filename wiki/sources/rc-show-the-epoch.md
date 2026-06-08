---
title: "Show the epoch (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-time]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Show_the_epoch
---

## Summary
This task asks the programmer to identify the epoch (the zero reference date) used by their language's popular date/time libraries and to display it. The preferred approach is a demonstration that sets the internal date representation to zero (0 ms/ns/ticks) so the epoch surfaces even if implementers change it behind the scenes; documentation citations are acceptable when a live demonstration is impractical. The key insight is that different platforms anchor time at different reference dates (e.g. the Unix epoch of 1970-01-01, .NET's 0001-01-01, or others).

## Task Requirements
- Choose the popular date libraries used by the language.
- Show the epoch (reference date) those libraries use.
- Prefer a demonstration (e.g. setting the internal representation to 0 ms/ns/etc.) over plain documentation text.
- Where documentation links are used instead, that is acceptable when a demonstration is impossible or impractical.
- For consistency, show the date in UTC time where possible.

## Language Coverage
88 languages implement this task, spanning systems languages, scripting languages, functional languages, and BASIC/legacy dialects. Representative implementations include C, C++, Java, Python, JavaScript, Ruby, Perl, Go, Rust, Haskell, and COBOL.

## Connections
- [[UnixTime]] — the 1970-01-01 epoch most commonly returned by these libraries
- [[Epoch]] — the general concept of a reference zero date for time measurement
- [[CoordinatedUniversalTime]] — UTC, the timezone the task requests for output
- [[DateAndTime]] — the date/time handling domain this task probes

## Contradictions
- None — reference task page.
