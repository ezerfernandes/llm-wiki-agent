---
title: "Dive into Systems — Ch 2.9.7 Compiling C to Assembly, and Compiling and Linking Assembly and C Code"
type: source
tags: [dive-into-systems, c-language, assembly, gcc, compilation-process, ia32, objdump]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/advanced_assembly.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **seventh and final subsection of [[dis-2-9-advanced|Ch 2.9]]** of *[[DiveIntoSystems]]* — closes Ch 2 *A Deeper Dive Into C* and the *"C the build workflow"* arc by exposing the **`.c` → `.s` → `.o` → executable** pipeline through three concrete [[GCC|`gcc`]] invocations and one inspection tool. Promotes [[AssemblyLanguage|assembly language]] from a *named, deferred* concept (referenced throughout Ch 2.9.5 / 2.9.6) into a **first-class artifact** the toolchain emits, consumes, and re-emits. Headline payoff: the [[CompilationProcess|five-stage pipeline]] [[dis-2-9-5-libraries|Ch 2.9.5]] codified is **not a black box** — [[GCC|`gcc -S`]] cracks it open after stage 2 to produce human-readable [[AssemblyStage|assembly]] you can read, edit, and re-feed into the same toolchain. The **first corpus bridge to Ch 3** (assembly / [[ComputerArchitecture|architecture]]).

## Key Claims

- **C compilers are bidirectional toolchain front-ends.** *"A compiler can compile C code to assembly code, and it can compile assembly code into a binary form that links into a binary executable program."* The same [[GCC|`gcc`]] driver handles `.c` → `.s` (via [[CompilationStage|compile]]) and `.s` → `.o` (via [[AssemblyStage|assemble]]) — same tool, different invocation flags.

- **The `-S` flag emits human-readable assembly.** [[GCC|`gcc -m32 -S simpleops.c`]] stops the pipeline after the [[CompilationStage|compile stage]] and produces `simpleops.s` — a text file containing the [[IA32|IA32 (32-bit x86)]] assembly translation of the C program. The file is editable in any text editor.

- **The `-c` flag converts assembly back to object code.** [[GCC|`gcc -m32 -c myfunc.s`]] feeds a hand-written or compiler-emitted `.s` through the [[AssemblyStage|assemble stage]] to produce `myfunc.o` — same `.s → .o` path the toolchain uses internally when compiling from C source.

- **Mixed-language linking works.** Hand-written assembly in `myfunc.s` and C source in `main.c` link together via `gcc -m32 -o myprog myfunc.o main.c` — assembly functions become callable from C and vice versa through the standard [[LinkingStage|link-edit]] path.

- **`objdump -d` displays binary-to-assembly mappings.** *"Systems provide utilities that allow users to view binary files. For example, `objdump` displays the machine code and assembly code mappings in `.o` files: `$ objdump -d simpleops.o`."* The [[Objdump|`objdump`]] tool **disassembles** an [[ObjectFile|`.o` file]] — reverses the [[AssemblyStage|assemble stage]] to show the original mnemonics alongside the machine-code bytes.

- **C statements have a direct, line-by-line assembly correspondence.** The chapter's `simpleops.c` example pairs C statements with their IA32 translations to show the direct mapping — a single `x = x*100;` line maps to `movl -8(%ebp), %eax` + `imull $100, %eax, %eax` + `movl %eax, -4(%ebp)` (load → multiply → store). [[LocalVariable|Local variables]] live at **stack-frame offsets from `%ebp`** (`-8(%ebp)` is `x`, `-4(%ebp)` is `y`).

- **Assembly is architecture-specific, the workflow is universal.** The chapter uses [[IA32|IA32]] via the `-m32` flag for its examples but notes that *"this functionality is supported by any C compiler, and most compilers support compiling to a number of different assembly languages"* — the `-S`/`-c` workflow is portable across [[ISA|ISAs]] ([[X86_64|x86-64]] / [[ARM|ARM]] / [[RISCV|RISC-V]]) even though the emitted assembly is not.

- **Why C dominates OS code:** *"because C is a portable language and is much higher level than assembly languages, the vast majority of operating system code is written in C"* — written once, [[GCC|`gcc`]] re-emits architecture-specific assembly per target. Ties the chapter back to [[dis-0-introduction|Ch 0]]'s thesis that understanding the [[ComputerSystem|computer system]] beneath your code is what lets you write efficient programs.

## Key Quotes

