---
title: "Dive into Systems — Ch 7.11 Exercises (x86-64)"
type: source
tags: [book, dive-into-systems, exercises, x86-64, assembly]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/exercises.html
---

## Summary

Section 7.11 of [[DiveIntoSystems]] is the **exercises section that closes Ch 7 *64-bit x86 Assembly*** — a single-page redirect (*"All Chapter 7 Exercises"*) into the book's interactive exercises platform rather than inline problems. The exercise set drills the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] surface area Ch 7 built up across its ten content leaves: [[dis-7-1-x86-64-basics|Ch 7.1]]'s [[GeneralPurposeRegister|register set]] / [[AtAndTSyntax|AT&T syntax]] / [[X86AddressingMode|addressing modes]], [[dis-7-2-x86-64-common|Ch 7.2]]'s [[X86MovInstruction|`mov`]] / [[X86ArithmeticInstructions|`add`/`sub`]] / [[X86StackInstructions|`push`/`pop`]] core, [[dis-7-3-x86-64-arithmetic|Ch 7.3]]'s [[X86MulInstruction|`imul`]] / [[X86DivInstruction|`idiv`]] / [[X86ShiftInstructions|shifts]] / [[X86BitwiseInstructions|bitwise]] / [[LeaInstruction|`lea`]] expansion, [[dis-7-4-x86-64-conditional-loops|Ch 7.4]]'s [[X86FlagsRegister|FLAGS]] + [[CmpInstruction|`cmp`]] + [[X86JumpInstructions|conditional jumps]] + [[AsmIfThenElse|if/else]] / [[AsmLoopPattern|loop]] compilation patterns, [[dis-7-5-x86-64-functions|Ch 7.5]]'s [[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] / [[LeaveInstruction|`leaveq`]] + [[CallingConvention|System V calling convention]] + [[StackFrame|stack-frame]] discipline, [[dis-7-6-x86-64-recursion|Ch 7.6]]'s [[Recursion|recursion]] frame stacking, [[dis-7-7-x86-64-arrays|Ch 7.7]]'s [[AsmArrayAccess|scaled-index array]] compilation, [[dis-7-8-x86-64-matrices|Ch 7.8]]'s 2-D-matrix [[RowMajorOrder|row-major]] vs [[ArrayOfArrays|array-of-arrays]] split, [[dis-7-9-x86-64-structs|Ch 7.9]]'s [[StructLayout|struct layout]] + [[AlignmentRule|alignment]] + [[StructPadding|padding]] mechanism, and [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]]'s [[StackSmashing|stack-smashing]] / [[ReturnAddressOverwrite|return-address-overwrite]] / [[StackCanary|canary]] / [[AddressSpaceLayoutRandomization|ASLR]] / [[ExecutableSpaceProtection|NX]] / [[ReturnOrientedProgramming|ROP]] security stack. Carries no new conceptual material — its role is to **operationalize** Ch 7's claims by making the reader trace, write, and exploit [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] end-to-end, in line with [[dis-0-introduction|Ch 0]]'s *active-reading-by-typing-the-code* pedagogy. **Structural sibling of [[dis-1-8-exercises|Ch 1.8]] / [[dis-2-11-exercises|Ch 2.11]] / [[dis-4-10-exercises|Ch 4.10]] / [[dis-5-11-exercises|Ch 5.11]]** — exercise-set-closes-chapter pattern. **Fully completes Ch 7** *64-bit x86 Assembly*.

## Key Claims

