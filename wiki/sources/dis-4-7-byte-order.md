---
title: "Dive into Systems — Ch 4.7 Integer Byte Order"
type: source
tags: [dive-into-systems, ch4, binary, byte-order, endianness, memory, computer-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/byte_order.html
sources: [dis-4-7-byte-order]
last_updated: 2026-05-17
---

# Dive into Systems — Ch 4.7 *Integer Byte Order*

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 4.7** of *[[DiveIntoSystems]]* — the **memory-layout section** that closes Ch 4 *Binary and Data Representation* by codifying **[[ByteOrder|byte order]]** (a.k.a. [[Endianness|endianness]]): how the [[Byte|bytes]] of a multibyte integer are laid out across consecutive [[MemoryAddress|memory addresses]]. Bridges from Ch 4.1–4.6's value-level [[BinaryRepresentation|binary]] / [[BinaryArithmetic|arithmetic]] / [[BitwiseOperator|bit-manipulation]] surface — which treated multibyte integers as undifferentiated bit-strings — to the **address-level layout** that matters whenever bytes cross machine / file / wire boundaries. Distinguishes [[BigEndian|big-endian]] (MSByte at lowest address — left-to-right reading order) from [[LittleEndian|little-endian]] (LSByte at lowest address — x86 / most ARM); demonstrates the difference with a [[CCast|`char *` cast]] over an `int`; and names **network byte order = big-endian** as the [[IETF]] standardization that fixes the cross-host serialization protocol.

## Key Claims

- **Definition.** *"Byte order, sometimes referred to as endianness, describes the order in which the bytes of a multibyte value are ordered in memory."* Byte order is a property of the **hardware** (the [[CPU]] / [[InstructionSetArchitecture|ISA]]), not of the language or the program. Single-byte values (`char`, `uint8_t`) are unaffected — endianness is **only** meaningful for values wider than one byte ([[Int16|`short`]], [[Int32|`int`]] / `int32_t`, [[Int64|`long long`]] / `int64_t`, [[FloatingPoint|float]] / [[Double|double]], pointers).
- **[[BigEndian|Big-endian]].** The **most significant byte (MSByte)** occupies the **lowest** memory address; subsequent bytes follow in descending significance. Matches conventional left-to-right written-numeral order — the value `0xAABBCCDD` stored at address `p` reads `AA BB CC DD` walking `p, p+1, p+2, p+3`.
- **[[LittleEndian|Little-endian]].** The **least significant byte (LSByte)** occupies the **lowest** memory address; subsequent bytes follow in ascending significance. The value `0xAABBCCDD` stored at address `p` reads `DD CC BB AA` walking `p, p+1, p+2, p+3` — bytes appear reversed compared to the written numeral.
- **Architecture mapping.** *"x86 systems are little-endian."* *"Most ARM hardware uses little-endian."* (ARM is technically **bi-endian** — a runtime configuration bit selects mode — but virtually all deployed ARM systems run little-endian, especially [[ARMv7]] / [[ARMv8]] AArch64.) [[PowerPC]], [[SPARC]], and the historical [[Motorola68k]] / [[IBM360]] families are big-endian. [[RISCV|RISC-V]] is little-endian by default. [[MIPS]] is bi-endian.
- **Detection trick.** The chapter's worked C program reveals the host machine's endianness by [[Aliasing|aliasing]] an `int` through a `char *` and printing each byte:
  ```c
  int value = 0xAABBCCDD;
  char *p = (char *) &value;
  for (int i = 0; i < sizeof(value); i++) {
      printf("Address: %p, Value: %02hhX\n", p, *p);
      p += 1;
  }
  ```
  On x86 / x86-64 the output is `DD CC BB AA` — proof of [[LittleEndian|little-endian]] storage. The `%02hhX` specifier prints a [[SignedChar|signed char]] as **two hex digits**; pointer arithmetic on `char *` advances by exactly one byte (per the [[PointerArithmetic|type-scaled-stride rule]] of [[dis-2-9-4-ptr-arithmetic|Ch 2.9.4]]).
- **When endianness matters.** Three canonical scenarios where byte order leaks out of the [[Abstraction|abstraction]]: (1) **network transmission** — packets serialize integers that the receiver reinterprets; (2) **file formats** — a file written on a big-endian machine and read on a little-endian one (or vice versa) yields garbage unless the format pins endianness; (3) **debugger / raw-memory inspection** — [[GdbExamineMemory|`x/4xb`]] or `od -tx1` shows reversed bytes vs. the value the program holds.
- **[[NetworkByteOrder|Network byte order]] = big-endian.** *"The IETF (Internet Engineering Task Force) defines big-endian as the network byte order."* — the standardization choice that fixes serialization for [[TCPIP|TCP/IP]] headers, [[UDP]] payloads, and most binary network protocols. [[POSIX]] supplies the [[Htonl|`htonl` / `htons` / `ntohl` / `ntohs`]] conversion functions (host-to-network, network-to-host, long / short widths) in `<arpa/inet.h>` — on big-endian hosts they're identity, on little-endian hosts they [[ByteSwap|byte-swap]].
- **Historical etymology.** The terms originate from Jonathan Swift's *[[GulliversTravels|Gulliver's Travels]]* (1726) — the Big-Endians and Little-Endians waged satirical war over which end of an egg to crack. **[[DannyCohen|Danny Cohen]]'s 1980 IEN-137 memo** *On Holy Wars and a Plea for Peace* coined the technical usage and explicitly framed the endianness debate as a *"holy war"* — making the choice arbitrary but consequential.

