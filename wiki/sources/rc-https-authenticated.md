---
title: "HTTPS/Authenticated (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, http, security]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/HTTPS/Authenticated
---

## Summary
This task asks the programmer to make an HTTPS request that includes authentication credentials, demonstrating how a client proves its identity to a secured web resource over TLS. The key constraint is that authentication must be done without client certificates (which are handled by a separate task), so implementations typically rely on schemes such as HTTP Basic authentication or supplying a username and password to an HTTP client library.

## Task Requirements
- Demonstrate an HTTPS request that carries authentication.
- Do not use client certificates for authentication (that is the subject of the separate Client-Authenticated HTTPS Request task).

## Language Coverage
38 languages implement this task, covering general-purpose languages, scripting languages, and BASIC dialects. Representative implementations include C, C#, Java, Python, Ruby, Perl, Go, Rust, Haskell, and PowerShell.

## Connections
- [[HTTPS]] — the underlying secure transport protocol used.
- [[TLS]] — encryption layer that secures the connection.
- [[BasicAuthentication]] — a common scheme for supplying credentials over HTTP.
- [[HTTPRequest]] — the general mechanism this task specializes.

## Contradictions
- None — reference task page.
