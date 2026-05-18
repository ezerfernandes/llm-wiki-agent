---
title: "Instruction Throughput"
type: concept
tags: [computer-architecture, cpu, performance, pipelining, throughput]
sources: [dis-5-7-pipelining]
last_updated: 2026-05-17
---

# Instruction Throughput

**Instruction throughput** is the rate at which a [[CPU]] **completes** instructions — measured (in [[dis-5-7-pipelining|*Dive into Systems* Ch 5.7]]) in instructions per [[ClockCycle|clock cycle]]. It is the **performance metric that [[InstructionPipelining|pipelining]] optimizes** and is **distinct from per-instruction latency**.

## Throughput vs latency

| Metric | What it measures | Pipelining's effect |
|---|---|---|
| **Latency** | Cycles for **one** instruction to finish all stages | **Unchanged** (still 4 stages for a 4-stage pipeline) |
| **Throughput** | Instructions completed **per cycle** in steady state | **Improves** from ~1/4 (non-pipelined) to ~1 (full pipeline) |

Ch 5.7's headline: *"pipelining increases instruction throughput…without reducing individual instruction latency."*

## Steady-state result

For a four-stage [[FetchDecodeExecuteCycle|fetch-decode-execute]] pipeline, once enough cycles have passed to **fill** the pipeline:

> *"When the pipeline is full, the CPU completes the execution of one instruction every clock cycle!"* — Ch 5.7

The effective [[CyclesPerInstruction|CPI]] approaches **1**, even though each individual instruction still takes four cycles end-to-end.

## Relation to CPI and clock rate

Performance ≈ clock rate × instructions/cycle = (1 / [[ClockCycle|cycle period]]) × (1 / [[CyclesPerInstruction|CPI]]).

Ch 5.7's pipelining drives the second factor (throughput / inverse-CPI) up without changing the first.

## Scope note

Ch 5.7 introduces throughput in the **idealized full-pipeline** regime — it does **not** discuss the throughput losses caused by pipeline hazards (data dependencies, branches, memory stalls) or by pipeline startup / drain. Those are not covered in this section.

## Connections

- [[InstructionPipelining]] — the technique that improves throughput.
- [[CyclesPerInstruction]] — the inverse-rate metric throughput corresponds to.
- [[PipelineStages]] — the per-stage decomposition pipelining exploits to raise throughput.
- [[ClockCycle]] / [[ClockSpeed]] — the time units throughput is measured against.
- [[FetchDecodeExecuteCycle]] — the per-instruction cycle whose stages get overlapped.
- [[CPU]] — the device whose throughput this metric describes.
- [[dis-5-7-pipelining]] — primary source.
