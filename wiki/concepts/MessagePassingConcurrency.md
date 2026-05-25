---
title: "Message-Passing Concurrency"
type: concept
tags: [programming-languages, concurrency, message-passing, actor-model]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Message-Passing Concurrency

A concurrent paradigm in which **concurrent agents each running in a single thread send each other messages**. *"The languages CSP (Communicating Sequential Processes) and Erlang use message passing. CSP processes send synchronous messages (the sending process waits until the receiving process has taken the message) and Erlang processes send asynchronous messages (the sending process does not wait)."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Two flavors

- **Synchronous message passing** ([[CSP]]; Hoare 1985) — sender waits until receiver takes the message
- **Asynchronous message passing** ([[Erlang]]; Armstrong, Williams, Wikström & Virding 1996) — sender does not wait; receiver buffers incoming messages

## Position in Van Roy's taxonomy

Message-passing concurrency has:
- **Observable nondeterminism: yes** (the receiver does not know which sender's message arrives next)
- **Named state: yes** (each agent maintains its own state across messages)
- **Races possible: yes** (Table 2)

This places message-passing concurrency at the **named, nondeterministic, concurrent** position of the state lattice (Figure 3). But it has a critical structural property that mitigates the danger:

> *"Each agent runs in a single thread."*

Messages are processed *one at a time per agent* — internal agent state has no shared-memory race conditions, only the message ordering across agents is nondeterministic.

## Why Van Roy recommends it for general-purpose concurrent programming

Van Roy's policy recommendation for the [[DefinitiveLanguage|definitive language]] (Section 3.2): **message-passing concurrency is the correct default for general-purpose concurrent programming**, *not* shared-state concurrency.

> *"A final conclusion is that message-passing concurrency is the correct default for general-purpose concurrent programming instead of shared-state concurrency."*

The four converging definitive-language projects ([[Erlang]] / [[E_Language|E]] / [[DistributedOz|Distributed Oz]] / [[CTM|Didactic Oz]]) all place message-passing concurrency above declarative concurrency in their layered architecture (Table 1).

## Versus shared-state concurrency

> *"There are two popular paradigms for concurrency. The first is **[[SharedStateConcurrency|shared-state concurrency]]**: threads access shared data items using special control structures called monitors to manage concurrent access. This paradigm is by far the most popular. It used by almost all mainstream languages, such as Java and C#. ... The second paradigm is **message-passing concurrency**: concurrent agents each running in a single thread that send each other messages. ... Despite their popularity, monitors are the most difficult concurrency primitive to program with. Transactions and message passing are easier, but still difficult."*

Both paradigms can express the same computations; the difference is in **what is hard**. Monitors share mutable data + use locks → reasoning is about interleavings of statements. Message passing shares immutable messages + use private state → reasoning is about message sequences per agent.

## In this wiki

The wiki's anchor for the [[Erlang]] / [[CSP]] / Actor-style concurrency tradition — distinct from the wiki's existing [[Pthreads]] / [[Mutex]] (shared-state) coverage and from the modern LLM-agent vocabulary ([[AgenticAI]], [[react|`dspy.ReAct`]]) which uses "agent" in a different sense (LLM-driven decision loop, not concurrent message-handler). The agent / message-queue worked example in [[vol1000-oz-programming-model]] is the OPM-realized form of this paradigm.
