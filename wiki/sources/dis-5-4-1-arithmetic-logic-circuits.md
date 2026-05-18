---
title: "Dive into Systems — Ch 5.4.1 Arithmetic and Logic Circuits"
type: source
tags: [computer-architecture, circuits, alu, adder, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C5-Arch/arithlogiccircs.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 5.4.1** of *[[DiveIntoSystems]]* — first subsection of [[dis-5-4-circuits|Ch 5.4 *Circuits*]], delivering the **arithmetic-and-logic** category of the three-way circuit partition. Opens with a **three-step methodology** for designing a 1-bit circuit from [[LogicGate|gates]] — truth table → Boolean expression for each output → translation into a gate sequence — and applies it to two worked combinational circuits ([[OneBitEqualityCircuit|1-bit equals]], [[HalfAdder|1-bit adder]]). Extends the adder to a [[FullAdder|1-bit full adder]] with `CarryIn`, then cascades $N$ full adders into a [[RippleCarryAdder|ripple-carry adder]] — *"the SUM result ripples or propagates through the circuit from the low-order to the high-order bits."* Notes that a subtraction circuit can be built from adder + negation circuits, and that the [[ArithmeticLogicUnit|ALU]] is the umbrella arithmetic-logic circuit assembled from such pieces.

## Key Claims

- **Three-step circuit design methodology** for any 1-bit combinational circuit:
  1. Build a [[TruthTable|truth table]] specifying outputs for every input combination.
  2. For each output, write a Boolean expression in [[AndGate|AND]] / [[OrGate|OR]] / [[NotGate|NOT]] that evaluates to `1` exactly on the rows where the output is `1` (sum-of-minterms style).
  3. Translate the expression into a [[LogicGate|gate]]-level circuit.
- **1-bit equality circuit** ([[OneBitEqualityCircuit]]) outputs `1` iff `A == B`. Boolean form: `(NOT(A) AND NOT(B)) OR (A AND B)` — *"is 1 when A and B are both 0 or both 1."* Equivalent to the [[XnorGate|XNOR]] gate.
- **1-bit adder** ([[HalfAdder]]) has two inputs (`A`, `B`) and two outputs: `SUM = A XOR B` (a.k.a. `(NOT(A) AND B) OR (A AND NOT(B))` — `1` when exactly one input is `1`); `CARRY OUT = A AND B`. Two gates suffice — one [[XorGate|XOR]] and one [[AndGate|AND]].
- **1-bit full adder** ([[FullAdder]]) extends the half adder with a third input `CARRY IN`. Three inputs (`A`, `B`, `CarryIn`), two outputs (`Sum`, `CarryOut`); the 8-row truth table is the one [[dis-4-4-1-addition|Ch 4.4.1]] already introduced (`Sum = A XOR B XOR CarryIn`, `CarryOut = majority(A, B, CarryIn)`). Needed for multi-bit addition because every column above the LSB receives a carry from the column below it.
- **N-bit ripple-carry adder** ([[RippleCarryAdder]]) — cascades $N$ 1-bit full adders, wiring each adder's `CARRY OUT` into the next-higher adder's `CARRY IN`. *"This type of N-bit adder circuit, built from N 1-bit adder circuits, is called a **ripple carry adder**"* — *"the SUM result ripples or propagates through the circuit from the low-order to the high-order bits."* The LSB position's `CARRY IN` is wired to `0` for standard addition (and to `1` to deliver [[BinarySubtraction|two's-complement]] subtraction's *add-one* via the [[dis-4-4-2-subtraction|Ch 4.4.2]] flip-and-add-one trick).
- **Subtraction circuit** — *"a subtraction circuit that computes (A − B) can be built from adder and negation circuits"* — the same ripple-carry adder with `B` routed through a row of [[NotGate|inverters]] (or [[XorGate|XOR]] gates driven by a mode bit, per [[dis-4-4-2-subtraction|Ch 4.4.2]]) and `CarryIn` = 1.
- **[[ArithmeticLogicUnit|ALU]] as composition** — the [[ArithmeticLogicCircuit|arithmetic-and-logic circuit]] block of the [[ProcessingUnit|processing unit]] is assembled from these gate-level pieces; the ALU's logic side reuses [[dis-5-3-gates|Ch 5.3]]'s M-bit gates, the arithmetic side reuses the ripple-carry adder (and the subtraction wiring above it).
- **Methodology is recursive** — each combinational circuit becomes a black-box at the next level up, matching the [[Circuit|hierarchical composition]] discipline [[dis-5-4-circuits|Ch 5.4]] installed.

