---
title: "URL decoding (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/URL_decoding
---

## Summary
The task is to implement a function that converts a URL-encoded (percent-encoded) string back into its original unencoded form, the inverse of URL encoding. Each `%XX` triplet is replaced by the byte whose hexadecimal value is `XX`. The key subtlety is that decoding must be performed in a single pass: a decoded `%` must not itself be re-interpreted as the start of another escape sequence.

## Task Requirements
- Provide a function or mechanism to revert a percent-encoded string to its original characters.
- `http%3A%2F%2Ffoo%20bar%2F` decodes to `http://foo bar/`.
- `google.com/search?q=%60Abdu%27l-Bah%C3%A1` decodes to `google.com/search?q=`Abdu'l-Bahá` (handling multi-byte UTF-8 sequences such as `%C3%A1`).
- `%25%32%35` decodes to `%25`, not `%` — decoding is applied once, not recursively.

## Language Coverage
97 languages implement this task, reflecting the ubiquity of URL handling across general-purpose languages, scripting languages, and shells. Representative implementations include C, C++, Python, Java, JavaScript, Go, Rust, Haskell, Perl, and Bash.

## Connections
- [[PercentEncoding]] — the encoding scheme this task reverses
- [[URLEncoding]] — the inverse Rosetta Code task
- [[StringManipulation]] — the broader category this task belongs to
- [[UTF8]] — multi-byte sequences must be decoded byte-wise then interpreted as UTF-8
- [[HexadecimalParsing]] — each escape is a two-digit hex value

## Contradictions
- None — reference task page.
