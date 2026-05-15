---
title: "Tree of Thoughts (ToT)"
type: concept
tags: [reasoning, prompting, agents]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# Tree of Thoughts (ToT)

Yao et al. (NeurIPS 2023, *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*). A prompting framework that has the LLM **generate, evaluate, and search over multiple candidate "thoughts"** in a tree, framed using search-agent terminology (nodes, expansion, value functions).

## Reframing in [[2402.01817-llm-modulo]]
Kambhampati et al. argue ToT is **not** a search/deliberation framework in any meaningful System-2 sense:

> *The "tree" in ToT is essentially a way to generate diverse priming prompts (that the authors set up in a problem specific way). In other words, despite the use of terminology of problem-solving agents (Russell & Norvig, 2010)—search tree, expansion etc., there is really no deeper connection to search-based agents.*

The apparent reasoning gains on tasks like the **24-puzzle** come from the **external arithmetic verifier**, not from the tree structure. Outside tasks where such a verifier can be easily implemented (e.g., open-ended writing), ToT has no soundness story.

In the [[LLMModuloFramework]] frame: ToT is best understood as **prompt diversification** — a Meta-Controller strategy — riding on top of a *problem-specific external verifier* that is the actual source of any guarantee.

## Connections
- [[LLMModuloFramework]] — recasts ToT as prompt-diversification + external verifier
- [[ChainOfThought]], [[Reflexion]], [[react]] — sibling iterative-prompting families
- [[SelfVerification]] — what ToT implicitly assumes but does not deliver
- [[Planning]] — domain where ToT does *not* convey planning competence
- [[2402.01817-llm-modulo]] — source critiquing ToT
