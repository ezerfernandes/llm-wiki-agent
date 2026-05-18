---
title: "Standard Error (stderr)"
type: concept
tags: [c-language, io, unix]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# Standard Error (stderr)

**Standard error** (`stderr`) is the **third** default I/O stream a Unix-style process inherits from its parent shell — the canonical destination for **diagnostic output** that should stay visible even when the program's normal `stdout` is redirected to a file or pipe. File descriptor 2 ([[StandardInput|`stdin`]]=0, [[StandardOutput|`stdout`]]=1).

Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.1 — exposed by [[StandardIOLibrary|`<stdio.h>`]] as a [[FilePointer|`FILE *`]] value named `stderr`, written to via [[Fprintf|`fprintf`]]:

```c
fprintf(stderr, "Error: return code %d\n", ret);
```

## Why a separate stream

A program that prints both data and errors to `stdout` is a tooling hazard:

```
./prog > results.txt   # errors silently end up in results.txt
```

Splitting errors onto `stderr` makes `> results.txt` capture only data; errors still print to the terminal. Per-stream redirection lets the user choose:

```
./prog > out.txt 2> err.txt   # split
./prog &> all.txt              # merge stdout and stderr
./prog 2>&1 | tee log.txt      # interleave both into a pipe
```

## Buffering

Unlike [[StandardOutput|`stdout`]] (line-buffered to a terminal, fully buffered to a pipe), **`stderr` is unbuffered by default** — error output appears immediately even if the program crashes right after the call.

## Three default streams

| Stream | C name | FD | Buffering |
|---|---|---|---|
| [[StandardInput|Standard input]] | `stdin` | 0 | line / full |
| [[StandardOutput|Standard output]] | `stdout` | 1 | line (tty) / full (pipe) |
| Standard error | `stderr` | 2 | **unbuffered** |

## Connections

- [[StandardInput]] / [[StandardOutput]] — the other two default streams.
- [[Fprintf]] — the idiomatic writer (`fprintf(stderr, ...)`).
- [[FilePointer]] — `stderr` is a pre-opened one.
- [[StandardIOLibrary]] — declares the stream.
- [[StreamRedirection]] — shell-level redirection that uses FD 2 (`2> err.txt`, `2>&1`).
- [[OperatingSystem]] — opens the stream at process start.
- [[dis-2-8-io]] — introducing source.
