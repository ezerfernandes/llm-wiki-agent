---
title: "Stopping Condition"
type: concept
tags: [sampling, inference, llm]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Stopping Condition

The criterion that **terminates an autoregressive language model's token generation**. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "An autoregressive language model generates sequences of tokens by generating one token after another. A long output sequence takes more time, costs more compute (money), and can sometimes annoy users. We might want to set a condition for the model to stop the sequence."

## Three stopping methods

1. **Fixed token count.** Ask the model to stop after N tokens. **Downside**: outputs are often **cut off mid-sentence**.
2. **Stop tokens / stop words.** Stop on encountering specified tokens — most commonly the **end-of-sequence (EOS)** token.
3. **Custom regex / structural triggers.** E.g., stop when a valid JSON document is reached.

## Latency / cost / quality trade-off

Per Ch 2: stopping conditions are **helpful to keep latency and costs down** (model APIs typically charge by output token count). But stopping too early causes the opposite quality problem:

> "If you ask the model to generate JSON, early stopping can cause the output JSON to be missing things like closing brackets, making the generated JSON hard to parse." — Ch 2

This is one of several pressures motivating [[StructuredOutputs|structured-output techniques]].

## Connections
- [[StructuredOutputs]] — the broader pattern stopping conditions feed into.
- [[bestofn]] — test-time compute requires generating *multiple* outputs, each with its own stopping condition.
- [[Decode]] — the inference phase where stopping happens.
- [[TPOT]] — the per-token-output latency stopping conditions modulate.
- [[ai-engineering-ch02-foundation-models]] — primary source.
