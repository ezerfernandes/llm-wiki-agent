---
title: "Hello world/Web server (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, http, sockets]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hello_world/Web_server
---

## Summary
This task is the web-server equivalent of "Hello World": start a minimal HTTP server that serves the plain text `Goodbye, World!` at `http://localhost:8080/` so it can be viewed in a browser. The key insight is that it forces a program to bind a TCP socket, listen on a port, accept incoming client connections, and reply with an HTTP response — exercising the network stack rather than just standard output.

## Task Requirements
- Start or implement a server that serves the text `Goodbye, World!` at `http://localhost:8080/`.
- The server must accept multiple client connections.
- Serving plain text is acceptable; valid/formatted HTML is not required.
- Launching the browser or opening the URL is explicitly out of scope.

## Language Coverage
82 languages implement this task, spanning low-level socket code to high-level framework one-liners. Representative implementations include C, Rust, Go, Java, Python, Ruby, Perl, Haskell, Erlang, and even X86-64 Assembly.

## Connections
- [[HypertextTransferProtocol]] — the request/response protocol the server must speak
- [[TCPSockets]] — the underlying transport that must be bound and listened on
- [[NetworkProgramming]] — the broader domain of accepting and handling client connections
- [[ConcurrencyModel]] — needed to accept multiple simultaneous client connections

## Contradictions
- None — reference task page.
