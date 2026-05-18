---
title: "Dynamic Linking"
type: concept
tags: [c-language, libraries, linker, runtime, dynamic-linking, build]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Dynamic Linking

**Dynamic linking** is the [[Linker|linker]]'s mode where library symbols are **referenced but not copied** at build time, with final address resolution deferred to **process launch** via the [[DynamicLinker|dynamic linker]] (`ld.so` / `ld-linux.so`). Per [[dis-2-9-5-libraries|DIS Ch 2.9.5]] this is **the default** when both [[DynamicLibrary|`.so`]] and [[StaticLibrary|`.a`]] forms of a library exist: *"the compiler can choose to dynamically link when both a shared object (`.so`) and an archive (`.a`) version of a library are available."*

## How to invoke

```
gcc main.c -lfoo -o main          # dynamic by default
./main                            # ld.so loads libfoo.so at launch
```

No special flag is required — dynamic is the [[GCC|`gcc`]] default. To force dynamic when a `.a` is preferred, point `-L<path>` at a directory containing only the `.so`.

## Two-phase mechanism

1. **Build time (stage 4 [[LinkingStage|link-edit]])** — [[Linker|`ld`]] records the dependency on `libfoo.so` in the executable's `.dynamic` section and inserts a `PLT` / `GOT` stub for each unresolved symbol; the binary file lists `libfoo.so.1` as a `NEEDED` entry.
2. **Launch time (stage 5 [[RuntimeLinking|runtime link]])** — the kernel hands control to [[DynamicLinker|`ld.so`]], which reads the `NEEDED` list, maps each `.so` into the process [[AddressSpace|address space]], and either eagerly or lazily resolves the `PLT` stubs to the actual function addresses.

## The wins

- **Memory sharing** — every process on a Linux system that uses `libc.so` shares **one in-memory copy** (read-only `.text` pages are demand-mapped from disk and reference-counted across processes). Hundreds of MB system-wide.
- **Centralized patching** — a security update to `libc.so` is picked up by every dynamic consumer on next launch, no rebuilds required.
- **Smaller binaries** — references only.

## The costs

- **ABI fragility** — a breaking change in `libfoo.so` breaks every consumer. This is why versioned `.so.MAJOR` symlinks exist.
- **Launch latency** — [[DynamicLinker|`ld.so`]] resolution adds (small but nonzero) per-process startup cost.
- **Runtime failure mode** — *"error while loading shared libraries: libfoo.so.1: cannot open shared object file"* — the executable builds fine but won't launch on hosts missing the `.so`. Fixed via [[LDLibraryPath|`LD_LIBRARY_PATH`]] or installing the runtime package.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[StaticLinking]] — the contrasting `--static` mode.
- [[DynamicLibrary]] — the `.so` shared object consumed.
- [[DynamicLinker]] — the launch-time resolver.
- [[RuntimeLinking]] — stage 5 of the pipeline.
- [[Linker]] — the build-time agent (stage 4).
- [[LDLibraryPath]] — the runtime search-path override.
- [[CompilationProcess]] — the surrounding pipeline.
- [[GCC]] — the default-dynamic compiler driver.
- [[AddressSpace]] — where `.so` files are mapped at launch.
