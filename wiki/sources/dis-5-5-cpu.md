---
title: "Dive into Systems — Ch 5.5 Building a Processor"
type: source
tags: [systems, computer-architecture, cpu, alu, register-file, datapath, clock]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C5-Arch/cpu.html
---

## Summary

Chapter 5.5 *Building a Processor: Putting It All Together* assembles [[dis-5-4-circuits|Ch 5.4]]'s three circuit categories into a working [[CPU]]. The chapter has three subsections — **5.5.1 The ALU**, **5.5.2 The Register File** (plus *Special-Purpose Registers*), **5.5.3 The CPU** — and culminates in the **[[ProcessorDatapath|data path]]** as the integration concept: the [[ArithmeticLogicUnit|ALU]] + [[RegisterFile|register file]] + [[Bus|buses]] linking them, paced by a [[ClockSignal|clock]] that *"drives the circuitry of the CPU to execute program instructions."* The matching **control path** that drives instruction execution and the mechanics of clocking are explicitly forward-referenced to the next section.

## Key Claims

- The [[ArithmeticLogicUnit|ALU]] is a [[Circuit|circuit]] that *"performs arithmetic and logic operations on integer operands"* — operand A + operand B + an **opcode** input → result + **condition-code bits** (negative / zero / carry-out).
- The opcode comes from bits of the [[InstructionRegister|currently-executing instruction]] — an N-operation ALU needs $\log_2 N$ opcode bits, which select the chosen sub-operation's output via an internal [[Multiplexer|MUX]] (the gate-level realization from [[dis-5-4-2-control-circuits|Ch 5.4.2]]).
- A condition-code bit value of `1` *"indicates that the condition holds, and a bit value of 0 indicates that it does not hold for the ALU result"* — feeding eventual [[StatusRegister|status-flag]] / [[IntegerOverflow|overflow-detection]] logic from [[dis-4-5-overflow|Ch 4.5]].
- The [[RegisterFile|register file]] is a [[StorageCircuit|storage]] bank of **8 to 32 general-purpose [[CpuRegister|registers]]** with two simultaneous read ports and one write port. Read selection inputs `Sr0` / `Sr1` drive the output [[Multiplexer|MUXes]]; the write selection input `Sw` drives a [[Demultiplexer|DMUX]] that routes the `WE` bit to exactly the destination register.
- **Special-purpose registers** sit outside the general-purpose file: the [[ProgramCounter|program counter (PC)]] *"stores the memory address of the next instruction to execute"* and the [[InstructionRegister|instruction register (IR)]] *"stores the bits of the current instruction being executed by the CPU."*
- The **[[ProcessorDatapath|data path]]** *"consists of the parts of the CPU that perform arithmetic and logic operations (the ALU) and store data (registers), and the buses that connect these parts"* — the **integration concept** of Ch 5.5.
- A **control path** (driven by [[ControlCircuit|control circuits]] from [[dis-5-4-2-control-circuits|Ch 5.4.2]]) coordinates instruction execution alongside the data path — Ch 5.5 names it; mechanics deferred to the next section.
- The CPU also includes *"a clock that drives the circuitry of the CPU to execute program instructions"* — Ch 5.5 names the [[ClockSignal|clock]] role and forward-references its mechanism: *"In the next section, we discuss how the CPU executes program instructions and how the clock is used to drive the execution of program instructions."*

## Key Quotes

> "The data path consists of the parts of the CPU that perform arithmetic and logic operations (the ALU) and store data (registers), and the buses that connect these parts." — §5.5.3

> "The opcode input to the ALU comes from bits in the instruction that the CPU is executing." — §5.5.1

> "When the WE bit is 1, the DMUX outputs a WE bit value of 1 to only the register specified by the write selection input (Sw)." — §5.5.2

> "[A CPU includes] a clock that drives the circuitry of the CPU to execute program instructions." — §5.5.3

## Connections

- [[DiveIntoSystems]] — the source textbook; Ch 5.5 is the **integration chapter** of Ch 5 *Computer Architecture* that follows the three-subsection [[dis-5-4-circuits|Ch 5.4 *Circuits*]] block.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[CPU]] — the chapter's headline subject; Ch 5.5 supplies the assembled-from-subcircuits view to complement [[dis-5-2-von-neumann|Ch 5.2]]'s architectural view.
- [[ArithmeticLogicUnit]] / [[RegisterFile]] / [[CpuRegister]] — the building blocks Ch 5.4 supplied and Ch 5.5 wires together.
- [[ProgramCounter]] / [[InstructionRegister]] — the two special-purpose registers Ch 5.5 names alongside the GP file.
- [[ProcessorDatapath]] — the **new umbrella concept** Ch 5.5 introduces: ALU + registers + buses.
- [[ControlUnit]] / [[ControlCircuit]] — the **control path** Ch 5.5 names but defers to the next section.
- [[ClockSignal]] — Ch 5.5 names the clock's CPU role; the [[ClockCycle]] / [[ClockSpeed]] / [[CircuitDelay]] mechanism is forward-referenced.
- [[Multiplexer]] / [[Demultiplexer]] / [[Decoder]] — the [[dis-5-4-2-control-circuits|Ch 5.4.2]] control circuits Ch 5.5 cashes in for ALU opcode select + register file read/write selection.
- [[FullAdder]] / [[RippleCarryAdder]] — the [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] arithmetic circuits the ALU's add/subtract sub-operation contains.
- [[DLatch]] / [[WriteEnable]] — the [[dis-5-4-3-storage-circuits|Ch 5.4.3]] storage primitives each register cell is built from.
- [[FetchDecodeExecuteCycle]] — the operational loop the data path + control path implement together.
- [[VonNeumannArchitecture]] — Ch 5.5's CPU = [[ControlUnit|control]] + [[ProcessingUnit|processing]] units assembled from gates and circuits.

## Contradictions

None. Ch 5.5 is a clean integration of [[dis-5-2-von-neumann|Ch 5.2]]'s architectural decomposition with [[dis-5-4-circuits|Ch 5.4]]'s gate-level circuits — the [[ProcessorDatapath|data path]] concept it introduces is a forward-compatible umbrella, not a revision.

## Scope note (what Ch 5.5 does NOT cover)

- **No quantitative clock treatment**: the [[ClockCycle|clock cycle]], [[ClockSpeed|clock speed]] (Hz / GHz), [[CircuitDelay|circuit / propagation delay]], and the *clock-period ≥ longest-circuit-path* timing constraint are **not in Ch 5.5** — explicitly forward-referenced to the next section.
- **No pipelining / superscalar / out-of-order treatment.**
- **No instruction-set / opcode-encoding specifics** — the ADD-instruction layout (`OPCODE | OPERAND A SOURCE | OPERAND B SOURCE | RESULT DESTINATION`) is shown as a schematic only.
- **No memory hierarchy / cache treatment** — registers are the only storage at this level; main [[RAM|memory]] sits outside the data path of Ch 5.5.