## Key Quotes

> "Byte order, sometimes referred to as endianness, describes the order in which the bytes of a multibyte value are ordered in memory." — Ch 4.7, the chapter's headline definition.

> "x86 systems are little-endian." / "Most ARM hardware uses little-endian." — Ch 4.7, fixing the concrete architecture mapping for the two dominant modern ISA families.

> "The IETF (Internet Engineering Task Force) defines big-endian as the network byte order." — Ch 4.7, naming the standardization that resolves cross-host serialization.

## Connections

- [[DiveIntoSystems]] — corpus's **44th ingested chapter**; **closes Ch 4 *Binary and Data Representation*** by adding the address-level layout dimension that Ch 4.1–4.6 deferred (those sections treated multibyte integers as undifferentiated bit-strings; Ch 4.7 reveals the per-byte ordering in memory).
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[ByteOrder]] — **new concept page** — the umbrella covering [[BigEndian|big-endian]] / [[LittleEndian|little-endian]] / [[NetworkByteOrder|network byte order]] and the [[ByteSwap|byte-swap]] / [[Htonl|host-network conversion]] machinery.
- [[Endianness]] — **new concept page** — alias-with-disambiguation page pointing at [[ByteOrder]] (the term *endianness* is more common in code / docs; *byte order* is more common in textbooks).
- [[BigEndian]] — **new concept page** — MSByte-first; the [[NetworkByteOrder|network byte order]] standard; [[PowerPC]] / [[SPARC]] / [[Motorola68k]] historical home.
- [[LittleEndian]] — **new concept page** — LSByte-first; the [[X86]] / [[ARM]] / [[RISCV|RISC-V]] modern standard; dominant in deployed hardware as of 2025.
- [[Byte]] — the 8-bit unit whose ordering this chapter is about.
- [[MemoryAddress]] — the address that bytes are laid out across.
- [[CCast|C cast]] / [[Aliasing|type aliasing]] — the [[CLanguage|C]] mechanism the detection program uses to walk an `int` byte-by-byte via a `char *`.
- [[PointerArithmetic]] — supplies the `p += 1` stride that the detection program relies on (one byte per step for `char *`).
- [[CPU]] / [[InstructionSetArchitecture|ISA]] — endianness is a property of these, not of [[CLanguage|C]] / [[Assembly|assembly]] / the OS.
- [[X86]] / [[ARM]] / [[RISCV]] — the dominant little-endian ISAs.
- [[PowerPC]] / [[SPARC]] / [[Motorola68k]] — historical / specialized big-endian ISAs.
- [[BiEndian]] — runtime-switchable architectures ([[ARM]] / [[MIPS]] / [[PowerPC]] in some configurations) — wiki-only context.
- [[NetworkByteOrder]] — the big-endian convention that [[TCPIP|TCP/IP]] / [[UDP]] / most binary network protocols use.
- [[Htonl|`htonl` / `htons` / `ntohl` / `ntohs`]] — [[POSIX]] conversion functions for host ↔ network byte order — wiki-only (Ch 4.7 names the *concept* of network byte order but defers the functions to network-programming chapters).
- [[FileFormat|File-format portability]] — formats that survive cross-endian transfer either pin one endianness ([[JPEG]] big-endian; [[BMP]] / [[PNG]] little-endian for some fields) or include a byte-order mark ([[ByteOrderMark|BOM]] in [[UTF16]] / [[UTF32]]).
- [[Unicode|UTF-16 / UTF-32]] — text encodings where endianness matters and is resolved via the [[ByteOrderMark|BOM]] (`U+FEFF`) at file start — wiki-only context (Ch 4.7 stays at the integer layer).
- [[Serialization]] — the cross-host-cross-time concern that endianness directly governs.
- [[dis-4-1-bases|Ch 4.1]] — supplies the [[BinaryNumber|binary]] / [[HexadecimalNumber|hex]] representation Ch 4.7's worked example uses (`0xAABBCCDD`).
- [[dis-4-3-signed|Ch 4.3]] — supplies the [[MostSignificantBit|MSB]] / [[LeastSignificantBit|LSB]] vocabulary that scales up to MSByte / LSByte at the byte level.
- [[dis-4-6-bitwise|Ch 4.6]] — companion address-blind operator section; Ch 4.7 adds the address-aware layout dimension Ch 4.6 abstracts over.
- [[dis-2-9-3-voidstar|Ch 2.9.3]] / [[dis-2-9-4-ptr-arithmetic|Ch 2.9.4]] — supply the [[VoidPointer|`void *`]] / [[CCast|cast]] / [[PointerArithmetic|pointer-arithmetic]] machinery the byte-walking program uses.
- [[dis-2-2-pointers|Ch 2.2]] — supplies the [[AddressOfOperator|`&value`]] operator that yields the byte-walking starting address.

