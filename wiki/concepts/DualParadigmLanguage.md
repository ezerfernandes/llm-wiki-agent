---
title: "Dual-Paradigm Language"
type: concept
tags: [programming-languages, design, multiparadigm]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Dual-Paradigm Language

A language that **supports two paradigms** — *"typically one for programming in the small and another for programming in the large. The first paradigm is chosen for the kind of problem most frequently targeted by the language. The second paradigm is chosen to support abstraction and modularity and is used when writing large programs."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Examples

| Language | "In the small" paradigm | "In the large" paradigm |
|---|---|---|
| **Prolog** | Logic programming engine (unification + depth-first search) | Imperative (assert / retract clauses) |
| **Modeling languages (Comet, Numerica)** | Solver: constraint programming / local search / SAT | Object-oriented |
| **Solving libraries (Gecode)** | Solver library (advanced search algorithms) | Whatever the host language adds (e.g., C++ / Java OOP) |
| **Language embedding (SQL)** | Relational queries + transactional concurrent updates | Object-oriented host language → three-paradigm design |

The **SQL** example is particularly clean: SQL already supports two paradigms (queries + transactions); the host language adds a third (OOP for organization).

## Why it works

> *"A language is not designed in a vacuum, but for solving certain kinds of problems. Each problem has a paradigm that is best for it. No one paradigm is best for all problems. That is why it is important to choose carefully the paradigms supported by the language."*

A dual-paradigm language is the **minimum** for non-toy programs. Programs typically have parts dominated by one paradigm and parts dominated by another; a dual-paradigm language lets the programmer pick the right paradigm for each part without leaving the language.

## Relation to [[DefinitiveLanguage|definitive languages]]

A [[DefinitiveLanguage|definitive language]] is a **four-paradigm** layered architecture (functional + declarative concurrency + message passing + named state). Dual-paradigm languages are the simpler / more common version of the same multiparadigm thesis: *if one paradigm is not enough, why stop at two?*

## In this wiki

Anchor for the *language-design design space* between mainstream monoparadigm (Java, C++ targeting OOP only) and ambitious multiparadigm ([[Oz]], [[Alice]], [[Curry]], [[CIAO]]). Anchored by [[vanroy-programming-paradigms-for-dummies]].
