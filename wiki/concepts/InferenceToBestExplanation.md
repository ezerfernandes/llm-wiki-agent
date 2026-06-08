---
title: "Inference to the Best Explanation"
type: concept
tags: [logic, critical-thinking, inductive-reasoning, abduction, philosophy-of-science]
sources: [logic-text-v2]
last_updated: 2026-06-07
---

# Inference to the Best Explanation

**Inference to the best explanation (IBE)** is a form of [[InductiveReasoning|inductive]] argument whose premises are *(1)* a set of **observed facts**, *(2)* a **hypothesis** that explains them, and *(3)* a **comparison** showing no competing hypothesis explains them as well — and whose conclusion is that **the hypothesis is true** ([[logic-text-v2|Van Cleave]] §3.2). It is the critical-thinking presentation of what philosophy calls **[[Abduction|abduction]]**.

```
1. Observed: your car window is broken and your iPod is gone
2. Explanation: a thief broke the window and stole the iPod accounts for both facts
3. Comparison: no other hypothesis (stray baseball + stray dog) explains them as well
4. ∴ A thief broke your window and stole your iPod
```
It is **inductive, not deductive**: the premises can all be true while the conclusion is false (maybe the absurd baseball-dog story really happened). That gap is not a defect — it is what makes the argument inductive.

## The seven explanatory virtues
What makes one explanation **better** than another? The more of these it has, the better:

1. **Explanatoriness** — it must explain *all* the observed facts.
2. **Depth** — it should not raise more questions than it answers.
3. **Power** — it should apply across a range of similar contexts, not just this one.
4. **Falsifiability** — there must be possible evidence that would show it false (the "invisible sock gnome" fails here).
5. **Modesty** — claim no more than needed; no irrelevant specifics.
6. **Simplicity** — posit fewer entities/processes; **[[OccamsRazor|Ockham's razor]]**, after [[WilliamOfOckham|William of Ockham]].
7. **Conservativeness** — give up as few well-established beliefs as possible.

## Relation to the wiki's abduction page
The wiki's [[Abduction]] page (from [[mml-book|MML]]) frames machine-learning model selection *as* abduction and makes **simplicity** quantitative via the [[MarginalLikelihood|marginal likelihood]] / [[OccamsRazor|Occam's razor]]. Van Cleave's seven virtues are the **informal, critical-thinking** counterpart of that same idea — a **framing difference** (IBE here is a species of *induction*; MML treats abduction as a *third* mode of inference), not a substantive conflict.

## Connections
- [[Abduction]] — the philosophy-of-science name for the same inference; quantified in ML.
- [[OccamsRazor]] — the "simplicity" virtue. [[WilliamOfOckham]] — its namesake.
- [[InductiveReasoning]] — IBE is one of its sub-forms.
- [[NecessaryAndSufficientConditions]] — sibling Ch 3 tool for causal explanation.
- [[logic-text-v2]] — canonical source (§3.2).
