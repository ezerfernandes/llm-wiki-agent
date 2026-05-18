---
title: "Static Library (.a archive)"
type: concept
tags: [c-language, libraries, linker, static-linking, build]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Static Library (`lib<name>.a`)

A **static library** is the [[CLibrary|C-library]] implementation-half packaged as a `lib<name>.a` **archive** — a [[Unix|Unix]] `ar` (archiver) bundle of [[ObjectFile|`.o`]] files. Per [[dis-2-9-5-libraries|DIS Ch 2.9.5]], at [[StaticLinking|static-link]] time the [[Linker|linker]] **copies every referenced symbol's machine code from the archive into the final [[BinaryExecutable|executable]]**, producing a **self-contained binary** with no library dependency at launch.

## Anatomy

- File extension: `.a` (for "archive").
- Built by the library author with `ar rcs libfoo.a foo1.o foo2.o ...` after compiling each `.c` to `.o` with `gcc -c`.
- The archive is **not** itself an executable format — it is a concatenation-with-index of `.o` files. The [[Linker|linker]] cherry-picks **only the `.o` members containing symbols the executable actually uses**, not the whole archive.

## How it's consumed

```
gcc main.c -L. -lfoo --static -o main
```

- `-lfoo` finds `libfoo.a` (or `libfoo.so` — `--static` forces archive).
- Resulting `main` contains its own copy of the library's used symbols.

## Tradeoffs vs [[DynamicLibrary|dynamic libraries]]

| Axis | Static (`.a`) | Dynamic (`.so`) |
|---|---|---|
| Binary size | Larger (library code inlined) | Smaller (reference only) |
| Launch dependencies | None — self-contained | [[DynamicLinker|`ld.so`]] must find the `.so` |
| Memory sharing | Each process has its own copy | One in-memory copy across processes |
| Patching | Rebuild every consumer | Replace the `.so` once, system-wide |
| Predictability | Frozen at build time | Subject to host's installed `.so` versions |

Static libraries are the right choice when build-time-frozen behavior matters (firmware, security-sensitive binaries, single-file distributions); dynamic libraries are the right choice when memory footprint and centralized patching matter (most desktop / server software).

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[CLibrary]] — the umbrella concept.
- [[DynamicLibrary]] — the contrasting `.so` format.
- [[StaticLinking]] — the link mode that consumes archives.
- [[Linker]] — what reads and resolves `.a` members.
- [[ObjectFile]] — the constituent format inside an archive.
- [[GCC]] — `--static` forces archive resolution.
- [[BareMetalProgramming]] — embedded firmware overwhelmingly uses static libraries (no dynamic loader exists).
