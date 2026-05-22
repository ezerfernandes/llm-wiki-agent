---
title: "/sys Filesystem"
type: concept
tags: [unix, kernel, linux, system-info]
sources: [dis-app2-16-sysinfo]
last_updated: 2026-05-18
---

# `/sys` Filesystem

`/sys` is a Linux pseudo-filesystem (introduced with the **2.6 kernel**) that exposes the kernel's **device and driver model** as a directory tree. Like [[ProcFS|`/proc`]], files don't store data; they're synthesized on read.

## What lives here

- `/sys/class/` — devices grouped by class: `net/`, `block/`, `power_supply/`, etc.
- `/sys/devices/` — physical bus/device topology.
- `/sys/bus/` — devices grouped by bus type (pci, usb, i2c).
- `/sys/module/` — loaded kernel modules.
- `/sys/kernel/` — kernel-wide knobs and counters.

## Differences from `/proc`

| | `/proc` | `/sys` |
|---|---|---|
| Vintage | Original Unix concept | Linux 2.6 (2003) |
| Focus | Processes + global state | Devices + driver model |
| Writability | Some files writable (`/proc/sys/...`) | Many files writable (tune devices) |

## Tools that consume `/sys`

`lshw`, `lsusb`, `lspci`, `udevadm` — all walk `/sys` to enumerate hardware.

## Connections

- [[ProcFS]] — sibling pseudo-filesystem.
- [[Lshw]] — `/sys` consumer.
- [[OperatingSystem]] — kernel-side state being exposed.
- [[dis-app2-16-sysinfo]] — source.
