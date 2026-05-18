---
title: "Circuit Delay"
type: concept
tags: [systems, computer-architecture, circuits, timing, clock]
sources: [dis-5-5-cpu]
last_updated: 2026-05-17
---

# Circuit Delay

**Circuit delay** (propagation delay) is the time required for input changes to propagate through a [[Circuit|combinational circuit]] and settle at its outputs — the finite signal-travel time through the [[LogicGate|gate]] network plus interconnect.

## What [[dis-5-5-cpu|Ch 5.5]] says

Ch 5.5 **does not quantitatively treat circuit / propagation delay**. The chapter names the [[ClockSignal|clock]] that *"drives the circuitry of the CPU to execute program instructions"* but defers the delay-vs-clock-period relationship to the next section. The relevant bound — *clock period must be at least the longest combinational-path delay* — is a forward reference from the Ch 5.5 scope.

## What Ch 5.5 does NOT cover (forward-context)

- Quantitative gate-delay numbers (picoseconds per [[LogicGate|gate]]).
- The **critical-path** concept — the longest combinational delay between two storage stages caps the [[ClockSpeed|clock frequency]].
- [[RippleCarryAdder|Ripple-carry]]'s $O(N)$ carry-propagation delay vs carry-lookahead's $O(\log N)$ — though [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] *does* observe that the SUM result *"ripples or propagates through the circuit from the low-order to the high-order bits"* (qualitative, not numeric).
- Setup / hold timing margins of [[DLatch|latches]] / [[FlipFlop|flip-flops]] (Ch 5.4.3 abstracted these away behind [[WriteEnable|WE]]).
- Wire-delay scaling effects in deep-submicron nodes, clock-skew budgeting.

## Connections

- [[ClockCycle]] — the period that must be at least as long as the longest circuit-delay path.
- [[ClockSpeed]] — the frequency the circuit-delay floor caps.
- [[Circuit]] — what has the delay.
- [[RippleCarryAdder]] — the [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] circuit whose qualitative *ripple/propagate* behaviour is delay-relevant.
- [[CPU]] / [[ProcessorDatapath]] — the structure whose longest path bounds clock speed.
- [[dis-5-5-cpu]] — source naming the clock-drives-circuitry role; quantitative delay treatment deferred.
