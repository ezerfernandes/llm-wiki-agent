---
title: "objdump"
type: concept
tags: [binutils, disassembler, toolchain, inspection, elf]
sources: [dis-2-9-7-c-to-assembly]
last_updated: 2026-05-17
---

# objdump

**`objdump`** is the GNU binutils **disassembler** — the inverse of the [[AssemblyStage|assemble stage]]. Given an [[ObjectFile|`.o` file]] or a [[BinaryExecutable|binary executable]], it reads the machine-code bytes and emits the corresponding [[AssemblyLanguage|assembly]] mnemonics annotated with byte offsets.

[[dis-2-9-7-c-to-assembly|DIS Ch 2.9.7]]: *"Systems provide utilities that allow users to view binary files. For example, `objdump` displays the machine code and assembly code mappings in `.o` files:*

```
$ objdump -d simpleops.o
```

## The `-d` flag

`-d` requests **disassembly** of all executable (`.text`) sections. Other flags: `-x` (all headers), `-t` (symbol table), `-r` (relocations), `-S` (source-interleaved when `.o` has `-g` debug info), `-M intel` (Intel syntax instead of AT&T default).

## Round-trip with the compile pipeline

```
   .c              .s              .o              executable
    |    -S         |    -c          |    (link)         |
    +-------------> +--------------> +-----------------> +
                                     |
                                     | objdump -d
                                     v
                                  assembly text
```

`objdump` closes the loop by giving the **user** access to the same assembly the toolchain produced internally — even when the original `.s` was discarded (e.g., the user only ran `gcc -c foo.c`, not `gcc -S foo.c`).

## Why this matters

- **Verify compiler output** — when [[GCC|`gcc`]] doesn't expose `.s` (e.g., compiled with `-c` only), disassemble the `.o` to see what it generated.
- **Inspect optimized code** — `gcc -O2 -c` may produce assembly that doesn't match the C line-by-line; disassembly shows the real instruction stream.
- **Read libraries you don't have source for** — system `.a` archives, vendor `.so` files.
- **Debug at the instruction level** — pair with [[GDB|gdb]] `disas` to step through assembly.

## Related tools

- `as` — the assembler ([[AssemblyStage|`.s → .o`]]); inverse of `objdump -d`.
- `nm` — symbol-table dumper (lighter weight than `objdump -t`).
- `readelf` — ELF-format inspector; overlap with `objdump -x` but ELF-specific.
- `strings` — extract printable strings (forensic complement).

## Connections

- [[dis-2-9-7-c-to-assembly]] — introducing source.
- [[AssemblyLanguage]] — what `objdump -d` emits.
- [[AssemblyStage]] — the stage `objdump` inverts.
- [[ObjectFile]] — the typical input.
- [[BinaryExecutable]] — also a valid input.
- [[ELF]] — the binary format on Linux.
- [[GCC]] — the toolchain `objdump` lives alongside.
- [[GDB]] — pairs with `objdump` for instruction-level debugging.
