---
title: "Video display modes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, hardware]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Video_display_modes
---

## Summary
This task asks the programmer to demonstrate how to switch the video display mode from within the language, along with a brief description of the modes the platform supports. The key insight is that "video mode" is a hardware/OS-level concept (resolution, color depth, text vs. graphics) rather than a portable language feature, so solutions vary wildly: retro platforms set a hardware register or call a BIOS interrupt, while modern systems query a display API or simply note that the concept does not apply.

## Task Requirements
- Demonstrate how to switch between video display modes within the language.
- Provide a brief description of the supported video modes (e.g., resolution, text/graphics, color depth).

## Language Coverage
37 languages implement this task, dominated by retro and assembly platforms where direct video-mode control is natural. Representative implementations include 6502 Assembly, 8086 Assembly, ARM Assembly, Applesoft BASIC, Commodore BASIC, GW-BASIC, QBasic, FreeBASIC, Delphi, and XPL0, with modern languages such as Go, Java, Python, Lua, Perl, and Raku also appearing (often by querying the OS or reporting limited support).

## Connections
- [[ComputerGraphics]] — modes define resolution and color depth for drawing
- [[BIOSInterrupt]] — x86 mode switching via INT 10h on DOS-era platforms
- [[HardwareRegisters]] — retro systems set video modes by writing to chip registers
- [[TextMode]] — the alternative to graphics modes for character-cell displays

## Contradictions
- None — reference task page.
