---
title: "Runtime Linking"
type: concept
tags: [linker, runtime, dynamic-linking, toolchain, compilation-process]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Runtime Linking

**Runtime linking** is stage 5 of the five-stage [[CompilationProcess|compile pipeline]] [[dis-2-9-5-libraries|DIS Ch 2.9.5]] codifies — the **only stage that runs at process launch, not at build time**. The [[DynamicLinker|dynamic linker]] (`ld.so` / `ld-linux.so` on Linux) maps each required [[DynamicLibrary|`.so`]] into the process's [[AddressSpace|address space]] and resolves the deferred symbol references the build-time [[Linker|`ld`]] left in stage 4 ([[LinkingStage|link-editing]]).

## Trigger

The Linux kernel notices the `INTERP` field in the executable's ELF header (typically `/lib64/ld-linux-x86-64.so.2`) and hands control to that interpreter instead of jumping directly to the program's `_start`. The interpreter is the [[DynamicLinker|dynamic linker]].

## What it does

1. Reads the executable's `.dynamic` section to enumerate `NEEDED` libraries.
2. For each `NEEDED` entry (e.g., `libc.so.6`), searches:
   - the cache `/etc/ld.so.cache` (built by `ldconfig`),
   - the rpath embedded in the binary,
   - [[LDLibraryPath|`LD_LIBRARY_PATH`]],
   - the default paths `/lib` / `/usr/lib`.
3. `mmap`s the `.so` into the process address space (shared read-only text pages, private writable data).
4. Recursively resolves the `.so`'s own `NEEDED` dependencies.
5. Performs **relocations** — patches the `GOT` (Global Offset Table) entries with actual function/data addresses.
6. Calls each library's `_init` constructors.
7. Jumps to the executable's `_start`.

## Lazy vs eager resolution

By default the dynamic linker uses **lazy binding** via the PLT (Procedure Linkage Table) — function addresses are resolved on first call, amortizing startup cost. `LD_BIND_NOW=1` forces **eager binding** — all symbols resolved before `main`, predictable but slower startup.

## Failure mode

If a `NEEDED` `.so` cannot be found at launch: `error while loading shared libraries: libfoo.so.1: cannot open shared object file: No such file or directory`. The process never reaches `main`. Fix: install the runtime package or set [[LDLibraryPath|`LD_LIBRARY_PATH`]].

## Why this stage exists separately

The split between build-time [[LinkingStage|link-editing]] (stage 4) and runtime linking (stage 5) is what makes [[DynamicLinking|dynamic linking]] possible. If everything were resolved at build time, every binary would have to be rebuilt when `libc.so` was patched. Stage 5 trades a small per-launch cost for system-wide library sharing and centralized patching.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[CompilationProcess]] — the surrounding five-stage pipeline.
- [[DynamicLinker]] — the agent (`ld.so` / `ld-linux.so`).
- [[DynamicLibrary]] — the `.so` files mapped at this stage.
- [[DynamicLinking]] — the link mode that requires this stage.
- [[LinkingStage]] — the stage that defers work to here.
- [[LDLibraryPath]] — the search-path override consulted here.
- [[AddressSpace]] — the process memory where `.so`s are mapped.
- [[ELF]] — the format whose `INTERP` field triggers stage 5.
