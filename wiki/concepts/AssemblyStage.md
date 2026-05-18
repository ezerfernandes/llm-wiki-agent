---
title: "Assembly Stage"
type: concept
tags: [c-language, assembler, toolchain, compilation-process]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Assembly Stage

The **assembly stage** is stage 3 of the five-stage [[CompilationProcess|compile pipeline]] [[dis-2-9-5-libraries|DIS Ch 2.9.5]] codifies. It takes the [[AssemblyLanguage|assembly]] `.s` file (output of the [[CompilationStage|compile]] stage) and translates it to **machine-code binary** packaged as an [[ObjectFile|`.o` object file]] — same instructions, different format.

## What the assembler does

- **Mnemonic-to-opcode translation** — `mov %rax, %rbx` becomes the corresponding bytes for the target ISA.
- **Symbol table emission** — record names and offsets for every defined function/global.
- **Relocation entries** — leave placeholder addresses for external references (to be patched by the [[Linker|linker]] at stage 4).
- **Section layout** — pack code into `.text`, initialized globals into `.data`, zero globals into `.bss`, constants into `.rodata`.

On Linux the resulting `.o` is in [[ELF|ELF]] format.

## Output

A `.o` [[ObjectFile|object file]]. [[GCC|`gcc -c foo.c`]] stops after assembly and emits `foo.o`. The conventional Linux assembler is `as` (binutils); LLVM's is `llvm-mc`.

## Why this is its own stage

The translation from assembly to binary is mostly mechanical — no language semantics, no symbol resolution across files. Separating it from the prior [[CompilationStage|compile]] stage lets the compiler emit human-readable `.s` (debuggable, inspectable with `gcc -S`) and lets the toolchain accept hand-written assembly via the same `.s → .o` path.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[CompilationProcess]] — the surrounding pipeline.
- [[AssemblyLanguage]] — the input language.
- [[ObjectFile]] — the output file format.
- [[GCC]] — `-c` flag.
- [[CompilationStage]] — the previous stage.
- [[LinkingStage]] — the next stage.
- [[ELF]] — the binary format on Linux.
