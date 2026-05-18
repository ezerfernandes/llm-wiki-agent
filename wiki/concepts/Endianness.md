---
title: "Endianness"
type: concept
tags: [binary, memory, byte-order, endianness, alias]
sources: [dis-4-7-byte-order]
last_updated: 2026-05-17
---

# Endianness

**Endianness** is the common code / documentation term for what [[dis-4-7-byte-order|*Dive into Systems* Ch 4.7]] calls **[[ByteOrder|byte order]]** — the convention by which the [[Byte|bytes]] of a multibyte value are laid out across consecutive [[MemoryAddress|memory addresses]].

**See [[ByteOrder]] for the full treatment.** This page exists as a discoverability alias — *endianness* dominates in source code (GCC's `__BYTE_ORDER__`, POSIX `<endian.h>`, Rust's `to_le` / `to_be`, Python's `struct.pack(">i", x)`) while *byte order* dominates in textbooks.

## The two values

- **[[BigEndian|Big-endian]]** — MSByte at lowest address (left-to-right, matches written numerals). Used by [[NetworkByteOrder|network protocols]], [[PowerPC]], [[SPARC]], [[JavaVirtualMachine|JVM]] internals.
- **[[LittleEndian|Little-endian]]** — LSByte at lowest address (reversed from written numerals). Used by [[X86]] / [[X86_64]], [[ARM]] (default), [[RISCV|RISC-V]], [[Alpha]] — virtually all deployed modern CPUs as of 2025.

## Etymology

From Jonathan Swift's *[[GulliversTravels|Gulliver's Travels]]* (1726) via [[DannyCohen|Danny Cohen]]'s 1980 [[IETF]] IEN-137 memo *On Holy Wars and a Plea for Peace*.

## Related concepts

- [[ByteOrder]] — the canonical wiki page; this page is an alias pointer.
- [[BigEndian]] / [[LittleEndian]] — the two sub-conventions.
- [[NetworkByteOrder]] — the big-endian standard for cross-host serialization.
- [[ByteSwap]] — the conversion operation between the two.
- [[Htonl|`htonl` / `ntohl`]] — POSIX host ↔ network byte order functions.
