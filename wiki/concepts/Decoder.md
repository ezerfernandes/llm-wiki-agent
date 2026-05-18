---
title: "Decoder"
type: concept
tags: [hardware, circuits, control, digital-logic]
sources: [dis-5-4-2-control-circuits]
last_updated: 2026-05-17
---

# Decoder

A **decoder** is the [[ControlCircuit|control circuit]] that translates an encoded bit pattern into a **one-hot** selection. *"A decoder circuit takes an encoded input and enables one of several outputs based on the input value."* ([[dis-5-4-2-control-circuits|Ch 5.4.2]]).

## Shape

- $N$ input bits → $2^N$ output lines.
- Exactly **one** output is high at a time — the one indexed by the binary value of the input bits.
- Example: a 2-bit decoder has inputs `S1 S0` and outputs `Y0 Y1 Y2 Y3`. `S1 S0 = 10` → `Y2 = 1`, all others `0`.

Constructed from $2^N$ [[AndGate|AND]] gates, each receiving the input bits in the straight-or-inverted combination that matches its index, plus [[NotGate|NOT]] gates supplying the inverted forms.

## Role inside a MUX

Every $N$-way [[Multiplexer|MUX]] contains a decoder: the MUX's $\log_2 N$ select bits feed an internal decoder whose $N$ one-hot outputs become the per-input AND-gate enables. The decoder is the **select-bit translator**; the surrounding AND-OR layer is the **value gating + merge**.

## CPU role

The [[ControlUnit|control unit]]'s **instruction decode** stage of the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]] uses decoder circuits to translate the opcode bits of the [[InstructionRegister|IR]] into control signals — one-hot enables that select which [[ArithmeticLogicUnit|ALU]] operation runs, which [[CpuRegister|register]] gets read or written, and which [[MemoryHierarchy|memory-hierarchy]] level participates. The name *"decode"* in *"fetch-decode-execute"* refers to exactly this decoder.

## Relationship to encoder

The conceptual inverse — $2^N$ one-hot inputs → $N$ encoded output bits — is an **encoder**. **Ch 5.4.2 does not introduce an encoder**; the word *"encoded"* in the decoder definition refers to the input pattern's interpretation, not to a separate circuit.

## Connections

- [[ControlCircuit]] — category page; decoder is one of three named examples.
- [[Multiplexer]] — contains a decoder as its internal select-bit translator.
- [[Demultiplexer]] — with a constant `1` input, a DMUX behaves identically to a decoder.
- [[ControlUnit]] / [[FetchDecodeExecuteCycle]] / [[InstructionRegister]] — the architectural context where opcode decoding lives.
- [[AndGate]] / [[NotGate]] — the gate-level primitives.

## Sources

- [[dis-5-4-2-control-circuits]] — Ch 5.4.2; defines the decoder and names it as the internal selection mechanism inside every $N$-way MUX.
