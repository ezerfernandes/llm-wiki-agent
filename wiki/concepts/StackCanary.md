---
title: "Stack Canary"
type: concept
tags: [security, buffer-overflow, compiler-defense, mitigation, stack]
sources: [dis-7-10-x86-64-buffer-overflow]
last_updated: 2026-05-17
---

# Stack Canary

A **stack canary** is a [[CCompiler|compiler]]-inserted **guard value** placed in the [[StackFrame|stack frame]] between local buffers and the saved [[FramePointer|`%rbp`]] / return address. Before the function returns, the prologue's canary value is compared against a known-good copy held in non-writable memory — a mismatch indicates a [[StackSmashing|stack-smashing]] overflow has corrupted intervening memory, and the program is aborted **before** the corrupted return address reaches [[RetInstruction|`retq`]]. Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] of [[DiveIntoSystems]]: *"a guard value in nonwriteable memory detecting stack corruption."*

The name comes from the *canary in a coal mine* — a sacrificial sentinel that dies first to warn of danger.

## Mechanism

```
high addr  ┌─────────────────────────┐
           │   return address        │
           ├─────────────────────────┤
           │   saved %rbp            │
           ├─────────────────────────┤
           │   CANARY VALUE          │  ← inserted by compiler
           ├─────────────────────────┤
           │   local variables       │
           ├─────────────────────────┤
           │   char buf[N]           │
low addr   └─────────────────────────┘
```

A linear [[BufferOverflow|buffer overflow]] writing past `buf` toward the return address **must** cross the canary slot — the overflow either preserves the canary (it was a benign write) or modifies it (an exploit attempt). The epilogue compares the in-frame canary against the reference copy and calls `__stack_chk_fail` on mismatch.

## In GCC

Enabled by `-fstack-protector` (only functions with large buffers) or `-fstack-protector-strong` / `-fstack-protector-all` (broader coverage). Most modern Linux distributions ship binaries built with `-fstack-protector-strong` by default.

## Canary value choices

- **Random canary** — per-process random value chosen at process start, stored in [[ThreadLocalStorage|TLS]]. The dominant production form. Attacker must leak the canary to reproduce it.
- **Terminator canary** — fixed byte pattern containing string terminators (`\0`, `\n`, `\xff`) that defeat the string-copy class of overflow (which would stop at those bytes).
- **NULL canary** — single `\0` byte, defeats string-copy overflows specifically.

## Bypass techniques

Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]], canaries are **not unbypassable**:

- **Canary value leak.** A separate vulnerability (format-string bug, info-leak primitive) reveals the canary; the attacker writes the original value back into the canary slot during the overflow, defeating the check.
- **Brute force on forking servers.** A child process inherits the parent's canary; an attacker can guess one byte at a time, observing crash-or-not, in $256 \times 8 = 2048$ tries instead of $2^{64}$.
- **Targeted overwrites that skip the canary.** Bugs that write to a specific offset (rather than a contiguous overflow) — e.g., indexed writes through an attacker-controlled index — bypass the canary entirely.
- **Non-contiguous corruption.** [[HeapOverflow|Heap overflows]] and [[FormatStringVulnerability|format-string bugs]] often don't touch the canary slot.

## Position in the defense stack

Per [[BufferOverflow]]'s defense list, stack canaries are **defense #2** (after *don't use unbounded functions*). They make the *simple linear-overflow stack-smashing* exploit much harder; combined with [[ExecutableSpaceProtection|NX]] and [[AddressSpaceLayoutRandomization|ASLR]], they raise the bar dramatically. None of the three is sufficient alone; together they form **defense in depth**.

## Sources

- [[dis-7-10-x86-64-buffer-overflow]] — Ch 7.10 introduces canaries as *"a guard value in nonwriteable memory detecting stack corruption"* and names attacker-replacement as the bypass technique.
