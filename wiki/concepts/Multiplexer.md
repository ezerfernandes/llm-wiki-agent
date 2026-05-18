---
title: "Multiplexer (MUX)"
type: concept
tags: [hardware, circuits, control, digital-logic]
sources: [dis-5-4-2-control-circuits]
last_updated: 2026-05-17
---

# Multiplexer (MUX)

A **multiplexer** is the headline [[ControlCircuit|control circuit]] of [[dis-5-4-2-control-circuits|Ch 5.4.2]] — *"a multiplexer (MUX) is an example of a control circuit that selects, or chooses, one of several values."* Takes $N$ data inputs + $\log_2 N$ select bits, outputs the input chosen by the select bits.

## Two-way 1-bit MUX

Two data inputs `A`, `B`, one select bit `S`:

- `S = 1` → `Out = A`
- `S = 0` → `Out = B`

Boolean form: `Out = (NOT(S) AND B) OR (S AND A)` — two [[AndGate|AND]]s gating the data inputs by `S` / `NOT(S)`, one [[OrGate|OR]] merging the two AND outputs. The Ch 5.4.1 methodology applied to a 3-row truth table.

## $N$-way 1-bit MUX

$\log_2 N$ select bits. Each of $N$ AND gates receives:

- the corresponding data input, and
- the conjunction of the decoded select-bit combination that selects it (each select bit straight or inverted as needed).

A single $N$-way [[OrGate|OR]] merges the $N$ AND outputs. The select-bit decoding is itself a [[Decoder|decoder]] — *every MUX contains a decoder inside it*.

**Example (4-way MUX):** two select bits `S1 S0` decode into one of four AND-gate enables; four 3-input ANDs + one 4-input OR.

## Two-way $N$-bit MUX

$N$ parallel 1-bit MUXes sharing one select line — operates on the corresponding bit position of two $N$-bit inputs. The composition pattern: *"a two-way N-bit MUX is built from N 1-bit multiplexers, each operating on the corresponding bit position of the two N-bit inputs."*

## CPU role

*"The CPU may use a multiplexer circuit to select from which [[CpuRegister|CPU register]] to read an instruction operand value."* — the canonical use: the [[ControlUnit|control unit]]'s decode phase emits register-selector bits that drive a MUX in front of the [[CpuRegister|register file]]'s read port, routing the addressed register's value into the [[ArithmeticLogicUnit|ALU]]'s operand input. The same pattern routes data *"between registers, cache, and [[RAM|RAM]]"* across the [[MemoryHierarchy|memory hierarchy]].

## Connections

- [[ControlCircuit]] — category page; MUX is the canonical example.
- [[Demultiplexer]] — the dataflow inverse (1 → $N$ vs. $N$ → 1).
- [[Decoder]] — sits *inside* every $N$-way MUX as the select-bit decoder.
- [[ControlUnit]] — emits the select-bit signals that drive CPU MUXes.
- [[CpuRegister]] — the headline read-port-selection target.
- [[AndGate]] / [[OrGate]] / [[NotGate]] — the gate-level primitives.
- [[LogicGate]] / [[Circuit]] — the abstraction layers above.

## Sources

- [[dis-5-4-2-control-circuits]] — Ch 5.4.2; introduces the MUX with the two-way 1-bit construction, the $N$-way generalization, and the CPU register-selection use case.
