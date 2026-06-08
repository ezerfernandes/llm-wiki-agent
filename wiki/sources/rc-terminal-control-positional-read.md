---
title: "Terminal control/Positional read (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Positional_read
---

## Summary
This task asks the programmer to determine the character currently displayed on the terminal screen at a specific cell — column 3, row 6 — and store that character in a variable. The key insight is that reading back screen contents is not a portable terminal operation: the task explicitly permits using system or language facilities, maintained display records, or screen buffers (rather than directly querying the terminal) when those are the more natural mechanism for the platform.

## Task Requirements
- Read the character displayed at column 3, row 6 of the terminal screen.
- Store that character in a variable.
- It is acceptable to use system/language methods, system records, available buffers, or maintained display records instead of querying the terminal directly, if those are more usual for the platform.

## Language Coverage
20 languages implement this task, spanning low-level system languages, scripting languages, and Lisp dialects, reflecting the wide variation in how platforms expose screen-cell reads. Representative implementations include C, Go, Python, Perl, Raku, Kotlin, Common Lisp, Racket, PowerShell, and REXX.

## Connections
- [[TerminalControl]] — part of the terminal control task family
- [[ScreenBuffer]] — reading from a maintained display/screen buffer
- [[Ncurses]] — common library for terminal cell access on Unix-like systems
- [[StandardOutput]] — the terminal as an addressable I/O surface

## Contradictions
- None — reference task page.
