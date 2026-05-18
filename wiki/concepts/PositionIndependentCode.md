---
title: "Position-Independent Code (-fPIC)"
type: concept
tags: [c-language, build, toolchain, dynamic-library, address-space]
sources: [dis-2-9-6-writing-libraries]
last_updated: 2026-05-17
---

# Position-Independent Code (-fPIC)

**Position-Independent Code (PIC)** is machine code that executes correctly regardless of the [[AddressSpace|address]] at which it is loaded — no bake-in of absolute addresses, all internal references reached via PC-relative offsets or [[GOT|Global Offset Table]] indirection. Required for [[DynamicLibrary|shared objects (`.so`)]] because the [[DynamicLinker|dynamic linker]] maps each `.so` at a runtime-chosen address that varies per process (and per launch under [[ASLR|ASLR]]).

[[GCC|`gcc`]] generates PIC with the **`-fPIC`** flag, introduced in [[dis-2-9-6-writing-libraries|DIS Ch 2.9.6]] as part of the two-step shared-object build:

```bash
gcc -fPIC -c mylib.c       # PIC-compiled object file
gcc -shared -o libmylib.so mylib.o
```

## Why shared objects need PIC

A non-PIC `.o` contains absolute addresses for globals and function calls — *"the value at address `0x401234`"*. If two processes load the same `.so` at different addresses, those absolute addresses are wrong in at least one process. Three resolution strategies exist:

1. **Load-time relocation** — the dynamic linker rewrites every absolute address per load. Defeats memory sharing (each process needs its own patched copy of the `.text` section) and is slow at launch.
2. **Fixed load address** — every consumer agrees to load the `.so` at the same address. Defeats [[ASLR|ASLR]] and forces global coordination across all libraries.
3. **Position-independent code** — all references are PC-relative or [[GOT|GOT]]-indirect, so the same `.text` works at any address. **The standard solution.**

## `-fPIC` vs `-fpic`

- **`-fPIC`** — full position-independent code, no GOT-size limit. The portable choice; mandatory on some architectures (x86-64, ARM64).
- **`-fpic`** — same idea but assumes a small GOT (~64 KB on x86). Slightly faster code, but fails to link if the GOT grows past the limit. Mostly obsolete.

DIS Ch 2.9.6 uses uppercase `-fPIC` — the safe default.

## Skipping `-fPIC`: the silent footgun

`gcc -shared -o libmylib.so mylib.o` (without `-fPIC` at the compile step) is **not a hard error on x86** — the linker emits text relocations, the loader applies them at load time, and the `.so` works. But:

- Memory pages can no longer be shared across processes (each process patches its own copy).
- `SELinux` and modern hardening configurations **reject** text relocations as a security risk.
- On x86-64 and ARM64, the build **does** fail with *"relocation R_X86_64_32 against `.rodata' can not be used when making a PIE object; recompile with -fPIC"*.

## Connections

- [[dis-2-9-6-writing-libraries]] — introducing source.
- [[DynamicLibrary]] — `-fPIC` is mandatory for `.so` builds.
- [[StaticLibrary]] — `-fPIC` is **not** needed for `.a` archives (statically linked into one fixed-address executable).
- [[GCC]] — the compiler that consumes the flag.
- [[Linker]] — `ld -shared` produces the `.so` from PIC `.o` files.
- [[CompilationProcess]] — `-fPIC` affects stage 2 (compile) code generation.
- [[AddressSpace]] — the runtime-varying address PIC accommodates.
- [[GOT]] — the indirection table PIC uses for global references.
- [[ASLR]] — the security feature PIC enables.
- [[BinaryExecutable]] — modern Linux distros build executables as PIEs (Position-Independent Executables) using the same mechanism.
