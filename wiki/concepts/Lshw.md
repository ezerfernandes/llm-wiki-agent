---
title: "lshw"
type: concept
tags: [unix, system-info]
sources: [dis-app2-16-sysinfo]
last_updated: 2026-05-18
---

# `lshw`

`lshw` ("list hardware") walks [[SysFS|`/sys`]] + [[ProcFS|`/proc`]] and prints a tree describing every hardware unit the kernel has detected — CPU, RAM, storage, network, display, USB, audio, etc.

```bash
sudo lshw -short      # one-line-per-device table
sudo lshw -class disk # filter to disks
sudo lshw -html       # HTML report
```

Typically run with `sudo` to access privileged details (firmware versions, serial numbers).

## Connections

- [[SysFS]] / [[ProcFS]] — backing data sources.
- [[Lscpu]] — narrower CPU-only sibling.
- [[dis-app2-16-sysinfo]] — source.
