---
title: "System time (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/System_time
---

## Summary
This task asks the programmer to output the current system time, using any units as long as they are documented, retrieved either via a system command or a facility built into the language. It is a simple introductory exercise in accessing the operating system's clock. The key insight is that system time underpins many practical needs — debugging, network information, random number seeding, and program performance measurement.

## Task Requirements
- Output the system time.
- Any units are acceptable, provided they are noted.
- Obtain the time either through a system command or a language built-in.

## Language Coverage
162 languages implement this task, reflecting its status as a near-universal "Simple" exercise that almost every environment can satisfy through a standard clock API or shell call. Representative implementations include C, Python, Java, JavaScript, Go, Rust, Ruby, Haskell, Perl, and the UNIX Shell.

## Connections
- [[DateAndTime]] — the broader category this task belongs to
- [[UnixTime]] — the common epoch-seconds representation used by many solutions
- [[ExecuteASystemCommand]] — one of the two sanctioned retrieval mechanisms
- [[RandomNumberGeneration]] — system time is frequently used as a PRNG seed
- [[PerformanceMeasurement]] — timing program execution is a primary motivation

## Contradictions
- None — reference task page.
