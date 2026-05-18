---
title: "Dive into Systems — Ch 5.4.2 Control Circuits"
type: source
tags: [computer-architecture, circuits, control, multiplexer, decoder, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C5-Arch/controlcircs.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 5.4.2** of *[[DiveIntoSystems]]* — **second subsection** of [[dis-5-4-circuits|Ch 5.4 *Circuits*]], delivering the **control** category of the three-way circuit partition. Defines [[ControlCircuit|control circuits]] as the circuitry that *"drive[s] the execution of program instructions on program data"* and that routes data between storage levels and hardware devices. Walks three canonical examples — [[Multiplexer|multiplexer (MUX)]] (selects one of $N$ inputs by a $\log_2 N$-bit select line), [[Demultiplexer|demultiplexer (DMUX)]] (the inverse — routes one input to one of $N$ outputs), and [[Decoder|decoder]] (*"takes an encoded input and enables one of several outputs based on the input value"*) — and ties them back to the [[CPU]]: *"the CPU may use a multiplexer circuit to select from which [[CpuRegister|CPU register]] to read an instruction operand value."* Constructions are gate-level: a two-way 1-bit MUX is `(NOT(S) AND B) OR (S AND A)`; an $N$-way MUX uses $\log_2 N$ select bits decoded into $N$ AND-gate selectors merged by an $N$-way OR; a two-way $N$-bit MUX is $N$ parallel 1-bit MUXes sharing one select line.

## Key Claims

- **Definition** — *"Control circuits are used throughout a system. On the processor, they drive the execution of program instructions on program data. They also control loading and storing values to different levels of storage (between registers, cache, and RAM)."* Control circuits are the **second** of the three [[Circuit|circuit]] categories ([[dis-5-4-circuits|Ch 5.4]] partition); siblings are [[ArithmeticLogicCircuit|arithmetic-and-logic]] and [[StorageCircuit|storage]].
- **Multiplexer (MUX)** — *"a multiplexer (MUX) is an example of a control circuit that selects, or chooses, one of several values."* Two data inputs `A`, `B`, one select bit `S`; output `= A` when `S = 1`, `= B` when `S = 0`. Gate-level form: `Out = (NOT(S) AND B) OR (S AND A)` — two [[AndGate|AND]]s, one [[NotGate|NOT]], one [[OrGate|OR]]. Generalizes to **$N$-way** with $\log_2 N$ select bits: each of $N$ AND gates receives the data input plus the decoded select-bit combination that selects that input; the AND outputs are merged by a single $N$-way [[OrGate|OR]]. A **two-way $N$-bit MUX** stacks $N$ parallel 1-bit MUXes sharing one select line — *"a two-way N-bit MUX is built from N 1-bit multiplexers, each operating on the corresponding bit position of the two N-bit inputs."*
- **Demultiplexer (DMUX)** — *"the inverse of a multiplexer. Whereas a multiplexer chooses one of N inputs, a demultiplexer chooses one of N outputs."* Same selection logic, dataflow direction reversed: one data input, $\log_2 N$ select bits, $N$ outputs — the selected output gets the input, the others receive `0`.
- **Decoder** — *"a decoder circuit takes an encoded input and enables one of several outputs based on the input value."* An $N$-input decoder activates exactly one of $2^N$ outputs corresponding to the input encoding (one-hot output). The decoder is the **internal selection mechanism** an $N$-way MUX uses to translate its $\log_2 N$ select bits into the $N$ per-input AND-gate enables.
- **CPU role** — *"the CPU may use a multiplexer circuit to select from which CPU register to read an instruction operand value."* This is the architectural payoff: the [[ControlUnit|control unit]]'s decode phase emits select-bit signals that drive MUXes in front of the [[CpuRegister|register file]] (read-port selection) and DMUXes behind the [[ArithmeticLogicUnit|ALU]] (write-port routing). Control circuits are also the dispatch mechanism for moving data *"between registers, cache, and [[RAM]]"* across the [[MemoryHierarchy|memory hierarchy]].
- **Encoder not covered** — the section walks MUX / DMUX / decoder but **does not introduce an encoder circuit** (the conceptual inverse of a decoder — $2^N$ inputs to $N$ encoded output bits). The word *"encoded"* appears only inside the decoder definition, not as a circuit name.
- **Methodology continuity** — Same hierarchical-composition + black-box [[Abstraction|abstraction]] discipline from [[dis-5-4-circuits|Ch 5.4]]: each control circuit, once built, becomes a primitive at the next level up. The truth-table → Boolean-expression → gate-network methodology from [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] still applies — the MUX's `(NOT(S) AND B) OR (S AND A)` is the methodology's output for the 3-row truth table specifying `Out(A, B, S)`.

## Key Quotes

> "A multiplexer (MUX) is an example of a control circuit that selects, or chooses, one of several values." — naming the section's headline circuit.

> "A demultiplexer (DMUX) is the inverse of a multiplexer. Whereas a multiplexer chooses one of N inputs, a demultiplexer chooses one of N outputs." — the DMUX-as-inverse-of-MUX framing.

> "A decoder circuit takes an encoded input and enables one of several outputs based on the input value." — the decoder definition; also names the internal selection mechanism inside any $N$-way MUX.

> "Control circuits are used throughout a system. On the processor, they drive the execution of program instructions on program data. They also control loading and storing values to different levels of storage (between registers, cache, and RAM)." — the category-level definition; pins the [[ControlCircuit]] page's primary claim.

> "The CPU may use a multiplexer circuit to select from which CPU register to read an instruction operand value." — the architectural payoff that ties MUXes to the [[ControlUnit|control unit]]'s decode-phase register-file read.

## Connections

- [[DiveIntoSystems]] — chapter 53 of the corpus; second subsection beneath [[dis-5-4-circuits|Ch 5.4 *Circuits*]].
- [[dis-5-4-circuits]] — parent hub page; this section delivers the **control** category of the three-way circuit partition.
- [[dis-5-4-1-arithmetic-logic-circuits]] — sibling subsection (arithmetic-and-logic category); shares the truth-table → Boolean-expression → gate-network methodology, applied here to the MUX rather than the adder.
- [[dis-5-3-gates]] — supplies the [[AndGate|AND]] / [[OrGate|OR]] / [[NotGate|NOT]] primitives the MUX / DMUX / decoder are built from.
- [[dis-5-2-von-neumann]] — the [[ControlUnit|control unit]] this category's circuits implement; the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]] is the operational pattern the control circuits dispatch over.
- [[ControlCircuit]] — promoted **from forward-reference to category page** this ingest.
- [[Multiplexer]] / [[Demultiplexer]] / [[Decoder]] — the three named circuits this section introduces.
- [[ControlUnit]] — the [[CPU]]-level umbrella above the [[ControlCircuit|control circuits]].
- [[CpuRegister]] — the target of the section's headline use case (register-file read-port selection).
- [[MemoryHierarchy]] — control circuits also dispatch data movement *"between registers, cache, and [[RAM]]"* (forward reference; treated in detail in later chapters).

## Contradictions

None. Ch 5.4.2 is the **control-category gate-level construction layer** that complements the [[ControlUnit|control unit]] introduced operationally in [[dis-5-2-von-neumann|Ch 5.2]] — same abstraction, now realized as physical [[LogicGate|gate]] networks.

## Scope Notes (wiki-flagged, not in source)

- **No encoder** — the section covers MUX / DMUX / decoder but does **not** introduce an encoder circuit. Per the task's *"only what's covered"* rule, no [[Encoder]] page is minted this ingest.
- **No sequencer / state-machine control** — Ch 5.4.2 stops at the combinational selection circuits (MUX / DMUX / decoder); the [[ControlUnit|control unit]]'s sequencing logic (microcode ROMs, FSM-based controllers) is deferred.
- **No tri-state buffers** — an alternative bus-selection mechanism (tri-state drivers on shared wires) is not introduced; the section uses the AND-OR MUX construction throughout.
- **No ALU op-select diagram** — the section names register-file selection as the canonical MUX use but does not draw the full ALU operation-select MUX (the [[ArithmeticLogicUnit|ALU]]'s operation-code routing remains a forward reference).
