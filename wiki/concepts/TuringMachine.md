---
title: "Turing Machine"
type: concept
tags: [theoretical-cs, computability, foundational, history]
sources: [dis-5-1-history]
last_updated: 2026-05-17
---

# Turing Machine

An **abstract model of computation** introduced by [[AlanTuring]] in his 1937 paper *On Computable Numbers, with an Application to the Entscheidungsproblem*. Defines a mechanical device with:

- An **infinite tape** divided into cells holding symbols from a finite alphabet
- A **read/write head** that scans one cell at a time
- A **finite set of internal states**
- A **transition function** that, given the current state and symbol under the head, specifies the next state, the symbol to write, and a direction to move

A function is **Turing-computable** if some Turing machine computes it. The **[[ChurchTuringThesis|Church-Turing thesis]]** posits that every effectively calculable function is Turing-computable — making the Turing machine the canonical definition of *algorithm* and *what a computer can do in principle*.

## Relation to physical computers

The Turing machine is the **theoretical pole** of computing — paired with the **engineering pole** of the [[VonNeumannArchitecture|von Neumann architecture]] (the practical [[StoredProgram|stored-program]] machine). Per [[dis-5-1-history|*Dive into Systems* Ch 5.1]], real computers are *finite-tape, bounded-memory* approximations of the Turing-machine model — but every general-purpose modern [[CPU]] is **Turing-complete**, meaning it can simulate any Turing machine (subject to finite memory).

Originally called the *"Logical Computing Machine"* by Turing himself; the name *Turing machine* was coined later by his contemporaries.
