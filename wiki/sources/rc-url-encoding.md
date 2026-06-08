---
title: "URL encoding (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/URL_encoding
---

## Summary
This task asks the programmer to convert an arbitrary string into its URL-encoded (percent-encoded) representation. Every character outside the unreserved set 0-9, A-Z, and a-z is replaced by a percent sign followed by its two-digit hexadecimal byte value, so a space becomes `%20` and `http://foo bar/` becomes `http%3A%2F%2Ffoo%20bar%2F`. The key insight is mapping each non-alphanumeric byte to `%` plus its hex code, with optional standard-specific exception sets.

## Task Requirements
- Convert a provided string into percent-encoded form.
- Encode every character except 0-9, A-Z, and a-z as `%` followed by a two-digit hex code.
- Characters needing conversion: ASCII control codes (00-1F, 7F), symbols (20-2F, 3A-40, 5B-60, 7B-7E), and extended characters (80 hex and above).
- Optionally support an exception string of symbols left unconverted (e.g. RFC 3986 preserves `-._~`).

## Language Coverage
93 languages implement this task, spanning systems, scripting, functional, and BASIC dialects. Representative entries include C, C++, Rust, Go, Java, Python, JavaScript, Haskell, Perl, Ruby, and Tcl.

## Connections
- [[PercentEncoding]] — the encoding scheme this task implements
- [[HexadecimalNotation]] — bytes are emitted as two-digit hex codes
- [[StringProcessing]] — per-character transformation of an input string
- [[CharacterEncoding]] — handling ASCII ranges and extended bytes
- [[UrlDecoding]] — the inverse operation (related task)

## Contradictions
- None — reference task page.
