---
title: "Vibe Coding"
type: concept
tags: [agents, coding-agents, software-development, llm, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Vibe Coding

**Vibe coding** is a development paradigm in which a developer provides a high-level goal, a desired "vibe", or a general direction in natural language, and an AI coding assistant generates code to match — moving away from precise, step-by-step specifications toward intuitive, conversational, iterative collaboration. Described in [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix B]] (and revisited as a "starting point" in Appendix G) (Gulli).

## Characteristics (Appendix B)
- **Conversational Prompts** — e.g. *"Create a simple, modern-looking landing page"* or *"Refactor this function to be more Pythonic"*; the AI interprets the "vibe" and generates corresponding code.
- **Iterative Refinement** — initial output is a starting point; the developer gives natural-language feedback (*"can you make the buttons blue?"*, *"add error handling"*) until the code meets expectations.
- **Creative Partnership** — the AI suggests ideas/solutions the developer hadn't considered, accelerating development.
- **Focus on "What" not "How"** — the developer owns the desired outcome; implementation details are left to the AI, enabling rapid prototyping without boilerplate.
- **Optional Memory Banks** — developers can save key information, preferences, coding style, or project requirements to the AI's memory so future generations stay consistent with the established "vibe" without repeating instructions.

## Relationship to coding agents (Appendix G)
The book positions vibe coding as **excellent for ideation and the "blank page" problem** — rapid drafts, prototypes, exploring unfamiliar APIs or novel architectural patterns — but warns that building **robust, scalable, maintainable** software requires shifting from pure generation to a structured collaborative partnership with specialized [[CodingAgent|coding agents]]. Vibe coding is the entry point; the [[CodingAgent]] team pattern is the production discipline that follows.

## Why it matters
Popularized by frontier models ([[GPT|GPT-4]], [[anthropic|Claude]], [[gemini|Gemini]]) integrated into IDEs, vibe coding shifts software engineering toward creativity and high-level thinking over rote syntax/API memorization — but it is a *catalyst*, not a substitute for architectural discipline.

## Connections
- [[agentic-design-patterns-appendices-bg]] — source.
- [[CodingAgent]] — the structured production paradigm vibe coding leads into.
- [[MemoryManagement]] — "memory banks" are a vibe-coding memory mechanism.
- [[claudecode|Claude Code]] / [[GeminiCLI|Gemini CLI]] / [[Aider]] — tools that enable vibe-coding workflows.
