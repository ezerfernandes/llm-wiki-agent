---
title: "I/O Redirection"
type: concept
tags: [unix, shell, io]
sources: [dis-app2-12-io-redirect]
last_updated: 2026-05-18
---

# I/O Redirection

**I/O redirection** is the [[UnixShell|shell]] mechanism for rewiring a process's [[StandardStream|standard streams]] — [[Stdin|stdin]] (fd 0), [[Stdout|stdout]] (fd 1), [[Stderr|stderr]] (fd 2) — to and from files, without modifying the program.

## Operators (from [[dis-app2-12-io-redirect|DIS App 2.12]])

| Operator | Effect |
|---|---|
| `cmd > file` | Redirect [[Stdout]] to `file` (**overwrite**). |
| `cmd >> file` | Redirect [[Stdout]] to `file` (**append**). |
| `cmd < file` | Read [[Stdin]] from `file`. |
| `cmd 2> file` | Redirect [[Stderr]] only. |
| `cmd 2>> file` | Append [[Stderr]]. |
| `cmd &> file` | Redirect both [[Stdout]] and [[Stderr]] (equivalent to `> file 2>&1`). |
| `cmd > out 2> err` | Stdout to `out`, stderr to `err` (independent). |
| `cmd 2>&1` | Duplicate fd 2 onto fd 1 (merge stderr into stdout). |

## Why fd 1 vs fd 2 separation matters

Logs and errors deserve separate channels — `make 2> build_errors.log` keeps the error stream isolated while the normal build output still streams to the terminal.

## Connections

- [[StandardStream]] / [[Stdin]] / [[Stdout]] / [[Stderr]] — the three streams.
- [[FileDescriptor]] — the integer addressing scheme (0/1/2).
- [[ShellPipe]] / [[Pipe]] — sibling stream-rewiring mechanism (process-to-process rather than process-to-file).
- [[UnixShell]] / [[Bash]] — host.
- [[dis-app2-12-io-redirect]] — source.
