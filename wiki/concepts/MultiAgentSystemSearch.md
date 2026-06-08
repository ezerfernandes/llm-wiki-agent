---
title: "Multi-Agent System Search (MASS)"
type: concept
tags: [multi-agent, optimization, agentic-design-patterns, prompt-optimization, topology, reasoning]
sources: [agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# Multi-Agent System Search (MASS)

**MASS (Multi-Agent System Search)** is a framework that **automates and optimizes the design of multi-agent systems (MAS)**. It is presented as an optional advanced topic among the [[ReasoningTechniques|Reasoning Techniques]] in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[agentic-design-patterns-ch17-reasoning|Ch 17]]; "Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies," arXiv:2502.02533).

## The problem

A MAS's effectiveness is critically dependent on **both** (1) the **quality of the prompts** used to program individual agents and (2) the **topology** that dictates their interactions. The design space is vast and intricate, making manual design hard. MASS navigates it with a multi-stage optimization that **interleaves prompt and topology optimization**.

## The three stages

1. **Block-Level Prompt Optimization** — locally optimize prompts for individual agent types ("blocks": Aggregate, Reflect, Debate, Summarize, Tool-use) so each component performs its role well *before* integration, avoiding the compounding impact of poorly configured agents. (Example: a "Debator" agent for HotpotQA is creatively framed as an "expert fact-checker for a major publication.")
2. **Workflow Topology Optimization** — select and arrange agent interactions from a customizable design space using an **influence-weighted** method: it computes each topology's *incremental influence* (performance gain relative to a baseline agent) and steers the search toward promising combinations. (Example: for the MBPP coding task, the best topology is a hybrid of iterative self-refinement + external verification — a predictor agent that does several rounds of [[Reflection|reflection]], with its code verified by an executor agent running it against test cases.)
3. **Workflow-Level Prompt Optimization** — a final **global** optimization of the whole system's prompts as a single integrated entity, tailored for orchestration so agent interdependencies are optimized. (Example: for DROP, the final "Predictor" prompt is highly detailed — dataset summary + few-shot examples + a high-stakes role-play instruction.)

## Key design principles

The research derives three principles for effective MAS:
- **Optimize individual agents with high-quality prompts before composing them.**
- **Construct MAS by composing influential topologies** rather than exploring an unconstrained search space.
- **Model and optimize the interdependencies between agents** through a final, workflow-level joint optimization.

Experiments show MASS-optimized systems significantly outperform manually designed systems and other automated design methods across a range of tasks.

## Why it matters in agentic systems

MASS is the *meta-level* reasoning technique of the chapter: rather than improving a single agent's reasoning, it **automates how a team of reasoning agents is designed and wired together** — making [[ChainOfDebates|debate]]-, [[Reflection|reflection]]-, and tool-use-based [[multiagentsystems|multi-agent systems]] systematically optimizable instead of hand-crafted.

## Connections
- [[agentic-design-patterns-ch17-reasoning]] — source (Ch 17).
- [[ReasoningTechniques]] — the chapter's parent pattern.
- [[multiagentsystems]] / [[MultiAgentCollaboration]] — the systems MASS designs.
- [[ChainOfDebates]] / [[GraphOfDebates]] — debate is one of MASS's building-block agent types.
- [[Reflection]] — self-refinement is a block MASS composes (predictor + executor verification).
- [[ToolUse]] — tool-use is one of the agent building blocks.
- [[PromptEngineering]] — block-level and workflow-level prompt optimization.
