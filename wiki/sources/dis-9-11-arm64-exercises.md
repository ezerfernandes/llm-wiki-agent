---
title: "Dive into Systems — Ch 9.11 Exercises (ARM64)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, exercises]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/exercises.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Eleventh and final leaf** of Ch 9 *64-bit ARM Assembly* of *[[DiveIntoSystems]]* — the **exercise-set close** that **fully completes Ch 9**. Single-page redirect (*"All Chapter 9 Exercises"*) into the book's interactive exercises platform — no inline problems. Drills the full Ch 9.1–Ch 9.10 [[ARM64|AArch64]] [[AssemblyLanguage|assembly]] surface area built up over ten content leaves. **Structural twin** of [[dis-7-11-x86-64-exercises|Ch 7.11]] / [[dis-8-11-ia32-exercises|Ch 8.11]]; structural sibling of [[dis-1-8-exercises|Ch 1.8]] / [[dis-2-11-exercises|Ch 2.11]] / [[dis-4-10-exercises|Ch 4.10]] / [[dis-5-11-exercises|Ch 5.11]] — *exercise-set closes chapter* pattern across the entire [[DiveIntoSystems]] book. **All three assembly chapters** of *[[DiveIntoSystems]]* (Ch 7 *x86-64* + Ch 8 *IA32* + Ch 9 *ARMv8*) are now in the wiki. **No new concept pages** — pure problem-set close.

## Key Claims

- **Exercise-set drills the full Ch 9.1–Ch 9.10 surface.** Topics include: [[dis-9-1-arm64-basics|Ch 9.1]]'s [[AArch64Registers|register set]] / [[ARM64AddressingMode|addressing modes]] / [[LoadStoreArchitecture|load/store discipline]]; [[dis-9-2-arm64-common|Ch 9.2]]'s [[ARM64DataMovement|`mov` / `ldr` / `str` / `ldp` / `stp`]] primitives; [[dis-9-3-arm64-arithmetic|Ch 9.3]]'s [[ARM64ArithmeticInstructions|arithmetic]] / [[ARM64ShiftInstructions|shift]] / [[ARM64BitwiseInstructions|bitwise]] families; [[dis-9-4-arm64-conditional-loops|Ch 9.4]]'s [[ARM64FlagsRegister|NZCV]] + [[ARM64Cmp|`cmp`]] + [[ARM64ConditionalBranch|`b.cond`]] + [[ARM64ConditionalSelect|`csel`]] control flow; [[dis-9-5-arm64-functions|Ch 9.5]]'s [[ARM64BranchAndLink|`bl`]] / [[ARM64Ret|`ret`]] + [[ARM64CallingConvention|AAPCS64]] + [[ARM64FunctionPrologue|prologue/epilogue]]; [[dis-9-6-arm64-recursion|Ch 9.6]]'s recursive frame stacking; [[dis-9-7-arm64-arrays|Ch 9.7]]'s scaled-index array access; [[dis-9-8-arm64-matrices|Ch 9.8]]'s 2-D row-major vs array-of-arrays matrices; [[dis-9-9-arm64-structs|Ch 9.9]]'s struct layout + alignment + padding; and [[dis-9-10-arm64-buffer-overflow|Ch 9.10]]'s stack-smashing security payoff.
- **Same redirect-page format as [[dis-7-11-x86-64-exercises|Ch 7.11]] / [[dis-8-11-ia32-exercises|Ch 8.11]].** The page contains no inline exercise text — only a link to the book's external interactive exercises platform. **Structural twin** behavior — same single-page pattern as the [[dis-7-11-x86-64-exercises|x86-64]] and [[dis-8-11-ia32-exercises|IA32]] exercise closes.
- **Operationalizes [[dis-0-introduction|Ch 0]]'s active-reading-by-typing-the-code pedagogy at the [[ARM64]] assembly surface.** Drives [[GDB|`gdb`]] / [[Objdump|`objdump`]] tracing, register/stack/NZCV-flag simulation, and (for the [[dis-9-10-arm64-buffer-overflow|Ch 9.10]] strand) hands-on payload-crafting at [[AArch64]] width.
- **Closes Ch 9 — completes Part III for the third ISA.** Ch 9 *64-bit ARM Assembly* is now fully ingested into the wiki (sections 9.1 through 9.11). Combined with Ch 7 *x86-64 Assembly* and Ch 8 *32-bit IA32 Assembly*, the wiki now has **full coverage of all three assembly chapters** of [[DiveIntoSystems]] — the [[CISC]] (x86-64 / IA32) and [[RISC]] ([[ARM64]]) [[ISA|ISAs]] are now cross-ingestable for comparative ISA-design analysis.
- **No new concept pages.** Exercise pages by convention introduce no new wiki concepts — the concept inventory is fixed by the preceding content leaves. **Structural twin** of [[dis-7-11-x86-64-exercises|Ch 7.11]] / [[dis-8-11-ia32-exercises|Ch 8.11]] in this respect.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **104th ingested chapter** / **eleventh and final leaf of Ch 9**. **Ch 9 fully complete.**
- [[dis-9-10-arm64-buffer-overflow]] — immediate predecessor; the security-payoff content leaf. Ch 9.11 closes the chapter.
- [[dis-9-1-arm64-basics]] through [[dis-9-10-arm64-buffer-overflow]] — the ten content leaves Ch 9.11 drills.
- [[dis-7-11-x86-64-exercises]] / [[dis-8-11-ia32-exercises]] — structural twins; same redirect-page format at the chapter-close slot.
- [[dis-1-8-exercises]] / [[dis-2-11-exercises]] / [[dis-4-10-exercises]] / [[dis-5-11-exercises]] — structural siblings; *exercise-set closes chapter* pattern across [[DiveIntoSystems]].
- [[ARM64]] / [[AArch64Registers]] / [[LoadStoreArchitecture]] / [[ARM64AddressingMode]] / [[ARM64DataMovement]] / [[ARM64ArithmeticInstructions]] / [[ARM64ShiftInstructions]] / [[ARM64BitwiseInstructions]] / [[ARM64FlagsRegister]] / [[ARM64Cmp]] / [[ARM64ConditionalBranch]] / [[ARM64ConditionalSelect]] / [[ARM64CallingConvention]] / [[ARM64FunctionPrologue]] / [[LinkRegister]] — the full [[ARM64]] concept inventory Ch 9 mints across its eleven leaves.

## Contradictions

None. Pure problem-set close — adds no new claims to the wiki.
