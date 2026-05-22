---
title: "Dive into Systems — App 2.16 System Information"
type: source
tags: [book, unix, system-info, proc]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/sysinfo.html
---

## Summary
Sixteenth and **final** subchapter of [[DiveIntoSystems]] Appendix 2 *Using Unix*. Codifies system-state inspection tools: the dynamic [[TopCommand|`top`]] / `htop` process viewers, the [[ProcFS|`/proc`]] and [[SysFS|`/sys`]] pseudo-filesystems that expose [[OperatingSystem|OS]] state as readable files, and convenience utilities (`lscpu`, `lsmem`, `lshw`) that summarize the same data. **Closes Appendix 2 and the entire [[DiveIntoSystems]] textbook.**

## Key Claims
- *"Running `top` or `htop` at the command line provides dynamic summary information about the state of the system"* — live CPU / memory / process view, refreshes every second.
- [[ProcFS|`/proc`]] and [[SysFS|`/sys`]] are pseudo-filesystems — they *"don't store actual data but provide interfaces to OS information."*
- `/proc/<PID>/status` shows per-process memory, context switches, state.
- `cat /proc/meminfo`, `cat /proc/cpuinfo`, `cat /proc/stat` expose system-wide resource data.
- `lscpu` / `lsmem` / `lshw` provide human-readable summaries of the same `/proc`+`/sys` data.

## Connections
- [[TopCommand]] — minted here.
- [[ProcFS]] / [[SysFS]] — minted here.
- [[Lscpu]] / [[Lshw]] — convenience wrappers minted here.
- [[OperatingSystem]] — the system whose state these tools expose; full coverage in Ch 13.
- [[ProcessID]] — the PID used to index `/proc/<PID>/`.
- [[DiveIntoSystems]] — Appendix 2.16, **closes the textbook**.
