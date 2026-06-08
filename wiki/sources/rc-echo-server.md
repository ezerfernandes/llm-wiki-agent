---
title: "Echo server (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, concurrency, sockets]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Echo_server
---

## Summary
This task asks the programmer to build a TCP network service that listens on port 12321, accepts client connections, and echoes back complete CRLF-terminated lines. The key challenge is concurrency: the server must handle multiple simultaneous clients (via threads or processes) and must not block on one slow or misbehaving client while serving others.

## Task Requirements
- Listen on TCP port 12321 and accept incoming connections.
- Echo back complete lines, using carriage-return/line-feed (CRLF) as the line separator.
- Support connections from localhost (127.0.0.1 or ::1); no error handling required.
- Logging connection information to standard output is recommended.
- Handle simultaneous connections from multiple clients (multi-threaded or multi-process).
- Each connection must echo more than one line.
- A partial line or a non-reading client must not block responses to other clients.

## Language Coverage
50 languages implement this task, spanning systems, scripting, and functional ecosystems. Representative examples include C, C#, Go, Rust, Java, Python, Haskell, Erlang, Ruby, and Tcl.

## Connections
- [[SocketProgramming]] — the core network I/O abstraction used by every solution.
- [[TCP]] — the connection-oriented transport protocol the server speaks.
- [[Concurrency]] — required to serve multiple clients without blocking.
- [[Multithreading]] — a common strategy for per-connection isolation.
- [[NonBlockingIO]] — the event-loop alternative to one thread/process per client.

## Contradictions
- None — reference task page.
