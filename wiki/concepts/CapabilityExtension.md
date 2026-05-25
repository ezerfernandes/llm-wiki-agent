---
title: "Capability Extension"
type: concept
tags: [agents, tools]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Capability Extension

**Capability extension** is the second of [[ChipHuyen|Huyen]]'s three tool categories in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]: tools that **address the inherent limitations of AI models**. Sister categories: [[KnowledgeAugmentation]] (tools that give the agent data) and [[WriteAction|write actions]] (tools that mutate state).

## Why the category exists

Per Ch 6: *"AI models are notorious for being bad at math. If you ask a model what is 199,999 divided by 292, the model will likely fail. However, this calculation is trivial if the model has access to a calculator. Instead of trying to train the model to be good at arithmetic, it's a lot more resource-efficient to just give the model access to a tool."*

## Examples

- **Calculator** — arithmetic-deficiency fix.
- **Calendar / timezone converter / unit converter** — deterministic lookups.
- **Translator** — covers languages the base model is weak in.
- **[[CodeInterpreter|Code interpreter]]** — execute code, return results, analyze failures. Powers data-analyst and research-assistant agent shapes.
- **Image captioner / transcription / OCR** — make a text-only model **multimodal at the input** without retraining it.
- **[[DALLE|DALL-E]] / image generator** — make a text-only model multimodal at the output.
- **LaTeX compiler** — render math.
- **Browser** — render HTML.

## The "make a text-only model multimodal" pattern

Per Huyen: *"External tools can make a text-only or image-only model multimodal. ... a model that can generate only texts can leverage a text-to-image model as a tool, allowing it to generate both texts and images. ... a model that can process only text inputs can use an image captioning tool to process images and a transcription tool to process audio."*

This is the structural reason capability extension matters: it lets you build a multimodal *application* without retraining the model to be multimodal.

## Empirical evidence

[[Chameleon]] (Lu et al. 2023) demonstrates the headline result: a GPT-4 agent with 13 capability-extension + knowledge-augmentation tools beats GPT-4 alone by **+11.37%** on [[ScienceQA]] and **+17%** on [[TabMWP]].

## Security caveat

Per Huyen: *"Automated code execution comes with the risk of code injection attacks, as discussed in 'Defensive Prompt Engineering' on page 235. Proper security measurements are crucial to keep you and your users safe."*

## Connections

- [[Agent]] / [[ToolInventory]] — what capability extension is a category within.
- [[KnowledgeAugmentation]] / [[WriteAction]] — sibling tool categories.
- [[CodeInterpreter]] — the most powerful capability-extension tool.
- [[Chameleon]] — the canonical capability-extension agent benchmark.
- [[ScienceQA]] / [[TabMWP]] — Chameleon's benchmarks.
- [[ai-engineering-ch06-rag-agents]] — primary source.
