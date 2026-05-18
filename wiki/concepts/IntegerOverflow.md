---
title: "Integer Overflow"
type: concept
tags: [binary, arithmetic, overflow, twos-complement, computer-systems, hardware]
sources: [dis-4-5-overflow, dis-4-4-1-addition, dis-4-4-2-subtraction]
last_updated: 2026-05-17
---

# Integer Overflow

**Integer overflow** is the condition in which the mathematical result of an integer arithmetic operation exceeds the range representable in the fixed-width storage holding the result. Per [[dis-4-5-overflow|Dive into Systems Ch 4.5]]: *"A computation that lacks the storage to represent its result has **overflowed**."* The visible result is the true result **modulo $2^N$** for $N$-bit registers — an instance of [[ModularArithmetic|modular arithmetic]] dictated by the bit-width limit.

Distinct from [[BufferOverflow|buffer overflow]] (an out-of-bounds memory write) despite the shared word.

## The odometer analogy

A one-digit decimal odometer (range $0$–$9$) on $8 + 4$ shows $2$, not $12$ — the leftmost digit has nowhere to go. Binary $N$-bit storage behaves identically with the wrap boundary at $2^N$. Per [[dis-4-5-overflow|Ch 4.5]], this is what *"arithmetic in any fixed-width representation"* means: the result is mathematically correct **modulo** the storage range.

## Two detection rules, one adder

[[dis-4-4-arithmetic|Ch 4.4]]'s **interpretation-invariance** thesis — the same N-bit [[FullAdder|adder]] serves both [[UnsignedInteger|unsigned]] and [[TwosComplement|two's-complement]] operands — produces a subtle consequence: **the bit pattern that is overflow depends on which encoding software intends.** [[dis-4-5-overflow|Ch 4.5]] supplies two distinct detection rules.

### Unsigned overflow

For $N$-bit [[UnsignedInteger|unsigned]] integers (range $[0,\,2^N-1]$), the discontinuity sits between $2^N - 1$ and $0$. The shortcut rule per [[dis-4-5-overflow|Ch 4.5]]:

> *"The carry out must match the carry in, otherwise the operation causes overflow."*

For addition: a [[CarryOut|carry-out]] from the MSB indicates the true sum exceeded $2^N - 1$ — overflow. For [[BinarySubtraction|subtraction]] (implemented as addition of the two's-complement negation with [[CarryIn|`CarryIn`]] = 1): the **absence** of an expected MSB carry-out indicates the true difference dropped below 0 — overflow. This resolves the *"doesn't necessarily indicate overflow"* caveat [[dis-4-4-2-subtraction|Ch 4.4.2]] flagged.

CPUs typically expose this signal as the **`CF` (carry flag)** in the status register (x86 `CF`, ARM `C`).

### Signed (two's-complement) overflow

For $N$-bit [[TwosComplement|two's-complement]] signed integers (range $[-2^{N-1},\,2^{N-1}-1]$), the discontinuity sits between $2^{N-1}-1$ (most positive) and $-2^{N-1}$ (most negative). Detection rule per [[dis-4-5-overflow|Ch 4.5]]:

> When adding two operands with **the same sign**, overflow occurred iff the **result's sign differs from both operands**.

Mixed-sign addition can never overflow — the result's magnitude can only shrink toward zero from either operand. Worked 4-bit examples from [[dis-4-5-overflow|Ch 4.5]]:

| operation | binary | unsigned read | signed read | signed overflow? |
|---|---|---|---|---|
| $4 + 5$ | `0100 + 0101 = 1001` | $9$ ✓ | $-7$ | **yes** (pos + pos → neg) |
| $-3 + (-8)$ | `1101 + 1000 = 0101` | $5$ — but unsigned wraps | $5$ | **yes** (neg + neg → pos) |
| $5 + (-4)$ | `0101 + 1100 = 10001` → `0001` | wraps to $1$ | $1$ ✓ | **no** (mixed sign — impossible) |

CPUs expose this signal as the **`OF` (overflow flag)** — distinct from the carry flag (x86 `OF`, ARM `V`).

The two flags are produced **simultaneously** by the same adder hardware; software (or the [[CCompiler|C compiler]]) chooses which to read based on the operand types.

## Mathematical equivalence

For $N$-bit storage, all integer arithmetic obeys $\text{result} \equiv \text{true\_result} \pmod{2^N}$. The interpretation of that bit pattern is what determines whether the user calls it overflow:

- **Unsigned**: result outside $[0,\,2^N-1]$ ⇒ visible bits wrap ⇒ `CF` raised.
- **[[TwosComplement|Two's-complement]]**: result outside $[-2^{N-1},\,2^{N-1}-1]$ ⇒ visible sign bit wrong ⇒ `OF` raised.

## C language consequence (forward-pointer)

[[dis-4-5-overflow|Ch 4.5]] is a hardware-level treatment and does **not** discuss language semantics. The [[CLanguage|C]] standard adds a load-bearing layer the wiki captures separately on [[UndefinedBehavior]]:

- **Unsigned overflow** in [[CLanguage|C]] is **defined** as modular wrap-around (`UINT_MAX + 1u == 0u`).
- **Signed overflow** in [[CLanguage|C]] is **[[UndefinedBehavior|undefined behavior]]** — the compiler may legally assume it never happens and aggressively optimize accordingly. Code like `if (x + 1 < x)` for `signed int x` can be deleted by [[GCC]] / [[Clang]] under `-O2`.

This asymmetry is why production C code uses **`unsigned`** for ring-buffer counters / hash mixers (defined wrap) and **signed** with explicit overflow checks (or `__builtin_add_overflow`) where wrap is unwanted.

## Real-world consequences

[[dis-4-5-overflow|Ch 4.5]] supplies three canonical historical examples:

- **YouTube view counter (2014)** — *Gangnam Style* approached $2^{32} - 1 \approx 4.29 \times 10^9$ views. YouTube migrated counters to 64-bit before the wrap manifested.
- **Pac-Man (1980)** — an 8-bit unsigned level counter wraps at level $256$, corrupting the right half of the board — the arcade community's *"split-screen kill screen."*
- **Therac-25 (1980s)** — overflow in a flag variable *"bypassed safety mechanisms"* in the radiation-therapy machine's [[OperatingSystem|OS]], contributing to patient overdoses. Cited as the canonical *"integer overflow with human consequences"* case study in safety-critical software literature.

## See also

- [[UndefinedBehavior]] — the [[CLanguage|C]]-language consequence for signed overflow.
- [[TwosComplement]] — the encoding whose asymmetric range produces the same-sign-different-result rule.
- [[UnsignedInteger]] — the encoding whose carry-out *is* the overflow signal.
- [[Carry]] / [[CarryIn]] / [[CarryOut]] — the bit-level signals the unsigned rule consults.
- [[BinaryAddition]] / [[BinarySubtraction]] — the operations overflow accompanies.
- [[FullAdder]] / [[ArithmeticLogicUnit]] — the hardware that produces both flags.
- [[BufferOverflow]] — a distinct (memory-safety) phenomenon sharing the *overflow* name.
- [[dis-4-5-overflow|Dive into Systems Ch 4.5]] — primary source.
