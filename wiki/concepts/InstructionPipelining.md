---
title: "Instruction Pipelining"
type: concept
tags: [computer-architecture, cpu, pipelining, throughput, performance]
sources: [dis-5-7-pipelining]
last_updated: 2026-05-17
---

# Instruction Pipelining

**Instruction pipelining** is the CPU-microarchitecture technique that **overlaps the execution of successive instructions** across a [[CPU]]'s stage-specific circuitry, starting a new instruction every [[ClockCycle|clock cycle]] rather than waiting for the current instruction to finish all four [[FetchDecodeExecuteCycle|fetch-decode-execute]] stages. [[dis-5-7-pipelining|*Dive into Systems* Ch 5.7]] introduces it as the headline throughput optimization that turns the four-stages-per-instruction sequential baseline into one-instruction-per-cycle steady-state throughput.

## The core observation

In non-pipelined execution, while a given instruction sits in (say) the Execute stage, the Fetch and Decode circuitry is **idle** — fully built, powered, but doing no useful work. Pipelining cashes that idleness in: stage $k$ starts working on instruction $i+1$ as soon as instruction $i$ advances to stage $k+1$.

## Throughput vs latency — the load-bearing distinction

Pipelining **does not reduce individual-instruction latency** — each instruction still walks through four stages and therefore still takes four cycles end-to-end. What changes is [[InstructionThroughput|throughput]]: once the pipeline is full, *"the CPU completes the execution of one instruction every clock cycle"* (Ch 5.7), driving the effective [[CyclesPerInstruction|CPI]] from 4 (non-pipelined) toward 1.

## What the optimization costs

Pipelining demands **additional storage and control circuitry** between stages — the per-stage latches that hold the in-flight instruction's intermediate state. Ch 5.7 frames this as the design trade-off the throughput payoff justifies.

## Pipeline depth in practice

Modern microprocessors implement pipelining at varying depths:

- **ARM**: 3+ stages.
- **Intel Core i7**: 14 stages.

Deeper pipelines allow higher clock rates (each stage's combinational delay is shorter — see [[CircuitDelay]]) at the cost of more in-flight state and worse penalties when the pipeline must be flushed.

## Scope note (Ch 5.7 omissions)

Ch 5.7 does **not** introduce pipeline **hazards** (data dependencies, control / branch hazards, structural conflicts), forwarding / bypassing, branch prediction, or out-of-order execution. Those are not covered in this section.

## Connections

- [[FetchDecodeExecuteCycle]] — the per-instruction four-stage cycle pipelining overlaps.
- [[PipelineStages]] — the stage-by-stage decomposition pipelining exploits.
- [[InstructionThroughput]] — the metric pipelining optimizes.
- [[CyclesPerInstruction]] — drops from 4 toward 1 as the pipeline fills.
- [[ClockCycle]] — the unit of pipeline advancement.
- [[ProcessorDatapath]] — pipelining inserts per-stage latches into the data path.
- [[CPU]] — the device pipelining microarchitects.
- **ARM** / **Intel Core i7** — Ch 5.7's named pipeline-depth exemplars (no dedicated wiki pages yet).
- [[dis-5-7-pipelining]] — primary source.
