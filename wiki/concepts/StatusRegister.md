---
title: "Status Register (SREG)"
type: concept
tags: [embedded, cpu-register, avr, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Status Register

The single most important register on a [[Microcontroller|microcontroller]] (per [[embedded-controllers-fiore]] ch. 21): a small bag of flag bits that record the results of recent [[ALU]] operations and gate critical features like global interrupt enable. On the [[AVR]] core, called **SREG** and exposed at memory address `0x5F`.

## SREG bits on the AVR

| Bit | Name | Meaning |
|---|---|---|
| 7 | **I** | Global Interrupt Enable. Set by `sei()`, cleared by `cli()`. Hardware auto-clears on ISR entry, set by `RETI`. |
| 6 | **T** | Bit Copy Storage. Source / destination for `BLD` / `BST` instructions. |
| 5 | **H** | Half Carry. Used in BCD arithmetic. |
| 4 | **S** | Sign = N ⊕ V. Two's-complement sign of the result. |
| 3 | **V** | Two's-Complement Overflow. |
| 2 | **N** | Negative result. |
| 1 | **Z** | Zero result. |
| 0 | **C** | Carry out / borrow in. |

All bits are read/write and zero-initialized.

## SREG and interrupts

The key embedded-relevant fact (per [[embedded-controllers-fiore]] ch. 16, 21, 29): **SREG is not automatically saved by hardware on ISR entry, and is not automatically restored on `RETI`.** The application must save and restore it manually. Concretely, that's why every Arduino library function that does a read-modify-write on a peripheral register brackets the write with:

```c
oldSREG = SREG;
cli();
// … critical section: e.g.  *reg |= bit; …
SREG = oldSREG;
```

This preserves whatever interrupt-enable state the caller had — if interrupts were on, they stay on after; if off, they stay off — without races.

The AVR-GCC `ISR(...)` macro takes care of this on the *entry* side: it expands into a function whose prologue pushes SREG (and the working registers it clobbers) and whose epilogue pops them. So user ISR bodies don't have to do it explicitly.

## Connections

- [[ALU]] — what produces the flags.
- [[InterruptServiceRoutine]] — why the I bit and SREG-save discipline matter.
- [[AVR]] / [[ATmega328P]] — the chip family.
- [[embedded-controllers-fiore]] — the source.
