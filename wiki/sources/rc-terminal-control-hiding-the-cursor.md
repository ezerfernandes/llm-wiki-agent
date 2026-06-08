---
title: "Terminal control/Hiding the cursor (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, ansi-escape-codes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Hiding_the_cursor
---

## Summary
This task asks the programmer to hide the terminal's text cursor and then make it visible again. The key insight is that this is typically done by emitting terminal control sequences — on most modern terminals the ANSI/VT220 escape codes `ESC[?25l` (hide) and `ESC[?25h` (show) — rather than through any standard library facility, so portability depends on the terminal emulator or on a curses-style library.

## Task Requirements
- Hide the terminal cursor.
- Show the cursor again afterward.

## Language Coverage
51 languages implement this task, spanning systems languages, scripting languages, and many BASIC dialects, reflecting how universal terminal manipulation is. Representative implementations include C, C++, C#, Go, Python, Perl, Ruby, Lua, Tcl, Julia, and several BASIC variants such as FreeBASIC and PureBasic.

## Connections
- [[AnsiEscapeCodes]] — the `ESC[?25l` / `ESC[?25h` sequences used to toggle cursor visibility
- [[TerminalControl]] — the broader family of Rosetta Code tasks for manipulating a text terminal
- [[Ncurses]] — curses libraries provide `curs_set()` as a portable abstraction for this operation

## Contradictions
- None — reference task page.
