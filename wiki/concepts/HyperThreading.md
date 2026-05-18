---
title: "Hyper-Threading"
type: concept
tags: [computer-architecture, cpu, parallelism, multithreading, intel]
sources: [dis-5-9-modern]
last_updated: 2026-05-17
---

# Hyper-Threading

**Hyper-Threading** is Intel's commercial [[HardwareMultithreading|hardware-multithreading]] technology, exposing **two logical threads per physical core** to the operating system. [[dis-5-9-modern|Ch 5.9]] makes an explicit pedagogical point about it: **Hyper-Threading implements *interleaved* multithreading, not true [[SimultaneousMultithreading|simultaneous multithreading (SMT)]]** — i.e. it does not issue instructions from multiple threads in the same cycle.

## Why the distinction matters

A user reading marketing copy could conflate "two threads per core" with "two-way SMT." Ch 5.9's classification:

| Implementation | Threads per cycle | Max IPC |
|---|---|---|
| Intel **Hyper-Threading** (interleaved) | **1** (alternating) | 1 |
| IBM Power 9 **8-way SMT** | **up to 8** | **> 1 — up to 8 per core** |

Hyper-Threading still helps performance — by hiding latency and filling pipeline slots wasted by stalls — but it does **not** push per-core IPC above 1 the way true SMT does.

## Scope note

Ch 5.9 introduces Hyper-Threading specifically to anchor the classification of [[HardwareMultithreading|hardware-multithreading]] variants. The page does not get into microarchitectural details, generational variation across Intel families, or the security implications of shared microarchitectural state between Hyper-Threaded siblings.

## Connections

- [[HardwareMultithreading]] — the family Hyper-Threading belongs to.
- [[SimultaneousMultithreading]] — the **other** family Hyper-Threading is often (incorrectly) conflated with.
- [[Superscalar]] — what SMT requires that interleaved multithreading does not.
- [[Intel]] — the vendor (per existing wiki convention; no entity page exists yet — named-reference only).
- [[CPU]] — the device class.
- [[dis-5-9-modern]] — primary source.
