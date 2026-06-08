---
title: "Hello world/Newline omission (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hello_world/Newline_omission
---

## Summary
This task asks the programmer to print the string `Goodbye, World!` to standard output without a trailing newline. The key insight is that many languages' default print routines append a newline automatically, so the programmer must use a lower-level write call, a print variant that suppresses the newline, or an explicit terminator/flag to omit it.

## Task Requirements
- Display the exact string `Goodbye, World!`.
- Ensure no trailing newline character is emitted after the string.

## Language Coverage
206 languages implement this task, an extremely broad set spanning systems, scripting, functional, esoteric, and assembly languages. Representative examples include C, C++, Python, Java, JavaScript, Go, Rust, Haskell, Ruby, and assembly variants such as 68000 Assembly.

## Connections
- [[StandardOutput]] — the task targets the stdout stream directly
- [[StringProcessing]] — emitting a literal string verbatim
- [[OutputBuffering]] — newline-free output often interacts with line buffering and flushing
- [[HelloWorldProgram]] — a variant of the canonical introductory program

## Contradictions
- None — reference task page.
