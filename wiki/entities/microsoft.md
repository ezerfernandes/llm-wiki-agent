---
title: "Microsoft"
type: entity
tags: [entity]
sources: [2604.28181-synthetic-computers-at-scale, 2605.02572-long-horizon-llm-training, 2605.03808-agentic-imodels, ai-engineering-ch01-intro, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Microsoft

Parent of [[microsoftresearch|Microsoft Research]]. In this corpus: authors Synthetic Computers at Scale (Ge / Peng / Cheng / Gao), and via MSR co-authors the long-horizon training study and AGENTIC-IMODELS.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] in *AI Engineering* Ch 1 cites Microsoft as:

- **Originator of the [[CrawlWalkRun|Crawl-Walk-Run framework]]** for gradually increasing AI automation in products — a deployment-ladder framework that pairs with [[humanintheloop|HITL]] policy mechanisms.
- **Foundation-model builder** — listed among big corporations with the resources to develop FMs from scratch (alongside [[google|Google]], [[meta|Meta]], Baidu, Tencent).
- **[[GitHubCopilot|GitHub Copilot]] parent company** (via GitHub subsidiary) — Copilot is one of Ch 1's anchor examples of an early FM production success ($100M ARR in 2 years).
- **Microsoft 365 + VSCode plug-in ecosystem** — example of integrated-AI-via-API surfaces (alongside Shopify) that Ch 1 names in the [[AIInterface|AI interface]] discussion.
- **OpenAI partner** — implicitly throughout, given OpenAI's prominence in the chapter.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 anchors Microsoft as the **provider of the book's recurring worked model** — [[Phi3Mini|Phi-3-mini]] (`microsoft/Phi-3-mini-4k-instruct`) — 3.8B parameters, MIT-licensed, runs in <8 GB VRAM (and <6 GB with quantization). The Phi family is cited as one of four representative [[OpenSourceLLM|open-weights LLM]] families in Ch 1:

> "Cohere's Command R, the Mistral models, Microsoft's Phi, and Meta's Llama models are all examples of open models." — Ch 1

The choice of Phi-3-mini is structural to the book's pedagogy: it's the smallest credible 2024 LLM that fits comfortably on a free Google Colab T4, supporting the *"this book is for the GPU-poor"* commitment.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 adds **[[deberta|DeBERTa v3]]** (`microsoft/deberta-v3-xsmall`, paired with `microsoft/deberta-base` tokenizer) as a second Microsoft model — used in the chapter's contextualized-token-embedding worked example. Ch 2 cites DeBERTa v3 as *"at the time of writing one of the best-performing language models for token embeddings while being small and highly efficient."* Plus the recurring [[Phi3Mini|Phi-3]] worked example from Ch 1.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 cites Microsoft in three roles:

1. **[[AGIEval]]** (2023) — Microsoft's human-exam-derived [[MultipleChoiceQuestion|MCQ]] benchmark. Excluded open-ended tasks deliberately *"to avoid inconsistent assessment."*
2. **Azure API for GPT-4** — *"GPT-4 is available through both OpenAI and Azure APIs. There might be slight differences in the performance of the same model provided through different APIs."* Microsoft is the primary cloud-side commercial-model API provider.
3. **MS MARCO** (Microsoft Machine Reading Comprehension) — information-retrieval benchmark that [[HELMLite]] **excluded** *"because it's expensive to run."* The fact that even Stanford couldn't afford MS MARCO is a data point on the cost economics of public benchmarks.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Microsoft appears in Ch 5 in **three roles**:

1. **The 2023 few-shot-vs-zero-shot analysis** — Ch 5's headline empirical claim that few-shot's advantage shrinks with stronger models comes from a Microsoft 2023 study: *"For GPT-3, few-shot learning showed significant improvement compared to zero-shot learning. However, for the use cases in Microsoft's 2023 analysis, few-shot learning led to only limited improvement compared to zero-shot learning on GPT-4 and a few other models."*
2. **Tay 2016 brand-risk anecdote** — Ch 5 cites Microsoft's Tay chatbot incident (2016, racist comments) as one of two canonical examples of brand-risk failures from generative-AI-in-production (alongside Google AI Overviews' 2024 "eat rocks" incident).
3. **LLM red-teaming write-up + PyRIT.** Ch 5's defenses section cites Microsoft's **public LLM red-teaming write-up** as the canonical practitioner reference for [[LLMRedTeaming|planning and running LLM red-team exercises]], and names **[[AzurePyRIT|Azure/PyRIT]]** (Python Risk Identification Toolkit) as Microsoft's open-source automated red-teaming toolkit — making Microsoft a structural contributor to the defense-side of [[DefensivePromptEngineering|defensive prompt engineering]].

## From [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]]

Ch 6 uses Microsoft assets in two roles:

1. **[[Phi3Mini|Phi-3-mini]] as the prompt-engineering substrate** — carried forward from Chs 1–5; Ch 6 uses both the `microsoft/Phi-3-mini-4k-instruct` `transformers` variant and the **`microsoft/Phi-3-mini-4k-instruct-gguf`** quantized variant (the latter for the grammar-constrained-decoding worked example).
2. **[[Guidance]]** — Microsoft's templating + constrained-decoding open-source library; named in Ch 6 alongside [[Guardrails]] and [[LMQL]] as one of three canonical Python packages for constrain-and-validate LLM output.

Microsoft sits at both endpoints of Ch 6's grammar-constrained-decoding worked example — providing the [[Phi3Mini|model]] and (in the broader toolchain ecosystem) authoring [[Guidance]] as one of the canonical constrained-sampling libraries.
