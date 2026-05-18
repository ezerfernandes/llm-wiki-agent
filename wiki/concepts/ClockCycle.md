---
title: "Clock Cycle"
type: concept
tags: [systems, computer-architecture, cpu, clock, timing]
sources: [dis-5-5-cpu]
last_updated: 2026-05-17
---

# Clock Cycle

A **clock cycle** is one period of the [[ClockSignal|clock signal]] that paces a synchronous [[CPU]] — the time window during which the [[ProcessorDatapath|data path]]'s combinational logic settles and [[StorageCircuit|storage cells]] latch new values.

## What [[dis-5-5-cpu|Ch 5.5]] says

Ch 5.5 names the clock's CPU role only: a CPU includes *"a clock that drives the circuitry of the CPU to execute program instructions."* The chapter explicitly **defers the clock-cycle mechanism**:

> "In the next section, we discuss how the CPU executes program instructions and how the clock is used to drive the execution of program instructions."

So in the Ch 5.5 scope, *clock cycle* is named as the unit of CPU-execution timing, but the quantitative treatment (how long one cycle lasts, what fits inside it, how it relates to instruction execution) is forward-referenced.

## What Ch 5.5 does NOT cover (forward-context)

- The period-vs-frequency relation $T = 1 / f$ — [[ClockSpeed|clock speed]] is a sibling page.
- The *clock-period ≥ longest combinational-circuit propagation delay* timing constraint — see [[CircuitDelay]].
- Per-instruction cycle counts (CPI), pipelining, multi-cycle vs single-cycle datapaths.
- Setup / hold times of [[DLatch|D-latches]] / [[FlipFlop|flip-flops]] (Ch 5.4.3 already abstracted these away behind [[WriteEnable|WE]]).

## Connections

- [[ClockSignal]] — the periodic wire; one cycle = one period of this signal.
- [[ClockSpeed]] — the frequency reciprocal of cycle length.
- [[CircuitDelay]] — the lower bound on cycle length.
- [[CPU]] / [[ProcessorDatapath]] — what one cycle drives.
- [[FetchDecodeExecuteCycle]] — the multi-step instruction-execution loop a cycle is the timing unit of.
- [[dis-5-5-cpu]] — source.
