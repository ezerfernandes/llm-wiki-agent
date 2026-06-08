---
title: "Distributed programming (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, concurrency, serialization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Distributed_programming
---

## Summary
This task asks the programmer to write two programs (or one program with two modes) that run on networked computers and exchange messages between them. The key insight is that the communication protocol must be generic and suitable for general distributed programming — capable of carrying the independent communications of many components and transferring arbitrary language-native data structures — rather than a one-off protocol designed for a single example. It is meant to showcase high-level communication facilities beyond raw socket creation.

## Task Requirements
- Implement two programs, or one program with two modes (e.g., client and server roles).
- The programs run on networked computers and send messages to each other.
- The protocol may be language-specific or not, but must be suitable for general distributed programming.
- The protocol should be generic, not tailored to the particular example application.
- It should handle the independent communications of many different components of a single application.
- It should support transferring arbitrary data structures that are natural for the language.
- Demonstrate high-level communication facilities beyond just creating sockets.

## Language Coverage
30 languages implement this task, spanning systems languages, functional languages, and scripting languages, often leveraging built-in distribution or RPC frameworks (e.g., Erlang and LFE message passing, Ada's distributed annex, Go's net/rpc, Python's facilities). Representative implementations include Ada, C, C#, Erlang, Go, Haskell, JavaScript, OCaml, Python, Ruby, Racket, and Tcl.

## Connections
- [[DistributedComputing]] — the broader paradigm this task demonstrates
- [[RemoteProcedureCall]] — a common high-level mechanism for sending messages between programs
- [[MessagePassing]] — the communication model emphasized by languages like Erlang
- [[Serialization]] — required to transfer arbitrary data structures over the network
- [[Sockets]] — the lower-level primitive the task asks implementations to go beyond

## Contradictions
- None — reference task page.
