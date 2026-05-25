---
title: "Tone (Prompt Component)"
type: concept
tags: [prompt-engineering, prompt-component, llm, style]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Tone (Prompt Component)

**The tone of voice the LLM should use in the generated text.** One of the seven modular prompt components in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]]:

> *"Tone — The tone of voice the LLM should use in the generated text. If you are writing a formal email to your boss, you might not want to use an informal tone of voice."* — Ch 6

The tone component specifies **register and style** — formal vs informal, professional vs conversational, optimistic vs cautious, technical vs accessible. It is distinct from **[[AudiencePrompt|audience]]** (*who reads*) and **[[Persona|persona]]** (*who speaks*), though all three interact.

## Example (Ch 6's paper-summary prompt)

```python
tone = "The tone should be professional and clear.\n"
```

Common tone specifications: *"formal and academic"*, *"casual and conversational"*, *"empathetic and supportive"*, *"objective and factual"*, *"enthusiastic and persuasive"*.

## Interplay with audience and persona

If **persona** is the speaker and **audience** is the listener, **tone** is the *register* of the communication between them. The three components specify the social context of the generated text together:

| Component | Specifies |
|---|---|
| **[[Persona|Persona]]** | Who the speaker is |
| **[[AudiencePrompt|Audience]]** | Who the listener is |
| **Tone** | Register / style between them |

For automated pipelines, an explicit tone is more reliable than implicit social cues — *"a formal email to your boss"* without an explicit tone may default to ChatGPT-style chatty register depending on the model's RLHF training distribution.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[PromptEngineering]] — parent discipline.
- [[Persona]] / [[InstructionPrompt]] / [[ContextPrompt]] / [[OutputFormat]] / [[AudiencePrompt]] — sibling prompt components.
- [[Persona]] — speaker side of the speaker/listener/register triangle.
- [[AudiencePrompt]] — listener side.
