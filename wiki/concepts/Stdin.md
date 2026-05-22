---
title: "stdin"
type: concept
tags: [unix, io]
sources: [dis-app2-12-io-redirect]
last_updated: 2026-05-18
---

# stdin

**stdin** (standard input, [[FileDescriptor|fd]] **0**) is the input stream a process reads from by default. Defaults to the terminal keyboard; can be redirected from a file via `cmd < file` or wired from another process via a [[ShellPipe|pipe]].

C wrappers: [[Scanf|`scanf`]], `fgets(buf, n, stdin)`, `getchar`.

## Connections

- [[StandardStream]] / [[Stdout]] / [[Stderr]] — siblings.
- [[IORedirection]] — `<` redirects stdin.
- [[ShellPipe]] — `cmd1 | cmd2` wires cmd1's stdout into cmd2's stdin.
- [[dis-app2-12-io-redirect]] — source.
