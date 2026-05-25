---
title: "Outlines"
type: entity
tags: [tool, library, llm, structured-output, open-source]
sources: [leh-ch05-supervised-fine-tuning, leh-ch07-evaluating-llms, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

## What it is
Outlines is an open-source Python library for **structured generation** with LLMs — generating outputs that strictly conform to a schema (JSON, regex, context-free grammar, Pydantic model) by constraining the model's token-by-token sampling.

## In LLM Engineer's Handbook
Ch. 5 ([[leh-ch05-supervised-fine-tuning]]) lists Outlines as one of the tools for structured JSON-mode generation during synthetic instruction-dataset construction. Ch. 7 ([[leh-ch07-evaluating-llms]]) recommends Outlines (along with OpenAI's `response_format={"type": "json_object"}`) for producing reliable structured judge outputs in LLM-as-a-judge evaluations.

## Connections
- [[Pydantic]] — schemas Outlines constrains output to.
- [[openai]] — JSON mode is the OpenAI-side equivalent.
- [[LLMAsAJudge]] — typical Outlines use case.
- [[InstructionDataset]] — domain.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

[[ChipHuyen|Huyen]] names Outlines alongside [[Guidance]] and [[Instructor]] as the canonical examples of **partial-workflow [[PromptEngineeringTools|prompt-engineering tools]]** — specifically the *"guide models toward structured outputs"* subcategory. Distinct from the full-workflow optimizers ([[DSPy]], [[OpenPrompt]], [[PromptBreeder]], [[TextGrad]]).

The Ch 5 framing slots Outlines as one of the *low-risk* tool choices — structured-output libraries have well-defined success criteria (the output matches the schema or it doesn't) and don't suffer from the hidden-cost-multiplication problem Ch 5 warns about for full-workflow optimizers.

## In *Hands-On LLMs* Ch 6

[[hands-on-llm-ch06-prompt-engineering|Ch 6]] does *not* name Outlines directly — Ch 6's named set for [[GrammarConstrainedDecoding|grammar-constrained decoding]] is **[[Guidance]] / [[Guardrails]] / [[LMQL]]**. The two books' name sets overlap on Guidance but diverge on the other libraries; together they cover the broader landscape captured in [[PromptEngineeringTools]]. Outlines is the Python library most closely associated with this technique outside the [[llamacpp|llama.cpp]] ecosystem — Ch 6 demonstrates [[ConstrainedSampling|constrained sampling]] through `llama-cpp-python`'s built-in JSON grammar (`response_format={"type": "json_object"}`) rather than Outlines, but the techniques are equivalent.
