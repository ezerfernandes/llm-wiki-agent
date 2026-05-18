---
title: "Bitwise Operations"
type: concept
tags: [embedded, programming, c-language]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Bitwise Operations

Logical operations applied to integers **bit by bit** rather than to whole numeric values. The mechanism C programs use to set, clear, test, toggle, and pack individual bits in [[MemoryMappedIO|memory-mapped]] peripheral registers — pervasive in embedded code, rare in desktop application code.

## C operators (per [[embedded-controllers-fiore]] ch. 4)

| Op | Name | Example |
|---|---|---|
| `&` | AND | `x & 0x0F` → keeps low 4 bits |
| `\|` | OR | `x \| 0x80` → sets bit 7 |
| `^` | XOR | `x ^ 0x01` → toggles bit 0 |
| `~` | NOT (one's complement) | `~0xF0` → `0x0F` |
| `>>` | Shift right | `x >> 2` → divide-by-4 (unsigned) |
| `<<` | Shift left | `1 << 5` → bit-mask for bit 5 |

The **unary `&`** is "address of" (`scanf("%d", &x)`); the **binary `&`** is bitwise AND. Same symbol, two different operators distinguished by arity.

## Idioms

```c
// Set bit n          : x |= (1U << n)
// Clear bit n        : x &= ~(1U << n)
// Toggle bit n       : x ^= (1U << n)
// Test bit n         : (x & (1U << n)) != 0
// Set a mask         : x |= 0x06
// Clear a mask       : x &= ~0x06
// Replace bits 0..3  : x = (x & 0xF0) | (newval & 0x0F)
```

The Arduino headers (per [[embedded-controllers-fiore]] ch. 18) define these as inline-expanded macros:

```c
#define bitRead(value, bit)   (((value) >> (bit)) & 0x01)
#define bitSet(value, bit)    ((value) |= (1UL << (bit)))
#define bitClear(value, bit)  ((value) &= ~(1UL << (bit)))
#define bitWrite(value, bit, bitvalue) \
    (bitvalue ? bitSet(value, bit) : bitClear(value, bit))
```

`1UL` is "1 as an unsigned long" — defensive cast so that `(1UL << bit)` doesn't accidentally promote a `1` literal to a signed `int` that overflows when `bit >= 31`.

## Why embedded C drowns in these

A peripheral control register packs several semantic fields into one byte:

```
ADCSRA: | ADEN | ADSC | ADATE | ADIF | ADIE | ADPS2 | ADPS1 | ADPS0 |
```

Setting one field without disturbing the others is exactly the **mask-and-OR** / **mask-with-complement-and-AND** pattern. There's no language-level abstraction in C that captures "bit field of register" — you write the masks by hand or hide them in `#define`s. ([[TheEmbeddedRustBook|Rust]] wraps the same hardware in typed `R.field().write(...)` calls generated from the SVD file, but the bus operation is identical.)

## Connections

- [[CLanguage]] — the host language.
- [[MemoryMappedIO]] — what bitwise operations operate *on* in embedded contexts.
- [[DataDirectionRegister]] / [[GPIO]] — heaviest single use case.
- [[embedded-controllers-fiore]] — the source.
