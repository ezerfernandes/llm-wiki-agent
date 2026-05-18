---
title: "Data Hazard"
type: concept
tags: [computer-architecture, cpu, pipelining, hazards]
sources: [dis-5-8-pipelining-advanced]
last_updated: 2026-05-17
---

# Data Hazard

A **data hazard** is a [[PipelineHazard|pipeline hazard]] in which *"two instructions attempt to access common data in an instruction pipeline"* ([[dis-5-8-pipelining-advanced|Ch 5.8]]). It's the register-dependency failure mode of [[InstructionPipelining|pipelining]].

## The canonical example

A `MOV` writes a [[CpuRegister|register]] and the immediately-following `ADD` reads that same register. Under non-pipelined execution this is fine — `MOV` finishes WriteBack before `ADD` enters Decode. Under a pipelined CPU the two instructions are in flight simultaneously: when `ADD` reaches Decode it tries to read from the [[RegisterFile|register file]] **before** `MOV`'s WriteBack stage has written the new value back, so it would get the stale prior value.

## Mitigations Ch 5.8 covers

- **[[PipelineStall|Pipeline stalling]] / bubbles** — inject [[NoOperation|NOP]] instructions for stages not needed, forcing all instructions to take the same number of pipeline stages and giving `MOV`'s WriteBack time to land before `ADD`'s Decode reads. Simple, but degrades [[CyclesPerInstruction|CPI]].
- **[[Forwarding|Operand forwarding]] (a.k.a. bypassing)** — *"rather than stalling, the pipeline reads the result from the previous operation"* ([[dis-5-8-pipelining-advanced|Ch 5.8]]). Wires the producing instruction's stage output directly into the consuming instruction's stage input, skipping the round-trip through the register file. The preferred mitigation when applicable.

## Connections

- [[PipelineHazard]] — parent category.
- [[ControlHazard]] — sibling hazard category (branch-related).
- [[Forwarding]] — primary mitigation (no stall).
- [[PipelineStall]] — fallback mitigation (with stall).
- [[CpuRegister]] / [[RegisterFile]] — the contended resource.
- [[InstructionPipelining]] — the optimization data hazards threaten.
- [[dis-5-8-pipelining-advanced]] — primary source.
