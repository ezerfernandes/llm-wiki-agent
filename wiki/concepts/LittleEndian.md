---
title: "Little-Endian"
type: concept
tags: [binary, memory, byte-order, endianness, little-endian]
sources: [dis-4-7-byte-order]
last_updated: 2026-05-17
---

# Little-Endian

**Little-endian** is one of the two [[ByteOrder|byte-order]] conventions: the **least significant byte (LSByte)** of a multibyte value occupies the **lowest** memory address, with subsequent bytes following in **ascending** significance. Bytes appear **reversed** compared to the conventional written-numeral form.

For `int value = 0xAABBCCDD;` at address `p`:

| Address | `p`  | `p+1` | `p+2` | `p+3` |
|---------|------|-------|-------|-------|
| Byte    | `DD` | `CC`  | `BB`  | `AA`  |

## Where it's used

- **[[X86]] / [[X86_64]]** — universal little-endian since the [[Intel8080]] (1974). All [[Intel]] / [[AMD]] / desktop / laptop / server CPUs.
- **[[ARM]]** — default in [[ARMv7]] / [[ARMv8]] / [[AArch64]]. Bi-endian capability exists (`SETEND` instruction, `E` bit in `CPSR`) but is dormant on [[Linux]] / [[iOS]] / [[Android]] / [[Windows]]-on-ARM.
- **[[RISCV]]** — little-endian by default (the spec allows big-endian but no deployed implementation uses it).
- **[[Alpha]]** — [[DEC]] / [[Compaq]] workstations and servers (now discontinued).
- **[[VAX]]** — historical [[DEC]] minicomputer (technically *middle-endian* for some types, but the integer ABI is little-endian).
- **[[POWER8]]+ on Linux** — the [[PowerPC]] family flipped to little-endian mode in this generation to ease porting from x86.
- **Most modern binary file formats** — [[BMP]], [[WAV]] / [[RIFF]], [[PE|PE/COFF]] (Windows executables), [[ELF]] (on little-endian targets), [[ZIP]], the [[USB]] protocol headers.

## Mental model

*"Little end first"* — the **little end** of the number (the low-order byte, the one with the smallest place value) comes **first** in memory. This is **counterintuitive** when first encountered — `gdb`'s `x/4xb &my_int` shows bytes in *reverse* of the value's hex literal — but has useful properties (see below).

## Why it persists / why it might even be preferable

Despite the visual confusion, little-endian has several practical advantages that explain its dominance:

- **Address-of-low-byte == address-of-value** — a `uint32_t *p` and a `uint8_t *p` cast at the same address both read the **low byte** first. Casting a wider type to a narrower one is a no-op (just ignore high addresses) — useful for [[Promotion|integer promotion]] and [[TruncatingCast|truncating casts]].
- **Increment-with-carry flows naturally** — addition processes bytes from low to high, matching the memory layout. Hardware adders can streaming-fetch bytes in address order.
- **Variable-width arithmetic is easier** — a [[BigInteger|big-integer]] library can treat the low bytes of a 32-bit value identically to the low limbs of a 256-bit value.
- **Multiprecision shifts** — left-shift moves bits toward higher addresses (toward the *big end*), matching the visual direction of `<<` in C source code.

## Practical implications

- **Reading raw memory needs mental byte-reversal** — `gdb`'s `x/4xb` output shows `DD CC BB AA` for the value `0xAABBCCDD`. Use `x/1wx` to view as a single 4-byte word and `gdb` will reverse for you.
- **Network I/O needs `htonl` / `ntohl`** — these are real byte-swap operations on little-endian hosts (no-ops on big-endian); ignoring them on little-endian hosts is the **#1 cross-platform networking bug**.
- **`memcmp` is unrelated to numeric order** — comparing two little-endian integers byte-by-byte gives a meaningless result; always compare via the value type, not the bytes.
- **Hex dumps "look wrong"** — `hexdump -C` of a 4-byte integer storing `0x12345678` shows `78 56 34 12` — a perennial source of confusion for newcomers.

## Dominance in 2025

Little-endian is **effectively the universal convention** for application programmers:

- Desktop / laptop / server: 100% little-endian ([[X86]] / [[X86_64]]).
- Mobile: 100% little-endian ([[ARM]] / [[AArch64]] in Android / iOS).
- Embedded: predominantly little-endian ([[ARM]] [[CortexM|Cortex-M]] / [[RISCV]]).
- Network protocols: still big-endian (the one remaining big-endian island).

## Etymology

From Jonathan Swift's *[[GulliversTravels|Gulliver's Travels]]* (1726) — the **Little-Endians** broke their eggs on the little (pointed) end. **[[DannyCohen|Danny Cohen]]'s 1980 IEN-137 memo** *On Holy Wars and a Plea for Peace* coined the technical usage.

## Related concepts

- [[ByteOrder]] — the umbrella concept covering both endianness conventions.
- [[BigEndian]] — the opposite convention; the [[NetworkByteOrder|network byte order]] standard.
- [[Endianness]] — common alias term for byte order.
- [[X86]] / [[X86_64]] / [[ARM]] / [[RISCV]] — the dominant little-endian ISAs.
- [[Htonl|`htonl` / `ntohl` / `htons` / `ntohs`]] — POSIX network byte-order conversion (real byte-swap on little-endian hosts).
- [[ByteSwap]] / [[BSWAP|`bswap`]] — the cross-endian conversion operation; single-cycle on x86 since 80486.
- [[LeastSignificantBit|LSByte]] — the low-order byte that little-endian places first.
- [[GulliversTravels]] — etymological origin.
- [[DannyCohen]] — author of the 1980 IEN-137 *"On Holy Wars"* memo.
