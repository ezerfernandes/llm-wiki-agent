---
title: "Dive into Systems — Appendix 2.8 tar Archives"
type: source
tags: [unix, archive, compression, command-line]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/tar.html
---

## Summary
Eighth subchapter of [[DiveIntoSystems]] Appendix 2. Codifies [[Tar|`tar`]] as the canonical Unix archive utility — bundle many files into one *tape archive* (`.tar`), optionally pipelined through gzip (`.tar.gz`) or bzip2 (`.tar.bz2`) compression.

## Key Claims
- **Create**: `tar -cvf archive.tar file1 file2 dir/` — `-c` create, `-v` verbose, `-f` filename.
- **Extract**: `tar -xvf archive.tar` — `-x` extract.
- **List**: `tar -tvf archive.tar`.
- **gzip compression** (`-z`): `tar -czvf project.tar.gz mydir/` create; `tar -xzvf project.tar.gz` extract.
- **bzip2 compression** (`-j`): `tar -cjvf project.tar.bz2 mydir/`; `tar -xjvf ...` extract.
- Flags are routinely concatenated (`-cvf` rather than `-c -v -f`).
- Composes with [[SCP|`scp`]] (Appendix 2.3) — archive + compress *before* transferring to reduce wire time.

## Connections
- [[Tar]] — the archive tool.
- [[SCP]] — common downstream use case (bulk file transfer).
- [[UnixCommandLine]] — invocation context.
- [[DiveIntoSystems]] — 159th ingested chapter; **closes Appendix 2 first half (subchapters 2.1–2.8)**.

## Contradictions
- None.
