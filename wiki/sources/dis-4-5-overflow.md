---
title: "Dive into Systems — Ch 4.5 Overflow"
type: source
tags: [dive-into-systems, ch4, binary, overflow, twos-complement, arithmetic, computer-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/overflow.html
sources: [dis-4-5-overflow]
last_updated: 2026-05-17
---

# Dive into Systems — Ch 4.5 *Overflow*

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 4.5** of *[[DiveIntoSystems]]* — the **detection-rules section** that finally formalizes the [[IntegerOverflow|integer-overflow]] phenomenon Ch 4.4.1–4.4.2 named-and-deferred. Defines overflow as *"a computation that lacks the storage to represent its result has **overflowed**"* and supplies the **two encoding-specific detection rules** — the [[UnsignedInteger|unsigned]] rule (*MSB carry-out must equal carry-in*) and the [[TwosComplement|two's-complement]] rule (*same-sign operands produce a different-sign result*) — closing the [[BinaryArithmetic|binary-integer-arithmetic]] story by explaining how the same N-bit [[FullAdder|adder]] hardware can flag two different overflow conditions depending on how software interprets the bits.

## Key Claims

- **Overflow definition**: *"A computation that lacks the storage to represent its result has **overflowed**."* — the result needed more bits than the fixed-width storage provides.
- **Modular-arithmetic framing** via the **one-digit decimal odometer** (range $0$–$9$): $8 + 4 = 12$ wraps to $2$ — the visible result is the true result **modulo $10$**. N-bit binary obeys the same rule modulo $2^N$.
- **Unsigned $N$-bit range**: $[0,\,2^N-1]$ — the discontinuity (wrap point) sits between $2^N - 1$ and $0$.
- **Unsigned overflow shortcut**: *"the carry out must match the carry in, otherwise the operation causes overflow"* — equivalently, [[CarryOut|MSB carry-out]] in addition mode signals overflow; in subtraction mode the *absence* of an expected carry-out signals overflow (resolving the *"doesn't necessarily indicate overflow"* caveat [[dis-4-4-2-subtraction|Ch 4.4.2]] flagged).
- **[[TwosComplement|Two's-complement]] $N$-bit range**: $[-2^{N-1},\,2^{N-1}-1]$ — the discontinuity sits between $2^{N-1}-1$ (most positive) and $-2^{N-1}$ (most negative).
- **Signed overflow direction rule**: *operations moving toward zero cannot overflow* — overflow only happens when the magnitude grows past one of the two extremes.
- **Signed overflow detection rule**: when adding two operands with **identical sign**, overflow occurred iff the **result's sign differs from both operands**. Mixed-sign addition can never overflow (the result magnitude can only shrink). Examples on 4-bit: $4 + 5 = -7$ (both positive → negative result = **overflow**); $-3 + (-8) = 5$ (both negative → positive result = **overflow**); $5 + (-4)$ = no overflow possible.
- **Hardware implication**: the same N-bit adder produces both overflow signals; CPUs expose them as separate flags (typically `CF` for unsigned, `OF` for signed) and software / the compiler chooses which flag to consult based on the operand types.
- **Real-world overflow consequences** (three historical examples):
  - **YouTube (2014)** — Gangnam Style's view counter approached the 32-bit unsigned ceiling ($2^{32} - 1 \approx 4.3 \times 10^9$); YouTube migrated counters to 64-bit before the wrap.
  - **Pac-Man (1980)** — an 8-bit unsigned level counter wraps at level 256; the arcade machine corrupts the board (the *"split-screen kill screen"*).
  - **Therac-25 (1980s)** — overflow in a flag variable *"bypassed safety mechanisms,"* contributing to patient radiation overdoses.

## Key Quotes

> "A computation that lacks the storage to represent its result has **overflowed**." — Ch 4.5, defining the phenomenon.

> "The carry out must match the carry in, otherwise the operation causes overflow." — Ch 4.5, the unsigned-overflow shortcut.

> "When adding two operands with the same sign, overflow occurs if the result has the opposite sign." — Ch 4.5, the [[TwosComplement|two's-complement]] detection rule (paraphrased).

## Connections

- [[DiveIntoSystems]] — corpus's **42nd ingested chapter**; advances Ch 4 *Binary and Data Representation* past the [[BinaryArithmetic|arithmetic]] block (4.4.1 / 4.4.2 / 4.4.3) into the **rules-and-consequences** layer.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[IntegerOverflow]] — **promoted from forward-reference stub to first-class page** by this chapter (was named in [[dis-4-4-1-addition|Ch 4.4.1]] and [[dis-4-4-2-subtraction|Ch 4.4.2]] without formal definition).
- [[UndefinedBehavior]] — **new concept page**; the chapter doesn't use the term explicitly but the wiki page records the C-language consequence (signed overflow is [[UndefinedBehavior|UB]] in C; unsigned overflow is **defined** as modular wrap-around) — load-bearing context the systems-level chapter omits.
- [[TwosComplement]] — the encoding whose **asymmetric range** $[-2^{N-1},\,2^{N-1}-1]$ produces the same-sign-different-result detection rule.
- [[UnsignedInteger]] — the $[0,\,2^N-1]$ range whose discontinuity at $2^N - 1 \to 0$ is the unsigned overflow boundary.
- [[BinaryAddition]] — the operation overflow most commonly accompanies; Ch 4.4.1's MSB-carry-out *"silent truncation"* is now formalized as the unsigned-overflow signal.
- [[BinarySubtraction]] — Ch 4.4.2's *"doesn't necessarily indicate overflow"* caveat is **resolved** here: in subtraction mode the rule inverts (no carry-out when expected = overflow).
- [[Carry]] — the [[CarryIn|carry-in]] / [[CarryOut|carry-out]] pair whose mismatch *is* the unsigned overflow rule.
- [[FullAdder]] — the per-bit primitive that produces both carry signals; one adder serves both overflow rules.
- [[BinaryArithmetic]] — Ch 4.4's hub; Ch 4.5 closes the consequences-of-arithmetic discussion the hub opened.
- [[SignedInteger]] — the [[TwosComplement|two's-complement]]-specific detection rule applies to all signed-integer arithmetic the corpus treats.
- [[MostSignificantBit]] — the bit position whose sign role (signed) vs. carry role (unsigned) is the *reason* one bit pattern produces two different overflow rules.
- [[ArithmeticLogicUnit]] — the hardware that produces both `CF` and `OF` flags simultaneously; the [[CLanguage|C]] compiler / programmer chooses which to read.
- [[dis-4-4-arithmetic|Ch 4.4]] — the hub that previewed this material.
- [[dis-4-4-1-addition|Ch 4.4.1]] — flagged MSB-carry-out as the silent-overflow root mechanism; Ch 4.5 formalizes the rule.
- [[dis-4-4-2-subtraction|Ch 4.4.2]] — flagged the deferred *"full overflow rule"* now delivered here.
- [[dis-4-3-signed|Ch 4.3]] — supplies the asymmetric-range fact $[-2^{N-1},\,2^{N-1}-1]$ that the signed-overflow rule exploits.
- [[BufferOverflow]] — a **distinct phenomenon** despite the shared word *"overflow"*: integer overflow is an arithmetic-result-too-large condition on a register / variable; [[BufferOverflow|buffer overflow]] is an out-of-bounds memory write. The two interact in security exploits (integer-overflow-induced under-sized buffer allocations).

## Contradictions

- None with existing wiki content. Ch 4.5 **closes** the deferral chain from [[dis-4-4-1-addition|Ch 4.4.1]] (*"the hardware simply drops or truncates"* the MSB carry-out — what does it mean?) and [[dis-4-4-2-subtraction|Ch 4.4.2]] (*"doesn't necessarily indicate overflow"* in subtraction mode — when does it?). The earlier *"deferred to a later Ch 4 section"* phrasing is now satisfied.

## Scope Notes

- **Not covered by Ch 4.5**: the [[CLanguage|C]] / [[CPlusPlus]] language-level rule that signed-integer overflow is [[UndefinedBehavior|undefined behavior]] (the wiki's [[UndefinedBehavior]] concept page records this). The chapter stays at the hardware-level bit-mechanics layer.
- **Not covered**: hardware exception-on-overflow modes (MIPS `add` trapping vs `addu` wrapping; x86 `INTO` instruction). Ch 4.5 treats overflow as a flag-producing condition only — trap-vs-wrap behaviour is ISA-dependent and deferred.
- **Not covered**: saturating arithmetic (ARM NEON / DSP `qadd` / `qsub` — clamp-to-max-instead-of-wrap semantics). Standard integer arithmetic only.
