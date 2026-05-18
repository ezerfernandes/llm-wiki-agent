---
title: "Dive into Systems — Ch 9.10 Buffer Overflows (ARM64)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, security, buffer-overflow, stack-smashing]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/buffer_overflow.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Tenth leaf** of Ch 9 *64-bit ARM Assembly* of *[[DiveIntoSystems]]* — **non-twin structural sibling** of [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] / [[dis-8-10-ia32-buffer-overflow|Ch 8.10]] — the **security payoff** of the whole Ch 9 stack-discipline tour. Inverts the [[dis-9-5-arm64-functions|Ch 9.5]] / [[dis-9-6-arm64-recursion|Ch 9.6]] [[CallStack|call-stack]] discipline: an unbounded `scanf("%s", buf)` writes past a stack buffer, overwriting **the saved [[LinkRegister|`x30`]] in the current [[StackFrame|stack frame]]** (spilled there by the [[ARM64FunctionPrologue|prologue]]'s `stp x29, x30, [sp, #-N]!`), redirecting the [[ARM64Ret|`ret`]] (which sets `pc = x30`) to attacker-chosen code like `endGame()`. **Headline [[ARM64]]-distinctive attack-surface note**: although [[LinkRegister|`x30`]] is **register-resident** during the call, **non-leaf functions spill it to the stack** in their prologue — re-creating the same stack-resident return-address vulnerability [[X86_64|x86]] / [[IA32]] have natively. **Leaf functions are immune** to this specific overwrite (no `x30` spill) — a structural defense [[X86_64|x86]] / [[IA32]] cannot offer. **Same defense taxonomy** as [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] — [[StackCanary|stack canaries]] / [[AddressSpaceLayoutRandomization|ASLR]] / [[ExecutableSpaceProtection|NX]] / bounded input functions. **No new concept pages** — reuses [[BufferOverflow]] / [[StackSmashing]] / [[ReturnAddressOverwrite]] / [[StackCanary]] / [[AddressSpaceLayoutRandomization]] / [[ExecutableSpaceProtection]] / [[ReturnOrientedProgramming]] from Ch 7.10.

## Key Claims

- **Stack-resident saved `x30` is the [[ARM64]] return-address vulnerability.** Although [[LinkRegister|`x30`]] is register-resident during the active function, **non-leaf functions spill it to the stack** in the prologue via `stp x29, x30, [sp, #-N]!` — creating a stack-resident return-address slot vulnerable to overwrite when an adjacent buffer overflows. *"ARM64 systems store the return address (x30) on the stack within the call frame, making it vulnerable to overwrite when buffers overflow, despite architectural differences from x86."* **Leaf functions** (no nested `bl`) skip the spill — structurally immune to this specific attack on their own frame.
- **Control-flow hijacking via `ret`.** *"By carefully constructing overflow payloads, attackers can overwrite the saved return address to redirect execution to arbitrary functions like `endGame()`"* — same [[ReturnAddressOverwrite|control-flow hijack]] pattern as [[X86_64|x86]] / [[IA32]], realized at the moment [[ARM64Ret|`ret`]] reads the overwritten `x30` value from the corrupted stack slot via `ldp x29, x30, [sp], #N`.
- **Stack-smashing mechanism — same root cause.** *"Buffer overruns corrupt the call stack by writing beyond allocated buffer boundaries, overwriting saved frame pointers and return addresses that control program execution flow"* — the [[StackSmashing|stack-smashing]] mechanism is **ISA-independent** at the C-language level (*"the C language does not perform automatic array bounds checking"*); only the specific stack-slot offsets differ between [[X86_64]] / [[IA32]] / [[ARM64]].
- **[[StackCanary|Stack canaries]] as compiler-level defense.** *"Modern GCC implementations use stack canaries — guard values in non-writable memory compared against stack copies — to detect corruption before function returns"* — same canary mechanism as [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]], compiled via `-fstack-protector`. Canaries can be circumvented but raise attack difficulty significantly.
- **Length specifiers as programmer-level defense.** *"Using bounded input functions (e.g., `scanf("%12s", buf)` instead of `scanf("%s", buf)`) prevents buffer overflow by restricting how many bytes the system reads"* — same first-line defense as Ch 7.10's [[BoundsChecking|bounded library functions]] catalog ([[Strncpy|`strncpy`]] / `snprintf` / `fgets` / format-string width specifiers).
- **[[ARM64]]-specific attack-surface delta — leaf-function immunity.** Functions that make **no nested calls** (leaf functions in [[AAPCS64|AAPCS64]] parlance) have **no reason to spill [[LinkRegister|`x30`]] to the stack** — their return address lives entirely in the register file for the duration of the call. Overflowing a buffer in a leaf function corrupts neither `x30` (still register-resident) nor a saved-`x30` slot (none exists). A structural defense [[X86_64|x86]] / [[IA32]] cannot offer because [[CallInstruction|`callq` / `call`]] **always** pushes the return address onto the stack. **Caveat**: still vulnerable to overwriting other state (local variables, [[FramePointer|saved `x29`]]) — leaf-function immunity is **partial** and **specific to the return-address overwrite primitive**.

## Key Quotes

> "An attacker can overwrite the stack so that the return address is replaced with the address of `endGame`." — the [[ReturnAddressOverwrite|return-address overwrite]] primitive, [[ARM64]] surface.

> "The best line of defense is always the programmer." — the headline pedagogical claim: **bounded input + memory-safe languages** outrank compiler / OS mitigations.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **103rd ingested chapter** / **tenth leaf of Ch 9**.
- [[dis-9-9-arm64-structs]] — immediate predecessor; closed the Ch 9 instruction-family + aggregate-data tour. Ch 9.10 fuses everything into the security payoff.
- [[dis-9-5-arm64-functions]] / [[dis-9-6-arm64-recursion]] — supplied the [[ARM64FunctionPrologue|prologue/epilogue]] discipline that spills [[LinkRegister|`x30`]] to the stack — the structural mechanism the overflow exploits.
- [[dis-7-10-x86-64-buffer-overflow]] / [[dis-8-10-ia32-buffer-overflow]] — structural siblings; same exploit class, same defense taxonomy. **Headline [[ARM64]]-specific delta**: leaf-function immunity (no stack-resident return address); non-leaf functions equivalent to [[X86_64|x86]] / [[IA32]] post-spill.
- [[BufferOverflow]] / [[StackSmashing]] / [[ReturnAddressOverwrite]] / [[StackCanary]] / [[AddressSpaceLayoutRandomization]] / [[ExecutableSpaceProtection]] / [[ReturnOrientedProgramming]] — reused concept pages (no new ones minted).
- [[LinkRegister]] — central [[ARM64]] mechanism; spill-to-stack is the vulnerability surface.
- [[ARM64FunctionPrologue]] — the `stp x29, x30, [sp, #-N]!` pattern that creates the stack-resident return-address slot.

## Contradictions

None. Ch 9.10 **operationalizes** [[BufferOverflow]] at the [[ARM64]] surface — same [[CLanguage|C]]-level root cause, same defense taxonomy. The [[LinkRegister|register-resident return address]] is a **partial structural mitigation** for leaf functions, not a contradiction of the [[ReturnAddressOverwrite|return-address overwrite]] class.
