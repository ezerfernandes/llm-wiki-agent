---
title: "Fixed length records (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fixed_length_records
---

## Summary
This task asks the programmer to read and write fixed-length records — a pre-terminal data format (rooted in 80-column Hollerith punch cards) that has no newline delimiters and pads every record to a constant width. The core program reads 80-column records from a file and writes out each record reversed, still as space-padded 80-byte records. The key insight is that record boundaries are implied by position (every 80 bytes), not by newline characters, and the data may contain arbitrary 8-bit bytes including NUL and embedded newlines.

## Task Requirements
- Read 80-column fixed-length records from a file (no newline terminators; newlines may appear within the data).
- Write out the reverse of each record as a fixed-length 80-column record, space-padded.
- Treat data as full 8-bit (NUL bytes and any byte values allowed), not limited to printable ASCII.
- Use sample file names: sample.txt, infile.dat, outfile.dat (the `dd` utility with cbs=80 conv=block/unblock can build/display such files).
- Bonus: convert a Forth-style BLOCK file (1024 bytes = 16 lines of 64 chars) to newline text with trailing spaces stripped, and convert text back to 64-char block form padded to a full 1024-byte block.

## Language Coverage
33 languages implement this task, spanning systems and mainframe-oriented languages alongside scripting ones — representative examples include Ada, C++, COBOL, Fortran, Go, Java, Python, Perl, Raku, Rust, REXX, and Tcl.

## Connections
- [[FileIO]] — reading and writing binary records by byte offset rather than by line
- [[FixedWidthFormat]] — the positional, non-delimited record layout central to the task
- [[PunchedCard]] — the 80-column Hollerith origin of the format
- [[EBCDIC]] — the encoding commonly paired with these formats on mainframes
- [[StringReversal]] — reversing each record's contents

## Contradictions
- None — reference task page.
