---
title: "Self-Critique"
type: concept
tags: [evaluation, llm, prompting, reflection, agentic-design-patterns]
sources: [ai-engineering-ch03-evaluation-methodology, ai-engineering-ch05-prompt-engineering, agentic-design-patterns-ch04-reflection, agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# Self-Critique

The operationalized verb of [[SelfEvaluation|self-evaluation]] — the prompting pattern in which a model is asked to critique its own response and then revise. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]] footnote: *"This technique is sometimes referred to as self-critique or self-ask."*

## The basic loop

```
1. Generate initial response.
2. Prompt model: "Is this answer correct? Why or why not?"
3. Have model produce a revised response based on its critique.
```

## Empirical support

Per Ch 3: *"Asking a model to evaluate itself can nudge a model to revise and improve its responses"* — citing Press et al. (2022), Gou et al. (2023), and Valmeekam et al. (2023).

## Position in the wiki

Adjacent to [[SelfEvaluation]] (the broader concept) and to existing self-* pages like [[selfconsistency]] (majority-vote across many samples) and [[SelfDelusion]] (the hallucination hypothesis). Self-critique is the **single-thread, multi-turn** version of self-correction, while [[selfconsistency]] is the **parallel-sample, majority-vote** version.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[SelfEvaluation]] — the broader concept.
- [[SelfBiasJudge]] — the bias that limits self-critique reliability.
- [[selfconsistency]] — parallel-sample alternative.
- [[TestTimeCompute]] — parent inference-time-scaffolding family.
- [[LLMAsAJudge]] — when the judge is the same model as the generator.
- [[CritiqueAgent]] — Ch 16's dedicated critic agent applying this loop to a cost-aware [[ModelRouter|router]]'s output ([[ResourceAwareOptimization]]).

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 names self-critique alongside [[chainofthought|CoT]] as one of two *"give the model time to think"* prompt-engineering techniques:

> "Self-critique means asking the model to check its own outputs. This is also known as self-eval, as discussed in Chapter 3. Similar to CoT, self-critique nudges the model to think critically about a problem."

**Trade-off.** Both CoT and self-critique increase user-perceived latency: *"A model might perform multiple intermediate steps before the user can see the first output token."* If the steps are model-chosen (rather than developer-fixed), the chain length and cost can grow unboundedly.

**Relation to CoT.** Ch 5 distinguishes the two by *where the reasoning happens*: CoT puts the reasoning inside one model call (single API call, more tokens); self-critique spreads it across multiple calls (more API calls, fewer tokens each). They can be combined.

## Agentic Design Patterns (Gulli) perspective

[[agentic-design-patterns-ch04-reflection|Ch 4 of *Agentic Design Patterns*]] generalizes self-critique into the agentic **[[Reflection]]** pattern: an agent evaluates its own output and iteratively refines it through an *Execution → Evaluation/Critique → Reflection/Refinement → Iteration* loop. Crucially, Gulli argues that single-agent self-critique is the *weaker* variant — separating the work into a distinct **Producer** and **Critic** (the [[Reflection|Generator-Critic / Producer-Reviewer]] model) "often yields more robust and unbiased results" because it "prevents the 'cognitive bias' of an agent reviewing its own work." This is the book's framing of the [[SelfBiasJudge|self-bias]] limitation already noted above: rather than relying on a model catching its own errors, give the Critic a separate persona and a fresh perspective dedicated to finding flaws.

[[agentic-design-patterns-ch17-reasoning|Chapter 17 (Reasoning Techniques)]] reuses the same loop under the name **self-correction / self-refinement**, listing it among the core [[ReasoningTechniques|reasoning techniques]] as the internal critique step *"particularly within Chain-of-Thought prompting"* — the single-thread draft→review→revise loop is the in-line companion to the multi-step deliberation of [[TreeOfThoughts|ToT]] and the acting loop of [[react|ReAct]].
