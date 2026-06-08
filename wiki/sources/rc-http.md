---
title: "HTTP (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, web]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/HTTP
---

## Summary
This task asks the programmer to access a URL over HTTP and print the content of the located resource to the console. It is the simplest form of web client work: issue a GET request, read the response body, and display it. A separate task covers the TLS-secured HTTPS variant.

## Task Requirements
- Access a URL (an HTTP resource).
- Fetch the located resource's content.
- Print that content to the console / standard output.

## Language Coverage
125 languages implement this task, spanning system languages, scripting languages, and even assembly, reflecting how ubiquitous HTTP clients are. Representative implementations include C, C++, Go, Rust, Python, Java, JavaScript, Perl, Ruby, Haskell, and UNIX Shell.

## Connections
- [[HypertextTransferProtocol]] — the protocol whose GET request the task exercises.
- [[UniformResourceLocator]] — the URL that identifies the resource to fetch.
- [[ClientServerModel]] — the request/response interaction underlying the task.
- [[HTTPSRequest]] — the related TLS-secured variant task.

## Contradictions
- None — reference task page.
