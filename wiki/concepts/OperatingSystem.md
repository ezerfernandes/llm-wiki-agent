---
title: "Operating System"
type: concept
tags: [systems, os, software, abstraction]
sources: [dis-0-introduction]
last_updated: 2026-05-17
---

# Operating System

The **operating system (OS)** is the software layer that mediates between user programs and physical hardware, turning bare [[ComputerHardware|hardware]] into a usable [[ComputerSystem|computer system]] ([[dis-0-introduction]]).

## The OS-as-mediator view

Per [[DiveIntoSystems]]'s Ch 0, the OS *"implements abstractions, policies, and mechanisms to ensure that multiple programs can simultaneously run"* on a single physical machine. The three responsibilities decompose as:

| Responsibility | What it means | Example |
|---|---|---|
| [[Abstraction|Abstractions]] | Virtualized resource views | Process per program; virtual address space per process; file as a stream of bytes. |
| Policies | Rules for sharing | Scheduling priority; page-replacement algorithm; file permissions. |
| Mechanisms | Implementation enforcing the policy | Context switch; page table walk; syscall dispatch. |

Without these three the hardware exists but is **not** a [[ComputerSystem|computer system]] by this book's definition.

## What the OS makes possible

- **Multiprogramming** — multiple processes share a single CPU.
- **Isolation** — one program's bug or compromise does not corrupt another.
- **Resource management** — finite CPU time, RAM, disk, and I/O bandwidth are arbitrated.
- **Reprogrammability** — new software can be installed and run on top of the same hardware.

## Contrast with the embedded world

[[TheEmbeddedRustBook]]'s [[HardwareAbstractionLayer]] page notes that the *Wikipedia* HAL definition presumes an OS — the HAL is exposed as a syscall surface. Embedded firmware images typically run with **no OS at all**, and so use a different (trait-based) HAL flavor. The OS and the embedded-`no_std` worlds are duals, not synonyms.

## Connections

- [[ComputerSystem]] — the OS is what makes hardware into one.
- [[ComputerHardware]] — what the OS sits on top of.
- [[Abstraction]] — the OS's primary product.
- [[HardwareAbstractionLayer]] — the OS-syscall flavor of HAL; the embedded world's dual.
- [[EmbeddedSystems]] / [[Microcontroller]] — typical no-OS world.
- [[dis-0-introduction]] — source.
