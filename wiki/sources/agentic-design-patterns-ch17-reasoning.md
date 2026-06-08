---
title: "Chapter 17 — Reasoning Techniques (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, reasoning, chain-of-thought, tree-of-thought, react, self-correction, multi-agent-debate, test-time-compute, deep-research]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 17 of [[AntonioGulli|Antonio Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] is the **[[ReasoningTechniques|Reasoning Techniques]]** pattern (the 17th of 21) — advanced methodologies that make an agent's internal "thought" process explicit so it can decompose multi-step problems, explore solution paths, and reach more robust conclusions. Its organizing principle is the **allocation of more computation at inference time**: granting the agent extra processing time/steps for iterative refinement, multi-path exploration, or external tool use. The chapter surveys [[ChainOfThought|Chain-of-Thought]], [[TreeOfThoughts|Tree-of-Thought]], [[Reflection|Self-Correction]], [[ProgramAidedLanguageModel|Program-Aided Language Models]], [[rlvr|Reinforcement Learning with Verifiable Rewards]], [[react|ReAct]], [[ChainOfDebates|Chain of Debates]], [[GraphOfDebates|Graph of Debates]], the [[MultiAgentSystemSearch|MASS]] multi-agent-search framework, [[DeepResearch|Deep Research]], and the [[ScalingInferenceLaw|Scaling Inference Law]] (Agentic Design Patterns, PDF pp 262–285).

## Key Claims
- The core principle of advanced reasoning is **increased compute at inference** — iterative refinement, multiple solution paths, and tool use during generation often significantly improve accuracy, coherence and robustness for complex problems.
- **Chain-of-Thought (CoT)** elicits step-by-step intermediate reasoning (few-shot examples or "think step by step"); it decomposes hard single-step problems into manageable sub-problems and increases transparency/auditability — "a cornerstone technique for enabling advanced reasoning."
- **Tree-of-Thought (ToT)** builds on CoT by branching into a tree of intermediate steps, enabling backtracking, self-correction, and exploration of alternative solutions before finalizing an answer.
- **Self-correction / self-refinement** is an internal critique loop (draft → review against requirements → revise) — a quality-control measure built directly into generation; detailed in Chapter 4 (Reflection).
- **Program-Aided Language Models (PALMs)** integrate LLMs with symbolic reasoning: the model generates and executes code (e.g. Python) to offload precise computation to a deterministic environment, then converts results back to natural language. Example uses Google ADK's `BuiltInCodeExecutor`.
- **Reinforcement Learning with Verifiable Rewards (RLVR)** is the training strategy behind a new class of "reasoning models" that dedicate variable "thinking" time (chains of thousands of tokens), enabling self-correction and backtracking learned via trial-and-error on problems with known correct answers (math/code).
- **ReAct** (Reasoning and Acting) interleaves CoT-style reasoning with tool/environment actions in a Thought → Action → Observation loop, letting agents dynamically adapt plans and correct errors.
- **Chain of Debates (CoD)** is a Microsoft framework where multiple diverse models collaborate and argue like an "AI council," critiquing each other to enhance accuracy, reduce bias, and create a transparent reasoning record — a shift from a solitary agent to a collaborative team.
- **Graph of Debates (GoD)** reimagines debate as a dynamic non-linear graph where argument nodes are connected by 'supports'/'refutes' edges; a conclusion is the most robust, well-supported cluster of arguments (grounded in ground truth, search grounding, or multi-model consensus).
- **MASS (Multi-Agent System Search)** automates multi-agent-system design via a three-stage optimization: block-level prompt optimization, influence-weighted workflow-topology optimization, then workflow-level (global) prompt optimization. Key principles: optimize agents with good prompts before composing; compose influential topologies; jointly optimize interdependencies.
- **Deep Research** tools (Perplexity AI, Google Gemini, OpenAI/ChatGPT) act as autonomous research assistants given a "time budget," running Initial Exploration → Reasoning & Refinement → Follow-up Inquiry → Final Synthesis.
- The **Scaling Inference Law** governs the relationship between LLM performance and compute allocated *at inference* (distinct from training scaling laws): a smaller model granted a larger "thinking budget" can surpass a larger model with a simpler generation process — balancing model size, response latency, and operational cost, moving beyond "bigger is better."

## Key Quotes
> "A core principle among these advanced methods is the allocation of increased computational resources during inference. This means granting the agent, or the underlying LLM, more processing time or steps to process a query and generate a response." — chapter intro, on test-time compute

> "CoD (Chain of Debates) is a formal AI framework proposed by Microsoft where multiple, diverse models collaborate and argue to solve a problem, moving beyond a single AI's 'chain of thought.' This system operates like an AI council meeting." — on multi-agent debate

> "The law posits that a smaller model, when granted a more substantial 'thinking budget' during inference, can occasionally surpass the performance of a much larger model that relies on a simpler, less computationally intensive generation process." — Scaling Inference Law

## Connections
- [[AgenticDesignPatterns]] — the book hub; Reasoning Techniques is pattern 17 of 21.
- [[ReasoningTechniques]] — the chapter's named pattern (concept hub created from this source).
- [[AntonioGulli]] — author.
- [[ChainOfThought]] / [[TreeOfThoughts]] — the two foundational prompting-reasoning techniques the chapter opens with.
- [[react|ReAct]] — the reasoning-and-acting paradigm that makes agents act, not just reason (Ch 17 reframes its own Ch on planning/tool-use here).
- [[Reflection]] / [[SelfCritique]] — the self-correction loop the chapter cross-references to Ch 4.
- [[ProgramAidedLanguageModel]] — PALMs / code-execution offloading (Google ADK `BuiltInCodeExecutor` example).
- [[rlvr|RLVR]] — the training method behind reasoning models with variable thinking time.
- [[ChainOfDebates]] / [[GraphOfDebates]] — multi-agent debate frameworks (Microsoft CoD; GoD graph variant).
- [[MultiAgentSystemSearch]] — the MASS optimization framework (arXiv:2502.02533).
- [[DeepResearch]] — the agentic research exemplar; Ch 17 details the agentic time-budget loop and the Google `gemini-fullstack-langgraph-quickstart` DeepSearch code.
- [[ScalingInferenceLaw]] — the chapter's core performance principle.
- [[TestTimeCompute]] / [[testtimescaling]] — the inference-compute family the chapter's central principle instantiates.
- [[multiagentsystems]] / [[MultiAgentCollaboration]] — CoD/GoD/MASS are multi-agent reasoning.
- [[Planning]] — strategic-planning use case; ReAct/Deep Research compose reasoning with planning.
- [[GoogleADK]] / [[langgraph|LangGraph]] / [[gemini|Gemini]] / [[google|Google]] / [[openai|OpenAI]] / [[microsoft|Microsoft]] / [[Perplexity]] — frameworks/products in the chapter's examples.
- [[selfconsistency|Self-Consistency]] — named as a multi-candidate-generation strategy under the Scaling Inference Law.

## Contradictions
- vs [[TreeOfThoughts]] / [[Planning]] on reasoning soundness: Gulli takes the **constructive/optimistic** stance (ToT/CoT/self-correction genuinely improve robustness), in *framing tension* with the [[2402.01817-llm-modulo|Kambhampati LLM-Modulo]] critique already on those pages (apparent gains come from external verifiers, not the reasoning structure itself). Recorded as a framing difference, consistent with how Ch 4/6 were ingested — not a strict contradiction.
