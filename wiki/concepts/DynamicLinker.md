---
title: "Dynamic Linker (ld.so / ld-linux.so)"
type: concept
tags: [linker, runtime, dynamic-linking, toolchain]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Dynamic Linker (`ld.so` / `ld-linux.so`)

The **dynamic linker** is the userspace program that performs **stage 5** ([[RuntimeLinking|runtime linking]]) of the [[CompilationProcess|compile pipeline]] [[dis-2-9-5-libraries|DIS Ch 2.9.5]] codifies — it loads [[DynamicLibrary|`.so`]] shared objects into a launching process's [[AddressSpace|address space]] and resolves the deferred symbol references the build-time [[Linker|`ld`]] left in stage 4.

On Linux it lives at `/lib64/ld-linux-x86-64.so.2` (or arch-specific variants); on glibc systems the `man 8 ld.so` documents it. On macOS the equivalent is `dyld`; on Windows it is the loader inside `kernel32.dll`.

## Distinction from the build-time linker

The names are similar — the **build-time linker** is `/usr/bin/ld` (or `lld`), the **dynamic linker** is `/lib64/ld-linux*.so`. They are **different programs** with **complementary roles**:

| | Build-time linker (`ld`) | Dynamic linker (`ld.so`) |
|---|---|---|
| When | Stage 4 ([[LinkingStage|link-edit]]) at build time | Stage 5 ([[RuntimeLinking|runtime link]]) at process launch |
| Invocation | Implicit from [[GCC|`gcc`]] | Implicit from the kernel via ELF `INTERP` |
| Output | An executable or `.so` file | A running process |
| Failure mode | [[UndefinedReferenceError|*"undefined reference"*]] | *"cannot open shared object file"* |

## Search path

In order:
1. `DT_RPATH` / `DT_RUNPATH` in the executable (rarely used).
2. [[LDLibraryPath|`LD_LIBRARY_PATH`]] env var.
3. `/etc/ld.so.cache` (built by `ldconfig` from `/etc/ld.so.conf`).
4. Default paths `/lib` and `/usr/lib`.

## Useful invocations

```
ldd ./prog                  # list NEEDED .so files and resolved paths
LD_DEBUG=files ./prog       # trace dynamic linker's resolution
LD_PRELOAD=./shim.so ./prog # inject a .so before the regular ones
LD_BIND_NOW=1 ./prog        # force eager binding (vs. lazy PLT)
```

## Why a userspace program, not the kernel

Putting the dynamic linker in userspace keeps the kernel small and the linking protocol upgradable independent of the kernel. The kernel knows only how to start `ld.so`; everything else is libc/glibc territory.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[RuntimeLinking]] — the stage this program implements.
- [[Linker]] — the build-time counterpart.
- [[DynamicLibrary]] — what it loads.
- [[DynamicLinking]] — the mode it enables.
- [[LDLibraryPath]] — its search-path override.
- [[AddressSpace]] — where it maps `.so` files.
- [[ELF]] — the format whose `INTERP` field names it.
