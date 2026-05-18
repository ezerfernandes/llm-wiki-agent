---
title: "Moore's Law"
type: concept
tags: [computer-architecture, cpu, history, scaling]
sources: [dis-5-9-modern]
last_updated: 2026-05-17
---

# Moore's Law

**Moore's Law** is Gordon Moore's observation (restated in 1975) that the **transistor density on an integrated circuit doubles approximately every two years**. [[dis-5-9-modern|Ch 5.9]] uses it as the framing device for the entire history of modern CPU architecture: every architectural era is a story about *how architects spent the doubling transistor budget*.

## Timeline (per Ch 5.9)

- **1965 / 1975 — Moore's original / revised observation.**
- **Late 20th c. through the 2000s** — architects spent transistors on ever-more-complex single processors: deeper pipelines, wider [[Superscalar|superscalar]] issue, larger caches, more aggressive [[OutOfOrderExecution|out-of-order]] machinery, better [[BranchPrediction|branch prediction]].
- **Early 2000s — the [[PowerWall|power wall]]**: clock-speed scaling stopped being free. Architects pivoted to **multiple cooperating execution streams** ([[HardwareMultithreading|HW multithreading]], [[SimultaneousMultithreading|SMT]], [[MulticoreProcessor|multicore]]) instead of one ever-faster core.
- **~2012** — transistor-density doubling **started slowing** in observable practice.
- **Mid-2020s** — Moore himself predicted the law would effectively end.

## What it is *not*

Moore's Law is about **transistor count / density**, not clock speed, not performance, not power efficiency. Decades of habit conflated the four because, while clock speeds scaled (~1971–2003) and ILP kept extracting more work per cycle, total performance roughly tracked the transistor count — a coincidence that ended with the [[PowerWall|power wall]].

## Why Ch 5.9 leads with it

The chapter's central narrative: *"multicore microprocessor design is the primary way in which the performance of processor architectures can continue to keep pace with Moore's Law without increasing the processor clock rate."* Multicore is the architectural response to the **decoupling of transistor budget from single-thread performance**.

## Connections

- [[PowerWall]] — the constraint that broke the "more transistors = faster single thread" link.
- [[InstructionLevelParallelism]] — how architects spent the transistor budget *before* the power wall.
- [[MulticoreProcessor]] — how they spent it *after*.
- [[SimultaneousMultithreading]] / [[HardwareMultithreading]] — additional post-power-wall scaling levers.
- [[ClockSpeed]] — the variable Moore's Law is **not** about.
- [[CPU]] — the device the law was originally observed on.
- [[dis-5-9-modern]] — primary source.
