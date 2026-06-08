---
title: "Terminal control/Preserve screen (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Preserve_screen
---

## Summary
This task asks the programmer to save the current state of the terminal screen, clear it and display some temporary output, and then restore the screen to exactly the state it was in beforehand. The key insight is that terminals can save and restore screen contents via an alternate screen buffer, typically driven by ANSI/VT100 escape sequences. Character decorations and attributes (and any altered font or kerning) must also be restored on exit.

## Task Requirements
- Preserve the current screen state before doing anything else.
- Clear the screen and output something to the display.
- Restore the screen to its preserved pre-task state.
- Preserve character decorations and attributes; if font or kerning is changed, restore those too before exiting.

## Language Coverage
40 languages implement this task, spanning system languages, scripting languages, and several BASIC dialects. Representative implementations include C, Go, Rust, Java, Python, Perl, Raku, Tcl, the UNIX Shell, and BBC BASIC.

## Connections
- [[ANSIEscapeCodes]] — alternate screen buffer save/restore sequences drive the solution
- [[TerminalControl]] — the broader category this task belongs to
- [[VT100]] — terminal standard whose escape codes are commonly used
- [[ScreenBuffer]] — the concept of an alternate buffer for temporary display

## Contradictions
- None — reference task page.
