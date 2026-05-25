---
title: "Feedback Loop"
type: concept
tags: [programming-languages, distributed-systems, architecture, control]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Feedback Loop

A three-agent structure forming the basic unit of a [[SelfSufficientSystem|self-sufficient system]]: a **monitoring agent**, a **correcting agent** ("calculate corrective action"), and an **actuating agent**, all interacting with a **subsystem**. *"Since each subsystem must be as self-sufficient as possible, there must be feedback loops at all levels."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Single loop structure (Figure 6)

```
                    ┌────────────────────────┐
                    │ Calculate corrective    │
                    │ action                  │
                    └────────────────────────┘
                       ↑                  ↓
              ┌─────────────────┐  ┌──────────────────┐
              │ Monitoring agent │  │ Actuating agent  │
              └─────────────────┘  └──────────────────┘
                       ↑                  ↓
                    ┌────────────────────────┐
                    │       Subsystem         │
                    └────────────────────────┘
```

The three agents run **concurrently** ([[MessagePassingConcurrency|message-passing concurrency]] paradigm). The subsystem is the part of the world the loop adapts to or maintains.

## Two ways loops interact

- **[[Stigmergy]]** — two loops share one subsystem. Indirect coordination through a common environment. (Term originates in biology, from termite-colony coordination via shared pheromone trails.)
- **Management** — one loop directly controls another loop. Hierarchical coordination.

## Worked examples in [[vanroy-programming-paradigms-for-dummies]]

### TCP as a feedback loop structure (Figure 7)

**Two nested loops**:

- **Inner loop (reliable transfer via sliding window protocol)**:
  - Monitor: receive ack
  - Calculate: calculate bytes to send (sliding window protocol)
  - Actuator: send packet
  - Subsystem: the network that sends packets to destinations and receives acks
- **Outer loop (congestion control)**:
  - Monitor: throughput
  - Calculate: policy modification (modify throughput)
  - **Actuator**: modify the inner loop's sliding-window size
  - The outer loop's actuator *is* the inner loop's policy parameter — **management interaction**

### Human respiratory system as a feedback loop structure (Figure 8)

**Four loops** — three in a **management tower** (breathing reflex → CO₂-trigger → conscious control → unconsciousness-trigger), the fourth (laryngospasm — seal air tube) interacting via **stigmergy**.

## Design lesson

Realistic large-scale systems are **not** monolithic. They are **sets of interacting feedback loops** at multiple abstraction levels, coordinated via stigmergy + management. *"In our view, the large-scale structure of software will more and more be done in this self-sufficient style."*

## In this wiki

The wiki's first **control-theoretic** anchor for software architecture. Distinct from the wiki's existing concurrency vocabulary (which focuses on synchronization primitives) and from the modern *agentic-AI* literature (which focuses on LLM-driven decision-making per agent rather than on the system topology of interacting loops). Anchored by [[vanroy-programming-paradigms-for-dummies]].
