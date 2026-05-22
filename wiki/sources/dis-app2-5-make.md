---
title: "Dive into Systems — Appendix 2.5 Make and Makefiles"
type: source
tags: [unix, build, make, c-language]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/makefiles.html
---

## Summary
Fifth subchapter of [[DiveIntoSystems]] Appendix 2. Promotes the [[Make|`make`]] build tool from forward-reference to first-class coverage — the *target / dependency / rule* model, variables, and *modification-time-driven selective rebuilding* that makes multi-file [[CLanguage|C]] projects manageable.

## Key Claims
- A **Makefile rule** has three parts: a **target** (file to build), zero or more **dependencies** (files it needs), and a **command** (recipe to produce the target).
- **Selective rebuild**: `make` consults file modification times and rebuilds *"just the object and executable files that depend on files that have been modified since the last time they were built."*
- **Variables** like `CC` (compiler), `CFLAGS` (flags), `SRCS` (sources) are referenced via `$(NAME)` — makes Makefiles reusable across projects.
- **Why use it**: hand-typed multi-file [[GCC|`gcc`]] commands with non-standard include paths and libraries are error-prone; `make` automates and minimizes rebuild work.
- **Modern alternatives** (CMake, GNU Autotools) exist for very large projects; basic Makefiles remain fundamental.

## Connections
- [[Make]] — the tool; promoted from forward-reference to fully treated.
- [[Makefile]] — the file format (already in the wiki via [[MLOps]]); DIS adds the C-build canonical use case.
- [[CompilationProcess]] / [[GCC]] — the underlying invocations a Makefile orchestrates.
- [[DiveIntoSystems]] — 156th ingested chapter.

## Contradictions
- None — DIS's C-build framing complements the [[Makefile]] page's existing MLOps-side framing.
