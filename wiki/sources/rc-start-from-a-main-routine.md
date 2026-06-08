---
title: "Start from a main routine (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, program-structure, event-driven]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Start_from_a_main_routine
---

## Summary
This task asks the programmer to force an application to begin execution in a conventional main procedure rather than dropping into an event-driven loop or an open GUI window at startup. Some languages (notably Gambas and Visual Basic) default to launching with a waiting window, so the task is to show the trickery needed to override that and run a startup routine instead. The key insight is that program entry points are language- and environment-specific, and event-driven runtimes may need explicit configuration to expose a procedural main.

## Task Requirements
- Demonstrate the steps that cause the application to run a main procedure at startup instead of an event-driven window.
- Languages that always run from `main()` may be omitted, since they already satisfy the requirement implicitly.

## Language Coverage
57 languages implement this task. Coverage is broad and skews toward BASIC dialects and event-driven environments where the issue actually arises; representative entries include Visual Basic, Gambas, FreeBASIC, Python, Go, Ada, Perl, Racket, Tcl, and Wren.

## Connections
- [[ProgramEntryPoint]] — the language-defined point where execution begins
- [[EventDrivenProgramming]] — the startup model this task works around
- [[GuiApplication]] — the windowed default mode being overridden
- [[ProgramStructure]] — how source is organized around an entry routine

## Contradictions
- None — reference task page.
