---
title: "Lost in the Middle"
type: concept
tags: [concept, attention, context, prompt-engineering]
sources: [2604.27707-agentic-memory-is-a-memo, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Lost in the Middle

Liu et al. 2023, *"Lost in the Middle: How Language Models Use Long Contexts"* (arXiv:2307.03172). Empirical demonstration that long-context models utilize the middle of their context poorly — outperforming at the **beginning** ([[PrimacyEffect|primacy effect]]) and **end** (recency effect) of the prompt. Used by Xu et al. (2604.27707) as capacity-bound corroboration distinct from (and weaker than) the compositional bound of Theorem 1.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 cites Liu et al. as the empirical foundation for its **third instruction-prompting tip**:

> *"Either begin or end your prompt with the instruction. Especially with long prompts, information in the middle is often forgotten. LLMs tend to focus on information either at the beginning of a prompt (primacy effect) or the end of a prompt (recency effect)."* — Ch 6

The practical consequence: place the [[InstructionPrompt|instruction]] at the **beginning** or **end** of the prompt; **avoid middle placement**. For prompts with large data blocks (long documents, RAG chunks, code), this implies a *start-of-prompt instruction* or *end-of-prompt instruction* pattern rather than a sandwich pattern.

## Connections

- [[2604.27707-agentic-memory-is-a-memo]] — uses Liu et al. as capacity-bound evidence.
- [[hands-on-llm-ch06-prompt-engineering]] — operationalizes Liu et al.'s finding as a prompt-engineering tip.
- [[PrimacyEffect]] — the beginning-of-prompt focus.
- [[MiddleContextDegradation]] — sibling concept page.
- [[ContextLength]] — the broader long-context capability the Liu et al. finding qualifies.
- [[PromptEngineering]] — discipline.
