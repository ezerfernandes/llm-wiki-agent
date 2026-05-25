---
title: "Data Abstraction"
type: concept
tags: [programming-languages, design, modularity, abstraction]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Data Abstraction

*"A data abstraction is a way to organize the use of data structures according to precise rules which guarantee that the data structures are used correctly. A data abstraction has an **inside**, an **outside**, and an **interface** between the two."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Three advantages

1. **Correctness guarantee** — the interface defines the authorized operations on the data structures; no other operations are possible.
2. **Easier-to-understand programs** — a user of the data abstraction does not need to understand how it is implemented. **Compositionality** (defining abstractions inside other abstractions) further reduces complexity.
3. **Large-program development** — the implementation can be divided among a team; each abstraction has one person who is responsible for it.

## Four kinds of data abstraction (Figure 14)

Two axes: **state** (stateful / stateless) × **bundling** (object — bundled / abstract data type — unbundled).

| | Abstract data type (unbundled) | Object (bundled) |
|---|---|---|
| **Stateless** | **"Pure" ADT** (e.g., Java integers — values + free-function operations) | **Declarative object** (less common) |
| **Stateful** | **Stateful ADT** (less common) | **"Pure" object** ⬅ very popular! |

The two **popular** quadrants in modern languages: pure ADT (e.g., integers in Java — values 1, 2, 3, ... with operations +, -, *) and pure object (Java class — data attributes + method operations bundled together with named state).

> *"The two other possibilities, the abstract data type with named state and the declarative object, can also be useful. But they are less used in current languages."*

## Polymorphism (Section 5.2)

*"We say an entity is polymorphic if it can take arguments of different types. ... All four kinds of data abstractions we saw before support polymorphism. But it is particularly simple for objects, which is one reason for the success of object-oriented programming."*

The **responsibility principle**: polymorphism *"is very important for organizing large programs so that the responsibilities of the program's design are concentrated in well-defined places instead of being spread out over the whole program."* Worked example: a `CompoundFigure` class containing a list of `Figure` objects — `draw` on the compound calls `draw` on each child, and *"each figure knows how to draw itself."*

## Inheritance (Section 5.3) — Van Roy's caution

> *"Inheritance can be a useful tool, but it should be used with care. ... Our recommendation is to use inheritance as little as possible. When defining a class, we recommend to define it as nonextensible if at all possible. In Java this is called a final class. Instead of inheritance, we recommend to use composition instead."*

If inheritance must be used, **follow the [[SubstitutionPrinciple|substitution principle]]** (Liskov): any procedure that works with objects of class B must also work with objects of class A inheriting from B. Inheritance should be a **conservative extension**, not a behavior-changing override.

Van Roy's cautionary tale: an unnamed multinational lost a multi-billion-dollar OO project to two specific inheritance errors — **violating the substitution principle** + **using subclasses to mask bugs**.

## In this wiki

The wiki's first proper anchor for **data abstraction as a paradigm-neutral design principle** — the framing that lets one talk about ADTs (Java integers, OCaml records) and objects (Java classes, Python classes) as **points in a single design space** rather than rival paradigms. Anchored by [[vanroy-programming-paradigms-for-dummies]]. Relates to [[OPMObject]] (Smolka's concurrent-object derivation from cells + serve procedure), [[Polymorphism]], [[SubstitutionPrinciple]], and [[Inheritance]].
