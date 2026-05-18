---
title: "Byte Order (Endianness)"
type: concept
tags: [binary, memory, byte-order, endianness, computer-systems, hardware]
sources: [dis-4-7-byte-order]
last_updated: 2026-05-17
---

# Byte Order (Endianness)

**Byte order** — also called **endianness** — is the convention by which the [[Byte|bytes]] of a multibyte value (a 2 / 4 / 8-byte integer, a [[FloatingPoint|float]], a pointer) are laid out across consecutive [[MemoryAddress|memory addresses]]. It is a property of the [[CPU]] / [[InstructionSetArchitecture|ISA]] — not of the language or program — and becomes observable whenever bytes cross a machine, file, or wire boundary.

Single-byte values (`char`, `uint8_t`, `bool`) have no endianness — the question is only meaningful for values wider than one byte.

> *"Byte order, sometimes referred to as endianness, describes the order in which the bytes of a multibyte value are ordered in memory."* — [[dis-4-7-byte-order|*Dive into Systems* Ch 4.7]]

## The two conventions

### Big-endian

The **most significant byte (MSByte)** sits at the **lowest** memory address; bytes follow in **descending** significance. Matches the conventional left-to-right written order of decimal / hex numerals.

For `int value = 0xAABBCCDD;` at address `p`:

| Address | `p`  | `p+1` | `p+2` | `p+3` |
|---------|------|-------|-------|-------|
| Byte    | `AA` | `BB`  | `CC`  | `DD`  |

Used by: [[PowerPC]] (default), [[SPARC]], [[Motorola68k]], [[IBM360]] mainframes, [[NetworkByteOrder|network byte order]], [[JavaVirtualMachine|JVM]] internal layout.

See [[BigEndian]] (this page is the umbrella).

### Little-endian

The **least significant byte (LSByte)** sits at the **lowest** memory address; bytes follow in **ascending** significance. Appears reversed compared to the written numeral.

For `int value = 0xAABBCCDD;` at address `p`:

| Address | `p`  | `p+1` | `p+2` | `p+3` |
|---------|------|-------|-------|-------|
| Byte    | `DD` | `CC`  | `BB`  | `AA`  |

Used by: [[X86]] / x86-64 (universal), [[ARM]] (default in [[ARMv7]] / [[ARMv8]] / [[AArch64]] — technically bi-endian but virtually always little-endian in practice), [[RISCV|RISC-V]] (default), [[Alpha]], [[VAX]].

See [[LittleEndian]] (this page is the umbrella).

## Detection in C

The chapter's worked program aliases an `int` through a `char *` and walks one byte at a time — [[PointerArithmetic|pointer arithmetic]] on `char *` advances by exactly one byte:

```c
int value = 0xAABBCCDD;
char *p = (char *) &value;
for (int i = 0; i < sizeof(value); i++) {
    printf("Address: %p, Value: %02hhX\n", p, *p);
    p += 1;
}
```

On x86 / x86-64 the output is `DD CC BB AA` — confirming [[LittleEndian|little-endian]]. The `%02hhX` specifier prints a `signed char` as two hex digits.

For production code, prefer compile-time detection:

```c
#if __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
   /* little-endian path */
#elif __BYTE_ORDER__ == __ORDER_BIG_ENDIAN__
   /* big-endian path */
#endif
```

(GCC / Clang predefined macros; equivalent: [[POSIX]] `<endian.h>` `BYTE_ORDER == LITTLE_ENDIAN`.)

## When endianness matters

Three scenarios where the host's endianness leaks out of the [[Abstraction|abstraction]]:

1. **Network transmission.** Packets serialize integers as byte streams; the [[IETF]] standardizes **big-endian as [[NetworkByteOrder|network byte order]]** so [[TCPIP|TCP/IP]] / [[UDP]] / most binary protocols are interoperable regardless of host endianness. [[POSIX]] supplies `htonl` / `htons` / `ntohl` / `ntohs` (in `<arpa/inet.h>`) — on big-endian hosts these are no-ops; on little-endian hosts they byte-swap.

2. **File formats.** A binary file written on one host and read on another with different endianness yields garbage unless the format pins endianness. Common pinnings: [[JPEG]] (big-endian), [[BMP]] / [[PNG]] (mixed — some fields big, some little), [[WAV]] / [[RIFF]] (little-endian), [[TIFF]] (declares per-file via the `II` / `MM` magic). Text formats sidestep the issue at the integer layer but reappear in [[UTF16|UTF-16]] / [[UTF32|UTF-32]] via the [[ByteOrderMark|BOM]] (`U+FEFF`) at file start.

