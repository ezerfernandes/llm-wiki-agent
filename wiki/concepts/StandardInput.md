---
title: "Standard Input (stdin)"
type: concept
tags: [c-language, io, unix]
sources: [dis-1-2-input-output]
last_updated: 2026-05-17
---

# Standard Input (stdin)

**Standard input** (`stdin`) is the default input stream a Unix-style process reads from — typically the terminal keyboard, but redirectable from a file (`./prog < input.txt`) or piped from another process (`producer | ./prog`).

In [[CLanguage|C]], [[Scanf|`scanf`]] reads from `stdin` by default ([[dis-1-2-input-output|DIS Ch 1.2]]). The [[StandardIOLibrary|`<stdio.h>`]] library exposes the underlying stream as the `FILE *` named `stdin`, allowing the lower-level `fgets(buf, n, stdin)` / `fscanf(stdin, ...)` forms when finer control is needed.

## Defaults set by the OS

The process inherits three open streams from its parent shell:

| Stream | C name | FD |
|---|---|---|
| Standard input | `stdin` | 0 |
| [[StandardOutput|Standard output]] | `stdout` | 1 |
| Standard error | `stderr` | 2 |

These are an [[OperatingSystem|OS]]-level abstraction the C library wraps with buffered `FILE *` handles. [[dis-1-2-input-output|Ch 1.2]] uses `stdin` implicitly through `scanf`; the file-descriptor / [[Abstraction|abstraction]] view arrives in later DIS chapters on the OS.

## Connections

- [[Scanf]] — the canonical reader of `stdin`.
- [[StandardOutput]] — the output counterpart.
- [[StandardIOLibrary]] — `<stdio.h>` declares the stream and the readers.
- [[OperatingSystem]] — the OS sets up the stream when the process starts.
- [[CLanguage]] — the language using it.
- [[dis-1-2-input-output]] — introducing source.
