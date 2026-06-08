---
title: "URL parser (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/URL_parser
---

## Summary
The task asks the programmer to parse a well-formed URL into its component parts following the generic syntax `scheme://[username:password@]domain[:port]/path?query_string#fragment_id`. The key insight is that a URL is a structured string defined by RFC 3986, and only some components are always present (scheme is mandatory; port, query, and fragment are optional), with path/query/fragment being case-sensitive while scheme and domain are not. This is distinct from URL encoding/decoding.

## Task Requirements
- Parse a well-formed URL and extract its relevant fields: scheme, domain, path, and any of port, username, password, query, fragment.
- Handle the full generic syntax, including authority-less schemes such as `urn:`, `mailto:`, `news:`, and `tel:`.
- Correctly handle the provided test cases (e.g. `foo://example.com:8042/over/there?name=ferret#nose`, `urn:example:animal:ferret:nose`, IPv6 hosts like `ldap://[2001:db8::7]/...`).
- Return the parsed information in any language-appropriate structure (record, object, array, set of variables) as long as the code is clear and reusable.
- Extra credit for clear error diagnostics on malformed input.

## Language Coverage
39 languages implement this task, spanning systems, scripting, and functional styles. Representative examples include Python, Rust, Go, Haskell, JavaScript, Perl, Ruby, C#, Java, and Raku — many lean on a standard-library URL/URI parser rather than hand-rolling the grammar.

## Connections
- [[Parsing]] — decomposing a structured string into typed components
- [[RegularExpressions]] — a common implementation strategy for splitting URL fields
- [[FiniteStateMachine]] — alternative grammar-driven parsing approach
- [[StringManipulation]] — the broader category this task belongs to
- [[URLEncoding]] — explicitly contrasted relative; the task is not about percent-encoding

## Contradictions
- None — reference task page.
