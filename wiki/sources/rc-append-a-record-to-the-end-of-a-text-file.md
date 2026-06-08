---
title: "Append a record to the end of a text file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, concurrency]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Append_a_record_to_the_end_of_a_text_file
---

## Summary
The task asks the programmer to open a file in append mode, add a new record to its end, and verify the record landed there. The example data models a Unix `/etc/passwd` file: colon-separated fields with a comma-separated GECOS subfield. The key insight is that append mode keeps the write position pinned to end-of-file even across concurrent writers, which is why it is the safe choice for log files and shared records.

## Task Requirements
- Write two sample "passwd" records to a file in the system's typical record format (ideally with named, typed fields).
- Close the file, then reopen it in append mode.
- Append a new record and close the file again, taking care to avoid concurrent overwrites from other jobs (e.g. via file/record locking).
- Reopen the file and demonstrate the new record is at the end.
- Output format should mimic `/etc/passwd`, paying attention to the comma separator in the GECOS field.
- Provide a capability summary table covering in-core vs on-disk representation, IO library, append support, automatic append, and multi-tasking safety.

## Language Coverage
55 languages implement this task, spanning systems languages, scripting languages, functional languages, and shells. Representative entries include C, C++, Rust, Go, Java, Python, Perl, Ruby, Common Lisp, Haskell, and UNIX Shell.

## Connections
- [[FileIO]] — opening files in append mode is the central mechanism.
- [[FileLocking]] — record/file locking to guarantee safe concurrent appends.
- [[Concurrency]] — multi-tasking safety of append writes from multiple jobs.
- [[DelimitedTextFormat]] — colon-separated records with a comma-separated GECOS subfield, like `/etc/passwd`.

## Contradictions
- None — reference task page.
