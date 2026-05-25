---
title: "Low-Resource Language"
type: concept
tags: [nlp, multilingual, dataset]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Low-Resource Language

A language with **limited availability as training data** — typically a language not in the top 12 most common in [[CommonCrawl|Common Crawl]] (which collectively account for ≈85% of the corpus, dominated by English at 45.88%).

## The under-representation ratio

[[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]] introduces a metric: the **world-population-to-Common-Crawl ratio**. A ratio of 1 means representation matches speaker count. The higher the ratio, the more under-represented the language. Examples (from Lai et al. 2023):

| Language | Speakers (M) | % world | % CC | Ratio |
|---|---|---|---|---|
| Punjabi | 113 | 1.41% | 0.0061% | **231×** |
| Swahili | 71 | 0.89% | 0.0077% | 115× |
| Urdu | 231 | 2.89% | 0.0274% | 105× |
| Kannada | 64 | 0.80% | 0.0122% | 65× |
| Telugu | 95 | 1.19% | 0.0183% | 65× |
| Gujarati | 62 | 0.78% | 0.0126% | 62× |
| Marathi | 99 | 1.24% | 0.0213% | 58× |
| Bengali | 272 | 3.40% | 0.0930% | 36× |
| English (ref) | 1452 | 18.15% | 45.88% | 0.40× |

## Three structural problems

Per Ch 2, low-resource languages suffer from three compounding issues:

1. **Under-representation in pre-training data.** The three worst MMLU-performing languages for [[GPT4|GPT-4]] (Telugu, Marathi, Punjabi) are also among the most under-represented.
2. **Structural difference from English.** Some languages encode information English lacks (Vietnamese speaker-relationship pronouns) — this is lost in English-via-translation pipelines.
3. **Tokenization inefficiency.** Median tokens for the same MASSIVE-benchmark text: English **7**, Hindi **32**, Burmese **72**. Result: **≈10× latency and ≈10× API cost** for Burmese vs English.

## Worked example: GPT-4 math performance

Yennie Jun's six-Project-Euler-problem study found GPT-4 solved English problems **>3× more often** than Armenian or Farsi, and **failed all 6** for Burmese and Amharic.

## Mitigations

- [[MultilingualModel|Multilingual models]] trained with deliberate non-English focus (ChatGLM, CroissantLLM, PhoGPT, Jais).
- Avoid translate-to-English-and-back as a default workaround — it still requires understanding the source language and loses information.

## Connections
- [[MultilingualModel]] — the model class designed to address this.
- [[CommonCrawl]] — the dataset whose English bias creates the problem.
- [[Tokenization]] — the inefficient tokenization that compounds the cost.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[mmlu]] — the cross-language benchmark.
