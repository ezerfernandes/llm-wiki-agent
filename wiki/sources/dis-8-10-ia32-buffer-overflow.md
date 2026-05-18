---
title: "Dive into Systems — Ch 8.10 Buffer Overflows (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, buffer-overflow, security, stack-smashing, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/buffer_overflow.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 8.10 of *[[DiveIntoSystems]]* — **tenth leaf** of Ch 8 *32-bit IA32 Assembly* and the **32-bit structural twin** of [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]], plus the **security payoff** of the whole Ch 8 tour. Inverts the [[CallStack|call-stack]] discipline from [[dis-8-5-ia32-functions|Ch 8.5]] / [[dis-8-6-ia32-recursion|Ch 8.6]] / [[dis-8-7-ia32-arrays|Ch 8.7]] — instead of *using* the saved-`%eip` / saved-`%ebp` / local-buffer frame to compute, an attacker *abuses* an unbounded write past a stack buffer to **overwrite the saved return address**, redirecting [[RetInstruction|`ret`]] to an attacker-chosen address. **Headline 32-vs-64 deltas**: (1) saved-return-address is a **4-byte saved-`%eip`** at `4(%ebp)` (vs 8-byte saved-`%rip` on Ch 7.10) — exploit payloads need 4-byte address strings (in [[LittleEndian|little-endian]] byte order) rather than 8-byte; (2) the buffer-to-saved-return-address distance is smaller because pointers are 4 bytes (so adjacent-stack stride is 4 bytes per word); (3) IA32 stack-write attack patterns work identically — `scanf("%s", buf)` with no length cap, `gets()`, `strcpy()` etc. — the C-language lack of bounds checking is ISA-independent. **Headline rules carry over unchanged**: (a) *"the C language does not perform automatic array bounds checking"* — the root cause; (b) [[LittleEndian|little-endian]] address byte order for payload construction; (c) **three defenses** — [[StackCanary|stack canaries]] (guard values between buffer and saved-return-address detected at function exit), [[AddressSpaceLayoutRandomization|ASLR]] (randomize stack base to defeat hardcoded payload addresses), and [[ExecutableSpaceProtection|NX / W^X]] (mark stack pages non-executable to prevent shellcode-on-stack execution); (d) **[[ReturnOrientedProgramming|ROP]]** as the bypass for NX — *"an attacker can cherry-pick instructions in executable regions and jump from instruction to instruction to build an exploit"*; (e) the prevention prescription: use length-specified safe functions (`scanf("%12s", buf)` instead of `scanf("%s", buf)`). **89th ingested DIS chapter — tenth leaf of Ch 8.** **No new concept pages** — reuses [[BufferOverflow]], [[StackSmashing]], [[ReturnAddressOverwrite]], [[StackCanary]], [[AddressSpaceLayoutRandomization]], [[ExecutableSpaceProtection]], [[ReturnOrientedProgramming]] from [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]].

## Key Claims

- **Root cause: C performs no bounds checking.** *"The C language does not perform automatic array bounds checking"* — unbounded writes (`scanf("%s")`, `gets()`, `strcpy()`) past a stack buffer's end corrupt adjacent stack data. The very *contiguity* that made stack frames efficient ([[dis-8-5-ia32-functions|Ch 8.5]]) becomes the attack vector.
- **[[ReturnAddressOverwrite|Return-address overwrite]] enables arbitrary control flow.** A write past a stack buffer can reach the **saved-`%eip`** at `4(%ebp)` of the current frame. When the function executes [[RetInstruction|`ret`]], the corrupted saved-`%eip` is popped into [[InstructionPointer|`%eip`]] — control flow now goes wherever the attacker wrote — e.g., the `endGame` function in [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]]'s worked example.
- **Control-flow hijacking, not code modification.** *"Attackers can force functions to execute in unintended sequences, changing program behavior without modifying code"* — the exploit changes only **data** (the saved-`%eip` slot on the stack) and exploits the existing instruction stream. This is what makes [[BufferOverflow|buffer overflows]] so insidious — no code-segment write is needed.
- **[[LittleEndian|Little-endian]] payload construction.** On IA32 (and x86-64), return-address bytes must be written in reverse byte order when constructing exploit payloads. A 4-byte target address `0x080484A1` is written as the byte sequence `0xA1 0x84 0x04 0x08` in the input buffer — *"return addresses must be written in reverse byte order when constructing exploits"*.
- **Three defenses, three attack-class bypasses.** (1) [[StackCanary|Stack canaries]] — guard values between buffer and saved-return-address, checked at function exit, abort on mismatch; defeats naive bulk-writes but not surgical canary-preserving overwrites. (2) [[AddressSpaceLayoutRandomization|ASLR]] — OS allocates stack at random base address per execution; defeats hardcoded-address payloads but not relative-offset gadgets. (3) [[ExecutableSpaceProtection|NX bit / W^X]] — stack pages marked non-executable; defeats shellcode-on-stack but not [[ReturnOrientedProgramming|ROP]] gadget chains that reuse existing executable instruction sequences.

## Key Quotes

> "The C language does not perform automatic array bounds checking." — the root-cause invariant that makes [[BufferOverflow|buffer overflows]] possible.

> "An attacker can 'cherry-pick' instructions in executable regions and jump from instruction to instruction to build an exploit." — the [[ReturnOrientedProgramming|ROP]] technique that bypasses [[ExecutableSpaceProtection|NX / W^X]].

## Connections

- [[DiveIntoSystems]] — book; **89th ingested chapter**, tenth leaf of Ch 8 *32-bit IA32 Assembly*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-7-10-x86-64-buffer-overflow]] — **structural twin** at [[X86_64|x86-64]] width; same attack mechanism, same three defenses, same ROP bypass — only the saved-return-address width differs (4 bytes vs 8 bytes).
- [[dis-8-9-ia32-structs]] — Ch 8.9; direct predecessor (data-layout chapter; Ch 8.10 weaponizes the stack-buffer layout).
- [[dis-8-5-ia32-functions]] / [[dis-8-6-ia32-recursion]] — the [[CallStack|call-stack]] discipline Ch 8.10 inverts.
- [[BufferOverflow]] — the core vulnerability class.
- [[StackSmashing]] — synonym for stack-buffer overflow leading to control-flow hijacking.
- [[ReturnAddressOverwrite]] — the mechanism that turns a buffer overflow into arbitrary code execution.
- [[StackCanary]] — defense 1: guard value before saved-return-address.
- [[AddressSpaceLayoutRandomization]] — defense 2: stack/heap base randomization.
- [[ExecutableSpaceProtection]] — defense 3: NX / W^X non-executable stack pages.
- [[ReturnOrientedProgramming]] — the ROP bypass that defeats NX by chaining existing executable instruction sequences.
- [[CallStack]] / [[StackFrame]] — the frames whose saved-`%eip` slot is the overwrite target.
- [[InstructionPointer]] — the `%eip` register whose value [[RetInstruction|`ret`]] restores from the (corrupted) saved slot.
- [[LittleEndian]] — the byte order of x86 / IA32 return addresses, dictating exploit payload byte sequence.
- [[CLanguage]] — the source of the unbounded-write primitive (`scanf("%s")`, `gets()`).
- [[IA32]] — the 32-bit ISA whose stack discipline is exploited.

## Contradictions

None. Ch 8.10 is a **consistent 32-bit re-presentation** of [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] — the attack mechanism, three-defense taxonomy, and ROP-as-NX-bypass framework are structurally identical; the only delta is the saved-return-address width (4 vs 8 bytes), which changes payload construction details but not the underlying vulnerability or defense architecture.
