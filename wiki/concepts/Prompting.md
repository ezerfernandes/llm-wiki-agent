---
title: "Prompting"
type: concept
tags: [cs324, llm, prompt-engineering]
sources: [cs324-capabilities, cs324-adaptation, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

Prompting adapts a language model to a task by phrasing the task as a textual prompt, optionally including a few input-output examples, without updating the model's weights. It contrasts with weight-based adaptation methods like fine-tuning and is the mechanism behind in-context learning.

[[agentic-design-patterns-appendix-a-prompting|*Agentic Design Patterns* Appendix A]] frames prompting as **"the primary interface for interacting with language models … the process of crafting inputs to guide the model towards generating a desired output."** Well-designed prompts maximize a model's potential (accurate, relevant, creative responses); poorly designed prompts yield ambiguous or erroneous output. See [[PromptEngineering]] for the disciplined practice and the full technique survey.

## Connections
- [[InContextLearning]] — prompting with examples in context
- [[PromptEngineering]] — the engineering discipline built on prompting; Appendix A's technique catalog
- [[PromptTuning]] — learned soft-prompt variant
- [[cs324-capabilities]] — discussed in this CS324 lecture
- [[cs324-adaptation]] — discussed in this CS324 lecture
- [[agentic-design-patterns-appendix-a-prompting]] — Gulli's prompting survey
