---
title: "Agent Laboratory"
type: entity
tags: [ai-agent, multi-agent, autonomous-research, scientific-discovery, framework, open-source]
sources: [agentic-design-patterns-ch21-exploration]
last_updated: 2026-06-07
---

# Agent Laboratory

**Agent Laboratory** is an autonomous research-workflow framework developed by **[[SamuelSchmidgall|Samuel Schmidgall]]** under the MIT License. It leverages specialized LLMs to automate stages of the scientific research process, freeing human researchers to focus on conceptualization and critical analysis — augmenting human scientific endeavors rather than replacing them. It is the hands-on code example of the [[ExplorationAndDiscovery|Exploration and Discovery]] pattern in [[AntonioGulli|Antonio Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Ch 21). The framework integrates **[[AgentRxiv]]**, a decentralized repository for autonomous research agents.

## Research phases

1. **Literature Review** — specialized LLM-driven agents autonomously collect and critically analyze scholarly literature, leveraging external databases such as [[ArXiv|arXiv]] to build a knowledge base.
2. **Experimentation** — collaborative formulation of experimental designs, data preparation, execution, and analysis; agents use **Python** for code generation/execution and **[[HuggingFace|Hugging Face]]** for model access, with iterative refinement based on real-time outcomes.
3. **Report Writing** — synthesizes findings into comprehensive research reports, structured per academic conventions, integrating **LaTeX** for professional formatting and figure generation.
4. **Knowledge Sharing** — via **[[AgentRxiv]]**, enabling agents to share, access, and collaboratively advance discoveries and build on previous findings for cumulative progress.

## Multi-agent hierarchy

Mirrors an academic research team ([[MultiAgentCollaboration]]):

- **Professor Agent** — primary research director: sets the agenda, defines research questions, delegates tasks.
- **PostDoc Agent** — executes research (literature reviews, experiment design/implementation, paper generation); can write and execute code; primary producer of research artifacts.
- **Reviewer Agents** — critically evaluate outputs from the PostDoc agent, emulating academic peer review.
- **ML Engineering Agents** — generate uncomplicated data-preprocessing code in dialogic collaboration with a PhD student.
- **SW Engineer Agents** — guide the ML Engineering agents toward simple, directly relevant data-prep code.

## Tripartite agentic judgment

To emulate human evaluation, the system deploys **three distinct reviewer agents**, each with a perspective — harsh-but-fair (expects insightful experiments), impact-focused (looks for field-impactful ideas), and novelty-focused (looks for genuinely new ideas). Each produces a structured JSON review (Summary, Strengths, Weaknesses, plus 1–4 ratings for Originality/Quality/Clarity/Significance/Soundness/Presentation/Contribution, an Overall 1–10, Confidence 1–5, and a binary Accept/Reject Decision), collectively capturing the multi-faceted nature of human judgment.

## Connections

- [[SamuelSchmidgall]] — author (MIT license).
- [[AgentRxiv]] — the decentralized repository it integrates for knowledge sharing.
- [[ExplorationAndDiscovery]] — the Ch 21 pattern it exemplifies (its hands-on code example).
- [[MultiAgentCollaboration]] — its academic-team agent hierarchy.
- [[GoogleCoScientist]] — sibling scientific-discovery system in the same chapter.
- [[ArXiv]] / [[HuggingFace]] — external data/tooling for literature review and experimentation.
- [[ToolUse]] — Python, LaTeX, arXiv, and Hugging Face as research tools.
- [[AgenticDesignPatterns]] — Chapter 21; [[AntonioGulli]].
- [[agentic-design-patterns-ch21-exploration]] — source page.
