---
title: "Learning and Adaptation"
type: concept
tags: [agents, learning, adaptation, agentic-design-patterns, reinforcement-learning, self-improvement, online-learning]
sources: [agentic-design-patterns-ch09-learning-adaptation]
last_updated: 2026-06-07
---

# Learning and Adaptation

**Learning and Adaptation** is the agentic design pattern by which an agent **improves autonomously through experience and environmental interaction** rather than remaining fixed to its initial, predefined parameters. It is Chapter 9 of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) and one of the routes to genuine [[AgenticAI|agentic]] autonomy catalogued by [[AgenticDesignPattern|the meta-pattern]]. Agents *learn* by changing their **thinking, actions, or knowledge** based on new data and experiences; *adaptation* is the **visible change in behavior or knowledge** that results. This page is the chapter's pattern — distinct from the generic machine-learning notion of "learning"; it links to the underlying ML techniques rather than redefining them.

> "Agents learn and adapt by changing their thinking, actions, or knowledge based on new experiences and data. This allows agents to evolve from simply following instructions to becoming smarter over time."

## Why it matters in agentic systems

The chapter's *What/Why*: AI agents often operate in dynamic, unpredictable environments where pre-programmed logic is insufficient and performance degrades on novel situations not anticipated at design time. Without the ability to learn from experience, agents cannot optimize their strategies or personalize their interactions — limiting effectiveness and preventing true autonomy. The standardized solution is to integrate learning and adaptation mechanisms, transforming **static agents into dynamic, evolving systems** that refine their knowledge and behaviors from new data and interactions.

**Rule of thumb:** use this pattern when building agents that must operate in dynamic, uncertain, or evolving environments — especially for personalization, continuous performance improvement, and handling novel situations autonomously.

## The six learning mechanisms

The chapter catalogs the learning approaches available to agents:

| Mechanism | What it does | Typical agent use |
|---|---|---|
| [[reinforcementlearning\|Reinforcement learning]] | Try actions, receive rewards (positive) / penalties (negative), learn optimal behaviors | Robots, game-playing |
| [[SupervisedLearning\|Supervised learning]] | Learn input→output mappings from labeled examples | Sorting emails, predicting trends |
| [[UnsupervisedLearning\|Unsupervised learning]] | Discover hidden structure/patterns in unlabeled data | Building a mental map of an environment |
| Few-shot / zero-shot with LLMs | Rapidly adapt to new tasks from minimal examples or clear instructions | [[InContextLearning\|In-context]] adaptation to new commands |
| Online learning | Continuously update knowledge from streaming data in real time | Dynamic environments, continuous data streams |
| Memory-based learning | Recall past experiences to adjust current actions | [[MemoryManagement\|Memory]]-equipped agents |

Few-shot/zero-shot adaptation leverages [[FewShotLearning]] and [[ZeroShotLearning]]; online learning is the [[OnlineInference|online]] / [[continuallearning|continual]] paradigm; memory-based learning makes [[MemoryManagement|memory]] (Ch 8) a **prerequisite** — stored successful strategies and recalled mistakes feed adaptation. "Knowledge Base Learning Agents" extend this by using [[RAG|Retrieval-Augmented Generation]] (the book's Ch 14) as a dynamic store of problem descriptions and proven solutions.

## Aligning LLM agents: PPO vs DPO

For LLM-based agents the chapter highlights two preference/policy optimizers:

- **[[PPO|Proximal Policy Optimization]]** — an RL algorithm that makes **small, careful updates** to the agent's policy. Its **clipping mechanism** defines a trust region (a "safety brake") preventing updates too far from the current strategy, avoiding catastrophic performance collapse and yielding stable learning. Used to align LLMs via a **two-step** route: train a separate [[RewardModel|reward model]] from human-preference comparisons, then fine-tune the LLM with PPO to maximize its score (the reward model is the "judge").
- **[[DPO|Direct Preference Optimization]]** — skips the reward model entirely, using preference data *directly* to update the LLM's policy (increase probability of preferred responses, decrease that of disfavored ones). This avoids the complexity and instability (e.g., reward-model "hacking") of the PPO route, making alignment more efficient and robust.

Both connect to [[rlhf|RLHF]] more broadly; see those pages for the mathematical detail the chapter omits.

## Self-improvement case studies

The chapter grounds the pattern in agents that improve their *own* code:

- **[[SelfImprovingCodingAgent|SICA (Self-Improving Coding Agent)]]** — acts as both modifier and modified, iterating over an archive of its past versions and benchmark scores to directly rewrite its own codebase. A form of [[recursiveselfimprovement|recursive self-improvement]].
- **[[AlphaEvolve]]** — Google's agent pairing a [[gemini|Gemini]] ensemble (Flash + Pro) with an evolutionary-algorithm framework to discover and optimize algorithms; deployed inside Google's infrastructure for real efficiency gains.
- **[[OpenEvolve]]** — the open-source evolutionary coding agent embodying the same LLM-driven generate/evaluate/select loop.

A standing research challenge: prompting LLM agents to propose genuinely **novel, innovative, feasible** modifications each iteration — *open-ended learning* and authentic creativity.

## Connections
- [[AgenticDesignPatterns]] — the book; Chapter 9. [[AntonioGulli]], [[google|Google]].
- [[AgenticDesignPattern]] — the meta-pattern; learning/adaptation is a defining agentic capability.
- [[MemoryManagement]] — Chapter 8 and the prerequisite for memory-based learning.
- [[reinforcementlearning]] / [[SupervisedLearning]] / [[UnsupervisedLearning]] — three of the six mechanisms.
- [[InContextLearning]] / [[FewShotLearning]] / [[ZeroShotLearning]] — LLM few-shot/zero-shot adaptation.
- [[OnlineInference]] / [[continuallearning]] — online/continuous learning.
- [[PPO]] / [[DPO]] / [[DirectPreferenceOptimization]] / [[RewardModel]] / [[rlhf]] — alignment optimizers.
- [[SelfImprovingCodingAgent]] / [[AlphaEvolve]] / [[OpenEvolve]] / [[recursiveselfimprovement]] — self-improving systems.
- [[FineTuning]] / [[ModelAdaptation]] — adaptation via weight updates (complementary to the in-context route).
- [[agentic-design-patterns-ch09-learning-adaptation]] — source page.
