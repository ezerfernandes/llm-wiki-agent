---
title: "Chapter 9 — Learning and Adaptation (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, learning, adaptation, reinforcement-learning, self-improvement, online-learning]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 9 of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) is the **Learning and Adaptation** pattern: how agents move beyond predefined parameters and improve autonomously through experience and environmental interaction. It enumerates the learning mechanisms available to agents ([[reinforcementlearning|reinforcement]], [[SupervisedLearning|supervised]], [[UnsupervisedLearning|unsupervised]], few-shot/zero-shot with LLMs, [[OnlineInference|online]], and memory-based learning), explains the two dominant LLM-alignment optimizers — [[PPO]] and [[DPO]] — and grounds the pattern in two flagship case studies: the **Self-Improving Coding Agent (SICA)**, which modifies its own source code across benchmarked generations, and Google's **[[AlphaEvolve]]** (plus the open-source **OpenEvolve**), which pair LLMs with evolutionary algorithms to discover and optimize algorithms. (Agentic Design Patterns, PDF pp 154–166.)

## Key Claims
- **Learning and adaptation transform static agents into evolving systems.** Agents learn and adapt by changing their *thinking, actions, or knowledge* based on new experiences and data, evolving "from simply following instructions to becoming smarter over time"; adaptation is the *visible* change in behavior or knowledge that results from learning. This is the standardized solution to agents operating in dynamic, unpredictable environments where pre-programmed logic degrades on novel situations.
- **The chapter catalogs six learning mechanisms for agents.** (1) [[reinforcementlearning|Reinforcement learning]] — try actions, receive rewards/penalties, learn optimal behaviors (robots, games); (2) [[SupervisedLearning|supervised learning]] — learn input→output mappings from labeled examples (sorting emails, predicting trends); (3) [[UnsupervisedLearning|unsupervised learning]] — discover hidden structure in unlabeled data; (4) **few-shot/zero-shot with LLM-based agents** — rapidly adapt to new tasks from minimal examples or clear instructions ([[InContextLearning|in-context learning]], [[FewShotLearning]], [[ZeroShotLearning]]); (5) **online learning** — continuously update knowledge from streaming data for real-time adaptation; (6) **memory-based learning** — recall past experiences to adjust current actions ([[MemoryManagement|memory]] as a learning substrate).
- **PPO makes small, careful policy updates.** [[PPO|Proximal Policy Optimization]] trains agents in continuous-action environments; its "clipping" mechanism creates a trust region around the current policy, acting as a "safety brake" that prevents updates too different from the current strategy, preventing catastrophic performance collapse and yielding more stable learning.
- **DPO is a simpler, more direct alternative to PPO for LLM alignment.** The PPO alignment route is a two-step process — train a separate [[RewardModel|reward model]] from human-preference comparisons, then fine-tune the LLM with PPO to maximize the reward-model score (the reward model is the "judge"). This is complex and unstable; the LLM may "hack" the reward model. [[DPO|Direct Preference Optimization]] skips the reward model entirely and uses the preference data *directly* to update the LLM's policy — increasing the probability of preferred responses and decreasing that of disfavored ones — making alignment more efficient and robust.
- **SICA is a self-improving coding agent that modifies its own source code.** Developed by Maxime Robeyns, Laurence Aitchison, and Martin Szummer, SICA acts as *both* the modifier and the modified entity (contrasting with one agent training another). Its iterative cycle: review an archive of past versions + benchmark scores, select the highest-scoring version via a weighted formula over **success, time, and computational cost**, then directly alter its own codebase, re-benchmark, and record results in the archive — learning directly from past performance without traditional training paradigms.
- **SICA's self-improvement produced concrete tooling.** It evolved a "Smart Editor," then a "Diff-Enhanced Smart Editor" and "Quick Overwrite Tool," "Minimal Diff Output Optimization" and "Context-Sensitive Diff Minimization" using [[AbstractSyntaxTree|AST]] parsing, plus an "AST Symbol Locator" and an optimized "Hybrid Symbol Locator" combining quick search with AST checking.
- **SICA's architecture uses sub-agents, a structured context window, and an asynchronous overseer.** A foundational toolkit (file ops, command execution, arithmetic) plus specialized sub-agents (coding, problem-solving, reasoning) decompose complex tasks and manage context length. The LLM's context window (its short-term memory) is structured into System Prompt (goals, tool/sub-agent docs), Core Prompt (problem statement, open files, directory map), and Assistant Messages (step-by-step reasoning, tool/sub-agent call records, overseer comms). An **asynchronous overseer** — another LLM — monitors for pathological patterns like loops/stagnation and can halt execution. The project emphasizes [[Docker]] containerization for security/isolation given the agent's shell-execution ability.
- **A key open challenge is prompting LLM agents to propose genuinely novel modifications.** Eliciting novel, innovative, feasible, and engaging modifications each meta-improvement iteration — fostering *open-ended learning* and authentic creativity — remains a key research area.
- **AlphaEvolve discovers and optimizes algorithms via LLMs + evolution.** Google's [[AlphaEvolve]] combines an ensemble of [[gemini|Gemini]] models (Flash for breadth of proposals, Pro for depth/refinement), automated evaluation/scoring, and an evolutionary-algorithm framework. Deployed in Google's infrastructure, it achieved a **0.7% reduction in global compute resource usage** (data-center scheduling), suggested Verilog optimizations for upcoming [[TPU|TPUs]], delivered a **23% speedup in a core Gemini kernel** and up to **32.5% optimization of low-level GPU instructions for FlashAttention**, found a **4×4 complex-matrix-multiplication method using 48 scalar multiplications** (beating prior solutions), rediscovered SOTA solutions to 50+ open problems in 75% of cases, and improved on existing solutions in 20% of cases (incl. the kissing-number problem).
- **OpenEvolve is an open-source evolutionary coding agent.** It orchestrates a pipeline of LLM-driven code generation, evaluation, and selection to iteratively optimize code, evolving *entire code files* (not just single functions), supporting multiple languages and OpenAI-compatible APIs, multi-objective optimization, flexible prompt engineering, and distributed evaluation. Its architecture is a controller-orchestrated **evolutionary loop** over a Program Database (stores programs + metrics), a Prompt Sampler (context-rich prompts), an LLM Ensemble (code modifications), and an Evaluator Pool (tests + scores).
- **Rule of thumb:** use the Learning and Adaptation pattern when building agents that must operate in dynamic, uncertain, or evolving environments — especially for personalization, continuous performance improvement, and handling novel situations autonomously.

