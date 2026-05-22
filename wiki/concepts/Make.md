---
title: "Make"
type: concept
tags: [unix, build, tooling, c-language]
sources: [dis-app2-5-make]
last_updated: 2026-05-18
---

# Make

**`make`** is the canonical Unix build tool — a *dependency-driven, incremental* command runner that consults file modification times to rebuild only what is stale. Configured by a [[Makefile|Makefile]].

Per [[dis-app2-5-make|DIS Appendix 2.5]], `make` is essential once a [[CLanguage|C]] project has multiple `.c` / `.h` files, non-standard library paths, or complex link lines — the alternative is error-prone hand-typed [[GCC|`gcc`]] invocations.

## The rule model

A **rule** consists of three parts:

```
target: dep1 dep2 ...
<TAB>command to build target
```

`make`'s decision procedure: if any dependency is newer than the target (or the target doesn't exist), run the command. Otherwise skip.

## Selective rebuilding

Headline efficiency claim from DIS: `make` rebuilds *"just the object and executable files that depend on files that have been modified since the last time they were built."* In a project with N source files, editing one file triggers recompilation of only the affected `.o` plus the final link — not the full N-way rebuild.

## Variables

Conventional macros — `CC` (compiler), `CFLAGS` (compiler flags), `LDFLAGS` (linker flags), `SRCS` (sources) — are referenced with `$(NAME)`. Lets the same Makefile work across projects with minimal edits.

## Scope note

DIS covers basic Makefiles; for very large projects, modern alternatives include **CMake** and **GNU Autotools** (which *generate* Makefiles).

## Related
- [[Makefile]] — the file format consumed by `make`.
- [[CompilationProcess]] — what a Makefile orchestrates ([[PreprocessingStage|preprocess]] → [[CompilationStage|compile]] → [[AssemblyStage|assemble]] → [[LinkingStage|link]]).
- [[GCC]] — typical `$(CC)` value.
- [[DiveIntoSystems]] — Appendix 2.5.

## Sources
- [[dis-app2-5-make]] — DIS Appendix 2.5 *Makefiles*.
