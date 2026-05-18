---
title: "Dynamic Library (.so shared object)"
type: concept
tags: [c-language, libraries, linker, dynamic-linking, runtime, build]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Dynamic Library (`lib<name>.so`)

A **dynamic library** (a.k.a. **shared object**) is the [[CLibrary|C-library]] implementation-half packaged as a `lib<name>.so` **shared object** — a position-independent binary loaded into a process's [[AddressSpace|address space]] **at launch** by the [[DynamicLinker|dynamic linker]] (`ld.so` / `ld-linux.so`). Per [[dis-2-9-5-libraries|DIS Ch 2.9.5]], at [[DynamicLinking|dynamic-link]] time the [[Linker|build-time linker]] only **records the symbol references** in the executable; the actual addresses are resolved at stage 5 ([[RuntimeLinking|runtime link]]) when the process starts.

## Anatomy

- File extension: `.so` on Linux/Unix (for "shared object"); `.dylib` on macOS; `.dll` on Windows.
- Built by the library author with `gcc -shared -fPIC -o libfoo.so foo1.c foo2.c` — `-fPIC` emits **position-independent code** so the library can load at any address.
- Versioned via the `libfoo.so.MAJOR.MINOR.PATCH` filename convention and symlinks (`libfoo.so.1 → libfoo.so.1.2.3`).

## How it's consumed

```
gcc main.c -L. -lfoo -o main      # build-time link: records reference
./main                            # launch: ld.so loads libfoo.so
```

The default `-l<name>` link prefers the `.so` over the `.a` when both exist. At launch, the [[DynamicLinker|dynamic linker]] searches `/lib`, `/usr/lib`, `/usr/local/lib`, and any path in [[LDLibraryPath|`LD_LIBRARY_PATH`]] for `libfoo.so`; failure surfaces as `error while loading shared libraries: libfoo.so.1: cannot open shared object file`.

## Tradeoffs vs [[StaticLibrary|static libraries]]

| Axis | Dynamic (`.so`) | Static (`.a`) |
|---|---|---|
| Binary size | Smaller — reference only | Larger — inlined |
| Memory sharing | One copy across all processes (`libc.so` shared system-wide) | Each binary has its own copy |
| Launch cost | [[DynamicLinker|`ld.so`]] resolution + page-in | None (already in executable) |
| Patching | Replace the `.so`, every consumer picks up the fix | Rebuild every consumer |
| Failure mode | Missing `.so` at launch — *"cannot open shared object file"* | Cannot happen — binary is self-contained |
| ABI fragility | A breaking change in the `.so` breaks every consumer | Frozen at build time |

## Why the default

The compiler defaults to dynamic when both are available because **the wins are systemic** — every process on a Linux system shares one resident copy of `libc.so` (saving hundreds of MB of RAM), and a security patch to `libc.so` applies to every binary without rebuilding. The cost — runtime resolution and ABI fragility — is acceptable for hosted environments.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[CLibrary]] — the umbrella concept.
- [[StaticLibrary]] — the contrasting `.a` archive.
- [[DynamicLinking]] — the link mode that defers symbol resolution.
- [[DynamicLinker]] — the runtime resolver (`ld.so` / `ld-linux.so`).
- [[RuntimeLinking]] — stage 5 of the [[CompilationProcess|pipeline]].
- [[LDLibraryPath]] — the runtime search-path env var.
- [[Linker]] / [[LinkingStage]] — stage-4 reference recording.
- [[AddressSpace]] — where `.so` files are mapped at launch.
- [[GCC]] — `-shared` / `-fPIC` flags to author a `.so`.
