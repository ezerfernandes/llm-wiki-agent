---
title: "Superscalar Execution"
type: concept
tags: [computer-architecture, cpu, pipelining, parallelism, throughput]
sources: [dis-5-8-pipelining-advanced]
last_updated: 2026-05-17
---

# Superscalar Execution

**Superscalar** is [[dis-5-8-pipelining-advanced|Ch 5.8]]'s name for the parallelism layer that lets a CPU complete **more than one instruction per [[ClockCycle|cycle]]** — pushing past the steady-state ceiling of [[dis-5-7-pipelining|Ch 5.7]]'s single-issue pipeline.

## The mechanism

The CPU **replicates** pipeline stage circuitry so that multiple instructions can occupy the *same* stage in the *same* cycle. With two-wide superscalar issue, the Fetch / Decode / Execute / WriteBack stages each contain enough hardware to process two instructions per cycle in parallel — bringing the throughput-limit [[CyclesPerInstruction|CPI]] below 1 (equivalently, [[InstructionThroughput|IPC]] above 1).

## Relationship to pipelining

Superscalar is **orthogonal** to [[InstructionPipelining|pipelining]]: pipelining overlaps successive instructions across *time* (different stages each cycle); superscalar overlaps successive instructions across *space* (multiple copies of the *same* stage each cycle). Real CPUs combine both — a 4-wide superscalar with a 14-stage pipeline has up to 4 × 14 = 56 instructions in flight.

## Scope note (Ch 5.8)

Ch 5.8 names superscalar as one of the modern-CPU performance levers on top of the pipeline; it does **not** detail issue-width tradeoffs, scheduling complexity, or vendor-specific microarchitectures (Intel's port-based dispatch, ARM's dual-issue Cortex, etc.). Page captures the mechanism as the chapter introduces it.

## Connections

- [[InstructionPipelining]] — the time-axis parallelism superscalar complements.
- [[OutOfOrderExecution]] — the dynamic-reordering parallelism Ch 5.8 pairs with superscalar.
- [[InstructionThroughput]] — the metric superscalar pushes above one instruction per cycle.
- [[CyclesPerInstruction]] — the metric superscalar pushes below 1.
- [[PipelineStages]] — what superscalar replicates.
- [[dis-5-8-pipelining-advanced]] — primary source.
