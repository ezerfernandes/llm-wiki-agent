---
title: "Joystick position (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, hardware-io, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Joystick_position
---

## Summary
This task asks the programmer to read the position of the first (calibrated) joystick and render it as a crosshair on the display. A centred stick puts the crosshair at screen centre; pushing the stick in any direction moves the crosshair proportionally toward the corresponding screen edge, which represents maximum extent. The program loops continuously, redrawing the crosshair and showing currently pressed buttons until terminated. The key wrinkle is mapping a 2D analog axis range onto screen coordinates, with digital (non-analog) joysticks treated as always-at-full-extent.

## Task Requirements
- Read the position of the first joystick (calibration assumed); optionally offer joystick selection.
- Draw a crosshair that tracks the stick: left/right axis maps to horizontal position, forward/back maps to vertical position.
- Centred stick yields a centred crosshair; full deflection moves the crosshair to the matching screen edge.
- Crosshair may be graphical or an ASCII `+` symbol on a terminal.
- Show pressed pushbuttons as an alphanumeric sequence (e.g. buttons 1, 4, 10 shown as "1 4 A") in a reserved status area.
- Continuously redraw position and button state in a loop until terminated.
- Digital joysticks with no extent data should register as full-extent movement.

## Language Coverage
26 languages implement this task, skewing toward platforms with direct hardware or game-input access (many retro BASIC dialects plus a few systems languages). Representative solutions include C, Go, Haskell, OCaml, Julia, Python, Raku, Tcl, Wren, BBC BASIC, FreeBASIC, and Delphi.

## Connections
- [[HumanInterfaceDevices]] — joystick is an HID input device polled for axes and buttons
- [[EventLoop]] — continuous poll-and-redraw loop is core to the task
- [[CoordinateMapping]] — scaling analog axis ranges onto screen pixel/character coordinates
- [[Bitmask]] — pressed-button state is typically read as a bitfield decoded into a button list

## Contradictions
- None — reference task page.
