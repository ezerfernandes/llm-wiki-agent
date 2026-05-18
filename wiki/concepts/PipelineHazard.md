---
title: "Pipeline Hazard"
type: concept
tags: [computer-architecture, cpu, pipelining, hazards]
sources: [dis-5-8-pipelining-advanced]
last_updated: 2026-05-17
---

# Pipeline Hazard

A **pipeline hazard** is a situation in a pipelined [[CPU]] where two in-flight instructions interfere with each other — breaking the idealized [[dis-5-7-pipelining|Ch 5.7]] *"one instruction completion per cycle"* assumption. [[dis-5-8-pipelining-advanced|Ch 5.8]] introduces the term as the umbrella for the failure modes [[InstructionPipelining|pipelining]] must defend against.

## What Ch 5.8 covers

Ch 5.8 covers **two** hazard categories explicitly:

- **[[DataHazard|Data hazards]]** — two instructions in the pipeline attempt to access **common data** (typically the same [[CpuRegister|register]]) in overlapping stages, with the later instruction needing a value the earlier one has not yet written.
- **[[ControlHazard|Control hazards]]** — a [[BranchInstruction|branch (conditional) instruction]] is in the pipeline and the processor cannot determine which instruction follows it until the branch resolves.

Structural hazards (two instructions needing the same hardware unit in the same cycle) are *not* introduced under that name in Ch 5.8 — the chapter's scope is data + control.

## Why hazards matter

Hazards force the pipeline off its steady-state throughput. The mitigations Ch 5.8 catalogues — [[PipelineStall|stalling]], [[Forwarding|operand forwarding]], [[BranchPrediction|branch prediction]], eager execution — are all hazard-avoidance machinery. Ch 5.8's framing quote:

> *"Compilers and processors do whatever they can to avoid pipeline stalls in order to maximize performance."*

## Connections

- [[InstructionPipelining]] — the optimization hazards threaten.
- [[DataHazard]] — register-dependency hazard category.
- [[ControlHazard]] — branch-resolution hazard category.
- [[PipelineStall]] — generic mitigation (NOP bubbles).
- [[Forwarding]] — data-hazard-specific mitigation.
- [[BranchPrediction]] — control-hazard-specific mitigation.
- [[CyclesPerInstruction]] — the metric hazards degrade.
- [[dis-5-8-pipelining-advanced]] — primary source.
