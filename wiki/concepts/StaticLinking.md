---
title: "Static Linking"
type: concept
tags: [c-language, libraries, linker, build, static-linking]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Static Linking

**Static linking** is the [[Linker|linker]]'s mode where every referenced symbol's machine code is **copied from a [[StaticLibrary|`.a` archive]] (or `.o` file) directly into the [[BinaryExecutable|executable]]** at stage 4 of the [[CompilationProcess|compile pipeline]]. The resulting binary is **self-contained** — no [[DynamicLibrary|`.so`]] dependency at launch. Per [[dis-2-9-5-libraries|DIS Ch 2.9.5]], `--static` forces archive-only resolution even when a shared object is present.

## How to invoke

```
gcc main.c -lfoo --static -o main
```

Without `--static` the linker prefers a `.so` if one exists alongside the `.a`; with `--static` it ignores the `.so` and pulls members out of `libfoo.a`.

## Mechanism

The linker:
1. Scans every undefined reference in the input `.o` files.
2. For each `-l<name>`, opens `lib<name>.a` and **selectively pulls only the `.o` archive members that define a needed symbol** (transitively — pulled members may themselves have undefined references).
3. Concatenates all pulled code into the output executable's `.text` segment and resolves all symbol references to fixed in-binary addresses.

The whole archive is **not** copied — only the members actually used. A 50 MB `libfoo.a` from which `main` uses three functions might add 30 KB to the executable.

## When it's the right choice

- **Single-file distribution** — no runtime dependency wrangling.
- **Frozen build** — the binary's behavior cannot change because someone replaced `libfoo.so` on the host.
- **No dynamic loader available** — [[BareMetalProgramming|bare-metal]] firmware, early-boot tools, container scratch images.
- **Security-sensitive contexts** — Go binaries, most Rust binaries, statically linked C tools — known supply-chain surface at build time.

## When it's the wrong choice

- **Library memory sharing matters** — every statically linked Linux binary carries its own ~2 MB `libc` copy; dynamic linking shares one resident copy across hundreds of processes.
- **Centralized patching matters** — a CVE in `libc` requires rebuilding **every** statically linked consumer.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[DynamicLinking]] — the contrasting default mode.
- [[StaticLibrary]] — the `.a` archive consumed.
- [[Linker]] — the agent that does the work.
- [[LinkingStage]] — stage 4 of the pipeline.
- [[BinaryExecutable]] — the self-contained result.
- [[GCC]] — `--static` flag.
- [[BareMetalProgramming]] — context where static linking is mandatory (no `ld.so` exists).
