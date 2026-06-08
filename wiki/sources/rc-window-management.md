---
title: "Window management (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, windowing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Window_management
---

## Summary
This Rosetta Code task asks the programmer to treat GUI windows (or at least their identities) as first-class objects: store window references in variables and compare them for equality. The core insight is that a windowing toolkit must expose handles that can be passed around like any other value, then act on them to manipulate the window's visible state.

## Task Requirements
- Treat windows, or at least window identities, as first-class objects.
- Store window identities in variables and compare them for equality.
- Demonstrate some of: hide, show, close, minimize, maximize, move, and resize a window.
- The target window may or may not have been created by the program itself.

## Language Coverage
24 languages implement this task, spanning native GUI toolkits and cross-platform bindings rather than pure algorithmic code. Representative implementations include C, Java, Python, Go, Perl, Raku, Tcl, Racket, Nim, and AutoHotkey, with several BASIC dialects (BBC BASIC, FreeBASIC, PureBasic) also present.

## Connections
- [[GraphicalUserInterface]] — the task is fundamentally about manipulating GUI windows.
- [[FirstClassObject]] — window handles must be storable in variables and comparable.
- [[EventDrivenProgramming]] — GUI windows live inside an event/message loop.
- [[ObjectIdentity]] — comparing window identities for equality.

## Contradictions
- None — reference task page.