- **Closes Ch 7 with a problem set, not prose.** Ch 7.11 is a one-line section pointing readers to *"All Chapter 7 Exercises"* on the book's interactive exercises platform — no inline problems appear on the chapter page itself.
- **Drills the Ch 7.1–Ch 7.10 surface area.** Targets the full [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] stack: register naming and [[X86AddressingMode|addressing modes]] ([[dis-7-1-x86-64-basics|Ch 7.1]]), instruction-by-instruction tracing of `mov` / `add` / `sub` / `push` / `pop` ([[dis-7-2-x86-64-common|Ch 7.2]]), arithmetic and [[LeaInstruction|`lea`]] / shift / bitwise strength reductions ([[dis-7-3-x86-64-arithmetic|Ch 7.3]]), [[ConditionCode|condition-code]]-driven [[AsmIfThenElse|if/else]] and [[AsmLoopPattern|loop]] compilation ([[dis-7-4-x86-64-conditional-loops|Ch 7.4]]), [[CallingConvention|System V]] function-call stack discipline ([[dis-7-5-x86-64-functions|Ch 7.5]]), [[Recursion|recursive]] frame stacking ([[dis-7-6-x86-64-recursion|Ch 7.6]]), array / matrix / struct memory layouts ([[dis-7-7-x86-64-arrays|Ch 7.7]] / [[dis-7-8-x86-64-matrices|Ch 7.8]] / [[dis-7-9-x86-64-structs|Ch 7.9]]), and the [[BufferOverflow|buffer-overflow]] / [[StackSmashing|stack-smashing]] security payoff ([[dis-7-10-x86-64-buffer-overflow|Ch 7.10]]).
- **Operationalizes the active-reading pedagogy at the assembly surface.** Per [[dis-0-introduction|Ch 0]], *Dive into Systems* expects readers to type, compile, and trace code. Ch 7.11 enforces that at the [[AssemblyLanguage|assembly]]-level — the exercises drive [[GDB|`gdb`]] / [[Objdump|`objdump`]] disassembly tracing, instruction-by-instruction register / stack / FLAGS state simulation, and (for Ch 7.10's payload-crafting exercises) hands-on construction of [[StackSmashing|stack-smashing]] inputs.
- **Introduces no new concepts.** Like [[dis-7-9-x86-64-structs|Ch 7.9]]'s siblings, Ch 7.11 is purely a problem set — any concept it tests is already minted by [[dis-7-1-x86-64-basics|Ch 7.1]]–[[dis-7-10-x86-64-buffer-overflow|Ch 7.10]].
- **Marks Ch 7 complete.** With Ch 7.11 ingested, all eleven sections of Ch 7 *64-bit x86 Assembly* are now in the wiki — the largest single chapter of [[DiveIntoSystems]] and the canonical [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] reference of the corpus.

## Key Quotes

> "All Chapter 7 Exercises" — the section's sole inline content, a hyperlink to the book's interactive exercises platform; the exercises themselves are hosted off-page.

## Connections

- [[DiveIntoSystems]] — the book; this is Ch 7.11, the exercise set that **closes Ch 7** *64-bit x86 Assembly* — the chapter is now **fully complete** (7.1 through 7.11).
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-0-introduction]] — supplies the *active-reading-by-typing-the-code* pedagogy.
- [[dis-7-1-x86-64-basics]] — [[X86_64|x86-64]] register set / [[AtAndTSyntax|AT&T syntax]] / [[X86AddressingMode|addressing modes]] / [[OperandSize|operand-size]] suffixes drilled.
- [[dis-7-2-x86-64-common]] — [[X86MovInstruction|`mov`]] / [[X86ArithmeticInstructions|`add`/`sub`]] / [[X86StackInstructions|`push`/`pop`]] traces.
- [[dis-7-3-x86-64-arithmetic]] — [[X86MulInstruction|`imul`]] / [[X86DivInstruction|`idiv`]] / [[X86ShiftInstructions|shifts]] / [[X86BitwiseInstructions|bitwise]] / [[LeaInstruction|`lea`]] strength reductions.
- [[dis-7-4-x86-64-conditional-loops]] / [[dis-7-4-1-x86-64-preliminaries]] / [[dis-7-4-2-x86-64-if-statements]] / [[dis-7-4-3-x86-64-loops]] — [[X86FlagsRegister|FLAGS]] / [[CmpInstruction|`cmp`]] / [[X86JumpInstructions|jumps]] / [[AsmIfThenElse|if/else]] / [[AsmLoopPattern|loop]] compilation.
- [[dis-7-5-x86-64-functions]] — [[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] / [[LeaveInstruction|`leaveq`]] / [[CallingConvention|System V]] / [[StackFrame|frame]] discipline.
- [[dis-7-6-x86-64-recursion]] — [[Recursion|recursive]] [[CallStack|call-stack]] frame stacking.
- [[dis-7-7-x86-64-arrays]] — [[AsmArrayAccess|scaled-index]] [[CArray|array]] compilation.
- [[dis-7-8-x86-64-matrices]] — 2-D [[MultidimensionalArray|matrix]] [[RowMajorOrder|row-major]] vs [[ArrayOfArrays|array-of-arrays]] layouts.
- [[dis-7-9-x86-64-structs]] — [[StructLayout|struct layout]] + [[AlignmentRule|x86-64 alignment]] + [[StructPadding|padding]].
- [[dis-7-10-x86-64-buffer-overflow]] — the [[StackSmashing|stack-smashing]] security payoff; payload-crafting exercises.
- [[dis-1-8-exercises]] / [[dis-2-11-exercises]] / [[dis-4-10-exercises]] / [[dis-5-11-exercises]] — structural siblings (exercise-set-closes-chapter pattern across the corpus).
- [[X86_64]] / [[AssemblyLanguage]] — the ISA and surface language being drilled.

## Contradictions

- No contradictions — Ch 7.11 is a problem set with no new claims and introduces no concepts not already established in [[dis-7-1-x86-64-basics|Ch 7.1]]–[[dis-7-10-x86-64-buffer-overflow|Ch 7.10]].
