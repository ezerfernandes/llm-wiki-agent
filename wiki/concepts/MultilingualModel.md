---
title: "Multilingual Model"
type: concept
tags: [llm, multilingual, language-coverage]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Multilingual Model

A foundation model deliberately trained to perform well in non-English languages. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], general-purpose models work much better in English than other languages — driven by the **English bias of [[CommonCrawl|Common Crawl]]** (45.88% English, 8× the next language). On [[mmlu]], [[GPT4|GPT-4]] performs much better in English than in [[LowResourceLanguage|under-represented languages]] like Telugu.

## Why translation-as-a-fallback isn't enough

The naive workaround — translate the query into English, generate the response in English, translate back — is "not ideal" for two reasons:
1. **It still requires a model that sufficiently understands the under-represented language to translate.**
2. **Translation causes information loss.** Vietnamese has pronouns denoting speaker-relationship that all collapse to "I" / "you" in English.

## Named multilingual models

Ch 2 mentions:
- **Chinese**: ChatGLM, YAYI, Llama-Chinese — the most active non-English language for FM development.
- **French**: CroissantLLM.
- **Vietnamese**: PhoGPT.
- **Arabic**: Jais.

## Cross-language failure modes

NewsGuard (April 2023) found that **ChatGPT-3.5 produced false claims in simplified Chinese and traditional Chinese all 7/7 times** for misinformation prompts, but declined 6/7 in English. Cause unclear — possibly biases in pre-training data or alignment data.

## Tokenization-driven cost asymmetry

Beyond quality, [[Tokenization|tokenization efficiency]] varies by language. For the MASSIVE benchmark (Yennie Jun), median English token length is **7**, Hindi **32**, Burmese **72** — meaning Burmese is **10× slower and 10× more expensive** per API call for the same content.

## Connections
- [[LowResourceLanguage]] — the problem multilingual models address.
- [[CommonCrawl]] — the English-biased dataset that creates the gap.
- [[Tokenization]] — the secondary cost / latency asymmetry.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[FoundationModel]] / [[LargeLanguageModel]] — parent category.
