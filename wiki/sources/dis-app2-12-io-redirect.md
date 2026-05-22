---
title: "Dive into Systems — App 2.12 I/O Redirection"
type: source
tags: [book, unix, shell, io]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/ioredirect.html
---

## Summary
Twelfth subchapter of [[DiveIntoSystems]] Appendix 2 *Using Unix*. Codifies the [[IORedirection|I/O redirection]] operators (`>`, `>>`, `<`, `2>`, `&>`) that rewire a process's [[StandardStream|standard streams]] — [[Stdin|stdin]] (fd 0), [[Stdout|stdout]] (fd 1), [[Stderr|stderr]] (fd 2) — to and from files at the shell level.

## Key Claims
- Every process has three default streams — *"standard in (stdin), standard out (stdout), and standard error (stderr)"* — with [[FileDescriptor|file descriptors]] **0**, **1**, **2**.
- `cmd > file` (or `1> file`) redirects stdout to a file, **overwriting**; `cmd >> file` **appends**.
- `cmd < file` reads stdin from a file; `cmd 2> errs` redirects stderr separately.
- `cmd &> all` is equivalent to `cmd > all 2>&1` — merges stdout + stderr into one file.
- Operators can be combined in one command for independent multi-stream redirection.

## Connections
- [[IORedirection]] — minted here.
- [[StandardStream]] / [[Stdin]] / [[Stdout]] / [[Stderr]] — the three default streams.
- [[FileDescriptor]] — fd 0/1/2 mechanism.
- [[ShellPipe]] / [[Pipe]] — sibling stream-rewiring operator from [[dis-app2-13-pipes|App 2.13]].
- [[DiveIntoSystems]] — Appendix 2.12.
