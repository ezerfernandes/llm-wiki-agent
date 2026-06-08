---
title: "Nautical bell (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time, scheduling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Nautical_bell
---

## Summary
The task asks for a small program that emulates a ship's bell, emitting the traditional ringing pattern at the appropriate times of day. Naval watches run in four-hour periods subdivided into eight half-hour intervals; the bell sounds once at the first half-hour and adds one ring every half-hour up to eight bells at the end of each watch, then resets. The key insight is mapping the current time-of-day onto this repeating eight-bell cycle, with timing keyed to Greenwich Mean Time unless local convention says otherwise.

## Task Requirements
- Emulate a nautical bell producing the correct ringing pattern at certain times throughout the day.
- Base the bell timing on Greenwich Mean Time (GMT), unless locale dictates otherwise.
- Permitted to run as a daemon/service or slave off a scheduler.
- Permitted to use alternative notification methods (e.g., printing a written notice such as "Two Bells Gone") if more usual for the system.

## Language Coverage
30 languages implement this task, spanning systems and scripting languages with strong time-handling and concurrency support. Representative implementations include Ada, C, C++, Go, Haskell, Java, Julia, Python, Perl, Raku, Ruby, PowerShell, and Tcl.

## Connections
- [[DateAndTime]] — the core domain: mapping wall-clock time onto a schedule.
- [[GreenwichMeanTime]] — the reference time standard specified for bell timing.
- [[Daemon]] — a permitted long-running background execution model for the program.
- [[Scheduling]] — using a scheduler to trigger the periodic bell events.
- [[ModularArithmetic]] — the eight-bell cycle is naturally expressed as a modulo computation.

## Contradictions
- None — reference task page.
