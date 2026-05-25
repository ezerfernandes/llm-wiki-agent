---
title: "Named State"
type: concept
tags: [programming-languages, semantics, state, modularity]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Named State

*"State is the ability to remember information, or more precisely, to store a sequence of values in time. ... Named state is a sequence of values in time that has a single name."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

Van Roy's **second key paradigm-classification axis** (Figure 2 / Figure 3 — paradigms are arranged by how strongly they support state). Three sub-axes:

- **unnamed vs named** (a sequence of values may be passed around by argument, or addressed by a single fixed name)
- **deterministic vs nondeterministic** (whether reads of the state can produce a unique value or a chosen one)
- **sequential vs concurrent**

Eight combinations exist; six are practically useful and shown in Figure 3:

| | Deterministic | Nondeterministic |
|---|---|---|
| **Sequential** | unnamed-det-seq (declarative) / named-det-seq (imperative) | named-nondet-seq (Dijkstra GCL) |
| **Concurrent** | unnamed-det-conc ([[DeclarativeConcurrency]]) | unnamed-nondet-conc ([[ConcurrentConstraintProgramming|concurrent logic]]) / named-nondet-conc ([[MessagePassingConcurrency|message-passing]] / [[SharedStateConcurrency|shared-state]]) |

## Why named state matters: **modularity**

Van Roy's headline argument (Section 4.4 worked example): without named state, **extending a module forces every caller to rewrite their code**. The scenario: developer P maintains module `M` with functions `F` and `G`; user U2 wants to count calls to `F` without changing the public interface.

- **Without named state**: `F` must accept `Fin` and return `Fout` — both `F`'s signature and every caller of `F` change. U1 (who never asked for the change) is also forced to rewrite their program.
- **With named state**: `M` holds a private [[Cell|cell]] counter; `F`'s public signature is unchanged; nobody but P has to touch any code.

> *"Named state is important for a system's modularity. We say that a system (function, procedure, component, etc.) is modular if updates can be done to part of the system without changing the rest of the system."*

## Blessing and curse

> *"Having named state is both a blessing and a curse. It is a blessing because it allows the component to adapt to its environment. It can grow and learn. It is a curse because a component with named state can develop erratic behavior if the content of the named state is unknown or incorrect."*

Recommended discipline: **concentrate named state in a small part of the program**; the bulk should be pure functional or [[DeclarativeConcurrency|declarative concurrent]]. *"Named state should never be invisible: there should always be some way to access it from the outside."*

## In this wiki

The **modularity argument for named state** is the canonical answer to the question "if functional programming is so good, why do we ever need mutable state?" — and it generalizes far beyond functional vs imperative debates. Anchored by [[vanroy-programming-paradigms-for-dummies]]; the OOP / class-based concurrency vocabulary throughout [[DiveIntoSystems]] / [[TheEmbeddedRustBook]] inhabits the **named** half of this axis without explicitly engaging with the trade-off.
