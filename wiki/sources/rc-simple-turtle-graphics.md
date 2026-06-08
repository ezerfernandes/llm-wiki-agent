---
title: "Simple turtle graphics (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, turtle-graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Simple_turtle_graphics
---

## Summary
This task asks the programmer to use turtle graphics (a relative pen-based drawing model driven by forward/turn commands) to render two figures. The first is the classic "house" — a square with a triangle roof — inspired by Seymour Papert's *Mindstorms*. The second is a bar chart drawn from a list of non-negative numbers, scaled to fit exactly within a square of a given size. The key constraint is that each drawing function must leave the turtle's position and heading unchanged from before it ran, encouraging clean, composable subroutines.

## Task Requirements
- Write a function/subroutine that draws a house of a specified size: a square body with a triangular roof, optionally embellished with doors and windows.
- Write a function/subroutine that takes a list of non-negative numbers and draws a bar chart, scaled to fit exactly in a square of a specified size (the enclosing square need not be drawn).
- Both functions must restore the turtle to its original location and heading after executing.

## Language Coverage
20 languages implement this task, spanning dedicated turtle environments and general-purpose languages with graphics libraries. Representative implementations include Logo (the language that popularized turtle graphics), Python, Java, Go, Julia, Perl, Raku, Wren, FreeBASIC, and J.

## Connections
- [[TurtleGraphics]] — the core relative-movement drawing paradigm the task is built on
- [[Logo]] — the educational language that originated turtle graphics
- [[ComputerGraphics]] — the broader rendering domain this task exercises
- [[Subroutines]] — the task's restore-state requirement emphasizes composable, side-effect-free procedures

## Contradictions
- None — reference task page.
