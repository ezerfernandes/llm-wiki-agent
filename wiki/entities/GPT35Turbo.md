---
title: "gpt-3.5-turbo"
type: entity
tags: [llm, openai, chatgpt, gpt-3.5, decoder-only, api-model]
sources: [hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# gpt-3.5-turbo

**`gpt-3.5-turbo`** is [[openai|OpenAI]]'s decoder-only chat-completion model first released in March 2023 — the model that powered the public-facing [[ChatGPT]] product before [[GPT4|GPT-4]]. Cheap, fast, and the default *"good-enough"* baseline in 2023–2024 LLM stacks. Accessed via the OpenAI Chat Completions API; the `temperature=0` configuration is the standard for classification, labeling, and tool-use workflows.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses **`gpt-3.5-turbo-0125`** as the closed-source decoder-only generative classifier on the Rotten Tomatoes sentiment task — **F1 = 0.91**, the best result across all four classification regimes the chapter compares. Configuration: `temperature=0`, system prompt *"You are predicting whether a movie review is positive (1) or negative (0). Only return 1 or 0, nothing else."* Total API cost: 3 cents for the 1,066-row test sweep.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 uses **`gpt-3.5-turbo`** as the [[GenerativeTopicLabeling|generative topic-labeling]] representation model for [[BERTopic]] — feeding each topic's top keywords + 4 most-representative documents into a labeling prompt template and parsing the resulting natural-language label. Output quality is markedly higher than [[FLANT5|Flan-T5-small]]'s: *"Advancements in Aspect-Based Sentiment Analysis,"* *"Neural Machine Translation Enhancements,"* etc., where Flan-T5 produced generic labels like *"Science/Tech."* The labels generated here become the legend of the chapter's closing [[Datamapplot|Datamapplot]] visualization.

The chapter notes the standard prompt-engineering trick for label parsing: ask for the label in a strict format (*"extract a short topic label in the following format: topic: <short topic label>"*) and parse the post-colon span.

## Connections

- [[hands-on-llm-ch04-text-classification]] — generative-classifier worked example.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — topic-labeling worked example.
- [[ChatGPT]] — the product that exposed `gpt-3.5-turbo` to end users.
- [[openai]] — provider.
- [[GenerativeClassification]] / [[GenerativeTopicLabeling]] — the two prompt-engineering patterns Ch 4 and Ch 5 demonstrate.
- [[GPT4]] — the successor model.
