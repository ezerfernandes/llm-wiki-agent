---
title: "Primacy Effect (Prompt Order)"
type: concept
tags: [prompt-engineering, llm, attention, context]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Primacy Effect (Prompt Order)

**The tendency for an LLM to focus more on information at the beginning of a prompt.** Named alongside the **recency effect** (focus on the end) in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]] as the empirical justification for placing the instruction *either* at the start *or* end of long prompts, never in the middle:

> *"Either begin or end your prompt with the instruction. Especially with long prompts, information in the middle is often forgotten. LLMs tend to focus on information either at the beginning of a prompt (primacy effect) or the end of a prompt (recency effect)."* — Ch 6

The middle-of-prompt degradation is the **[[lostinthemiddle|lost-in-the-middle]] phenomenon** (Liu et al. 2023, arXiv:2307.03172) — empirical demonstration that long-context models utilize the middle of their context poorly.

## Practical consequence

Ch 6's instruction-prompting tip #3: place the [[InstructionPrompt|instruction]] component at the **beginning** or **end** of the prompt. Middle placement risks the model focusing on surrounding data and missing the instruction.

For prompts with large data blocks (long documents, retrieved RAG chunks, code files), this implies:
- **Start-of-prompt placement** for the instruction so the model sees the task before the data.
- **Or end-of-prompt placement** so the instruction is the last thing the model sees before generation.
- **Avoid sandwich placement** (data → instruction → data).

## Position-effect interaction with [[SystemPrompt|system prompts]]

System prompts are by convention first in the wire-format chat template, which means **system-prompt content benefits from the primacy effect mechanically**. [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]] cites this as **one of the two reasons** system prompts work better than equivalent user-prompt content (the other being the **[[InstructionHierarchy|instruction-hierarchy]] post-training** of Wallace et al. 2024).

## Distinct from human-evaluator primacy

[[RecencyBias|Human evaluators]] show a **recency bias** — preferring the last-shown option in pairwise comparisons. [[FirstPositionBias|AI judges]] show **first-position bias** — preferring the first-shown option. These are evaluator-side biases distinct from the primacy/recency effects in prompt processing. The terminology overlaps but the contexts differ.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[lostinthemiddle]] — the empirical phenomenon (Liu et al. 2023).
- [[InstructionPrompt]] — the prompt component most affected by position.
- [[PromptEngineering]] — discipline.
- [[PromptStructure]] — Huyen Ch 5's structural anatomy.
- [[MiddleContextDegradation]] — sibling concept.
- [[RecencyBias]] — the human-evaluator counterpart (different scope).
- [[FirstPositionBias]] — the AI-judge counterpart (different scope).
- [[InstructionHierarchy]] — the post-training mechanism that further privileges early-prompt instructions in system prompts.
