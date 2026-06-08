---
title: "Create a file on magnetic tape (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, hardware]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Create_a_file_on_magnetic_tape
---

## Summary
This task asks the programmer to create a new file named "TAPE.FILE" of any size on a magnetic tape device. The key insight is that on Unix-like systems a tape drive is just another device special file (typically `/dev/tape` or `/dev/st0`), so writing to tape often looks identical to ordinary file I/O — the difference lies in the target path and the sequential-access nature of the medium rather than the API used.

## Task Requirements
- Create a new file called "TAPE.FILE".
- The file may be of any size.
- The file must be created on magnetic tape (a tape device), not on disk.

## Language Coverage
42 languages implement this task, spanning modern application languages, systems languages, and legacy mainframe environments. Representative implementations include C, C++, Java, Python, Go, Rust, Haskell, COBOL, Fortran, Ruby, and notably JCL (mainframe Job Control Language), which expresses tape file creation through dataset and DD statements rather than runtime file calls.

## Connections
- [[FileIO]] — the task is fundamentally a file-creation/output operation.
- [[DeviceFiles]] — on Unix systems tape drives are accessed as special device files like `/dev/st0`.
- [[SequentialAccessStorage]] — magnetic tape is the canonical sequential-access medium.
- [[JobControlLanguage]] — the JCL solution models tape datasets in a mainframe context.

## Contradictions
- None — reference task page.
