---
title: "stdout"
type: concept
tags: [unix, io]
sources: [dis-app2-12-io-redirect]
last_updated: 2026-05-18
---

# stdout

**stdout** (standard output, [[FileDescriptor|fd]] **1**) is the output stream a process writes normal output to. Defaults to the terminal; redirected to a file via `cmd > file` or `cmd >> file` (append) or piped to another process via `|`.

C wrappers: [[Printf|`printf`]], `puts`, `fputs(s, stdout)`.

**Buffered by default** when output is to a non-terminal — call `fflush(stdout)` for explicit flushing.

## Connections

- [[StandardStream]] / [[Stdin]] / [[Stderr]] — siblings.
- [[IORedirection]] — `>` / `>>` redirect stdout.
- [[ShellPipe]] — `|` wires stdout into the next process.
- [[dis-app2-12-io-redirect]] — source.
