---
title: "Assembly Language"
type: concept
tags: [assembly, isa, low-level, compiler-output, ia32, x86, arm]
sources: [dis-2-9-7-c-to-assembly, dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Assembly Language

**Assembly language** is the human-readable text form of a machine's native instruction set — the mnemonics (`mov`, `add`, `imull`, `jmp`) and operand syntax that map **one-to-one** onto the [[BinaryExecutable|binary]] opcodes the [[CPU]] decodes. It sits between [[CLanguage|C]] and machine code in the [[CompilationProcess|compile pipeline]] as the **output of [[CompilationStage|stage 2 (compile)]]** and **input of [[AssemblyStage|stage 3 (assemble)]]**.

[[dis-2-9-7-c-to-assembly|DIS Ch 2.9.7]] promotes assembly from a *named-and-deferred* concept (referenced throughout [[dis-2-9-5-libraries|Ch 2.9.5]] / [[dis-2-9-6-writing-libraries|Ch 2.9.6]] as the artifact `-S` emits) into a **first-class artifact** by showing how to (a) emit it via [[GCC|`gcc -S`]], (b) read it as text, (c) hand-write a `.s` file, and (d) re-feed it to the toolchain via `gcc -c`.

## Architecture-specific by definition

Every assembly language is tied to one [[ISA|instruction set architecture]]:

- [[IA32]] (32-bit x86) — used by [[dis-2-9-7-c-to-assembly|DIS Ch 2.9.7]]'s worked examples via the `-m32` flag.
- [[X86_64|x86-64]] — the modern 64-bit superset.
- [[ARM|ARM / AArch64]] — phones, [[RaspberryPi|Raspberry Pi]], Apple Silicon.
- [[RISCV|RISC-V]] — open-standard ISA.

[[dis-2-9-7-c-to-assembly|Ch 2.9.7]] notes: *"this functionality is supported by any C compiler, and most compilers support compiling to a number of different assembly languages"* — the **workflow** (`-S` to emit, `-c` to assemble, `objdump -d` to disassemble) is universal, but each architecture produces incompatible `.s` files.

## Syntax conventions

Two competing surface syntaxes for x86:

- **AT&T syntax** (default on Linux / [[GCC|gcc]]): `movl source, dest`, registers prefixed `%`, immediates prefixed `$`, memory operand `disp(base, index, scale)`. The chapter's example `movl $1, -8(%ebp)` follows this.
- **Intel syntax**: `mov dest, source`, no prefixes, memory `[base + index*scale + disp]`. Used by Microsoft tools and most ISA reference manuals.

## The C-to-assembly mapping

[[dis-2-9-7-c-to-assembly|Ch 2.9.7]]'s worked `simpleops.c` example shows a **direct, almost line-by-line** correspondence between C statements and IA32 instructions:

```c
x = 1;          // movl $1, -8(%ebp)
x = x + 2;      // addl $2, -8(%ebp)
y = x * 100;    // movl -8(%ebp), %eax; imull $100, %eax, %eax; movl %eax, -4(%ebp)
```

What the mapping surfaces:

- **[[LocalVariable|Local variables]] live at stack-frame offsets** from `%ebp` (`x` at `-8(%ebp)`, `y` at `-4(%ebp)`) — the [[StackFrame|stack-frame]] machinery [[dis-1-4-functions|Ch 1.4]] introduced becomes byte-addressable.
- **Memory-operand arithmetic** — `addl`/`subl` can target memory directly, no register round-trip required.
- **Multiply requires a register** — `imull` only operates on registers, so `y = x * 100` becomes load-into-`%eax` → multiply-in-`%eax` → store-back.
- **AT&T direction** — `mov src, dst` reads left-to-right as data flows.

## Why expose assembly at all

Three reasons [[dis-2-9-7-c-to-assembly|Ch 2.9.7]] codifies:

1. **Inspection** — read the compiler's output to understand what your C actually does (load order, register allocation, optimization effects).
2. **Hand-writing** — drop into assembly for performance-critical inner loops, or for instructions the compiler won't emit (atomics, SIMD intrinsics, syscall stubs).
3. **Mixed-language linking** — `gcc -m32 -o myprog myfunc.o main.c` links hand-written assembly with C through the standard [[LinkingStage|link-edit]] path.

## Toolchain entry/exit points

| Operation | Tool | Direction |
|---|---|---|
| C → assembly | [[GCC\|`gcc -S`]] (stops after [[CompilationStage\|compile]]) | emit |
| Assembly → object | [[GCC\|`gcc -c`]] / `as` (the [[AssemblyStage\|assemble]] stage) | assemble |
| Object → assembly | [[Objdump\|`objdump -d`]] | disassemble |

## Connections

- [[dis-2-9-7-c-to-assembly]] — promoting source; the [[CLanguage|C]]-to-assembly worked example.
- [[dis-2-9-5-libraries]] — names assembly as the `.s` artifact `gcc -S` emits.
- [[CompilationStage]] — the stage whose **output** is assembly.
- [[AssemblyStage]] — the stage whose **input** is assembly.
- [[CompilationProcess]] — the surrounding pipeline.
- [[GCC]] — the driver that emits and consumes `.s` files.
- [[Objdump]] — disassembles [[ObjectFile|`.o` files]] back to assembly text.
- [[ISA]] — the architecture surface assembly maps onto.
- [[IA32]] — the specific assembly dialect used by [[dis-2-9-7-c-to-assembly|Ch 2.9.7]]'s examples.
- [[CLanguage]] — the higher-level source language.
- [[ObjectFile]] — the binary form assembly assembles into.
- [[BinaryExecutable]] — the final form after [[LinkingStage|linking]].
- [[ComputerArchitecture]] — the Ch 3 subject assembly opens onto.
