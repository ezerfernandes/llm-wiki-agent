---
title: "Standard Streams"
type: concept
tags: [unix, io]
sources: [dis-app2-12-io-redirect]
last_updated: 2026-05-18
---

# Standard Streams

Every Unix process is born with **three standard I/O streams**, each addressed by a fixed [[FileDescriptor|file descriptor]] integer:

| Stream | fd | Default destination |
|---|---|---|
| [[Stdin]] | **0** | Keyboard / terminal input |
| [[Stdout]] | **1** | Terminal display |
| [[Stderr]] | **2** | Terminal display (unbuffered) |

These streams can be **rewired** via [[IORedirection|I/O redirection]] (`<`, `>`, `2>`) or a [[ShellPipe|pipe]] (`|`) without changing the program — the abstraction that makes Unix tools **composable**.

## Connections

- [[Stdin]] / [[Stdout]] / [[Stderr]] — the three concrete streams.
- [[FileDescriptor]] — the integer addressing scheme.
- [[IORedirection]] / [[ShellPipe]] — the two rewiring mechanisms.
- [[Printf]] / [[Scanf]] — C wrappers that target stdout / stdin by default.
- [[dis-app2-12-io-redirect]] — source.
