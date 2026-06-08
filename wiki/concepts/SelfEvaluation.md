---
title: "Self-Evaluation"
type: concept
tags: [evaluation, llm, self-critique, reflection, agentic-design-patterns]
sources: [ai-engineering-ch03-evaluation-methodology, agentic-design-patterns-ch04-reflection]
last_updated: 2026-06-07
---

# Self-Evaluation

**Self-evaluation** (sometimes [[SelfCritique|self-critique]] or **self-ask**) is the technique of using a model to evaluate its own response. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "Using a model to judge itself, self-evaluation or self-critique, sounds like cheating, especially because of self-bias. However, self-evaluation can be great for sanity checks. If a model thinks its own response is incorrect, the model might not be that reliable."

## The sanity-check use

The key insight: even with [[SelfBiasJudge|self-bias]] (a model favoring its own outputs), a model **correctly identifying its own output as wrong** is strong negative signal — the bias works *against* this finding, so observing it is informative.

## Beyond sanity checks — self-correction

Per Ch 3, *"asking a model to evaluate itself can nudge a model to revise and improve its responses (Press et al., 2022; Gou et al., 2023; Valmeekam et al., 2023)."* The pattern:

```
Prompt [from user]: What's 10+3?
First response [from AI]: 30
Self-critique [from AI]: Is this answer correct?
Final response [from AI]: No it's not. The correct answer is 13.
```

## Relationship to inference-time scaffolding

Self-evaluation is a form of [[TestTimeCompute|test-time compute]]: spend additional inference budget on a critique step in hopes of catching errors. Related to:
- **Self-consistency**: sample multiple responses and majority-vote.
- **Verifier-guided sampling**: have a separate verifier model grade candidates.
- **Self-refine** loops: generate → critique → revise iteratively.

## Limitations

- **Self-bias** ([[SelfBiasJudge]]) — a model often rates its own answer higher than warranted; the sanity-check trick only works when self-bias is *not strong enough to hide* the error.
- **Same-knowledge ceiling** — if the model doesn't know the answer, asking it to critique its own answer rarely reveals the truth. Self-critique can't bridge knowledge gaps; it can only catch reasoning slips and inconsistencies the model can detect on second pass.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[SelfCritique]] — the sibling concept (self-critique is the operationalized verb).
- [[SelfBiasJudge]] — the bias that limits self-evaluation reliability.
- [[LLMAsAJudge]] — broader paradigm.
- [[TestTimeCompute]] / [[bestofn]] / [[selfconsistency]] — sibling inference-time strategies.
- [[Verifier]] — external-grader alternative.
- [[Reflection]] — the agentic-pattern generalization (Gulli Ch 4) that wraps self-evaluation in a generate→critique→refine loop.

## Agentic Design Patterns (Gulli) perspective

In [[agentic-design-patterns-ch04-reflection|Ch 4 of *Agentic Design Patterns*]], self-evaluation is the **Evaluation/Critique** step of the [[Reflection]] loop. Gulli's recommended implementation answers the self-bias concern raised above structurally: instead of having the producing model evaluate itself, a separate **Critic** agent (an [[LLMAsAJudge|LLM-as-judge]] with a distinct evaluator persona, e.g. "a meticulous fact-checker") performs the evaluation against explicit criteria and returns **structured feedback** (e.g. ADK's `{status: "ACCURATE"|"INACCURATE", reasoning}` dict). This trades the cheap-but-biased single-model self-eval for a more robust two-role evaluation — at the cost of an extra LLM call per iteration.