## Key Quotes
> "Agents learn and adapt by changing their thinking, actions, or knowledge based on new experiences and data. This allows agents to evolve from simply following instructions to becoming smarter over time." — the big picture

> "The core idea behind PPO is to make small, careful updates to the agent's policy. It avoids drastic changes that could cause performance to collapse." — PPO

> "This clipping acts like a safety brake, ensuring the agent doesn't take a huge, risky step that undoes its learning." — PPO's clipping mechanism

> "DPO skips the reward model entirely. Instead of translating human preferences into a reward score and then optimizing for that score, DPO uses the preference data directly to update the LLM's policy." — DPO

> "SICA acts as both the modifier and the modified entity, iteratively refining its code base to improve performance across various coding challenges." — the SICA case study

> "AlphaEvolve is an AI agent developed by Google designed to discover and optimize algorithms. It utilizes a combination of LLMs, specifically Gemini models (Flash and Pro), automated evaluation systems, and an evolutionary algorithm framework." — AlphaEvolve

## Connections
- [[LearningAndAdaptation]] — the chapter's named pattern (primary concept page).
- [[AgenticDesignPatterns]] — Chapter 9 of the book; [[AntonioGulli]], [[google|Google]].
- [[AgenticDesignPattern]] — the meta-concept; learning/adaptation is one path to true [[AgenticAI|agentic]] autonomy.
- [[MemoryManagement]] — Chapter 8 and a **prerequisite**: memory-based learning recalls past experiences, and stored successful strategies feed adaptation (the book cross-references this in "Memory-Based Learning" and "Knowledge Base Learning Agents").
- [[reinforcementlearning]] / [[SupervisedLearning]] / [[UnsupervisedLearning]] — three of the six learning mechanisms.
- [[InContextLearning]] / [[FewShotLearning]] / [[ZeroShotLearning]] — few-shot/zero-shot adaptation with LLM-based agents.
- [[OnlineInference]] / [[continuallearning]] — online/continuous learning from streaming data.
- [[PPO]] — the RL policy-optimization algorithm with its clipping trust region.
- [[DPO]] / [[DirectPreferenceOptimization]] — the direct, reward-model-free alignment alternative.
- [[RewardModel]] / [[rlhf]] — the PPO-based alignment route the chapter contrasts DPO against.
- [[SelfImprovingCodingAgent]] — the SICA case study (primary new concept page).
- [[AlphaEvolve]] — Google's LLM + evolutionary algorithm discovery agent.
- [[OpenEvolve]] — the open-source evolutionary coding agent.
- [[recursiveselfimprovement]] — the broader self-improvement framing SICA/AlphaEvolve exemplify.
- [[AbstractSyntaxTree]] — AST parsing underlies SICA's editor and symbol-locator tools.
- [[gemini|Gemini]] — the model ensemble (Flash + Pro) powering AlphaEvolve.
- [[TPU]] — AlphaEvolve optimized Verilog for upcoming TPUs.
- [[RAG]] — "Knowledge Base Learning Agents" use RAG (the book's Ch 14) as a dynamic store of problem/solution pairs to adapt.
- [[Docker]] — SICA runs sandboxed in a Docker container for safety.
- [[Reflection]] — Ch 4 self-critique pattern; the overseer/meta-improvement loop is the cross-agent analog.

## Contradictions
- None found. The chapter's PPO/DPO treatment is consistent with the wiki's existing [[PPO]] and [[DPO]] pages (drawn from *AI Engineering* Ch 2 and *Hands-On LLMs* Ch 12), which independently frame DPO as the simpler reward-model-free alternative to the PPO + reward-model RLHF stack. Gulli's account is higher-level (no math) but aligned. SICA's self-improvement framing is consistent with the existing [[recursiveselfimprovement]] page.
