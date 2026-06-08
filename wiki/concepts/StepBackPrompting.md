---
title: "Step-Back Prompting"
type: concept
tags: [reasoning, prompting, prompt-engineering, agentic-design-patterns, llm]
sources: [agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Step-Back Prompting

**Step-back prompting** is a reasoning technique that improves an LLM's answer by first asking it to consider a **general principle, concept, or higher-level abstraction** related to the task, then using the model's response to that broader question as **context** for solving the original, specific problem. Introduced as *"Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models"* (Zheng et al. 2023, arXiv:2310.06117) and surveyed in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] [[agentic-design-patterns-appendix-a-prompting|Appendix A]].

## How it works

A two-prompt sequence:
1. **Step-back (abstraction) prompt** — ask for the general factors/principles. *Example:* "What are the key factors that make a good detective story?" → the model lists red herrings, compelling motive, flawed protagonist, logical clues, satisfying resolution.
2. **Original task + step-back context** — feed that abstract answer back in. *Example:* "Using the key factors of a good detective story [insert response above], write a short plot summary for a new mystery novel set in a small town."

By activating relevant background knowledge and wider reasoning strategies before committing to specifics, the model produces more accurate and insightful answers that are **less influenced by superficial details** of the immediate query.

## Why it matters in agentic systems

Step-back prompting encourages critical thinking and the application of general knowledge, and can **mitigate biases** by grounding the response in principles rather than surface features. For an agent, deriving the governing principles first provides a stronger foundation for generating specific creative or analytical outputs, and is a lightweight, single-model alternative to heavier deliberation methods like [[TreeOfThoughts|Tree of Thoughts]].

## Relation to other techniques

- Like [[ChainOfThought|chain-of-thought]] it elicits reasoning, but the reasoning is **about the problem class** (abstraction) rather than the step-by-step solution of the specific instance.
- It is a form of [[PromptChaining|prompt chaining]] — the abstract answer becomes engineered [[ContextEngineering|context]] for the second call.
- It complements [[SelfConsistency|self-consistency]] and [[TreeOfThoughts]] in Appendix A's reasoning-techniques cluster.

## Connections
- [[agentic-design-patterns-appendix-a-prompting]] — source (Appendix A).
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — book hub and author.
- [[ReasoningTechniques]] — the Gulli Ch 17 reasoning-pattern hub.
- [[ChainOfThought]] / [[SelfConsistency]] / [[TreeOfThoughts]] — sibling reasoning techniques.
- [[PromptChaining]] / [[ContextEngineering]] — the abstract answer is engineered context for the next step.
- [[PromptEngineering]] — parent discipline.
