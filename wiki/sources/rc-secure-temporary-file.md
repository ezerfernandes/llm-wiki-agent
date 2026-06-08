---
title: "Secure temporary file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, security]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Secure_temporary_file
---

## Summary
This task asks the programmer to create a temporary file securely and exclusively, opening it in a way that eliminates race conditions. The key insight is that naively checking whether a name exists and then creating the file leaves a window for a time-of-check-to-time-of-use (TOCTOU) attack; the correct approach uses an atomic open-or-fail operation that both generates a unique name and creates the file in a single step. Implementations should automatically resolve name collisions, failing only on permission denial, a read-only or full filesystem, or similar conditions.

## Task Requirements
- Create a temporary file securely and exclusively, with no possible race conditions.
- Local filesystem semantics may be assumed (network filesystems like NFS have more complex requirements).
- Automatically resolve name collisions so the file is unique.
- Fail (return an error or raise an exception) only on conditions such as permission denied, read-only filesystem, or full filesystem.

## Language Coverage
49 languages implement this task, spanning systems languages, scripting languages, and functional languages, most relying on a standard-library routine that wraps the OS-level atomic create primitive. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Ruby, Haskell, and Tcl.

## Connections
- [[RaceCondition]] — the core hazard the task is designed to avoid
- [[TOCTOU]] — the specific check-then-use vulnerability eliminated by atomic creation
- [[AtomicOperation]] — the open-or-fail primitive (e.g. O_EXCL) that guarantees exclusivity
- [[FileIO]] — the task is a file-system operation
- [[mkstemp]] — the canonical POSIX library function for this purpose

## Contradictions
- None — reference task page.
