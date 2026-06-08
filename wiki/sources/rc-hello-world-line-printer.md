---
title: "Hello world/Line printer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, hardware-io, device-output]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hello_world/Line_printer
---

## Summary
This task asks the programmer to send the text "Hello World!" to a physical line printer attached to the computer, not to standard output. The key insight is that a line printer is a hardware device reached through an OS-specific path or port (such as a parallel port, a device file like `/dev/lp0`, or a print spooler), so the solution depends on how the platform exposes attached devices rather than on ordinary console I/O.

## Task Requirements
- Cause a line printer attached to the computer to print a line containing the message "Hello World!".
- Target the actual line printer device, distinct from standard output.
- Account for the fact that the printer may be any device attached to an appropriate port (e.g., a parallel port).

## Language Coverage
97 languages implement this task, spanning low-level assembly (360 Assembly, X86 Assembly, MIXAL) up through high-level scripting and functional languages; representative entries include C, C++, Python, Ruby, Perl, Java, Go, Rust, UNIX Shell, and Fortran. Some languages (PARI/GP, ML/I, SQL PL) are explicitly omitted because they lack printer-related device access.

## Connections
- [[FileIO]] — printing typically means writing to a device file or port handle
- [[DeviceDriver]] — the printer is reached through OS device abstractions
- [[ParallelPort]] — a common hardware attachment point for line printers
- [[StandardOutput]] — contrasted explicitly; the printer is not stdout
- [[PrintSpooler]] — many platforms route output through a spooling service

## Contradictions
- None — reference task page.
