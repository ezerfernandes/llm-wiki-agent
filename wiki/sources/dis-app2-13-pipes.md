---
title: "Dive into Systems — App 2.13 Pipes"
type: source
tags: [book, unix, shell, pipes, ipc]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/pipe.html
---

## Summary
Thirteenth subchapter of [[DiveIntoSystems]] Appendix 2 *Using Unix*. Codifies the [[ShellPipe|shell pipe `|`]] operator: chain commands so the [[Stdout|stdout]] of one becomes the [[Stdin|stdin]] of the next — *no intermediate files needed*. This is the **shell-level surface** of the [[Pipe]] [[InterprocessCommunication|IPC]] primitive ingested in [[dis-13-4-2-message-passing|Ch 13.4.2]].

## Key Claims
- `cmd1 | cmd2` wires `cmd1`'s stdout into `cmd2`'s stdin.
- Pipes chain arbitrarily: `cat file | grep pattern | wc -l`.
- Common composition: filter with [[Grep|`grep`]], count with `wc`, transform with `sort`/`uniq`/`awk` — **no temporary files**.
- [[Xargs|`xargs`]] differs from a raw pipe — it executes the downstream command **once per input value** rather than streaming.

## Connections
- [[ShellPipe]] — minted here as the shell-level alias.
- [[Pipe]] — extended in place; the underlying [[InterprocessCommunication|IPC]] primitive ([[dis-13-4-2-message-passing|Ch 13.4.2]]).
- [[IORedirection]] — sibling stream-rewiring operator from [[dis-app2-12-io-redirect|App 2.12]].
- [[Grep]] — most common pipe consumer.
- [[Xargs]] — adjacent per-arg execution helper.
- [[DiveIntoSystems]] — Appendix 2.13.
