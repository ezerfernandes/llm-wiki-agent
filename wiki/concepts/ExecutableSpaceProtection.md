---
title: "Executable Space Protection (NX / DEP / W^X)"
type: concept
tags: [security, buffer-overflow, hardware-mitigation, memory-protection, page-table]
sources: [dis-7-10-x86-64-buffer-overflow]
last_updated: 2026-05-17
---

# Executable Space Protection (NX / DEP / W^X)

**Executable space protection** — also called **NX** (No-eXecute), **DEP** (Data Execution Prevention on Windows), or **W^X** (write-XOR-execute on BSDs) — is the hardware-assisted mitigation that marks memory pages as either **writable** *or* **executable**, never both. The [[StackSection|stack]] and [[HeapSection|heap]] are writable but **non-executable**; the `.text` segment is executable but **non-writable**. Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] of [[DiveIntoSystems]]: *"restricts code execution to specific memory regions."*

This defeats the classical *injected-shellcode* form of [[StackSmashing|stack smashing]] — the attacker can still write shellcode bytes into a stack buffer, but jumping to those bytes raises a page fault instead of executing them.

## Hardware mechanism

The NX bit is bit 63 of the [[PageTable|page-table entry]] on [[X86_64|x86-64]] (the "No-Execute" bit, introduced by AMD with AMD64; Intel calls it the "XD bit"). Set NX = 1 → fetching an instruction from that page raises a fault. The [[OperatingSystem|OS]] sets NX = 1 on stack and heap pages by default.

[[ARM|ARMv8]] has an equivalent **XN** (eXecute Never) bit in its translation table entries.

## What it defeats

- **Stack shellcode injection** — the original [[StackSmashing|stack-smashing]] payload (write shellcode to buffer, point return address at buffer). Defeated entirely.
- **Heap shellcode injection** — analogous heap-buffer-overflow exploits. Defeated entirely.

## What it does **not** defeat

- **[[ReturnOrientedProgramming|Return-oriented programming (ROP)]]** — instead of injecting new instructions, the attacker **chains existing executable instructions** (gadgets) from `.text` / libc. Every gadget address points to *already-executable* memory, so NX is irrelevant. Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]]: ROP is the *"technique cherry-picking instructions across executable regions."*
- **Return-to-libc** — predecessor of ROP; the attacker returns into a single libc function (typically `system("/bin/sh")`). Still uses existing executable memory.
- **JIT spraying** — exploits a JIT compiler (V8, JVM) that legitimately needs writable→executable transitions; the attacker shapes the JIT's output to contain useful instruction sequences.
- **Bugs that achieve writes through legitimate code paths** — e.g., format-string bugs, arbitrary-write primitives that don't need to execute attacker-supplied bytes.

## Why ROP is the canonical NX bypass

When NX prevents shellcode, the attacker switches strategy: instead of *writing new instructions*, **find sequences already present in the binary** that perform useful operations and end in `retq`. Chain these "gadgets" by placing a list of their addresses at the saved return address and beyond — each `retq` advances to the next gadget. The first gadget executes, returns to the next, and so on, building up arbitrary computation from pre-existing fragments. See [[ReturnOrientedProgramming]].

## Position in the defense stack

Per [[BufferOverflow]]'s defense list, NX is **defense #3** (after *don't use unbounded functions* and *stack canaries*). Combined with [[AddressSpaceLayoutRandomization|ASLR]], it forces attackers into a *leak + ROP* pattern that requires substantially more setup. None of these defenses is sufficient alone; the **defense-in-depth** combination raises the bar dramatically.

## Compiler / OS support

- **Linux**: enabled by default since the early 2000s when supported by hardware. The `execstack` and `noexec` flags on ELF sections / mount options control finer policy.
- **Windows**: DEP since XP SP2, originally opt-in, now default-on.
- **macOS** / **FreeBSD**: enabled by default.
- **Older 32-bit x86** lacked the NX bit until PAE; pre-PAE software workarounds (Exec Shield, PaX) emulated NX via segment limits.

## Sources

- [[dis-7-10-x86-64-buffer-overflow]] — Ch 7.10 introduces executable-memory restriction and names [[ReturnOrientedProgramming|ROP]] as the bypass.
