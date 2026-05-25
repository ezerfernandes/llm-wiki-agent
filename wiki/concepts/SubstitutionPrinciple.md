---
title: "Substitution Principle (Liskov)"
type: concept
tags: [programming-languages, oop, design, inheritance]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Substitution Principle

The **right way to use inheritance** in object-oriented programming. *"Suppose that class A inherits from class B and we have two objects, $O_A$ and $O_B$. The substitution principle states that any procedure that works with objects $O_B$ of class B must also work with objects $O_A$ of class A. In other words, inheritance should not break anything. Class A should be a conservative extension of class B."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

Originally formulated by **Barbara Liskov** (Liskov Substitution Principle, LSP); restated by Van Roy as the discipline that makes inheritance compatible with polymorphism.

## Why it matters

[[Polymorphism]] lets a procedure that takes an argument of class B accept any instance of any subclass of B. The substitution principle is the **correctness contract** that makes this safe: every operation defined on B must continue to behave correctly when invoked on an instance of A.

Without LSP, polymorphism becomes a source of bugs: a procedure that works with class B may break unpredictably when invoked on a subclass that overrode B's behavior in incompatible ways.

## Failure modes Van Roy calls out

In the cautionary multibillion-dollar OO project story:

1. **Violating the substitution principle.** *"A procedure that worked with objects of a class no longer worked with objects of a subclass. As a result, many almost-identical procedures needed to be written."* — the polymorphism advantage vanishes; every callsite has to be aware of which subclass is in use.
2. **Using subclasses to mask bugs.** *"Instead of correcting bugs, subclasses were created to mask bugs, i.e., to test for and handle those cases where the bugs occurred. As a result, the class hierarchy was very deep, complicated, slow, and filled with bugs."*

## Recommended discipline

> *"Our recommendation is to use inheritance as little as possible. When defining a class, we recommend to define it as nonextensible if at all possible. In Java this is called a final class. Instead of inheritance, we recommend to use **composition** instead."*

Composition (Figure 16, right side): instead of class A inheriting from class B, an instance of A holds a reference to an instance of B as an attribute. A delegates B-related operations to its held instance; the relationship is *has-a*, not *is-a*.

## In this wiki

OOP-discipline anchor for [[vanroy-programming-paradigms-for-dummies]]. Companion to [[Polymorphism]], [[Inheritance]], [[DataAbstraction]]. Relevant for OOP cross-walks throughout the wiki ([[DiveIntoSystems]] Appendix 1 Java-vs-C; class-based Python in ML corpora; class-based [[CompoundAISystem|compound AI systems]] via [[DSPyModules|`dspy.Module`]] subclassing — though DSPy modules use composition rather than inheritance, matching Van Roy's recommendation).
