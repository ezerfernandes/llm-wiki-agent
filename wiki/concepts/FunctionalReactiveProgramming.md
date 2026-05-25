---
title: "Functional Reactive Programming"
type: concept
tags: [programming-languages, concurrency, reactive, deterministic, frp]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Functional Reactive Programming

Also called **continuous synchronous programming**. *"In this paradigm, programs are functional but the function arguments can be changed and the change is propagated to the output. ... Semantically, the arguments are continuous functions of a totally ordered variable (which can correspond to useful magnitudes such as **time** or **size**)."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Properties

- **No observable nondeterminism** — function applied to the same inputs always gives the same outputs
- **Accepts nondeterministic input** — but does not *add* nondeterminism of its own
- **Continuous time** — semantically, time is a real-valued variable; values are continuous functions of time; **discretization is introduced only when results are calculated** (so arbitrary scaling is possible without losing accuracy due to approximation)

## The glitch problem

A naive concurrent-stream implementation can produce a **glitch** — a transient incorrect result caused by partial propagation:

> *"For example, the simple functional expression `x+(x*y)` with `x=3` and `y=4` gives `15`. If `x` is changed to `5`, then the expression's result changes from `15` to `25`. Implementing this naively with a concurrent stream connecting a times agent to a plus agent is incorrect. This implementation can give a glitch, for example if the new value of `x` reaches the addition before the new value of the multiplication. This gives a temporary result of `17`, which is incorrect."*

FRP implementations *must* avoid glitches via **compile-time preprocessing** (topological sort of operations) or **thread scheduling constraints**. The closely-related **nonmonotonic dataflow paradigm** (Section 6) propagates changes immediately via "dataflow tokens" and can suffer glitches; FRP is *"similar to nonmonotonic dataflow but without the glitches."*

## Languages

- **[[Yampa]]** (Hudak, Courtney, Nilsson, Peterson 2003) — embedded in [[Haskell]]; used in robotics, game programming
- **[[FrTime]]** (Cooper 2008) — embedded in Scheme/Racket
- **Lambda-pix Reactive** — Conal Elliott's *Simply Efficient Functional Reactivity* (LambdaPix 2008)

## Position in Van Roy's Table 2

| Paradigm | Races possible? | Nondeterministic input? |
|---|---|---|
| [[DeclarativeConcurrency|Declarative concurrency]] | No | No |
| [[ConcurrentConstraintProgramming|Constraint programming]] | No | No |
| **Functional reactive programming** | **No** | **Yes** |
| [[DiscreteSynchronousProgramming|Discrete synchronous]] | No | Yes |
| [[MessagePassingConcurrency|Message passing]] | Yes | Yes |

FRP sits between strict declarative concurrency (which forbids nondeterministic input) and message-passing concurrency (which permits races) — it accepts arbitrary input streams but the program logic remains deterministic.

## In this wiki

The wiki's first FRP anchor. Distinct from the modern web-framework FRP tradition (React / RxJS / Solid signals) which inherits the name and the dataflow idea but typically operates in JavaScript's nondeterministic event-loop substrate. The Van Roy framing — **continuous time as a totally ordered variable** with discretization only at observation points — is the strict semantic form. Important for computer music ([[IRCAM]] [[OpenMusic]] / [[MaxMSP]]) and reactive UIs.
