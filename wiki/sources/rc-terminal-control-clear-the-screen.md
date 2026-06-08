---
title: "Terminal control/Clear the screen (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, ansi-escape-codes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Clear_the_screen
---

## Summary
This task asks the programmer to clear the terminal window. The key insight is that there is no single portable mechanism: most solutions either emit the ANSI/VT100 escape sequence (`ESC[2J` plus a cursor-home move), invoke a platform shell command (`clear` on Unix, `cls` on Windows), or call a library routine such as ncurses' `clear()`. The approach chosen reveals how each language interacts with the controlling terminal.

## Task Requirements
- Clear the terminal window (erase its visible contents).

## Language Coverage
102 languages implement this task, spanning systems languages, scripting languages, and many assembly dialects, reflecting how universal yet platform-dependent terminal control is. Representative implementations include C / C++, Python, Ruby, Go, Rust, Java, Perl, Lua, Haskell, and UNIX Shell.

## Connections
- [[ANSIEscapeCodes]] — the `ESC[2J` control sequence used to clear the display
- [[TerminalControl]] — the broader family of cursor and screen manipulation tasks
- [[Ncurses]] — terminal library exposing a portable `clear()` routine
- [[StandardOutput]] — escape sequences are written to stdout to reach the terminal

## Contradictions
- None — reference task page.
