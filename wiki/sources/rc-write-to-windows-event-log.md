---
title: "Write to Windows event log (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, system-programming, logging]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Write_to_Windows_event_log
---

## Summary
This task asks the programmer to write a script's status message into the Windows Event Log, the centralized logging facility used by the Windows operating system. The key insight is that most solutions delegate to the built-in `eventcreate` command or invoke Windows APIs (e.g. `ReportEvent`) rather than reimplementing the logging subsystem, so the challenge is mainly about correctly shelling out or binding to the platform-specific interface.

## Task Requirements
- Write a status message from a script into the Windows Event Log.
- Use the appropriate Windows mechanism (typically the `eventcreate` utility, WMI, or the Win32 event logging API).
- Specify event details such as type/severity, source, event ID, and the message text.

## Language Coverage
36 languages implement this task, showing broad coverage given its platform-specific nature; many simply wrap the `eventcreate` command. Representative implementations include C, C#, C++, Go, Java, Python, Perl, PowerShell, Ruby, Rust, Tcl, and VBScript.

## Connections
- [[WindowsEventLog]] — the OS subsystem being written to
- [[SystemLogging]] — the general practice this task exemplifies
- [[ShellCommandInvocation]] — most solutions shell out to `eventcreate`
- [[Win32API]] — native solutions call `ReportEvent` and related functions

## Contradictions
- None — reference task page.