## Key Quotes

> "This type of N-bit adder circuit, built from N 1-bit adder circuits, is called a **ripple carry adder**." — naming the cascaded-full-adder construction.

> "The SUM result ripples or propagates through the circuit from the low-order to the high-order bits." — operational characterization that names this section's namesake circuit.

> "(NOT(A) AND NOT(B)) OR (A AND B) # is 1 when A and B are both 0 or both 1" — the 1-bit equality circuit's Boolean form.

> "(NOT(A) AND B) OR (A AND NOT(B)) # 1 when exactly one of A or B is 1" — the 1-bit adder's `SUM` expression (equivalent to `A XOR B`).

> "a subtraction circuit that computes (A − B) can be built from adder and negation circuits" — names the subtraction circuit as a composition of already-built pieces, no new arithmetic hardware needed.

## Connections

- [[DiveIntoSystems]] — chapter 51 of the corpus; first subsection beneath [[dis-5-4-circuits|Ch 5.4 *Circuits*]].
- [[dis-5-4-circuits]] — parent hub page; this section delivers the **arithmetic-and-logic** category of the three-way circuit partition.
- [[dis-5-3-gates]] — supplies the gate-level primitives ([[AndGate|AND]] / [[OrGate|OR]] / [[NotGate|NOT]] / [[XorGate|XOR]]) the circuits in this section are built from.
- [[dis-4-4-1-addition]] — where the 8-row [[FullAdder|full-adder]] truth table was first introduced at the bit-pattern level; Ch 5.4.1 supplies the matching **gate-level construction**.
- [[dis-4-4-2-subtraction]] — the *flip-and-add-one* subtraction trick that the ripple-carry adder + inverters + `CarryIn = 1` wiring implements.
- [[dis-4-5-overflow]] — both `CF` (unsigned) and `OF` (signed) flags emerge from this same N-bit ripple-carry adder.
- [[ArithmeticLogicCircuit]] — this section's category label; this page is the canonical referent.
- [[ArithmeticLogicUnit]] — the [[CPU]]-level umbrella that aggregates these circuits.
- [[Circuit]] — design discipline (hierarchical composition + [[Abstraction|black-box abstraction]]) installed by the parent hub.
- [[OneBitEqualityCircuit]] / [[HalfAdder]] / [[FullAdder]] / [[RippleCarryAdder]] — the four named circuits this section walks through.

## Contradictions

None. Ch 5.4.1 is the **gate-level construction** layer that complements the bit-pattern-level treatment of [[dis-4-4-1-addition|Ch 4.4.1]] and [[dis-4-4-2-subtraction|Ch 4.4.2]] — same truth tables, now implemented as physical [[LogicGate|gate]] networks. Multiplexers are **not** discussed in this section (scope note: the multi-operation [[ArithmeticLogicUnit|ALU]]'s operation-select mechanism is deferred — Ch 5.4.1 stops at adder + subtraction wiring).

## Scope Notes (wiki-flagged, not in source)

- **No multiplexer** — the chapter does not introduce a MUX / op-select circuit at this level. The ALU operation-select story arrives later in the corpus.
- **No N-bit ALU diagram** — the section composes adders but does not depict a full multi-op ALU.
- **No carry-lookahead** — the ripple-carry adder's $O(N)$ propagation delay is named but not optimized (carry-lookahead, carry-select, Kogge-Stone are out of scope).
