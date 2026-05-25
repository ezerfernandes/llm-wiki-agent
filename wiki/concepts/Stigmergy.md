---
title: "Stigmergy"
type: concept
tags: [programming-languages, distributed-systems, coordination, biology]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Stigmergy

One of two fundamental interaction modes between [[FeedbackLoop|feedback loops]] in a [[SelfSufficientSystem|self-sufficient system]]: *"two loops share one subsystem."* The other mode is **management** — one loop directly controls another.

Term originates in **biology** (Pierre-Paul Grassé 1959), describing indirect coordination in social insects (e.g., termite colonies building mounds via shared pheromone trails — no central planner, but the trails accumulated by each insect modify the environment in ways that guide the others).

## In a software-system context

Two [[FeedbackLoop|feedback loops]] share one subsystem if they both monitor / actuate against the same piece of the world. Neither loop knows about the other; their coordination is **mediated by their shared environment**. Example (Van Roy's human-respiratory-system Figure 8, [[vanroy-programming-paradigms-for-dummies]]): the laryngospasm loop interacts with the breathing-reflex / CO₂-trigger / conscious-control tower **via stigmergy** — the shared subsystem is the breathing apparatus.

## Position in [[SelfSufficientSystem|self-sufficient-system]] design

Stigmergy is **looser coupling** than management:

| Coupling mode | Coordination | Knowledge required |
|---|---|---|
| **Stigmergy** | Indirect via shared subsystem | Neither loop knows the other |
| **Management** | Direct: one loop controls another | Manager loop knows the managed loop |

Realistic large-scale systems use both, with stigmergy typically for **peer-level interactions** and management for **hierarchy**.

## In this wiki

The wiki's first anchor for **biological-inspired coordination patterns** in software. Anchored by [[vanroy-programming-paradigms-for-dummies]]; reachable from [[FeedbackLoop]] / [[SelfSufficientSystem]] / [[MessagePassingConcurrency]].
