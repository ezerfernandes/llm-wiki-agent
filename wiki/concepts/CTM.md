---
title: "CTM — Concepts, Techniques, and Models of Computer Programming"
type: concept
tags: [textbook, programming-languages, paradigms, oz, pedagogy]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# CTM — Concepts, Techniques, and Models of Computer Programming

Textbook by **[[PeterVanRoy|Peter Van Roy]] & [[SeifHaridi]]**, MIT Press, **2004**. *"Familiarly known as CTM."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]]. Companion website: `ctm.info.ucl.ac.be`. French translation: *Programmation: Concepts, Techniques et Modèles* (Dunod 2007).

## Pedagogical thesis

Teach programming as a **unified discipline** covering all popular paradigms — not Java-as-OOP-only or Python-as-imperative-only, but a curriculum where the student learns **functional + declarative concurrent + object-oriented + constraint** programming within a single language and learns *which paradigm fits which problem*.

## Language: Oz

CTM uses **[[Oz]]** as its teaching vehicle because:

- *"It has many programming concepts in a well-factored design"* — adding or removing one kernel-language construct produces a different paradigm.
- *"It has a simple semantics"* — kernel calculus formalized in *Kernel Oz* (Smolka 1995).
- *"It has a high-quality implementation"* — the [[MozartProgrammingSystem|Mozart Programming System]] (first released 1999).

## Organization (Didactic Oz)

The book is organized **according to the [[CreativeExtensionPrinciple|creative extension principle]]** — concepts are introduced one at a time in the order a programmer would discover them when needing to factor away pervasive program modifications. Layered structure mirrors [[Table 1 in vanroy-programming-paradigms-for-dummies]]:

1. **Functional core** — closures as the foundation of all paradigms
2. **Deterministic [[DeclarativeConcurrency|declarative concurrency]]** — concurrency as easy as functional programming, no race conditions
3. **[[MessagePassingConcurrency|Asynchronous message passing]]** — multi-agent programming
4. **[[NamedState|Named state]]** — for modularity

## Pedagogical adoption

The CTM textbook **is the basis of programming courses at several dozen universities worldwide.** [[PeterVanRoy|Van Roy]] uses it at [[UCL]] since 2003 for his second-year programming course given to all engineering students, and his third-year concurrent programming course. The second-year course (since 2005, called **FSAB1402**) covers the three most important paradigms: **functional, object-oriented, and dataflow concurrent programming**, with many practical techniques and a formal semantics.

## Position in the wiki

The textbook anchor for [[Oz]] / [[OPM]] / [[DataflowVariable|dataflow]] / [[DeclarativeConcurrency]] / [[ConcurrentConstraintProgramming|concurrent constraint]] programming as a **teachable curriculum** — not just a research-paper line. Distinct from the wiki's existing textbook corpora ([[DiveIntoSystems]] for systems programming, [[TheEmbeddedRustBook]] for embedded Rust, [[islr-seventh-printing|ISLR]] / [[pml1-murphy|Murphy]] / [[d2l-preface|D2L]] for ML) in that **CTM is paradigm-agnostic at the level of the curriculum itself** — it teaches the *concept space*, not a particular paradigm. Reference page only — not ingested as a source.
