---
title: "ar (archive utility)"
type: concept
tags: [c-language, build, toolchain, unix, static-library]
sources: [dis-2-9-6-writing-libraries]
last_updated: 2026-05-17
---

# ar (Archive Utility)

**`ar`** is the [[Unix|Unix]] archiver — a `tar`-like utility that bundles one or more [[ObjectFile|`.o` object files]] into a single [[StaticLibrary|`lib<name>.a` static archive]]. Introduced in [[dis-2-9-6-writing-libraries|DIS Ch 2.9.6]] as the build step that packages a [[CLibrary|C library]]'s implementation half for [[StaticLinking|static linking]].

Canonical invocation per Ch 2.9.6:

```bash
ar -rcs libmylib.a mylib.o
```

## Flag decomposition

| Flag | Meaning |
|---|---|
| `r` | **Insert with replacement** — add the listed `.o` files, overwriting same-named existing members. |
| `c` | **Create** the archive if it does not exist; suppress the *"creating archive"* warning. |
| `s` | **Write an index** of symbols into the archive — equivalent to running [[Ranlib|`ranlib`]] separately. The index is what makes selective member extraction at link time fast. |

The combined `-rcs` form is the modern convention; on older systems `ar rcs libmylib.a *.o` (no leading dash) is also accepted.

## Relationship to the linker

`ar` does **not** modify the `.o` files — it concatenates them with a header and a symbol index. At [[LinkingStage|link-edit time]] (stage 4 of the [[CompilationProcess|compile pipeline]]) the [[Linker|`ld`]] uses the symbol index to find which archive members satisfy unresolved references and pulls in **only those members**. Result: a `100 MB libfoo.a` archive can yield a `10 KB` contribution to the final executable if only a few functions are referenced.

## Relationship to `tar`

`ar` predates `tar` (both date to early Unix). The name *archiver* applies to both, but the file formats differ — `ar` archives carry a symbol index and per-member alignment; `tar` archives carry filesystem metadata (permissions, timestamps, ownership). `tar` won the general-purpose battle; `ar` survives almost exclusively for `.a` static libraries and Debian `.deb` packages.

## Companion tools

- [[Ranlib|`ranlib`]] — regenerates the symbol index of an existing archive. Mostly historical; `ar -s` does the same job in one step.
- `nm libfoo.a` — lists the symbols in each archive member; the canonical debugging tool for *"why isn't this symbol being pulled in?"* link errors.
- `ar t libfoo.a` — lists the archive's member files.
- `ar x libfoo.a` — extracts archive members as standalone `.o` files.

## Connections

- [[dis-2-9-6-writing-libraries]] — introducing source.
- [[StaticLibrary]] — the `.a` archive `ar` produces.
- [[ObjectFile]] — the `.o` inputs `ar` bundles.
- [[StaticLinking]] — the consumption mode that uses the archive.
- [[Linker]] — `ld` selectively pulls archive members at stage 4.
- [[CompilationProcess]] — `ar` is a stage-3.5 packaging step between assemble and link-edit.
- [[GCC]] — invokes `ld`, which consumes `.a` archives via `-l<name>`.
- [[CLibrary]] — the umbrella concept; static-archive packaging is one of its two implementation forms.
