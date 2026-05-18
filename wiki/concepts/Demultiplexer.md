---
title: "Demultiplexer (DMUX)"
type: concept
tags: [hardware, circuits, control, digital-logic]
sources: [dis-5-4-2-control-circuits]
last_updated: 2026-05-17
---

# Demultiplexer (DMUX)

The **demultiplexer** is the [[Multiplexer|multiplexer]]'s dataflow inverse. *"A demultiplexer (DMUX) is the inverse of a multiplexer. Whereas a multiplexer chooses one of N inputs, a demultiplexer chooses one of N outputs."* ([[dis-5-4-2-control-circuits|Ch 5.4.2]]).

## Shape

- **MUX**: $N$ inputs + $\log_2 N$ select bits → **1 output**.
- **DMUX**: **1 input** + $\log_2 N$ select bits → $N$ outputs.

The selected output carries the input value; the other $N - 1$ outputs read `0`. Same selection logic as the MUX — only the dataflow direction is reversed.

## CPU role

DMUXes sit on the **write side** of the [[CpuRegister|register file]] and on the [[ArithmeticLogicUnit|ALU]] result path: the [[ControlUnit|control unit]]'s decode phase emits destination-register selector bits that drive a DMUX routing the [[ArithmeticLogicUnit|ALU]] result back into exactly one register. The same pattern dispatches stores *"between registers, cache, and [[RAM|RAM]]"* across the [[MemoryHierarchy|memory hierarchy]].

## Connections

- [[ControlCircuit]] — category page; DMUX is one of three named examples (MUX / DMUX / decoder).
- [[Multiplexer]] — the dataflow inverse.
- [[Decoder]] — closely related: a DMUX with a constant `1` input behaves exactly like a decoder over the select bits (one-hot output).
- [[ControlUnit]] / [[CpuRegister]] / [[ArithmeticLogicUnit]] — the architectural endpoints.

## Sources

- [[dis-5-4-2-control-circuits]] — Ch 5.4.2; defines the DMUX as the MUX inverse.
