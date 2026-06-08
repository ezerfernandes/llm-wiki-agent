---
title: "Terminal control/Unicode output (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, unicode]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Unicode_output
---

## Summary
The task asks the programmer to detect whether the terminal supports Unicode output before emitting a Unicode character, and only then print a Unicode delta (U+25B3 "△"); if Unicode is unsupported, raise an appropriate error. The key insight is that capability detection typically relies on inspecting the system's locale/encoding configuration (e.g. environment variables like `LANG`, `LC_CTYPE`, or codepage queries) rather than printing blindly.

## Task Requirements
- Check that the terminal supports Unicode output before outputting a Unicode character.
- If supported, output the Unicode delta character U+25B3.
- If not supported, raise an appropriate error.
- It is permissible to use system configuration data (locale, codepage) to determine terminal capabilities when the system exposes such a facility.

## Language Coverage
43 languages implement this task, spanning shells and BASIC dialects through to functional and systems languages. Representative implementations include C, Python, Perl, Ruby, Haskell, Common Lisp, Lua, Tcl, Kotlin, and UNIX Shell.

## Connections
- [[Unicode]] — the delta U+25B3 is a Unicode code point requiring proper encoding
- [[CharacterEncoding]] — UTF-8 vs legacy codepages determine output viability
- [[Locale]] — environment locale settings are the usual capability-detection signal
- [[TerminalControl]] — broader family of terminal capability and control tasks

## Contradictions
- None — reference task page.
