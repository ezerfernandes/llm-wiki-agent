---
title: "Propositional Logic"
type: concept
tags: [logic, deductive-reasoning, formal-logic, truth-functional]
sources: [logic-text-v2]
last_updated: 2026-06-07
---

# Propositional Logic

**Propositional logic** (also **sentential logic**) is the area of formal logic dealing with the logical relationships between **propositions** (= statements, things that can be true or false). [[logic-text-v2|Van Cleave]] Ch 2 introduces it as the first **formal** method of testing [[Validity|validity]], contrasted with the informal test of Ch 1.

## Atomic vs. complex propositions
An **atomic** proposition contains no truth-functional connective ("the floor has been mopped"). A **complex** proposition joins propositions with a **truth-functional connective** — one whose output truth value is fixed entirely by the truth values of its inputs.

## The four basic connectives
Lowercase `p`, `q` are placeholders for any statements:

| Connective | Symbol | Form | True when… |
|---|---|---|---|
| **Conjunction** | `⋅` | `p ⋅ q` | both conjuncts true |
| **Disjunction** (inclusive) | `v` | `p v q` | at least one disjunct true |
| **Negation** | `~` | `~p` | `p` is false |
| **Conditional** | `⊃` | `p ⊃ q` | false only when antecedent `p` true and consequent `q` false |

Their meanings are given exactly by [[TruthTable|truth tables]]. The book also covers parenthesization for complex sentences, "not both" / "neither nor", **"unless"** (= inclusive or), **material equivalence** (`≡`), and the classification of statements as **tautologies, contradictions, or contingent**.

## Two tests of validity
- **[[TruthTable|Truth-table test]]** — an [[Argument|argument]] is **valid** iff there is **no row** on which all premises are true and the conclusion is false. Decides validity *and* invalidity, but grows as $2^N$.
- **Proof** via the **8 [[RulesOfInference|valid forms of inference]]** — chains obvious steps from premises to conclusion. Proves validity only, but is far shorter for many-variable arguments.

## Its limitation
Propositional logic **cannot** validate intuitively valid arguments whose validity hinges on internal category structure (e.g. "All humans are mortal; all mortal things die; ∴ all humans die" reduces to the invalid `H, M ∴ D`). That gap motivates **[[CategoricalLogic|categorical logic]]**.

## Connections
- [[TruthTable]] — the semantics of every connective and the truth-table validity test.
- [[RulesOfInference]] — the proof method and its 8 rules.
- [[CategoricalLogic]] — supplements propositional logic where it falls short.
- [[Validity]] / [[DeductiveReasoning]] — what these methods evaluate.
- [[BooleanAlgebra]] — the algebraic/circuit-side cousin of the same two-valued logic.
- [[logic-text-v2]] — canonical source (Ch 2).
