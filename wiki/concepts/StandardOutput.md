---
title: "Standard Output (stdout)"
type: concept
tags: [c-language, io, unix]
sources: [dis-1-2-input-output]
last_updated: 2026-05-17
---

# Standard Output (stdout)

**Standard output** (`stdout`) is the default output stream a Unix-style process writes to — typically the terminal, but redirectable to a file (`./prog > out.txt`) or piped to another process (`./prog | consumer`).

In [[CLanguage|C]], [[Printf|`printf`]] writes to `stdout` by default ([[dis-1-2-input-output|DIS Ch 1.2]]). The [[StandardIOLibrary|`<stdio.h>`]] library exposes the stream as a `FILE *` named `stdout`, with `fprintf(stdout, ...)` available for the explicit form.

## Buffering

`stdout` is **line-buffered** when connected to a terminal and **fully buffered** when redirected to a pipe / file — a frequent source of *"my `printf` didn't appear"* surprises in long-running or interactive programs. Workarounds: end the format string with [[EscapeSequence|`\n`]] (line buffer flushes), call `fflush(stdout)`, or use `setbuf(stdout, NULL)` for unbuffered output. (Buffering details are not in Ch 1.2 but matter the moment `printf` is mixed with `scanf`.)

## Three default streams

| Stream | C name | FD |
|---|---|---|
| [[StandardInput|Standard input]] | `stdin` | 0 |
| Standard output | `stdout` | 1 |
| Standard error | `stderr` | 2 |

## Connections

- [[Printf]] — the canonical writer of `stdout`.
- [[StandardInput]] — the input counterpart.
- [[StandardIOLibrary]] — `<stdio.h>` declares the stream and the writers.
- [[EscapeSequence]] — `\n` ends a line and (for terminal `stdout`) flushes the buffer.
- [[OperatingSystem]] — sets up the stream at process start.
- [[CLanguage]] — the language using it.
- [[dis-1-2-input-output]] — introducing source.
