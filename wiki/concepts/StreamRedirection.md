---
title: "Stream Redirection (Shell)"
type: concept
tags: [unix, shell, io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# Stream Redirection

**Stream redirection** is the shell-level mechanism that rebinds a process's three default streams ([[StandardInput|`stdin`]] / [[StandardOutput|`stdout`]] / [[StandardError|`stderr`]]) to files or pipes **before** the process starts — no code change required. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.1.

## The Ch 2.8 vocabulary

```sh
./a.out < infile.txt                       # stdin <- infile.txt
./a.out > outfile.txt                      # stdout -> outfile.txt (truncate)
./a.out >> outfile.txt                     # stdout -> outfile.txt (append)
./a.out 2> err.txt                         # stderr -> err.txt
./a.out &> all.txt                         # both stdout and stderr -> all.txt
./a.out < in.txt 1> out.txt 2> err.txt     # all three independently
./a.out 2>&1 | tee log.txt                 # merge stderr into stdout, pipe
producer | consumer                         # producer's stdout -> consumer's stdin
```

The numbers `0`, `1`, `2` are the file descriptors of [[StandardInput|`stdin`]], [[StandardOutput|`stdout`]], [[StandardError|`stderr`]].

## Why it matters for a C program

Per Ch 2.8: a program that **already** uses `printf` / `scanf` / `fprintf(stderr, ...)` becomes a *Unix pipeline citizen* for free — no flag parsing, no `-i input.txt`, no `-o output.txt`. The shell does the binding, and the program is none the wiser.

This is the architectural reason [[StandardError|`stderr`]] exists separately from [[StandardOutput|`stdout`]] — `./prog > results.txt` should capture data but not error messages.

## Connections

- [[StandardInput]] / [[StandardOutput]] / [[StandardError]] — the three streams being rebound.
- [[OperatingSystem]] — performs the rebinding via `dup2` syscalls before `exec`.
- [[FilePointer]] — what the C library wraps the rebound file descriptors with.
- [[StandardIOLibrary]] — the C-level interface unaffected by where the streams actually go.
- [[dis-2-8-io]] — introducing source.
