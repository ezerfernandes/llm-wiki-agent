---
title: "ChatML"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning]
last_updated: 2026-05-22
---

## Definition
OpenAI-originated chat template using <|im_start|>role / <|im_end|> markers.

## In LLM Engineer's Handbook
OpenAI-originated [[ChatTemplate|chat template]] using `<|im_start|>role` ... `<|im_end|>` as per-turn role-delimited markers. The role (`system`, `user`, `assistant`) is plain tokenized string rather than a special token, keeping the template tokenizer-friendly across model families. Per [[leh-ch05-supervised-fine-tuning]] the most popular template choice in the open-source community for SFT.
