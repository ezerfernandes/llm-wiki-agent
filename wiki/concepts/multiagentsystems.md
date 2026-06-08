---
title: "Multi-Agent Systems"
type: concept
tags: [ml-method, system-architecture]
sources: [2512.04388-conductor, 2605.03310-coordination-architectural-layer, 2605.02396-heavyskill, agentic-design-patterns-00-frontmatter, agentic-design-patterns-ch07-multi-agent, agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# Multi-Agent Systems

Systems where multiple LLM agents collaborate or compete. Two competing positions in the corpus: (1) the Conductor learns coordination end-to-end via RL ([[2512.04388-conductor]]); (2) Nechepurenko & Shuvalov argue coordination should be a separately-specified architectural layer enabling pre-deployment failure-mode prediction ([[2605.03310-coordination-architectural-layer]]). HEAVYSKILL is a third axis: collapse multi-agent orchestration into one model's inner skill.

## Agentic Design Patterns (Gulli) perspective

[[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[AntonioGulli|Gulli]]) places multi-agent systems at **Level 3** of the [[AgentComplexitySpectrum|agent-complexity spectrum]] — "a significant paradigm shift … away from the pursuit of a single, all-powerful super-agent and towards the rise of sophisticated, collaborative multi-agent systems." The model mirrors a human organization: a "Project Manager" agent orchestrates specialists (Market Research, Product Design, Marketing), with success hinging on seamless [[AgentCommunication|communication]] and information sharing. The book treats this as the [[MultiAgentCollaboration|Multi-Agent Collaboration]] pattern (Ch 7) and notes present-day limits — effectiveness is constrained by the reasoning limits of underlying LLMs, and genuine inter-agent learning is still early-stage. The most speculative form is the future "goal-driven, metamorphic multi-agent system" that rewrites its own topology (creating, duplicating, or removing agents) to best achieve a declared goal.

[[agentic-design-patterns-ch07-multi-agent|Chapter 7]] details the pattern itself. It specifies the three constituent elements of any multi-agent system — **agent roles & responsibilities**, **communication channels**, and a **task flow / interaction protocol** — and enumerates a spectrum of interrelationship/communication **topologies**: *single agent → network (decentralized peer-to-peer) → supervisor (central hub) → supervisor-as-a-tool → hierarchical (multi-layer) → custom*. The *behavioral* forms of collaboration are sequential handoffs, parallel processing, debate & consensus, hierarchical (orchestrator-worker) delegation, expert teams, and critic-reviewer. See [[MultiAgentCollaboration]] for the full pattern treatment and its [[crewai|CrewAI]] / [[GoogleADK|Google ADK]] code realizations.

[[agentic-design-patterns-ch17-reasoning|Chapter 17 (Reasoning Techniques)]] returns to multi-agent systems as a **reasoning** mechanism: [[ChainOfDebates|Chain of Debates (CoD)]] and [[GraphOfDebates|Graph of Debates (GoD)]] frame multiple models arguing/debating as a way to *reason together* — reducing individual bias and producing more robust answers than a solitary agent. The chapter also introduces [[MultiAgentSystemSearch|MASS]], a framework that **automates the design** of multi-agent systems by jointly optimizing each agent's prompt and the interaction topology (Aggregate / Reflect / Debate / Summarize / Tool-use blocks).

## Connections
- [[coordinationlayer|CoordinationLayer]]
- [[agenticharness|AgenticHarness]]
- [[mast|MAST]]
- [[MultiAgentCollaboration]] / [[InterAgentCommunication]] — Gulli's Level-3 patterns.
- [[AgentComplexitySpectrum]] / [[AgenticDesignPatterns]]
- [[ChainOfDebates]] / [[GraphOfDebates]] / [[MultiAgentSystemSearch]] — Ch 17's multi-agent *reasoning* frameworks.
- [[ReasoningTechniques]] — the Ch 17 pattern that casts multi-agent debate as collaborative reasoning.
