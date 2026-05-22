---
title: "top Command"
type: concept
tags: [unix, system-info, process]
sources: [dis-app2-16-sysinfo]
last_updated: 2026-05-18
---

# `top` Command

**`top`** is the canonical Unix interactive process viewer — *"provides dynamic summary information about the state of the system"* ([[dis-app2-16-sysinfo|DIS App 2.16]]). Refreshes once per second, showing the most CPU-/memory-hungry processes plus aggregate system metrics.

## Header summary

- Load averages (1, 5, 15 minute).
- Total / running / sleeping / stopped / zombie process counts.
- Aggregate `%Cpu(s)` split into `us` (user), `sy` (system), `ni` (nice), `id` (idle), `wa` (I/O wait), `hi`/`si` (hardware/software interrupts), `st` (steal).
- Memory: total / free / used / buff/cache.

## Process table columns

| Col | Meaning |
|---|---|
| PID | [[ProcessID]] |
| USER | Owning user |
| PR / NI | Priority / nice value |
| VIRT / RES / SHR | Virtual / resident / shared memory |
| S | State (R running, S sleeping, D uninterruptible, Z zombie, T stopped) |
| %CPU / %MEM | Resource share |
| TIME+ | Cumulative CPU time |
| COMMAND | Process name |

## Interactive keys

- `q` quit, `h` help, `k` kill (prompts for PID + signal).
- `M` sort by memory, `P` sort by CPU.
- `1` show per-core CPU breakdown.

## `htop` — the friendlier alternative

`htop` adds color, mouse support, scrollable process list, and tree view (`F5`). Same data, better UX.

## Connections

- [[ProcFS]] — `top` reads `/proc/<PID>/stat` for every process.
- [[Ps]] — snapshot equivalent; `top` is the live view.
- [[ProcessID]] — the row index.
- [[OperatingSystem]] — exposes the data `top` displays.
- [[dis-app2-16-sysinfo]] — source.
