---
title: "Rules of Inference"
type: concept
tags: [logic, propositional-logic, proof, deductive-reasoning]
sources: [logic-text-v2]
last_updated: 2026-06-07
---

# Rules of Inference

In [[PropositionalLogic|propositional logic]], a **proof** is a series of statements starting with the premises and ending with the conclusion, where each new line is **derived from earlier lines by a valid form of inference**. Proofs are a second formal test of [[Validity|validity]] alongside [[TruthTable|truth tables]]: you can only prove an argument **valid** (not invalid), but a proof can be far shorter than a $2^N$-row truth table.

## The 8 valid forms of inference
[[logic-text-v2|Van Cleave]] §2.11 introduces eight basic rules. Each is itself provably valid by truth table; any argument matching the form (atomic *or* complex sub-statements) is valid. Symbols: `⊃` conditional, `⋅` conjunction, `v` disjunction, `~` negation.

| Rule | Form | Reads as |
|---|---|---|
| **Modus ponens** | `p ⊃ q`, `p` ∴ `q` | affirm the antecedent → get the consequent |
| **Modus tollens** | `p ⊃ q`, `~q` ∴ `~p` | deny the consequent → get the negated antecedent |
| **Hypothetical syllogism** | `p ⊃ q`, `q ⊃ r` ∴ `p ⊃ r` | "chain argument" — link conditionals |
| **Simplification** | `p ⋅ q` ∴ `p` | from a conjunction, take one conjunct |
| **Conjunction** | `p`, `q` ∴ `p ⋅ q` | join two asserted statements |
| **Disjunctive syllogism** | `p v q`, `~p` ∴ `q` | a disjunct fails → the other holds |
| **Addition** | `p` ∴ `p v q` | disjoin anything onto a truth |
| **Constructive dilemma** | `p v q`, `p ⊃ r`, `q ⊃ s` ∴ `r v s` | the most complex of the eight |

## Why "obvious" rules
Each rule is meant to be **transparently obvious** in isolation. The power of a proof is that it **breaks a non-obvious inference into a chain of obvious steps**, each justified by citing a rule and the line numbers it applies to:
```
1. (R v S) ⊃ (T ⊃ K)
2. ~K
3. R v S                /∴ ~T
4. T ⊃ K                Modus ponens, 1, 3
5. ~T                   Modus tollens, 2, 4
```

## Invalid look-alikes
Two formal [[LogicalFallacy|fallacies]] mimic the conditional rules and must never be confused with them: **denying the antecedent** (`p ⊃ q`, `~p` ∴ `~q`) and **affirming the consequent** (`p ⊃ q`, `q` ∴ `p`). Both are invalid in virtue of form.

## Connections
- [[PropositionalLogic]] — the system these rules operate in.
- [[Validity]] / [[TruthTable]] — proofs are the other validity test; each rule is truth-table-valid.
- [[LogicalFallacy]] — denying the antecedent / affirming the consequent are the invalid mimics.
- [[CategoricalLogic]] — the complementary formal method for category-based inferences.
- [[logic-text-v2]] — canonical source (§2.11–2.12).
