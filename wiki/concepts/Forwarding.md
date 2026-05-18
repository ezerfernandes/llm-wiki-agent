---
title: "Operand Forwarding (Bypassing)"
type: concept
tags: [computer-architecture, cpu, pipelining, hazards, forwarding]
sources: [dis-5-8-pipelining-advanced]
last_updated: 2026-05-17
---

# Operand Forwarding (Bypassing)

**Operand forwarding** — also called **bypassing** — is the [[dis-5-8-pipelining-advanced|Ch 5.8]] hardware mitigation for [[DataHazard|data hazards]] that **avoids the [[PipelineStall|stall]]** entirely:

> *"Rather than stalling, the pipeline reads the result from the previous operation."*

## What it does

When a producing instruction has computed a value (e.g. an ALU result at the end of Execute) but has not yet written it back into the [[RegisterFile|register file]], a forwarding path wires that result directly to the **input** of the consuming instruction's stage. The consumer therefore sees the correct value **before** the producer's WriteBack stage completes — eliminating the would-be data hazard.

## Why it matters

Without forwarding, every producer-then-consumer register dependency would force a [[PipelineStall|pipeline stall]] (NOP bubbles) until the producer's WriteBack landed — dragging the effective [[CyclesPerInstruction|CPI]] back above 1 and erasing much of [[InstructionPipelining|pipelining]]'s throughput gain. Forwarding makes the common case — back-to-back dependent instructions — run at full pipeline speed.

## Connections

- [[DataHazard]] — the hazard category forwarding mitigates.
- [[PipelineStall]] — the alternative (worse-performance) mitigation.
- [[RegisterFile]] / [[CpuRegister]] — the structure forwarding paths *bypass*.
- [[InstructionPipelining]] / [[PipelineStages]] — the optimization context.
- [[CyclesPerInstruction]] — the metric forwarding protects (keeps CPI near 1).
- [[dis-5-8-pipelining-advanced]] — primary source.
