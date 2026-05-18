---
title: "Dive into Systems — Ch 5.6 The Processor's Execution of Program Instructions"
type: source
tags: [systems, computer-architecture, cpu, fetch-decode-execute, instruction-set, clock, machine-code]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C5-Arch/instrexec.html
---

## Summary

Chapter 5.6 *The Processor's Execution of Program Instructions* operationalizes the [[dis-5-5-cpu|Ch 5.5]] [[ProcessorDatapath|data path]]: it walks through a concrete `ADD` instruction across the **four stages** of the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]] — **Fetch → Decode → Execute → WriteBack** — wiring the [[ProgramCounter|PC]] and [[InstructionRegister|IR]] into a synchronous loop paced by the [[ClockSignal|clock]]. The chapter also introduces the **[[InstructionSet|instruction set architecture]]** vocabulary — [[OpCode|opcode]] / operand / [[MachineCode|machine code]] / [[AssemblyLanguage|assembly]] — and explains why the **slowest stage** (typically Execute with its [[RippleCarryAdder|ripple-carry adder]]) bounds the minimum [[ClockCycle|clock-cycle]] period, motivating the modern shift to **multicore** after clock rates hit the [[PowerWall|power wall]] in the mid-to-late 2000s.

## Key Claims

- The CPU executes each instruction in **four stages** — **Fetch**, **Decode**, **Execute**, **WriteBack** — driven by the [[ClockSignal|clock]]; one stage advances per [[ClockCycle|clock cycle]] in the simplest single-cycle-per-stage design.
- **Fetch**: *"The PC keeps track of the memory address of the next instruction to fetch and is incremented as part of executing the fetch stage."* The [[ProgramCounter|PC]] addresses memory, the fetched bits land in the [[InstructionRegister|IR]], and the PC is bumped by the instruction-width (4 bytes for 32-bit instructions).
- **Decode**: the IR bits are split into [[OpCode|opcode]] (high-order bits selecting the operation) + operand fields (source-register selectors `Sr0`/`Sr1` + destination-register selector `Sw`). The opcode routes to the [[ArithmeticLogicUnit|ALU]]; the operand bits route to the [[RegisterFile|register file]]'s read-selection inputs.
- **Execute**: the ALU performs the opcode-selected operation on the register-file outputs and produces both a result and condition-code bits.
- **WriteBack**: the ALU result is written into the destination register via the register file's write-select input with `WE = 1`.
- An [[InstructionSet|instruction set architecture (ISA)]] defines the set of operations a CPU can execute; each operation has an [[OpCode|opcode]] and a fixed-bit-pattern [[MachineCode|machine-code]] encoding. [[AssemblyLanguage|Assembly]] is the human-readable form; the [[Assembler|assembler]] performs the [[AssemblerToMachineCode|assembly→machine-code translation]].
- **Clock pacing**: a [[ClockCycle|clock cycle]] is one period of the clock; the **[[ClockEdge|clock edge]]** transitions between voltage states — the **rising edge** signals inputs are ready, the **falling edge** signals outputs have stabilized after [[CircuitDelay|propagation delay]] through combinational circuits. **Clock rate** (or clock speed) is the cycle frequency — *"a 1-MHz clock rate has one million clock ticks per second, and 1-GHz has one billion clock ticks per second."*
- The **minimum clock-cycle length is bounded by the slowest stage** — typically Execute, because the ALU's [[RippleCarryAdder|ripple-carry adder]] is the longest combinational path.
- **Cycles Per Instruction ([[CyclesPerInstruction|CPI]])** is the more meaningful throughput metric than raw clock rate; a naive four-stage CPU pays **CPI = 4** in the best case.
- **Historical inflection**: *"Clock rates peaked in the mid to late 2000s with processors like the IBM z10, which had a clock rate of 4.4 GHz."* The subsequent **[[PowerWall|power wall]]** (heat-dissipation limit) drove the architectural pivot to [[MulticoreProcessor|multicore]].

## Key Quotes

> "The PC keeps track of the memory address of the next instruction to fetch and is incremented as part of executing the fetch stage." — §5.6

> "A 1-MHz clock rate has one million clock ticks per second, and 1-GHz has one billion clock ticks per second." — §5.6

> "Clock rates peaked in the mid to late 2000s with processors like the IBM z10, which had a clock rate of 4.4 GHz." — §5.6

## Connections

- [[DiveIntoSystems]] — the source textbook; Ch 5.6 is the operational counterpart of [[dis-5-5-cpu|Ch 5.5]]'s structural data-path picture. **Resolves** Ch 5.5's forward reference: *"in the next section, we discuss how the CPU executes program instructions and how the clock is used to drive the execution of program instructions."*
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[FetchDecodeExecuteCycle]] — Ch 5.6 supplies the **four-stage decomposition** (Fetch / Decode / Execute / WriteBack) operating the cycle.
- [[ProgramCounter]] — Ch 5.6 specifies the **PC++ during Fetch** mechanic (by instruction width — 4 bytes for 32-bit ISAs).
- [[InstructionRegister]] — Ch 5.6 specifies the **IR-receives-fetched-bits** half of Fetch.
- [[ArithmeticLogicUnit]] / [[RegisterFile]] — the [[dis-5-5-cpu|Ch 5.5]] components Decode wires up and Execute / WriteBack operate.
- [[OpCode]] / [[InstructionSet]] / [[MachineCode]] / [[AssemblerToMachineCode]] — the ISA-layer vocabulary Ch 5.6 introduces.
- [[ClockSignal]] / [[ClockCycle]] / [[ClockSpeed]] / [[ClockEdge]] / [[CircuitDelay]] — the timing layer that paces stage advancement; Ch 5.6 **promotes** the named-role-only [[dis-5-5-cpu|Ch 5.5]] forward references to operative concepts.
- [[CyclesPerInstruction]] — the throughput metric Ch 5.6 introduces.
- [[PowerWall]] / [[MulticoreProcessor]] — Ch 5.6's historical-context bridge to modern parallel-processor design.
- [[dis-5-4-1-arithmetic-logic-circuits]] — Ch 5.4.1's ripple-carry adder is the canonical slowest-path circuit setting the minimum cycle length here.

## Contradictions

None with existing wiki content; Ch 5.6 **resolves** rather than contradicts the [[dis-5-5-cpu|Ch 5.5]] forward reference.
