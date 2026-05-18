---
title: "Dive into Systems — Ch 7.10 Buffer Overflows (x86-64)"
type: source
tags: [textbook, dive-into-systems, x86-64, assembly, security, buffer-overflow, stack-smashing, memory-safety]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/buffer_overflow.html
---

## Summary

**Tenth leaf** of Ch 7 *x86-64 Assembly* of [[DiveIntoSystems]] — the **security payoff** of the whole Ch 7 stack-discipline tour. Takes the [[CallStack|call-stack]] mechanics built up across [[dis-7-5-x86-64-functions|Ch 7.5]] ([[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] / [[StackFrame|stack frames]] / [[FramePointer|`%rbp`]] / [[StackPointer|`%rsp`]]) and the [[CArray|C array]] / [[CString|string]] vulnerabilities flagged in [[dis-1-5-arrays-strings|Ch 1.5]] / [[dis-2-6-strings|Ch 2.6]] and **fuses them into the canonical [[StackSmashing|stack-smashing]] exploit**: an unbounded `scanf("%s", buf)` writes past a 12-byte stack buffer, **overwrites the saved return address** at `8(%rbp)`, and on `retq` redirects [[InstructionPointer|`%rip`]] into attacker-chosen code. Walks the `secret` worked example (12-byte `buf` + an `endGame()` function the normal program never calls) through three phases — crash on oversized input, careful 48-byte payload (40 bytes of padding + 8-byte little-endian address `0x4006da`), and `retq` into `endGame`. Surveys three categories of defense — **programmer-level** ([[BoundsChecking|length-specifying functions]]: `fgets` / `scanf("%12s")` / [[Strncpy|`strncpy`]] / `strncat` / `snprintf`), **compiler / OS-level** ([[StackCanary|stack canaries]], [[AddressSpaceLayoutRandomization|address-space layout randomization]], [[ExecutableSpaceProtection|NX / DEP non-executable stack]]), and **why each is bypassable** ([[ReturnOrientedProgramming|ROP]] defeats NX; canaries can be overwritten with the original value; ASLR can be brute-forced or sidestepped by NOP-sled techniques). Closes with two historical case studies — the **1988 Morris Worm** (buffer overrun in the UNIX `fingerd` [[Daemon|daemon]]) and the **AOL Chat Wars** (AOL weaponizing a buffer overflow in its own AIM client as a Microsoft MMS protocol-conformance check). **75th ingested chapter — tenth leaf of Ch 7.**

## Key Claims

- **[[CLanguage|C]] performs no [[BoundsChecking|array bounds checking]]** — *"The C language does not perform automatic array bounds checking"* — the root vulnerability every buffer overflow exploits.
- **A buffer overflow on the [[StackSection|stack]] corrupts the [[StackFrame|stack frame]] in a predictable order**: first adjacent local variables, then the saved [[FramePointer|`%rbp`]] at `0(%rbp)`, then the saved **return address** at `8(%rbp)`. The exact offset from buffer start to return address depends on the function's frame layout — the `secret` example needs **40 bytes of padding** before the 8-byte return-address target.
- **Overwriting the return address gives the attacker [[InstructionPointer|`%rip`]] control** — when [[RetInstruction|`retq`]] pops the saved return address into `%rip`, it pops whatever the attacker placed there. *"A clever attacker can inject malicious code that intentionally overruns the boundary of an array … to force the program to execute in an unintended manner."*
- **The exploit input is constructed in little-endian** because [[X86_64|x86-64]] is little-endian — the target address `0x4006da` becomes the byte sequence `\xda\x06\x40\x00\x00\x00\x00\x00` in the payload.
- **The vulnerable function family is well-known**: [[Gets|`gets`]], [[Scanf|`scanf("%s", buf)`]], [[Strcpy|`strcpy`]], `strcat`, [[Sprintf|`sprintf`]] — every function in `<string.h>` / `<stdio.h>` that writes a caller-controlled number of bytes into a fixed-size buffer with no length parameter.
- **The bounded counterparts are the first line of defense**: `fgets(buf, 12, stdin)`, `scanf("%12s", buf)`, [[Strncpy|`strncpy(dst, src, 12)`]], `strncat(dst, src, 12)`, `snprintf(buf, 12, "%d", num)`. *"The best line of defense is always the programmer."*
- **Three system-level defenses exist, all bypassable**:
  - **[[StackCanary|Stack canaries]]** — compiler-inserted guard value between locals and the saved [[FramePointer|`%rbp`]] / return address, checked before [[RetInstruction|`retq`]]. Defeat: the attacker who knows the canary value (or can read it via an info leak) overwrites it with the original value.
  - **[[AddressSpaceLayoutRandomization|Stack randomization / ASLR]]** — OS randomizes stack base address per process so the attacker cannot hardcode return targets. Defeat: brute force on small entropy, or **NOP sleds** padding the target region.
  - **[[ExecutableSpaceProtection|Non-executable stack / NX / DEP]]** — page-table `NX` bit marks the stack non-executable, so injected shellcode on the stack faults on execution. Defeat: **[[ReturnOrientedProgramming|return-oriented programming (ROP)]]** — chain gadgets ending in `retq` from existing executable code (e.g., libc) instead of injecting new instructions.
- **[[ReturnOrientedProgramming|ROP]] is the *cherry-picking* exploit** — *"a technique cherry-picking instructions across executable regions"* — defeats NX entirely because no attacker-controlled bytes need to execute; only existing instruction sequences (gadgets) are used.
- **Historical case studies anchor the threat model**: the **Morris Worm (1988)** exploited a buffer overrun in `fingerd` to propagate across UNIX hosts on the early internet; **AOL Chat Wars (late 1990s)** saw AOL weaponize a buffer overflow in its own AIM client as a protocol-conformance check to lock out Microsoft's MMS clones.

## Key Quotes

> "The C language does not perform automatic array bounds checking." — opening definition; the structural root of the entire vulnerability class.

> "A clever attacker can inject malicious code that intentionally overruns the boundary of an array … to force the program to execute in an unintended manner." — the threat model.

> "In the worst cases, the attacker can run code that allows them to gain root privilege, or OS-level access." — the [[PrivilegeEscalation|privilege-escalation]] endpoint.

> "The best line of defense is always the programmer." — the chapter's defense-prioritization claim.

## Connections

- [[DiveIntoSystems]] — **75th ingested chapter — tenth leaf of Ch 7 *x86-64 Assembly*.** The **security payoff** of the entire Ch 7 stack-discipline tour. Sibling of [[dis-7-9-x86-64-structs|Ch 7.9]] (struct layout / alignment, the *non-security* compile-time-offsets sibling).
- [[BufferOverflow]] — the concept this chapter develops in full at the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] surface. Prior chapters ([[dis-1-5-arrays-strings|Ch 1.5]] / [[dis-2-6-strings|Ch 2.6]]) **flagged** the hazard at the C source level; this chapter **operationalizes** it at the stack-frame surface.
- [[StackSmashing]] — the canonical exploit technique walked through the `secret` worked example. **New concept page** minted by this ingest.
- [[ReturnAddressOverwrite]] — the specific corruption that gives the attacker `%rip` control. **New concept page** minted by this ingest.
- [[StackCanary]] — the compiler-inserted runtime detection mechanism. **New concept page** minted by this ingest.
- [[AddressSpaceLayoutRandomization]] — the OS-level address-randomization defense. **New concept page** minted by this ingest.
- [[ExecutableSpaceProtection]] — the NX / DEP page-table defense. **New concept page** minted by this ingest.
- [[ReturnOrientedProgramming]] — the *cherry-picked-gadgets* technique that defeats NX. **New concept page** minted by this ingest.
- [[CallStack]] / [[StackFrame]] / [[FramePointer]] / [[StackPointer]] / [[RetInstruction|`retq`]] / [[CallInstruction|`callq`]] — the [[dis-7-5-x86-64-functions|Ch 7.5]] mechanism this chapter exploits.
- [[Strcpy]] / [[Gets]] / [[Sprintf]] / [[Scanf]] — the canonical vulnerable functions. **Source-level warnings** are at [[dis-1-5-arrays-strings|Ch 1.5]]; the **safer bounded alternatives** ([[Strncpy]] etc.) are at [[dis-2-6-strings|Ch 2.6]].
- [[X86_64|x86-64]] / [[AssemblyLanguage|assembly]] / [[CLanguage|C]] — the ISA / language substrate.
- [[ByteOrder|Little-endian]] — explains why exploit payloads write target addresses as `\xda\x06\x40\x00\x00\x00\x00\x00` rather than `\x00\x00\x00\x00\x00\x40\x06\xda`. The [[dis-4-7-byte-order|Ch 4.7]] convention now has a security-relevant consequence.
- [[Daemon]] — the UNIX background process category exploited by the Morris Worm. **New concept page** minted by this ingest.

## Contradictions

- None. Ch 7.10 **operationalizes** the [[BufferOverflow]] hazard flagged abstractly in [[dis-1-5-arrays-strings|Ch 1.5]] ([[Strcpy|`strcpy`]] warning) and [[dis-2-6-strings|Ch 2.6]] (safer-functions catalog) at the [[X86_64|x86-64]] [[StackFrame|stack-frame]] surface — concretizes the abstract claim into a specific 40-byte-padding + 8-byte-address exploit recipe. Adds mechanism rather than revising claims. The defenses listed are a superset of the [[BufferOverflow|BufferOverflow]] concept page's pre-existing five-point defense list — the structures **align**, not conflict.
