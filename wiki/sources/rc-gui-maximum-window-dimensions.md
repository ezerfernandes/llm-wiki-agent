---
title: "GUI/Maximum window dimensions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/GUI/Maximum_window_dimensions
---

## Summary
This task asks the programmer to determine the maximum height and width, in pixels, of a window that can fit within the physical display area of the screen without scrolling. The key insight is that this is the usable screen size — not the total desktop area — minus any space taken by window decorations and menubars or panels.

## Task Requirements
- Compute the maximum usable display area (height and width in pixels) for a maximized window without scrolling.
- Base the result on the physical screen display area, not the (potentially larger) total desktop area.
- Subtract adjustments for window decorations and menubars.
- For multiple monitors, report the usable area of the monitor that would display the window.
- For tiling window managers, report the maximum permissible window size, accounting for areas occupied by desktop bars.

## Language Coverage
48 languages implement this task, spanning native GUI toolkit bindings and platform APIs. Representative examples include C, C#, Java, Python, Go, Kotlin, Perl, Tcl, Haskell, and Mathematica, with strong representation from BASIC dialects such as FreeBASIC, PureBasic, and Visual Basic .NET.

## Connections
- [[GraphicalUserInterface]] — querying display and window geometry through a GUI toolkit
- [[ScreenResolution]] — the physical pixel dimensions of the display
- [[WindowManager]] — decorations, menubars, and tiling rules that reduce usable area
- [[PlatformAPI]] — OS-level calls used to retrieve screen metrics

## Contradictions
- None — reference task page.
