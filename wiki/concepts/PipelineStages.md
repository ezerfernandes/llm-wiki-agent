---
title: "Pipeline Stages"
type: concept
tags: [computer-architecture, cpu, pipelining, fetch-decode-execute]
sources: [dis-5-7-pipelining]
last_updated: 2026-05-17
---

# Pipeline Stages

**Pipeline stages** are the discrete steps a [[CPU]] [[InstructionPipelining|pipeline]] decomposes instruction execution into — each backed by dedicated stage-specific circuitry that can work on a **different in-flight instruction** every [[ClockCycle|clock cycle]]. [[dis-5-7-pipelining|*Dive into Systems* Ch 5.7]] uses two canonical decompositions.

## Four-stage pipeline (Ch 5.6 baseline)

The four stages [[dis-5-6-instruction-execution|Ch 5.6]] introduced as the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]]:

1. **Fetch** — load instruction from [[RAM|memory]] at the [[ProgramCounter|PC]] into the [[InstructionRegister|IR]]; advance PC.
2. **Decode** — split the [[InstructionRegister|IR]]'s bits into [[OpCode|opcode]] + operand selectors; read source [[CpuRegister|registers]].
3. **Execute** — the [[ArithmeticLogicUnit|ALU]] performs the opcode-selected operation.
4. **WriteBack** — the ALU result is written into the destination [[CpuRegister|register]] via the [[RegisterFile|register file]]'s write port.

When pipelined, the four stages can hold **four different in-flight instructions** simultaneously — one per stage.

## Five-stage pipeline (for memory instructions)

Loads and stores require an extra stage to access [[RAM|memory]]:

1. **Fetch**
2. **Decode**
3. **Execute** — typically address computation.
4. **Memory** — memory read (load) or write (store).
5. **WriteBack** — register-file write (load).

Ch 5.7: *"for load and store operations, a five-stage pipeline (Fetch-Decode-Execute-Memory-WriteBack) is typically employed."*

## Why stages are the right unit

Each stage owns **disjoint circuitry** — Fetch uses the PC + memory-read port; Decode uses the [[InstructionRegister|IR]]-parsing logic + register-file read ports; Execute uses the [[ArithmeticLogicUnit|ALU]]; WriteBack uses the register-file write port. Because the circuitry doesn't overlap, multiple stages can run *in the same cycle* on different instructions without contention — the structural property [[InstructionPipelining|pipelining]] exploits.

## Pipeline depth across real CPUs

Ch 5.7's named examples:

- **ARM**: 3+ stages.
- **Intel Core i7**: 14 stages.

Deeper pipelines slice each stage's combinational work into shorter pieces (see [[CircuitDelay]]), enabling higher clock rates at the cost of more in-flight state.

## Connections

- [[InstructionPipelining]] — the technique that overlaps work across these stages.
- [[FetchDecodeExecuteCycle]] — the per-instruction stage sequence.
- [[InstructionThroughput]] — the metric pipelining over stages optimizes.
- [[CyclesPerInstruction]] — drops as more stages run in parallel on distinct in-flight instructions.
- [[ProcessorDatapath]] — the data-path components each stage owns.
- [[ProgramCounter]] / [[InstructionRegister]] / [[ArithmeticLogicUnit]] / [[RegisterFile]] — the per-stage circuitry.
- [[dis-5-7-pipelining]] — primary source (introduces the 4- and 5-stage decompositions).
- [[dis-5-6-instruction-execution]] — the underlying four-stage cycle.
