---
title: "Creative Extension Principle"
type: concept
tags: [programming-languages, design, methodology]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Creative Extension Principle

A guide for organizing the design space of [[ProgrammingParadigm|programming paradigms]] — and for **discovering new concepts** when they are needed. First defined by **Matthias Felleisen** (1990, *"On the Expressive Power of Programming Languages"*, ESOP 1990) and independently rediscovered in [[CTM]] (Van Roy & Haridi 2004).

## Statement

> *"In a given paradigm, it can happen that programs become complicated for technical reasons that have no direct relationship to the specific problem that is being solved. This is a sign that there is a new concept waiting to be discovered."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

When the *need for pervasive (nonlocal) program modifications* manifests itself, take it as a signal that a new language concept should be added. Adding the concept eliminates the pervasive modifications and recovers the program's simplicity. *"The only complexity in the program is that needed to solve the problem. No additional complexity is needed to overcome technical inadequacies of the language."*

## Three canonical examples

Starting from a simple sequential functional paradigm:

| Need | Pervasive modification required without the concept | Concept to add |
|---|---|---|
| **Model several independent activities** | Implement several execution stacks, a scheduler, and a preemption mechanism — manually | [[Concurrency|concurrency]] |
| **Model updatable memory** | Add two extra arguments (input + output) to all function calls relative to the entity; the memory "travels" throughout the program; not modular | [[NamedState|named state]] |
| **Model error detection / correction** | Add error codes to all function outputs; add conditional tests on every call; the error-handling weaves through everything | exceptions (Figure 5) |

The exception example is particularly clear (Figure 5 of [[vanroy-programming-paradigms-for-dummies]]): without `try`/`catch`, **every procedure on the call path from the error site to the handler** must be modified to propagate the error code. With exceptions, **only the call site and the handler** are touched; intermediate procedures stay unchanged.

## Common theme

> *"The common theme in these three scenarios (and many others!) is that we need to do pervasive (nonlocal) modifications of the program in order to handle a new concept. If the need for pervasive modifications manifests itself, we can take this as a sign that there is a new concept waiting to be discovered. By adding this concept to the language we no longer need these pervasive modifications and we recover the simplicity of the program."*

Both Figure 2 ([[ProgrammingParadigm|paradigm taxonomy]]) and [[CTM]] (the textbook) are organized **according to the creative extension principle** — concepts are introduced in the order they would be discovered by a programmer noticing pervasive modifications they want to factor away.

## In this wiki

The wiki's first programming-language-design **principle** anchor. Connects [[ProgrammingParadigm]] / [[KernelLanguage]] / [[CTM]] / [[vanroy-programming-paradigms-for-dummies]]. The principle is a useful lens for evaluating any new language feature proposal: *what pervasive modifications would users have to do without it?*
