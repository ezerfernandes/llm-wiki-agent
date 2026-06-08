---
title: "Random number generator (device) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, randomness, operating-systems]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Random_number_generator_(device)
---

## Summary
This task asks the programmer to obtain a random 32-bit number from a hardware- or OS-provided entropy source rather than a pure software pseudo-random algorithm. On Unix-like systems the canonical sources are the `/dev/random` and `/dev/urandom` device files, which gather entropy from physical noise (interrupt timings, device activity, etc.). The key insight is the distinction between deterministic software PRNGs and true entropy sources backed by the operating system or hardware.

## Task Requirements
- Use a system mechanism that generates randomness from more than just a software algorithm (e.g. the `/dev/urandom` device on Unix, or an equivalent OS/hardware entropy facility).
- Show how to read a single random 32-bit number from that mechanism.

## Language Coverage
68 languages implement this task, spanning systems languages, scripting languages, and assembly. Representative implementations include C, C++, Rust, Go, Python, Perl, Ruby, Haskell, OCaml, and even AArch64/x86-64 Assembly, reflecting how each ecosystem exposes OS entropy devices or syscalls.

## Connections
- [[RandomNumberGeneration]] — the broader topic this task specializes
- [[Entropy]] — the underlying resource an OS device pool accumulates
- [[DevUrandom]] — the canonical Unix entropy device interface
- [[OperatingSystem]] — provider of the random device abstraction

## Contradictions
- None — reference task page.
