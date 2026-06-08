---
title: "File modification time (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, filesystem, date-time]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/File_modification_time
---

## Summary
This task asks the programmer to read and write the modification time (mtime) of a file. The key insight is that filesystem metadata is exposed differently across platforms and runtimes — most languages provide a stat-style call to retrieve the timestamp and a separate utime-style call to set it, often requiring conversion between the OS epoch representation and the language's native date/time type.

## Task Requirements
- Get the modification time of a file.
- Set (change) the modification time of a file.

## Language Coverage
89 languages implement this task, reflecting how universally filesystem metadata access is supported. Representative implementations include C, C++, Python, Perl, Ruby, Go, Rust, Java, Haskell, and Tcl, spanning systems languages, scripting languages, and shell utilities.

## Connections
- [[Filesystem]] — the task operates on file metadata via the filesystem layer
- [[FileMetadata]] — modification time is one attribute of a file's stat record
- [[UnixTimestamp]] — mtime is typically stored as seconds since the epoch
- [[DateTimeHandling]] — converting between epoch values and native date/time types

## Contradictions
- None — reference task page.
