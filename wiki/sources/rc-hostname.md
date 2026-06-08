---
title: "Hostname (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, system-information]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hostname
---

## Summary
This task asks the programmer to determine and report the name of the host machine on which the program is running. The key insight is that nearly every platform exposes the hostname through either a system call (e.g. `gethostname`), an environment variable, or a small command-line utility, so the solution is typically a one-liner that queries the operating system rather than computing anything.

## Task Requirements
- Find and output the name of the host on which the routine is currently running.

## Language Coverage
121 languages implement this task, making it one of the broadly covered system-information tasks since hostname retrieval is a near-universal OS primitive. Representative implementations include C/C++, Python, Java, Go, Rust, Ruby, Perl, Haskell, Common Lisp, and the UNIX Shell.

## Connections
- [[OperatingSystemInterface]] — hostname is obtained via OS-level calls or utilities
- [[SystemCall]] — many solutions wrap the POSIX `gethostname` call
- [[EnvironmentVariables]] — some platforms expose the name via variables like `HOSTNAME` or `COMPUTERNAME`
- [[NetworkingBasics]] — the host name identifies a machine on a network

## Contradictions
- None — reference task page.
