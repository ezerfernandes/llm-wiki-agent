---
title: "lscpu"
type: concept
tags: [unix, system-info]
sources: [dis-app2-16-sysinfo]
last_updated: 2026-05-18
---

# `lscpu`

`lscpu` formats the contents of [[ProcFS|`/proc/cpuinfo`]] and [[SysFS|`/sys/devices/system/cpu/`]] into a compact human-readable summary of CPU topology:

```
Architecture:        x86_64
CPU(s):              16
Thread(s) per core:  2
Core(s) per socket:  8
Socket(s):           1
Model name:          AMD Ryzen 7 5800X 8-Core Processor
CPU MHz:             3800.000
L1d cache:           32K
L1i cache:           32K
L2 cache:            512K
L3 cache:            32768K
```

Useful for [[MulticoreProcessor|multicore]] / [[HyperThreading|hyper-threading]] analysis — sockets × cores-per-socket × threads-per-core gives the total CPU count.

## Siblings

- `lsmem` — memory range topology.
- `lshw` — full hardware tree ([[SysFS]]-based).
- `lsusb` / `lspci` / `lsblk` — per-bus device enumeration.

## Connections

- [[ProcFS]] / [[SysFS]] — the underlying data sources.
- [[MulticoreProcessor]] / [[HyperThreading]] — concepts whose count `lscpu` exposes.
- [[TopCommand]] — sibling system-info tool.
- [[dis-app2-16-sysinfo]] — source.
