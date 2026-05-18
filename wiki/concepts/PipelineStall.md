---
title: "Pipeline Stall (Bubble)"
type: concept
tags: [computer-architecture, cpu, pipelining, hazards, stall, nop]
sources: [dis-5-8-pipelining-advanced]
last_updated: 2026-05-17
---

# Pipeline Stall (Bubble)

A **pipeline stall** — colloquially a **bubble** — is [[dis-5-8-pipelining-advanced|Ch 5.8]]'s simplest [[PipelineHazard|hazard]] mitigation: the processor *"forces all instructions to take the same number of pipeline stages by inserting [[NoOperation|no-operation]] instructions for stages not needed."* Equivalently, the pipeline pauses the affected instruction (and everything behind it) for one or more cycles, filling the affected stage with a NOP that does nothing useful.

## Where Ch 5.8 uses it

- Against [[DataHazard|data hazards]] — wait for the producer's WriteBack to land before letting the consumer's Decode read the register. Used when [[Forwarding|operand forwarding]] is not available.
- Against [[ControlHazard|control hazards]] — wait for a [[BranchInstruction|branch]] to resolve before letting more instructions enter Fetch. Used when [[BranchPrediction|branch prediction]] is not available or has just mispredicted.

## The performance cost

Each stall cycle is a wasted slot in the steady-state throughput pipeline — it pushes the effective [[CyclesPerInstruction|CPI]] back **above 1**, partially undoing [[InstructionPipelining|pipelining]]'s headline throughput win. That's why Ch 5.8 spends most of its airtime on the *alternatives* — forwarding, branch prediction, eager execution — that avoid the stall.

> *"Compilers and processors do whatever they can to avoid pipeline stalls in order to maximize performance."* — [[dis-5-8-pipelining-advanced|Ch 5.8]]

## Connections

- [[PipelineHazard]] / [[DataHazard]] / [[ControlHazard]] — what stalls mitigate.
- [[NoOperation]] — the bubble instruction stalls inject.
- [[Forwarding]] — preferred alternative for data hazards.
- [[BranchPrediction]] — preferred alternative for control hazards.
- [[CyclesPerInstruction]] — the metric stalls degrade.
- [[InstructionPipelining]] — the optimization stalls partially undo.
- [[dis-5-8-pipelining-advanced]] — primary source.
