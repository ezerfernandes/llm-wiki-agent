---
title: "Stored-Program Principle"
type: concept
tags: [computer-architecture, foundational]
sources: [dis-5-1-history, dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Stored-Program Principle

The architectural principle that **program instructions and data both reside in the same internal [[RAM|memory]]**, addressed uniformly, and fetched into the [[CPU]] for execution. Codified by [[JohnVonNeumann|von Neumann]]'s 1945 [[EDVAC]] paper and the defining feature of the [[VonNeumannArchitecture|von Neumann architecture]].

## Why it matters

Before stored-program machines, *programming* meant **physically reconfiguring the computer** — rewiring plugboards (the original [[ENIAC]]) or setting mechanical switches. The stored-program shift made *programs* into **data** that could be:

- Loaded from external storage
- Modified by other programs (the foundation of [[Compiler|compilers]], [[OperatingSystem|operating systems]], and [[JustInTimeCompilation|JIT compilation]])
- Treated as first-class values for [[Metaprogramming|metaprogramming]]
- Composed of [[Subroutine|subroutines]] that themselves live in addressable memory

Per [[dis-5-1-history|*Dive into Systems* Ch 5.1]], this principle is the single most important architectural inheritance of the 1930s–1940s computing convergence — the **structural difference** between *programmable* and *general-purpose programmable* computers.

## Operational restatement ([[dis-5-2-von-neumann|Ch 5.2]])

Ch 5.2 deepens the principle from *"both in memory"* to *"indistinguishable at every storage tier"*: *"there is no distinction between instructions and data in the von Neumann architecture."* This means **[[CpuRegister|registers]] hold either** — the same bit pattern can be an opcode-word during one [[FetchDecodeExecuteCycle|fetch phase]] and an integer operand during the next. The [[InstructionRegister|instruction register]] is just a register that happens to be wired to the [[ControlUnit|control unit]]'s decode logic.

## Independent discovery

[[AlanTuring]]'s 1946 [[AutomaticComputingEngine|ACE]] design at the [[NationalPhysicalLaboratory|UK NPL]] was a stored-program design developed roughly contemporaneously with [[JohnVonNeumann|von Neumann]]'s [[EDVAC]] paper — another instance of the *convergence-not-linear-progression* theme Ch 5.1 emphasizes.
