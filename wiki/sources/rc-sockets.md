---
title: "Sockets (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, sockets]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sockets
---

## Summary
This task asks the programmer to open a network socket to `localhost` on port 256, send the message "hello socket world", and then close the socket. It is a minimal demonstration of client-side TCP networking, exercising address resolution, connection setup, and writing bytes to a stream. Error and exception handling are explicitly out of scope.

## Task Requirements
- Open a socket to `localhost` on port 256.
- Send the message "hello socket world" over that connection.
- Close the socket afterward.
- Catching exceptions or errors is not required.

## Language Coverage
88 languages implement this task, reflecting how broadly TCP socket APIs are exposed across ecosystems — from systems languages to scripting and even assembly. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Ruby, Haskell, and X86 Assembly.

## Connections
- [[TCPIP]] — the transport/network protocol stack underlying the connection
- [[BerkeleySockets]] — the de facto socket API model most implementations follow
- [[ClientServerModel]] — this task is the client half of a network exchange
- [[NetworkProgramming]] — the broader domain this task belongs to

## Contradictions
- None — reference task page.
