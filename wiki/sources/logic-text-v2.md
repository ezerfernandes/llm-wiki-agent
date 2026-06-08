---
title: "Introduction to Logic and Critical Thinking (Van Cleave, v2.0)"
type: source
tags: [logic, critical-thinking, philosophy, argumentation, fallacies, open-textbook, book]
date: 2026-06-07
source_file: raw/books/logic-text-v2.md
---

# Introduction to Logic and Critical Thinking — Version 2.0

**Matthew J. Van Cleave** (Lansing Community College), January 4, 2016. An open textbook licensed **CC BY 4.0**. Converted from `Logic text v 2.0.pdf` via markitdown.

## Summary
An introductory textbook in **logic and critical thinking** centered on the **analysis and assessment of arguments**. It is deliberately *not* a pure formal-logic text but a "critical thinking textbook" that pairs an **informal** method of reconstructing and evaluating arguments (Ch 1) with **formal** methods of testing deductive validity (Ch 2: truth tables, natural-deduction proofs, Venn diagrams), then turns to **inductive** argument and **probabilistic/statistical fallacies** (Ch 3) and a catalog of **formal and informal fallacies** (Ch 4). Its distinctive pedagogical commitment — drawn from Kahneman — is to explain *why each fallacy is seductive* rather than make fallacies sound obvious.

## Key Claims
- An **argument** (in logic's sense) is a set of statements in which the **premises** give a reason for thinking the **conclusion** is true — distinct from a "heated exchange" and distinct from an **explanation** (which tells *why* something is so, not *that* it is so).
- **Validity is about logical form, not truth**: an argument is **valid** iff it is impossible for the premises to be true while the conclusion is false. The **informal test of validity** is the imagination/counterexample method; a single counterexample (premises true, conclusion false) shows invalidity.
- **Soundness = validity + all true premises.** Soundness is "outside the purview of logic" because verifying premises requires the relevant empirical discipline, not logic.
- **Deductive** arguments aim for certainty (and valid ones are *not defeasible*); **inductive** arguments aim for high probability and are **defeasible** — adding premises can overturn a strong inductive inference.
- **Propositional logic** uses four truth-functional connectives — **conjunction (⋅), disjunction (v), negation (~), conditional (⊃)** — whose meaning is fully captured by **truth tables**. The **truth-table test of validity**: an argument is valid iff there is no row where all premises are true and the conclusion false.
- There are **8 valid forms of inference** for constructing proofs: modus ponens, modus tollens, hypothetical syllogism, simplification, conjunction, disjunctive syllogism, addition, constructive dilemma. A **proof** chains these obvious steps to justify a non-obvious inference far more efficiently than a $2^N$-row truth table.
- **Categorical logic** (the four forms A/E/I/O over categories, tested with **Venn diagrams**) captures valid inferences — like "All humans are mortal; all mortal things die; ∴ all humans die" — that **propositional logic cannot**, exposing a real limitation of propositional logic.
- **Inference to the best explanation** is a form of inductive argument graded by **seven explanatory virtues**: explanatoriness, depth, power, falsifiability, modesty, **simplicity** (Ockham's razor), conservativeness.
- Causes operate against **background conditions**; diagnosing causes uses the **necessary-condition test** and **sufficient-condition test** over a presence/absence table (a Mill-style eliminative method).
- The **conjunction fallacy** (a conjunction can never be more probable than either conjunct — Tversky & Kahneman's "Linda" problem) and the **base-rate fallacy** (ignoring prior prevalence when reading a test result) are persistent because the mind substitutes **representativeness** for probability.
- A **formal fallacy** is invalid in virtue of form (e.g., **denying the antecedent**, **affirming the consequent**); an **informal fallacy** can only be identified by understanding the content (composition, division, begging the question, false dichotomy, equivocation, slippery slope, ad hominem, straw man, tu quoque, genetic, appeal to consequences, appeal to authority).

## Key Quotes
> "An argument … is a set of statements, some of which (the premises) attempt to provide a reason for thinking that some other statement (the conclusion) is true." — §1.1

> "Validity depends only on the logical relationship between the premises and the conclusion." — §1.6

> "All sound arguments are valid arguments, but not all valid arguments are sound arguments." — §1.7

> "Inductive arguments are defeasible arguments since by adding further information or premises to the argument, we can overturn (defeat) the verdict that the conclusion is well-supported." — §1.8

> "A conjunction can never be more probable than either one of its conjuncts." — §3.6 (the conjunction fallacy)

## Connections
- [[CriticalThinking]] — the book's organizing skill: reconstruct, then evaluate, arguments.
- [[Argument]] / [[Validity]] / [[Soundness]] — the Chapter 1 core (informal evaluation).
- [[DeductiveReasoning]] / [[InductiveReasoning]] — the two argument classes the book contrasts throughout.
- [[PropositionalLogic]] / [[TruthTable]] / [[RulesOfInference]] / [[CategoricalLogic]] — Chapter 2's formal methods.
- [[InferenceToBestExplanation]] — Chapter 3's abductive core; a species of [[Abduction]].
- [[NecessaryAndSufficientConditions]] — Chapter 3's causal-reasoning tests.
- [[ConjunctionFallacy]] / [[BaseRateFallacy]] — Chapter 3's probabilistic fallacies; connect to [[Probability]] and [[BayesTheorem]].
- [[LogicalFallacy]] — Chapter 4's formal/informal fallacy catalog.
- [[OccamsRazor]] — the "simplicity" explanatory virtue, attributed to [[WilliamOfOckham]].
- [[MatthewVanCleave]] — author. [[DanielKahneman]] / [[AmosTversky]] — the psychology behind the probabilistic fallacies.

## Contradictions
- No hard contradictions with existing wiki content. The book treats **[[Abduction]] / inference to the best explanation** as a kind of *inductive* argument graded by explanatory virtues, whereas [[mml-book|MML]]'s [[Abduction]] page frames abduction as a *third* mode of inference distinct from both induction and deduction — a **framing difference** (philosophy-of-science taxonomy vs. critical-thinking taxonomy), not a conflict on substance: both make **simplicity / [[OccamsRazor|Occam's razor]]** the central virtue of a good explanation.
- The book's [[Probability]] treatment is **elementary and frequentist-flavored** (worked numeric examples, the multiplication rule for independent conjuncts) and complements — does not contradict — the wiki's Bayesian/measure-theoretic [[Probability]] page; the [[BaseRateFallacy]] is exactly an informal statement of [[BayesTheorem|Bayes' theorem]].