> "A compiler can compile C code to assembly code, and it can compile assembly code into a binary form that links into a binary executable program." — opening definition, framing [[GCC|gcc]] as bidirectional between [[CLanguage|C]] and [[AssemblyLanguage|assembly]].

> "Because C is a portable language and is much higher level than assembly languages, the vast majority of operating system code is written in C." — the portability rationale that closes [[dis-2-9-advanced|Ch 2.9]] and motivates Ch 3.

> "Systems provide utilities that allow users to view binary files. For example, `objdump` displays the machine code and assembly code mappings in `.o` files: `$ objdump -d simpleops.o`." — the disassembly recipe.

## The Three-Command Workflow

| Command | Stage(s) consumed | Input → Output | What you get |
|---|---|---|---|
| `gcc -m32 -S simpleops.c` | 1+2 ([[PreprocessingStage\|preprocess]] + [[CompilationStage\|compile]]) | `.c` → `.s` | Human-readable [[IA32]] assembly text |
| `gcc -m32 -c simpleops.s` | 3 ([[AssemblyStage\|assemble]]) | `.s` → `.o` | [[ObjectFile\|machine-code object file]] |
| `gcc -m32 -o myprog myfunc.o main.c` | full pipeline | `.o` + `.c` → executable | [[BinaryExecutable\|Linked executable]] (mixed assembly + C) |
| `objdump -d simpleops.o` | (disassembly, not compile) | `.o` → text | Machine-code-with-mnemonics dump |

## The simpleops.c IA32 Example

The chapter's worked example shows how a handful of C statements (`x = 1; x = x + 2; x = x - 14; y = x * 100;`) translate to IA32 — local variables live at `%ebp`-relative offsets, arithmetic happens directly on stack memory for `addl`/`subl` but routes through `%eax` for multiplication:

```
movl    $1, -8(%ebp)      # x = 1
addl    $2, -8(%ebp)      # x = x + 2
subl    $14, -8(%ebp)     # x = x - 14
movl    -8(%ebp), %eax    # load x into R[%eax]
imull   $100, %eax, %eax  # %eax = x * 100
movl    %eax, -4(%ebp)    # y = x * 100
```

The example surfaces the **stack-frame addressing convention** ([[LocalVariable|locals]] at negative offsets from `%ebp`), the **AT&T syntax** convention (`movl source, dest`; `$1` is immediate, `%eax` is a register, `-8(%ebp)` is a memory operand), and the **register vs. memory operation** asymmetry — `addl`/`subl` accept a memory destination, `imull` requires a register.

## Connections

- [[DiveIntoSystems]] — the textbook; this is Ch 2.9.7, **the final subsection of [[dis-2-9-advanced|Ch 2.9]]** and the closing section of Ch 2.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — the three authors.
- [[dis-2-9-advanced]] — the parent hub page (Ch 2.9 *Advanced C Features*).
- [[dis-2-9-5-libraries]] — establishes the [[CompilationProcess|five-stage pipeline]] this section makes inspectable.
- [[dis-2-9-6-writing-libraries]] — the immediately prior subsection (author-side library workflow).
- [[dis-1-1-getting-started]] — first introduced [[GCC|`gcc`]] as the compile-then-run tool now revealed as a multi-stage pipeline.
- [[CompilationProcess]] — the surrounding five-stage pipeline.
- [[CompilationStage]] — the stage `-S` stops after.
- [[AssemblyStage]] — the stage `-c` operates as.
- [[GCC]] — the canonical [[CCompiler|C compiler]] this section drives.
- [[CLanguage]] — the source language.
- [[AssemblyLanguage]] — the **intermediate-but-inspectable** language this section promotes from named-and-deferred to first-class.
- [[IA32]] — the specific 32-bit x86 [[ISA|ISA]] the chapter's examples target via `-m32`.
- [[ObjectFile]] — the `.o` output of `-c`.
- [[BinaryExecutable]] — the final output of the full pipeline.
- [[Objdump]] — the disassembly tool the chapter introduces.
- [[ComputerArchitecture]] — Ch 3's subject, which this section opens onto.
- [[ISA]] — the architecture-specific surface assembly targets.

## Contradictions

- None. Purely additive — this section **operationalizes** the [[CompilationProcess|five-stage pipeline]] [[dis-2-9-5-libraries|Ch 2.9.5]] codified by making stages 2 and 3 directly inspectable. The [[AssemblyStage|assembly stage]] description in [[dis-2-9-5-libraries|Ch 2.9.5]] noted that the toolchain *"lets the toolchain also accept hand-written `.s` files via the same path"* — Ch 2.9.7 delivers the worked example proving it.
