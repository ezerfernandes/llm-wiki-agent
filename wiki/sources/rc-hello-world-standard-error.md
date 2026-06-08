---
title: "Hello world/Standard error (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, io-streams]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hello_world/Standard_error
---

## Summary
This task asks the programmer to write a message to the standard error stream (stderr) rather than standard output (stdout). The key insight is that most environments separate error/diagnostic output from normal program output so the two can be redirected independently. The concrete goal is to print "Goodbye, World!" specifically on the standard error channel.

## Task Requirements
- Print the message "Goodbye, World!" to the standard error stream.
- The output must go to stderr, not stdout, demonstrating awareness of the distinction between the two output streams.

## Language Coverage
165 languages implement this task, giving very broad coverage across systems, scripting, and functional languages. Representative implementations include C, Python, Java, Go, Rust, Haskell, Ruby, Perl, JavaScript, and the UNIX Shell.

## Connections
- [[StandardStreams]] — stdout/stderr/stdin as the foundational I/O channels this task exercises.
- [[FileDescriptors]] — stderr is conventionally file descriptor 2 on POSIX systems.
- [[IORedirection]] — separating streams enables redirecting errors away from normal output.
- [[HelloWorldProgram]] — this is a variant of the canonical introductory program.

## Contradictions
- None — reference task page.
