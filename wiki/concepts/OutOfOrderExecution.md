---
title: "Out-of-Order Execution"
type: concept
tags: [computer-architecture, cpu, pipelining, scheduling, ooo]
sources: [dis-5-8-pipelining-advanced]
last_updated: 2026-05-17
---

# Out-of-Order Execution

**Out-of-order execution** (OoO) is [[dis-5-8-pipelining-advanced|Ch 5.8]]'s second layered-on-top-of-pipelining performance lever (sibling to [[Superscalar|superscalar]] issue). The processor *dynamically reorders* in-flight instructions: when an instruction is stalled waiting for a slow operand (a [[DataHazard|data hazard]] not fixed by [[Forwarding|forwarding]], a cache miss, a long-latency multiply), the CPU runs **later** instructions that are *ready to execute*, then commits results in original program order at retirement.

## Why it matters

Strict in-program-order execution leaves the pipeline idle during any stall; out-of-order execution **finds work** for the otherwise-idle stage circuitry, raising effective [[InstructionThroughput|throughput]] without changing the program's observable result.

## Relationship to pipelining and superscalar

[[InstructionPipelining|Pipelining]] overlaps successive instructions in time. [[Superscalar|Superscalar]] replicates stages so multiple instructions can run in parallel. Out-of-order execution **chooses which** ready instructions to dispatch into those slots — so the three combine: a 14-stage 4-wide out-of-order CPU pipelines, replicates, *and* dynamically reorders.

## Scope note (Ch 5.8)

Ch 5.8 names out-of-order execution as a modern-CPU performance lever; it does **not** detail the mechanics (reservation stations, reorder buffer, register renaming, Tomasulo's algorithm) or the implications for [[BranchPrediction|speculative]] / [[Spectre|side-channel]] behavior. Page captures the mechanism as the chapter introduces it.

## Connections

- [[InstructionPipelining]] — the time-axis parallelism out-of-order schedules around.
- [[Superscalar]] — the space-axis parallelism Ch 5.8 pairs with out-of-order.
- [[DataHazard]] — the stall category out-of-order most directly works around.
- [[PipelineStall]] — what out-of-order avoids by finding ready work.
- [[InstructionThroughput]] — the metric out-of-order raises.
- [[dis-5-8-pipelining-advanced]] — primary source.
