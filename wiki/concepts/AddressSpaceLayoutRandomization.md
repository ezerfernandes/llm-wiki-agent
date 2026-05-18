---
title: "Address Space Layout Randomization (ASLR)"
type: concept
tags: [security, buffer-overflow, operating-system, mitigation, memory-layout]
sources: [dis-7-10-x86-64-buffer-overflow]
last_updated: 2026-05-17
---

# Address Space Layout Randomization (ASLR)

**Address Space Layout Randomization (ASLR)** is the [[OperatingSystem|OS]]-level mitigation that **randomizes the base addresses** of a process's memory regions — [[StackSection|stack]], [[HeapSection|heap]], shared libraries, and (with PIE / [[PositionIndependentCode|position-independent code]]) the executable's own code — at process start. Without ASLR, an attacker constructing a [[StackSmashing|stack-smashing]] payload can hardcode the target address of injected shellcode or an existing libc function; with ASLR, those addresses change every run, so a payload that worked yesterday fails today.

Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] of [[DiveIntoSystems]] (under the name *"stack randomization"*): the [[OperatingSystem|OS]] *"allocates random stack starting addresses,"* preventing fixed-address assumptions across runs and across machines.

## What gets randomized

A modern Linux process with full ASLR + PIE randomizes:

- **Stack base** — different `%rsp` value at `main` entry every run.
- **[[HeapSection|Heap]] base** — `brk` / `mmap` arena placement.
- **Shared libraries** ([[Libc|libc]], libpthread, etc.) — loaded at a randomized `mmap` slot.
- **The main executable itself** — only when built as a [[PositionIndependentCode|position-independent executable (PIE)]]. Without PIE, `.text` / `.data` are at fixed addresses even on an ASLR system.
- **`vdso` and `vsyscall`** — kernel-injected pages.

## Effect on exploitation

- **Return-to-libc** attacks must first **leak** the libc base address to compute the offset of `system` or `execve`.
- **Stack-resident shellcode** targets must be approximated — the attacker no longer knows the exact byte where shellcode lives.
- **[[ReturnOrientedProgramming|ROP]] gadget chains** require gadget addresses; those addresses live in randomized libc / PIE-executable regions, so the attacker first needs an info leak.

ASLR converts most one-shot exploits into **two-stage exploits** (leak + execute), raising the difficulty bar significantly.

## Bypass techniques

Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] and the broader literature:

- **Brute force on low-entropy systems.** 32-bit Linux had only ~8 bits of stack entropy — a forking network service could be brute-forced in seconds. 64-bit systems have 28–30 bits and are much harder to brute-force.
- **NOP sled.** An attacker pads injected shellcode with a long run of NOP instructions; landing anywhere in the sled flows down to the real payload. Reduces the precision required to roughly $\log_2(\text{sled length})$ bits.
- **Information leak.** A separate vulnerability — format-string bug, out-of-bounds read, side channel — reveals the randomized base, defeating ASLR for that process.
- **Non-randomized regions.** Without PIE, the main executable's `.text` is at a fixed address — gadgets from the executable itself work even on an ASLR system. (One of the major reasons modern distributions ship PIE by default.)
- **Fork-based brute force.** Forked children inherit the parent's randomization — same as the [[StackCanary|canary]]-bypass case.

## ASLR + companions

ASLR is most effective combined with the other two defenses on [[BufferOverflow]]'s defense stack:

- **[[ExecutableSpaceProtection|NX / DEP]]** — forces the attacker into [[ReturnOrientedProgramming|ROP]], which needs gadget addresses, which ASLR randomizes.
- **[[StackCanary|Stack canaries]]** — detect the contiguous overflow before it lands, regardless of where it would have jumped.

Together they require the attacker to chain **at least three primitives**: a write (to overflow), a leak (to defeat ASLR), and gadget chains (to defeat NX).

## Sources

- [[dis-7-10-x86-64-buffer-overflow]] — Ch 7.10 introduces stack randomization as preventing fixed-address assumptions and names brute force / NOP sleds as defeats.
