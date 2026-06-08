---
title: "Terminal control/Dimensions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, system-calls]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Dimensions
---

## Summary
This task asks the programmer to determine the current terminal's height and width (in rows and columns) and store those values into variables for later use. The key insight is that terminal dimensions are not fixed and must be queried at runtime from the operating system or terminal driver, typically via system calls (e.g. ioctl with TIOCGWINSZ on Unix), environment variables (LINES/COLUMNS), or platform-specific console APIs.

## Task Requirements
- Determine the height (number of rows) of the terminal.
- Determine the width (number of columns) of the terminal.
- Store this information into variables for subsequent use.

## Language Coverage
52 languages implement this task, spanning systems languages, scripting languages, and a wide range of BASIC dialects. Representative implementations include C, Go, Python, Perl, Ruby, Common Lisp, OCaml, Tcl, COBOL, and AArch64 Assembly.

## Connections
- [[TerminalControl]] — part of the broader terminal control task family
- [[SystemCall]] — querying the OS/terminal driver (e.g. ioctl) for window size
- [[EnvironmentVariables]] — LINES and COLUMNS as a fallback source of dimensions
- [[ANSIEscapeCodes]] — alternative cursor-position probing technique

## Contradictions
- None — reference task page.
