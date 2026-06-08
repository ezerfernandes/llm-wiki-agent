---
title: "Tree of Thoughts (ToT)"
type: concept
tags: [reasoning, prompting, agents]
sources: [2402.01817-llm-modulo, hands-on-llm-ch06-prompt-engineering, agentic-design-patterns-ch17-reasoning, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
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
- [[hands-on-llm-ch06-prompt-engineering]] — source presenting ToT operationally (without the critique)

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 takes the **operational rather than critical** stance on ToT — framing it as a step beyond [[chainofthought|chain-of-thought]] and [[selfconsistency|self-consistency]]:

> *"The ideas of chain-of-thought and self-consistency are meant to enable more complex reasoning. By sampling from multiple 'thoughts' and making them more thoughtful, we aim to improve the output of generative models. These techniques only scratch the surface of what is currently being done to mimic complex reasoning. An improvement to these approaches can be found in tree-of-thought, which allows for an in-depth exploration of several ideas."* — Ch 6

### Architectural (Yao et al. 2023) vs single-prompt approximation

Ch 6 documents **two operating points**:

**1. Multi-call architecture** (Yao et al. 2023). *"When faced with a problem that requires multiple reasoning steps, it often helps to break it down into pieces. At each step, the generative model is prompted to explore different solutions to the problem at hand. It then votes for the best solution and continues to the next step."* The full architecture requires *"many calls to the generative models, which slows the application significantly."*

**2. Single-prompt three-experts-roleplay approximation**. *"Instead of calling the generative model multiple times, we ask the model to mimic that behavior by emulating a conversation between multiple experts. These experts will question each other until they reach a consensus."*

The canonical Ch 6 prompt:

```
Imagine three different experts are answering this question. All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realizes they're wrong at any point then they leave. The question is '...' Make sure to discuss the results.
```

The model produces a back-and-forth discussion between three labeled experts that reaches an answer. This is the **single-prompt operating point** — *"such a conservation between 'experts' that demonstrates the creativity that comes with prompt engineering."*

### The tension with the Kambhampati critique

Ch 6's operational framing and [[2402.01817-llm-modulo|Kambhampati et al.]]'s critique together capture a **live methodological tension**: Ch 6 takes the position that ToT's *resemblance* to deliberation usefully improves outputs (regardless of whether it is *truly* reasoning); Kambhampati et al. argue the resemblance is empty without an external verifier and the apparent gains come from problem-specific verifiers like arithmetic checkers in the 24-puzzle task. Both positions are documented on [[System1And2]] as the constructive-vs-critical stance.

## Agentic Design Patterns (Gulli, Ch 17) perspective

[[agentic-design-patterns-ch17-reasoning|Chapter 17 of *Agentic Design Patterns*]] presents ToT operationally (like Ch 6, without the Kambhampati critique) as one of its core [[ReasoningTechniques|Reasoning Techniques]]: *"a reasoning technique that builds upon Chain-of-Thought… It allows large language models to explore multiple reasoning paths by branching into different intermediate steps, forming a tree structure."* Gulli stresses the **agentic affordances** the tree unlocks — *"backtracking, self-correction, and exploration of alternative solutions"* — and frames maintaining a tree of possibilities as the mechanism that lets a model evaluate various reasoning trajectories before finalizing, enhancing its ability to handle tasks requiring strategic planning and decision-making. In the chapter's arc, ToT (with [[Reflection|self-correction]]) gives agents the **crucial ability to deliberate** before execution; [[GraphOfDebates|Graph of Debates]] is presented as the multi-agent, graph-structured generalization of the same branch-and-evaluate idea.

The book's [[agentic-design-patterns-appendix-a-prompting|Appendix A]] repeats this operational framing at the prompt level: ToT *"extends the Chain of Thought method … enabling a language model to explore multiple reasoning paths concurrently, instead of following a single linear progression,"* where each node is a "thought" (a coherent intermediate language sequence) and the model branches to explore alternatives, backtrack, and recover from initial errors. Appendix A notes ToT is *"more computationally demanding and intricate to implement than the linear Chain of Thought"* but achieves superior results on tasks needing deliberate, exploratory problem-solving (its example: developing multiple distinct narrative branches for a story). This is the same constructive stance the [[2402.01817-llm-modulo|Kambhampati critique]] above contests.
