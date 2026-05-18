---
title: "Big-Endian"
type: concept
tags: [binary, memory, byte-order, endianness, big-endian]
sources: [dis-4-7-byte-order]
last_updated: 2026-05-17
---

# Big-Endian

**Big-endian** is one of the two [[ByteOrder|byte-order]] conventions: the **most significant byte (MSByte)** of a multibyte value occupies the **lowest** memory address, with subsequent bytes following in **descending** significance. Bytes appear in the same left-to-right order as the conventional written-numeral form.

For `int value = 0xAABBCCDD;` at address `p`:

| Address | `p`  | `p+1` | `p+2` | `p+3` |
|---------|------|-------|-------|-------|
| Byte    | `AA` | `BB`  | `CC`  | `DD`  |

## Where it's used

- **[[NetworkByteOrder|Network byte order]]** — the [[IETF]]-mandated convention for [[TCPIP|TCP/IP]] / [[UDP]] / most binary network protocols. *"The IETF (Internet Engineering Task Force) defines big-endian as the network byte order."* — [[dis-4-7-byte-order|*Dive into Systems* Ch 4.7]].
- **[[PowerPC]]** — default mode (bi-endian; runs little-endian in [[POWER8]]+ Linux configurations).
- **[[SPARC]]** — [[Sun]] / [[Oracle]] workstations and servers.
- **[[Motorola68k]]** — classic Mac, Amiga, Atari ST, early Sun.
- **[[IBM360]]** / [[IBMZArchitecture|z/Architecture]] — IBM mainframes.
- **[[JavaVirtualMachine|JVM]] internals** — the [[JVMByteCode|bytecode]] / class-file format pins big-endian (per the JVM spec) regardless of host.
- **Many file formats** — [[JPEG]] markers, [[TIFF]] (when `MM` magic is used), [[PNG]] chunk headers, [[ELF]] (on big-endian targets), historical Mac resource forks.

## Mental model

*"Big end first"* — the **big end** of the number (the high-order byte, the one that contributes the most to the value) comes **first** in memory. Matches how you read decimal numbers left-to-right: in `1234`, the `1` (thousands place — most significant) is leftmost. Big-endian memory follows the same convention.

## Practical implications

- **Reading raw memory is intuitive** — `gdb`'s `x/4xb` output matches the value's hex literal directly (no mental byte-reversal).
- **No conversion needed for network I/O** — `htonl(x) == x` and `ntohl(x) == x` on big-endian hosts; the [[POSIX]] network functions are no-ops.
- **Byte-by-byte comparison preserves numeric ordering** — `memcmp` on two big-endian integers returns the same sign as numeric comparison (modulo sign-bit issues). On little-endian hosts, `memcmp` is **unrelated** to numeric order.
- **Reads are sign-extension-aware** — loading the high byte first gives the sign immediately; some historical big-endian architectures exploited this for fast comparison.

## Decline in deployed hardware

As of 2025, big-endian is **rare** in deployed CPUs:

- [[X86]] / [[X86_64]] never supported big-endian — Intel committed to little-endian from the 8080.
- [[ARM]] AArch64 / ARMv8 runs little-endian almost universally (bi-endian capability exists but is dormant in [[Linux]] / [[iOS]] / [[Android]]).
- [[RISCV]] is little-endian by default.
- [[PowerPC]] flipped to little-endian in [[POWER8]] Linux distributions.

The **last major big-endian holdout** is the [[IBMZArchitecture|IBM z/Architecture]] mainframe family and network-protocol code paths.

## Related concepts

- [[ByteOrder]] — the umbrella concept covering both endianness conventions.
- [[LittleEndian]] — the opposite convention; dominates modern hardware.
- [[NetworkByteOrder]] — the standardization choice that makes big-endian permanently relevant.
- [[Endianness]] — common alias term for byte order.
- [[Htonl|`htonl` / `ntohl` / `htons` / `ntohs`]] — POSIX network byte-order conversion (no-op on big-endian hosts).
- [[ByteSwap]] — the cross-endian conversion operation.
- [[MostSignificantBit|MSByte]] — the high-order byte that big-endian places first.
- [[GulliversTravels]] — etymological origin (the "Big-Endians" who broke their eggs on the big end).
- [[DannyCohen]] — author of the 1980 IEN-137 *"On Holy Wars"* memo that coined the technical usage.
