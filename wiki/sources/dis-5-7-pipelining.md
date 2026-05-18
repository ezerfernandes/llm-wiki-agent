---
title: "Dive into Systems — Ch 5.7 Pipelining Instruction Execution"
type: source
tags: [systems, computer-architecture, cpu, pipelining, throughput, fetch-decode-execute]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C5-Arch/pipelining.html
---

## Summary

Chapter 5.7 *Pipelining Instruction Execution* extends [[dis-5-6-instruction-execution|Ch 5.6]]'s four-stage [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]] from sequential one-instruction-at-a-time execution into **[[InstructionPipelining|pipelined]]** execution, in which the CPU starts a new instruction every [[ClockCycle|clock cycle]] by **overlapping** successive instructions across [[PipelineStages|stage-specific circuitry]] that would otherwise sit idle. The headline result: once the pipeline is *full*, a four-stage pipelined CPU completes **one instruction per cycle** — the same individual-instruction latency as the non-pipelined baseline but with ~4× the [[InstructionThroughput|instruction throughput]]. Pipelining motivates the extra storage and control circuitry that distinguishes a pipelined data path from [[dis-5-5-cpu|Ch 5.5]]'s single-cycle picture, and explains why modern microprocessors range from ARM's 3+ stages to Intel Core i7's 14.

## Key Claims

- A **non-pipelined** four-stage CPU takes four [[ClockCycle|clock cycles]] per instruction (Fetch → Decode → Execute → WriteBack), giving [[CyclesPerInstruction|CPI]] = 4 for purely sequential execution.
- In non-pipelined execution, each stage's dedicated circuitry sits **idle for three cycles** after it completes its operation on the current instruction — wasted computational capacity.
- **[[InstructionPipelining|Pipelining]]** overlaps the execution of consecutive instructions by starting a new instruction in stage 1 while older instructions are simultaneously working through stages 2, 3, and 4 — *"pipelining increases instruction throughput…by overlapping the execution of sequential instructions in a staggered manner."*
- **Steady-state throughput**: once the pipeline is full, *"the CPU completes the execution of one instruction every clock cycle"* — effective CPI approaches 1 even though individual-instruction latency remains four cycles.
- **Throughput vs latency distinction**: pipelining improves [[InstructionThroughput|throughput]] (instructions completed per unit time) and overall performance **without reducing individual-instruction latency** — each instruction still takes four stages end-to-end.
- For instructions that touch [[RAM|memory]] (loads / stores), a **five-stage** Fetch → Decode → Execute → Memory → WriteBack pipeline is typically used.
- Pipelining requires **additional storage and control circuitry** between stages — the architectural trade-off that the CPI improvement justifies.
- Modern microprocessors implement pipelining at varying depths: **ARM** uses 3+ stages; **Intel Core i7** uses 14.

## Key Quotes

> "When the pipeline is full, the CPU completes the execution of one instruction every clock cycle!" — §5.7

> "Pipelining increases instruction throughput…by overlapping the execution of sequential instructions in a staggered manner." — §5.7

## Connections

- [[DiveIntoSystems]] — the source textbook; Ch 5.7 is the throughput-optimization follow-up to [[dis-5-6-instruction-execution|Ch 5.6]]'s baseline four-stage [[FetchDecodeExecuteCycle|cycle]].
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[FetchDecodeExecuteCycle]] — the four-stage cycle Ch 5.7 **overlaps** rather than replaces.
- [[InstructionPipelining]] — primary concept this chapter introduces.
- [[PipelineStages]] — the per-stage decomposition (Fetch / Decode / Execute / WriteBack, or with Memory for loads/stores).
- [[InstructionThroughput]] — the [[CPU]]-throughput metric pipelining optimizes, distinguished from per-instruction latency.
- [[CyclesPerInstruction]] — the CPI metric drops from 4 (non-pipelined) toward 1 (full pipeline) without latency change.
- [[ClockCycle]] — the unit of pipeline advancement; each cycle promotes every stage's in-flight instruction by one slot.
- [[ProcessorDatapath]] — pipelining inserts per-stage storage + control circuitry into the data path.
- **ARM** / **Intel Core i7** — Ch 5.7's named pipeline-depth exemplars (ARM 3+ stages; Intel Core i7 14 stages). No wiki pages for these yet.

## Contradictions

None with existing wiki content. Ch 5.7 strictly extends [[dis-5-6-instruction-execution|Ch 5.6]]'s sequential picture — does not retract any prior claim. **Scope note**: Ch 5.7 does **not** cover pipeline **hazards** (data / control / structural) — those are not introduced in this section per the source text.
