---
title: "Clock Speed"
type: concept
tags: [systems, computer-architecture, cpu, clock, timing, performance]
sources: [dis-5-5-cpu]
last_updated: 2026-05-17
---

# Clock Speed

**Clock speed** (clock *frequency* / *rate*) is the rate at which a [[CPU]]'s [[ClockSignal|clock]] ticks — the reciprocal of the [[ClockCycle|clock cycle]] period $f = 1 / T$. Measured in **hertz (Hz)**; modern CPUs operate in **gigahertz (GHz)** — `1 GHz = 10^9` cycles per second.

## What [[dis-5-5-cpu|Ch 5.5]] says

Ch 5.5 names the clock as *"a clock that drives the circuitry of the CPU to execute program instructions"* but **does not quantify clock speed**, does not introduce Hz / GHz units, and does not discuss its relation to instruction-throughput performance. The chapter forward-references:

> "In the next section, we discuss how the CPU executes program instructions and how the clock is used to drive the execution of program instructions."

So in the Ch 5.5 scope, *clock speed* is implicit in the named clock-as-pacing-signal, but quantitative treatment is deferred.

## What Ch 5.5 does NOT cover (forward-context)

- Specific GHz numbers for real CPUs.
- The clock-speed plateau ($\sim$2005-onward) that motivates [[MulticoreProcessor|multicore]] (handled by [[dis-0-introduction|Ch 0]] from the OS-architecture angle, not by Ch 5.5).
- The fundamental upper-bound rule **clock period ≥ longest [[CircuitDelay|circuit-delay]] path** — captured separately on the [[CircuitDelay]] page.
- Power / thermal limits, dynamic voltage-frequency scaling, turbo / boost behaviour.

## Connections

- [[ClockSignal]] — the wire whose frequency *is* clock speed.
- [[ClockCycle]] — the reciprocal unit ($T = 1/f$).
- [[CircuitDelay]] — the physical bound that caps achievable clock speed.
- [[CPU]] / [[MulticoreProcessor]] — the unit whose performance clock speed historically scaled.
- [[dis-5-5-cpu]] — source naming the clock role; quantitative treatment deferred.
