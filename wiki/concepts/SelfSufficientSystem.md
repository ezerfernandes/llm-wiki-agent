---
title: "Self-Sufficient System"
type: concept
tags: [programming-languages, distributed-systems, architecture, fault-tolerance]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Self-Sufficient System

*"The ultimate software system is one that does not require any human assistance, i.e., it can provide for every software modification that it needs, including maintenance, error detection and correction, and adaptation to changing requirements."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]] (Section 3.3, citing Van Roy 2007, *Self Management and the Future of Software Design*).

Self-sufficient systems can be **very robust** — peer-to-peer networks survive in extremely hostile environments by doing **reversible phase transitions** (Van Roy 2008).

## Architecture

Built on three programming-paradigm layers:

1. **Components as first-class entities** (specified by [[Closure|closures]]) that can be manipulated through higher-order programming.
2. Components behave as **isolated concurrent agents** communicating through [[MessagePassingConcurrency|message passing]].
3. **[[NamedState|Named state]] and transactions** for system reconfiguration and system maintenance. *"Named state allows us to manage the content of components and change their interconnections."*

This is **the same layered architecture** as the [[DefinitiveLanguage|definitive language]] (Table 1) — applied to self-sufficient-system construction rather than general-purpose programming.

## Feedback loops as the design pattern

> *"To allow the program to adapt itself to its environment, we take inspiration from biological systems and organize its components as feedback loops. The system then consists of a set of interacting feedback loops."*

A single [[FeedbackLoop|feedback loop]] (Figure 6) has three concurrent components interacting with a subsystem: a **monitoring agent**, a **correcting agent** ("calculate corrective action"), and an **actuating agent**.

Realistic systems consist of **many feedback loops**, each subsystem self-sufficient. The loops interact in two fundamental ways:

- **[[Stigmergy]]** — *"two loops share one subsystem"* (indirect coordination via a common environment)
- **Management** — *"one loop controls another loop directly"* (hierarchical coordination)

## Real-world examples

- **TCP** (Figure 7) — *"part of the Transmission Control Protocol as a feedback loop structure"*: inner loop = reliable transfer via sliding window protocol (calculate bytes to send / send packet / receive ack); outer loop = congestion control (if too many packets are lost, reduce the inner loop's transfer rate by reducing the window size).
- **Human respiratory system** (Figure 8, citing François 2009) — four loops: three form a tower connected by management (breathing reflex → CO₂-trigger → conscious control → unconsciousness-trigger), the fourth (laryngospasm — seal air tube) interacts via stigmergy.

## Why this matters for software at scale

> *"In our view, the large-scale structure of software will more and more be done in this self-sufficient style. If it is not done in this way, the software will simply be too fragile and collapse with any random error or problem."*

## In this wiki

The wiki's anchor for **self-managing distributed systems** as a programming-paradigm problem. Distinct from the wiki's modern *agentic-AI* vocabulary ([[AgenticAI]], [[react|`dspy.ReAct`]], [[CustomerServiceAgent]]) — Van Roy's "self-sufficient system" is a *system-architecture* idea (feedback loops + named state for reconfiguration), not an LLM-driven decision loop. The two concepts may converge: an LLM-driven monitoring/correcting/actuating agent inside a Van-Roy-style feedback loop is a natural fit. Anchored by [[vanroy-programming-paradigms-for-dummies]]; relates to [[FeedbackLoop]] / [[Stigmergy]] / [[MessagePassingConcurrency]] / [[NamedState]] / [[Closure]].
