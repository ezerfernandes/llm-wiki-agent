---
title: "Undefined Reference Error"
type: concept
tags: [linker, build-error, c-language, toolchain]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Undefined Reference Error

**`undefined reference to 'foo'`** is the signature error message from the [[Linker|linker]] (`ld`) at stage 4 ([[LinkingStage|link-edit]]) of the [[CompilationProcess|compile pipeline]] [[dis-2-9-5-libraries|DIS Ch 2.9.5]] codifies. It means the compiler **saw a prototype for `foo`** (so the source typechecks) but the linker **could not find a binary symbol** matching `foo` in any input `.o` file, `.a` archive, or `.so` shared object.

## The canonical cause: missing `-l<name>`

```
gcc prog.c -o prog                  # error: undefined reference to `pow'
gcc prog.c -lm -o prog              # OK: -lm tells ld to look in libm
```

`#include <math.h>` brings in the **prototype** for `pow` (satisfying the [[CompilationStage|compiler]]); `-lm` brings in the **implementation** from `libm.{so,a}` (satisfying the linker). Per [[dis-2-9-5-libraries|Ch 2.9.5]] this is the load-bearing distinction: *"missing the implementation (the library) gives an 'undefined reference' error from the linker `ld`; missing the header gives an 'implicit declaration' warning or 'undeclared' error from the compiler."*

## Diagnostic taxonomy

| Symptom | Stage | Cause | Fix |
|---|---|---|---|
| `foo.h: No such file or directory` | 1 [[PreprocessingStage|preprocess]] | header not on disk | install `-dev` package, add `-I<path>` |
| `implicit declaration of function 'foo'` | 2 [[CompilationStage|compile]] | header not `#include`d | add `#include <foo.h>` |
| `undefined reference to 'foo'` | 4 [[LinkingStage|link]] | library not linked | add `-l<name>` (and maybe `-L<path>`) |
| `cannot open shared object file` | 5 [[RuntimeLinking|launch]] | `.so` not findable at runtime | install runtime package, set [[LDLibraryPath|`LD_LIBRARY_PATH`]] |

Each row is a distinct stage, distinct tool reporting the error, distinct fix.

## Other causes

- **Symbol name mismatch** — e.g., calling a C++ function from C without `extern "C"` ([[ExternC]] resolves this); or forgetting `#[no_mangle]` on a Rust function exported to C ([[NoMangle]]).
- **Wrong library order** — `ld` is single-pass left-to-right; `gcc -lm prog.c` may fail where `gcc prog.c -lm` succeeds because the math library must appear **after** the source/object that references it.
- **Architecture mismatch** — linking a 32-bit object against a 64-bit library.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[Linker]] — the tool that emits this error.
- [[LinkingStage]] — the stage where it occurs.
- [[CompilerVsLinker]] — the diagnostic-stage taxonomy.
- [[CompilationProcess]] — the surrounding pipeline.
- [[GCC]] — the driver; flags `-l<name>` / `-L<path>` are the fix.
- [[ExternC]] / [[NoMangle]] — the Rust-side fixes for cross-language linkage.
- [[CStandardLibrary]] / [[CLibrary]] — what the user is trying to link against.