## Contradictions

- None with existing wiki content. Ch 4.7 **resolves** the cross-host-portability gap that Ch 4.1–4.6's bit-level treatment left implicit — those chapters tacitly assumed *single-host* execution; Ch 4.7 names the per-host variance.

## Scope Notes

- **Not covered by Ch 4.7**: **floating-point endianness** — IEEE 754 [[FloatingPoint|`float` / `double`]] values also undergo byte-reordering on little-endian hosts, generally following the host's integer endianness (though some embedded systems historically diverged — [[PDP11]] / [[VAX]] used unique mixed-endian *"middle-endian"* / *"PDP-endian"* layouts). Wiki-only context.
- **Not covered**: **bit-order within a byte** — endianness governs **byte** order in memory; *bit* order within a byte is a separate concern that arises in [[SerialProtocol|serial protocols]] ([[I2C]] / [[SPI]] / [[Ethernet]] PHY) and is generally **MSB-first on the wire** by convention. Higher-level [[CLanguage|C]] code never sees bit order — the [[CPU]] always presents bytes in a consistent way internally. Wiki-only.
- **Not covered**: the [[Htonl|`htonl` / `htons`]] conversion functions and the [[ByteSwap|`__builtin_bswap32` / `__builtin_bswap64`]] compiler intrinsics — Ch 4.7 names *network byte order* but defers the conversion API to network-programming chapters (Ch 15 *Networking*).
- **Not covered**: the [[ByteOrderMark|BOM]] (`U+FEFF`) convention in [[UTF16|UTF-16]] / [[UTF32|UTF-32]] text files — Ch 4.7 stays at the integer layer.
- **Not covered**: **alignment** and **padding** in [[CStruct|`struct`s]] — a separate memory-layout concern from endianness. [[dis-1-6-structs|Ch 1.6]] flagged the alignment caveat (`sizeof(struct) ≥ sum-of-fields`); endianness is orthogonal — it affects how each multibyte field's bytes are arranged, not the gaps between fields.
- **Not covered**: the [[CompileTimeEndianDetection|compile-time endianness detection]] idioms — `__BYTE_ORDER__` (GCC / Clang predefined macro), `<endian.h>` (Linux), `<sys/_endian.h>` (BSD), `WIN32` `REG_DWORD_BIG_ENDIAN` — that production code uses to dispatch byte-swap operations. Ch 4.7's runtime detection trick is a pedagogical demonstration, not the idiomatic production approach.
- **Not covered**: **middle-endian / mixed-endian** historical curiosities — the [[PDP11]] *"PDP-endian"* layout for 32-bit longs (`BB AA DD CC` for `0xAABBCCDD` — 16-bit big-endian halves stored little-endian). Effectively extinct as of 2025.
- **Not covered**: the [[CacheLine|cache-line]] / [[MemoryAlignment|alignment]] performance implications of cross-byte-boundary integer reads — those are [[MemoryHierarchy|memory-hierarchy]] concerns deferred to Ch 11.
