---
title: "Mouse position (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, input-devices]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mouse_position
---

## Summary
This task asks the programmer to retrieve the current location of the mouse cursor expressed relative to the active window (not the full screen). The key insight is that mouse coordinates are inherently platform- and toolkit-dependent: they require querying the windowing system or GUI framework, and the program must translate screen-space coordinates into window-relative ones. Solutions should also note whether the queried window may be one created externally by another process.

## Task Requirements
- Get the current position of the mouse cursor.
- Report the coordinates relative to the active window, not the screen.
- Specify whether the window in question may be externally created (owned by another application).

## Language Coverage
72 languages implement this task, reflecting that nearly every GUI-capable platform exposes cursor coordinates through its windowing API or toolkit. Representative implementations include C, C++, C#, Java, JavaScript, Python, Ruby, Rust, Go, Tcl, and AutoHotkey; the page also lists many environments where the task is impossible (e.g., AWK, UNIX Shell, PHP) because they lack a windowing concept.

## Connections
- [[GraphicalUserInterface]] — the task operates within a GUI windowing context
- [[EventDrivenProgramming]] — pointer position is typically read from input/event systems
- [[CoordinateSystems]] — requires translating screen-space to window-relative coordinates
- [[PlatformAbstraction]] — implementation depends heavily on OS/toolkit APIs

## Contradictions
- None — reference task page.
