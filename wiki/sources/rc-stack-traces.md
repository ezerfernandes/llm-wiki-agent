---
title: "Stack traces (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, debugging, introspection]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Stack_traces
---

## Summary
This task asks the programmer to print the current call stack in a way suitable for the platform, using the language's introspection or debugging facilities. Each printed frame must include at least the name of the function or method at that level. The key constraint is that the program must continue running after emitting the trace, so the trace is generated deliberately (not via an uncaught exception that terminates execution).

## Task Requirements
- Print the current call stack at the point of the call.
- Include at least the function or method name for each frame.
- The trace may be triggered by an explicit instrumentation call in the sample code.
- The program must be able to continue executing after the trace is produced.
- The reported solution must show the actual trace output from a sample run.

## Language Coverage
62 languages implement this task, spanning compiled, managed, and scripting environments, since most runtimes expose some form of call-stack introspection. Representative implementations include C, Java, Python, Ruby, Go, JavaScript, Perl, Common Lisp, Tcl, and Smalltalk.

## Connections
- [[CallStack]] — the runtime structure being inspected
- [[Introspection]] — the reflective capability that exposes stack frames
- [[Debugging]] — a primary use case for stack traces
- [[ExceptionHandling]] — related mechanism, often the source of automatic traces
- [[StackFrame]] — the per-call unit reported in the trace

## Contradictions
- None — reference task page.
