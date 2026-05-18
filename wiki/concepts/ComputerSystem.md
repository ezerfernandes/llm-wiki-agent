---
title: "Computer System"
type: concept
tags: [systems, architecture, definition]
sources: [dis-0-introduction]
last_updated: 2026-05-17
---

# Computer System

A **computer system** is the union of [[ComputerHardware|computer hardware]] (CPU, RAM, I/O ports, secondary storage) and an [[OperatingSystem|operating system]] that together provide a **general-purpose, reprogrammable** computing environment ([[dis-0-introduction]]).

## The hardware + OS definition

[[DiveIntoSystems]]'s opening definition is restrictive on purpose:

- Raw [[ComputerHardware|hardware]] alone is **not** a computer system — without an OS there is no abstraction layer, no resource management, no way to run multiple programs.
- A device with a processor and memory but no OS (e.g. a four-function calculator, a bare [[Microcontroller]] running a single firmware image) is likewise **not** a computer system by this definition.
- The qualifying criteria are **general-purpose** (capable of running arbitrary programs) and **reprogrammable** (new software can be installed and run after manufacture).

This is the wiki's first formal definition of "computer system." Contrast with the [[EmbeddedSystems|embedded-systems]] world covered in [[TheEmbeddedRustBook]], where the *absence* of an OS is the defining feature.

## What the OS contributes

The OS is what turns hardware into a usable system. It provides:

- [[Abstraction|Abstractions]] — virtualized views of physical resources (processes over CPUs, virtual memory over RAM, files over disks).
- **Policies** — decisions about *how* to share resources (scheduling, page replacement, file permissions).
- **Mechanisms** — implementations that enforce those policies (context switches, page tables, syscalls).

Together these let *"multiple programs simultaneously run"* on shared physical hardware ([[dis-0-introduction]]).

## Form factors

Modern computer systems span a wide range of physical scales — desktops, laptops, [[SingleBoardComputer|single-board computers]] like the [[RaspberryPi]], smartphone-class [[SystemOnAChip|systems-on-a-chip]] — but virtually all share two features today: an [[OperatingSystem|OS]] and a [[MulticoreProcessor|multicore CPU]].

## Connections

- [[ComputerHardware]] — the physical half of the definition.
- [[OperatingSystem]] — the software half.
- [[Abstraction]] — what the OS provides over raw hardware.
- [[MulticoreProcessor]] — the default CPU architecture for modern systems.
- [[SystemOnAChip]] / [[SingleBoardComputer]] / [[RaspberryPi]] — contemporary form factors.
- [[EmbeddedSystems]] / [[Microcontroller]] — the **non**-computer-system world by this definition.
- [[HardwareAbstractionLayer]] — the embedded-Rust-world dual; OS-syscall HAL vs. trait-HAL.
- [[dis-0-introduction]] — source.
