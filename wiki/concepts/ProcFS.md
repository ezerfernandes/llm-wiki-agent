---
title: "/proc Filesystem"
type: concept
tags: [unix, kernel, linux, system-info]
sources: [dis-app2-16-sysinfo]
last_updated: 2026-05-18
---

# `/proc` Filesystem

`/proc` is a Linux **pseudo-filesystem** — files in `/proc` don't store data on disk; they're synthesized by the kernel on demand and expose [[OperatingSystem|OS]] state through normal file-read APIs. *"Don't store actual data but provide interfaces to OS information"* ([[dis-app2-16-sysinfo|DIS App 2.16]]).

## System-wide files

| Path | Contents |
|---|---|
| `/proc/cpuinfo` | Per-core CPU model, MHz, cache size, features. |
| `/proc/meminfo` | Total / free / available memory, swap, buffers, caches. |
| `/proc/stat` | Aggregate CPU usage, context switches, interrupts since boot. |
| `/proc/loadavg` | 1/5/15-minute load averages. |
| `/proc/uptime` | Seconds since boot. |
| `/proc/version` | Kernel version. |
| `/proc/mounts` | Currently mounted filesystems. |
| `/proc/net/` | Per-protocol network stats (`tcp`, `udp`, `dev`). |

## Per-process directories

`/proc/<PID>/` exposes one directory per running [[Process]]:

| Path | Contents |
|---|---|
| `/proc/<PID>/status` | Human-readable state, memory, threads, context switches. |
| `/proc/<PID>/cmdline` | Process's argv (NUL-separated). |
| `/proc/<PID>/maps` | Memory mappings ([[VirtualMemory]] layout). |
| `/proc/<PID>/fd/` | Open [[FileDescriptor|file descriptors]] (symlinks to files/pipes/sockets). |
| `/proc/<PID>/environ` | Environment variables (NUL-separated). |
| `/proc/<PID>/stat` | Machine-readable counterpart of `status`. |

## How tools use it

[[TopCommand|`top`]], [[Ps|`ps`]], `free`, `uptime`, `lscpu` are all thin wrappers that read `/proc` + format the result.

## Connections

- [[SysFS]] — sibling pseudo-filesystem (device tree, kernel objects).
- [[TopCommand]] / [[Ps]] — direct consumers.
- [[Lscpu]] — formats `/proc/cpuinfo`.
- [[ProcessID]] — the per-PID directory index.
- [[VirtualMemory]] / [[OperatingSystem]] — the state being exposed.
- [[dis-app2-16-sysinfo]] — source.
