---
title: "Draw a clock (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, animation, real-time]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Draw_a_clock
---

## Summary
The task is to draw a working time-keeping device — a clock, stopwatch, hourglass, sundial, or similar — that visibly changes at least once per second and cycles on a regular interval. The display must be genuinely *drawn* (text-based ASCII or graphical), not merely a string of numbers printed to the terminal, and the seconds shown must agree with the system clock. The key insight is to drive updates with a proper timer, signal, or event mechanism rather than busy-polling the system clock, keeping the implementation simple and resource-friendly.

## Task Requirements
- Draw a time-keeping device that shows at least the seconds and cycles periodically (e.g. every minute or 30 seconds).
- The output must be drawn (text-based or graphical), not just numbers printed to a terminal.
- It need not be hyper-accurate, but the displayed seconds must agree with the system clock.
- Avoid being a CPU hog: use a timer/signal/event rather than polling the system timer in a busy loop.
- Keep the code simple, concise, and natural for the language.

## Language Coverage
73 languages implement this task, spanning text-based terminal renderers, GUI toolkits, and dedicated graphics or animation systems. Representative implementations include C, C++, C#, Java, JavaScript, Python, Haskell, Go, Rust, Processing, Lua, Tcl, and SVG.

## Connections
- [[Animation]] — the display must change every second, requiring frame/state updates over time.
- [[EventDrivenProgramming]] — the task explicitly favors timers, signals, and events over polling loops.
- [[RealTimeClock]] — output must stay synchronized with the system clock.
- [[ComputerGraphics]] — graphical implementations render clock faces, hands, or analog/digital displays.
- [[AsciiArt]] — text-based solutions draw the device using terminal characters.

## Contradictions
- None — reference task page.
