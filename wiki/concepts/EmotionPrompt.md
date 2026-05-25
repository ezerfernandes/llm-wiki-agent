---
title: "EmotionPrompt"
type: concept
tags: [prompt-engineering, llm, prompt-components, research]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# EmotionPrompt

**Appending emotional-stimulus phrases to prompts to improve LLM output quality.** Li et al. 2023, *"EmotionPrompt: Leveraging Psychology for Large Language Models Enhancement via Emotional Stimulus"* (arXiv:2307.11760). Named in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]] as an example of a **creative prompt component** that doesn't fit the standard taxonomic slots:

> *"There is all manner of components that we could add and creative components like using emotional stimuli (e.g., 'This is very important for my career.')."* — Ch 6

## The technique

Augment the prompt with **emotional appeals**:
- *"This is very important for my career."*
- *"Please give it your best effort."*
- *"You'd better be sure."*

The hypothesis is that LLMs trained on internet text have learned to associate higher effort or quality with emotionally weighted requests, mirroring human social dynamics. Empirically, the paper reports modest but consistent improvements across several benchmarks.

## Position in the prompt-engineering taxonomy

EmotionPrompt is an **add-on / cross-cutting** prompt component, not one of the seven core modular components ([[Persona|persona]] / [[InstructionPrompt|instruction]] / [[ContextPrompt|context]] / [[OutputFormat|format]] / [[AudiencePrompt|audience]] / [[TonePrompt|tone]] / data) Ch 6 enumerates. The chapter explicitly frames it as licensing **creative experimentation**: *"part of the fun in prompt engineering is that you can be as creative as possible to figure out which combination of prompt components contribute to your use case."*

## Caveats

- **Model-dependent.** Different models respond differently to emotional appeals.
- **Diminishing as models scale.** Like other prompt-engineering tricks, the marginal benefit shrinks with stronger instruction-tuning.
- **Not a substitute for specificity.** Ch 6's specificity rule is more important than any emotional decoration.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source naming EmotionPrompt.
- [[PromptEngineering]] — parent discipline.
- [[Persona]] / [[InstructionPrompt]] / [[ContextPrompt]] / [[OutputFormat]] / [[AudiencePrompt]] / [[TonePrompt]] — seven-component framework EmotionPrompt sits *outside* but can decorate.