3. **Debugger / raw-memory inspection.** [[GdbExamineMemory|`gdb`'s `x/4xb` command]], `od -tx1`, `hexdump -C`, and similar tools show **raw byte sequence** — which reads reversed compared to the value the program holds on little-endian hosts. A common source of beginner confusion when first reading `(gdb) x/4xb &my_int`.

## Conversion machinery

Cross-endian conversion is a **[[ByteSwap|byte swap]]** — reverse the byte order of a multibyte value. Common APIs:

- **[[POSIX]] network functions** — `htonl(x)` / `ntohl(x)` (32-bit) / `htons(x)` / `ntohs(x)` (16-bit) — host ↔ network byte order. *No-op on big-endian hosts; byte-swap on little-endian.*
- **GCC / Clang builtins** — `__builtin_bswap16(x)` / `__builtin_bswap32(x)` / `__builtin_bswap64(x)` — unconditional byte swap.
- **x86 instruction** — [[BSWAP|`bswap`]] — single-cycle 32 / 64-bit byte reverse (introduced in 80486). ARM equivalent: `REV` / `REV16`.
- **Manual** — `((x >> 24) & 0xFF) | ((x >> 8) & 0xFF00) | ((x << 8) & 0xFF0000) | ((x << 24) & 0xFF000000)` for 32-bit. Compilers recognize this idiom and emit `bswap`.

## Bi-endian architectures

Some ISAs are **bi-endian** — a runtime configuration bit selects mode. Examples:

- **[[ARM]]** — bi-endian; [[ARMv6]]+ adds `SETEND` instruction for in-flight mode switch. Linux / iOS / Android run [[LittleEndian|little-endian]]; some embedded firmware and routers run big-endian.
- **[[MIPS]]** — bi-endian; selected at boot via configuration pin. [[Cisco]] [[IOS]] historically ran big-endian MIPS.
- **[[PowerPC]]** — bi-endian; [[Linux]]-on-POWER ran big-endian historically, switched to little-endian in [[POWER8]]+ to ease porting from x86.

For most application programmers, the host is **little-endian** in 2025 — the [[X86]] / [[X86_64]] / [[ARM64|AArch64]] / [[RISCV64|RISC-V 64-bit]] convergence covers >99% of deployed CPUs.

## Etymology — the *"Holy Wars"* memo

The terms originate from Jonathan Swift's *[[GulliversTravels|Gulliver's Travels]]* (1726) — the Big-Endians and Little-Endians waged satirical war over which end of a soft-boiled egg to crack. **[[DannyCohen|Danny Cohen]]'s 1980 IEN-137 memo** *On Holy Wars and a Plea for Peace* coined the technical usage, explicitly framing the endianness debate as arbitrary-but-consequential — choose a convention and commit.

## Wiki context

This page is the **umbrella** for the byte-order family. Sub-pages:

- [[BigEndian]] — MSByte-first convention; [[NetworkByteOrder|network byte order]] standard; [[PowerPC]] / [[SPARC]] / [[Motorola68k]] historical home.
- [[LittleEndian]] — LSByte-first convention; the [[X86]] / [[ARM]] / [[RISCV|RISC-V]] modern standard.
- [[Endianness]] — alias term pointing back here (more common in code / docs; *byte order* is more common in textbooks).
- [[NetworkByteOrder]] — the big-endian convention used for cross-host serialization.
- [[ByteSwap]] — the conversion operation.

## Related concepts

- [[Byte]] — the 8-bit unit whose ordering is the subject.
- [[MemoryAddress]] — the address that bytes are laid out across.
- [[MostSignificantBit|MSBit]] / [[LeastSignificantBit|LSBit]] — the bit-level analogues; byte-level MSByte / LSByte scale up the same vocabulary.
- [[BinaryRepresentation]] — supplies the bit-string interpretation the byte layout sits on top of.
- [[BinaryNumber]] / [[HexadecimalNumber]] — the notation systems for the values being laid out.
- [[CCast]] / [[Aliasing]] — the [[CLanguage|C]] mechanism that exposes the byte layout to the program.
- [[PointerArithmetic]] — supplies the per-byte stride for `char *` walks.
- [[CPU]] / [[InstructionSetArchitecture|ISA]] — endianness is a property of these.
- [[Serialization]] — the cross-host-cross-time concern that endianness directly governs.
- [[FileFormat]] — the second canonical context where endianness leaks out.
- [[NetworkProtocol]] — the first canonical context (network packets).
- [[Unicode]] / [[UTF16]] / [[UTF32]] — text encodings where endianness reappears at the code-unit layer via the [[ByteOrderMark|BOM]].
- [[MemoryAlignment]] — orthogonal layout concern (gaps between fields, not byte order within a field).
- [[CacheLine]] / [[MemoryHierarchy]] — the performance layer above the byte-layout question.
