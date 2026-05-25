---
title: "Discrete Synchronous Programming"
type: concept
tags: [programming-languages, concurrency, reactive, deterministic, synchronous]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Discrete Synchronous Programming

A reactive paradigm: *"a program waits for input events, does internal calculations, and emits output events. This is called a **reactive system**. Reactive systems must be deterministic: the same sequence of inputs produces the same sequence of outputs."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Key property: discrete time

Unlike [[FunctionalReactiveProgramming|FRP]]'s continuous time, **time is discrete** — *"time advances in steps from one input event to the next. Output events are emitted at the same logical time instants as the input events. All calculations done to determine the next output event are considered to be part of the same time instant."*

This matches the model of **clocked digital logic**:
- Combinational circuits are *"instantaneous"* (within one clock cycle)
- Sequential circuits *"take time"* (use clocked memory, happen over several cycles)
- The clock signal is a sequence of input events

## Why it simplifies reactive programming

> *"Using discrete time enormously simplifies programming for reactive systems. For example, it means that subprograms can be trivially composed: output events from one subcomponent are instantaneously available as input events in other subcomponents."*

Composition reduces to the same-clock-tick rule — no glitches, no race conditions, no propagation order to manage.

## Mealy machine semantics

> *"Technically, a program in a synchronous language such as [[Esterel]] defines a deterministic Mealy machine, which is a finite state automaton in which each state transition is labeled with an input and an output."*

This is a **strong semantic guarantee** — compile a synchronous program and get a state machine that can be analyzed, model-checked, and certified.

## Languages

- **[[Esterel]]** (Berry, École des Mines / INRIA 1999) — imperative
- **[[Lustre]]** (Halbwachs & Pascal 2002) — functional dataflow
- **[[Signal]]** (Houssais, IRISA 2002) — relational dataflow
- **[[Faust]]** (Orlarey, Fober & Letz 2004) — signal-processing variant (similar to Lustre); discrete-synchronous with functional flavor; high clock frequency + efficient compilation to C++
- **Timed CC** (Olarte, Rueda & Valencia 2009) — combines discrete-synchronous with [[ConcurrentConstraintProgramming|concurrent constraint]] for music modeling

## Position in Van Roy's Table 2

Discrete synchronous programming is **paired** with [[FunctionalReactiveProgramming|FRP]] in the no-nondeterminism-but-nondeterministic-input cell — same property profile, different time model (discrete vs continuous).

## Applications

- **Safety-critical reactive systems** — avionics flight control, nuclear-reactor monitoring, automotive ABS. Esterel and Lustre are the canonical industrial languages here (Scade / Ansys SCADE Suite for avionics).
- **Computer music** — [[IRCAM]] systems ([[MaxMSP]], [[Antescofo]], [[Faust]]) use discrete-synchronous semantics for real-time deterministic music performance.

## In this wiki

The wiki's first **synchronous-language** anchor — important for an entire applied domain (safety-critical reactive systems + computer music) the wiki's ML / DL / systems corpora do not engage with. Anchored by [[vanroy-programming-paradigms-for-dummies]]; reachable from [[IRCAM]] / [[MaxMSP]] / [[Antescofo]] / [[Faust]] / [[OpenMusic]] applied-context.
