---
title: "Text processing/Max licenses in use (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, text-processing, log-parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Text_processing/Max_licenses_in_use
---

## Summary
The task is to parse a software license management log file (~10,000 lines) in which each line records either a checkout ("License OUT") or checkin ("License IN") event with a timestamp and job number. The program must determine the maximum number of licenses simultaneously in use at any point and report the time(s) at which that peak occurred. The key insight is to maintain a running counter that increments on each OUT and decrements on each IN, tracking the running maximum and the timestamps where it is reached.

## Task Requirements
- Read the provided log file where each line is either `License OUT @ <timestamp> for job <n>` or `License IN @ <timestamp> for job <n>`.
- Increment an in-use counter on each checkout (OUT) event and decrement it on each checkin (IN) event.
- Track and report the maximum concurrent license count observed.
- Report the timestamp(s) at which that maximum was reached (there may be more than one).

## Language Coverage
73 languages implement this task, giving broad coverage across systems, scripting, and functional families. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Raku, Ruby, Haskell, AWK, and REXX.

## Connections
- [[TextProcessing]] — line-by-line scanning and field extraction
- [[LogFileParsing]] — interpreting structured event records
- [[RunningMaximum]] — tracking a peak value across a stream
- [[CounterStateMachine]] — increment/decrement on event types

## Contradictions
- None — reference task page.
