---
title: "AI Engineering Ch 1 — Introduction to Building AI Applications with Foundation Models"
type: source
tags: [book, foundation-models, ai-engineering, oreilly, ai-engineering-book]
date: 2024-12-04
source_file: raw/papers/ai-engineering/ch01-intro.md
parent_source: ai-engineering-chip-huyen
---

# AI Engineering Ch 1 — Introduction to Building AI Applications with Foundation Models

## Summary

Chapter 1 of [[ChipHuyen|Chip Huyen]]'s *AI Engineering* ([[OReilly|O'Reilly Media]], 2024) frames the emergence of **[[AIEngineering|AI engineering]]** as a distinct discipline by tracing a three-step evolution: from classical **[[LanguageModel|language models]]** (statistical word-prediction; centuries of statistical-language work culminating in [[ClaudeShannon|Claude Shannon's]] 1951 entropy paper), to **[[LargeLanguageModel|large language models]]** (made possible by [[SelfSupervision|self-supervision]], which dissolves the data-labeling bottleneck that constrained the [[AlexNet]]-era supervised paradigm), to **[[FoundationModel|foundation models]]** (multimodal generalist models that extend LLMs to vision, audio, and beyond — [[CLIP]], [[GPT4|GPT-4V]], [[gemini|Gemini]], [[LLaVA15|LLaVA]]). The chapter argues that the rise of foundation models — usable via API without training — has produced an ideal condition for a new kind of engineering centered on **[[ModelAdaptation|model adaptation]]** rather than model development.

Huyen surveys [[FoundationModelUseCases|eight use-case categories]] (coding, image/video, writing, education, conversational bots, [[InformationAggregation|information aggregation]], [[DataOrganization|data organization]], [[WorkflowAutomation|workflow automation]]) drawn from interviewing 50 enterprises and analyzing 205 open-source GitHub apps. She then introduces a planning framework: **[[UseCaseEvaluation|use case evaluation]]** (why build), the **AI-and-human role taxonomy** ([[CriticalOrComplementary|critical/complementary]], [[ReactiveOrProactive|reactive/proactive]], [[DynamicOrStatic|dynamic/static]]), the **[[CrawlWalkRun|Crawl-Walk-Run automation framework]]**, **[[AIProductDefensibility|defensibility]]** for AI products, **[[UsefulnessThreshold|usefulness thresholds]]**, and the **[[LastMileChallenge|last-mile challenge]]** (going from 80% to 95% takes much longer than 0% to 80%).

The chapter closes with the **[[AIEngineeringStack|AI engineering stack]]**: three layers (application development, model development, infrastructure) and the contrast between [[AIEngineeringVsMLEngineering|AI engineering and ML engineering]] across [[ModelingAndTraining|modeling/training]], [[DatasetEngineering|dataset engineering]], [[InferenceOptimization|inference optimization]], [[Evaluation|evaluation]], [[PromptEngineering|prompt engineering]], and [[AIInterface|AI interface]]. The takeaway: ML knowledge becomes a nice-to-have rather than a must-have; evaluation, adaptation, and inference economics become first-class.

## Key Claims

- **Self-supervision is the crucial unlock that turned language models into LLMs.** Unlike supervised learning, which requires manual labels (e.g., $50k to label 1M ImageNet images), self-supervision derives labels from the input itself, enabling internet-scale training data.
- **"Foundation model" supersedes "LLM" once modality expands beyond text.** Models like [[GPT4|GPT-4V]] and [[ClaudeOpus47|Claude 3]] handle images alongside text; "foundation" signals both their general-purpose role and their build-upon-able nature.
- **[[CLIP|CLIP]] (OpenAI, 2021) demonstrated [[NaturalLanguageSupervision|natural language supervision]]** by scraping 400M (image, text) pairs co-occurring on the internet — 400× larger than ImageNet, with zero manual labeling cost — and produced the first model to zero-shot generalize across image classification tasks.
- **Three factors create the AI engineering opportunity**: (1) general-purpose model capabilities, (2) [[AIInvestmentBoom|increased AI investments]] (Goldman Sachs estimated $100B US / $200B global by 2025; 1-in-3 S&P 500 companies mentioned AI in Q2 2023 earnings calls), and (3) low entry barriers via [[ModelAsAService|model-as-a-service]] APIs.
- **Model adaptation has two technique families**: [[PromptBasedAdaptation|prompt-based]] (no weight changes — [[PromptEngineering|prompt engineering]], [[rag|RAG]]) and [[Finetuning|finetuning]] (weight changes). Prompt-based is faster, cheaper, lower-data; finetuning is needed for complex tasks and strict performance bars.
- **The McKinsey study cited in the chapter** finds AI doubles documentation productivity and yields 25–50% gains in code generation/refactoring, with minimal improvement on highly complex tasks. AI is observably better at frontend than backend.
- **AI-product defensibility comes from three sources**: technology, data, and distribution. With foundation models, technology converges; data and distribution become the durable moats. There is a real risk that an application's value is subsumed by the next base-model release ("OpenAI wrappers" joke).
- **The [[LastMileChallenge|last-mile problem]]**: LinkedIn (2024) reached 80% of target experience in one month, then needed four more months for 95% — citing UltraChat (Ding et al., 2023): "the journey from 0 to 60 is easy, whereas progressing from 60 to 100 becomes exceedingly challenging."
- **The AI engineering stack has three layers**: application development (prompts, context, interface, evaluation), model development (modeling/training, dataset engineering, inference optimization), and infrastructure (serving, compute, monitoring). Application-layer tooling exploded in 2023 after [[StableDiffusion|Stable Diffusion]] and [[ChatGPT|ChatGPT]] launched; infrastructure tooling grew more slowly because core needs (serving, monitoring) didn't change.
- **AI engineering differs from ML engineering in three ways**: (1) uses someone else's pretrained models, focusing on adaptation; (2) works with bigger, more compute-intensive, higher-latency models, raising the importance of inference optimization; (3) open-ended outputs make [[Evaluation|evaluation]] harder.
- **Inference optimization rises in importance** because foundation models are [[AutoregressiveLanguageModel|autoregressive]]: ~10ms/token × 100 tokens = 1s — far above the 100ms latency expected for typical web apps.
- **AI engineering converges toward full-stack engineering.** Anton Bacaj: *"AI engineering is just software engineering with AI models thrown in the stack."* The workflow inverts: build the product first, invest in data/models once the product shows promise.

## Key Quotes

> "AI engineering refers to the process of building applications on top of foundation models." — p. 12

> "Foundation models, thanks to their scale and the way they are trained, are capable of a wide range of tasks. Out of the box, general-purpose models can work relatively well for many tasks." — p. 10

> "It's easy to build a cool demo with foundation models. It's hard to create a profitable product." — p. 29 (Use Case Evaluation)

> "The journey from 0 to 60 is easy, whereas progressing from 60 to 100 becomes exceedingly challenging." — UltraChat (Ding et al., 2023), quoted on p. 33

> "AI engineering is just software engineering with AI models thrown in the stack." — Anton Bacaj, quoted on p. 46

## Concepts Introduced or Engaged

- [[AIEngineering]] — *new*, the discipline this chapter defines.
- [[FoundationModel]] — *new*, the chapter's organizing concept; supersedes LLM when modalities expand.
- [[LargeLanguageModel]] — *new*, the LLM definition (scaled language model trained via self-supervision); refines [[LanguageModel]].
- [[SelfSupervision]] — *new*, the training paradigm that enabled LLM scale.
- [[NaturalLanguageSupervision]] — *new*, CLIP's (image, text)-pair training scheme.
- [[AutoregressiveLanguageModel]] — *new*, the dominant text-generation LM type.
- [[GenerativeAI]] — *new*, output-open-endedness as the differentiator.
- [[ModelAdaptation]] — *new*, the umbrella term for prompt-based + finetuning techniques.
- [[PromptBasedAdaptation]] — *new*, prompt engineering / RAG as no-weight-update adaptation.
- [[AIEngineeringStack]] — *new*, the three-layer (application / model / infrastructure) stack.
- [[AIEngineeringVsMLEngineering]] — *new*, the comparison taxonomy.
- [[ModelAsAService]] — *new*, the API-served base-model business model.
- [[AIInterface]] — *new*, the UX surface (standalone, embedded, browser extension, voice, embodied).
- [[DatasetEngineering]] — *new*, the data curation/synthesis/quality-control discipline of AI engineering.
- [[InferenceOptimization]] — *new*, latency/cost-of-inference engineering for foundation models.
- [[ModelingAndTraining]] — *new*, the architecture/training portion of the model-development layer.
- [[UseCaseEvaluation]] — *new*, the why-build-this framework.
- [[CrawlWalkRun]] — *new*, Microsoft's gradual-automation framework.
- [[CriticalOrComplementary]] — *new*, Apple's product role taxonomy axis.
- [[ReactiveOrProactive]] — *new*, Apple's product role taxonomy axis.
- [[DynamicOrStatic]] — *new*, Apple's product role taxonomy axis.
- [[AIProductDefensibility]] — *new*, the moat framework (tech / data / distribution).
- [[UsefulnessThreshold]] — *new*, the deployment-readiness metric set.
- [[LastMileChallenge]] — *new*, the 80→95% slowdown.
- [[FoundationModelUseCases]] — *new*, the eight-category use-case taxonomy.
- [[InformationAggregation]] — *new*, the summarization/distillation use case.
- [[DataOrganization]] — *new*, the extract-structure-from-unstructured use case.
- [[WorkflowAutomation]] — *new*, the AI-agent-driven automation use case.
- [[AIInvestmentBoom]] — *new*, the 2023–2025 capital surge and its drivers.
- [[TTFT]] — *new*, time-to-first-token latency metric.
- [[TPOT]] — *new*, time-per-output-token latency metric.
- [[mmlu]] — *engaged*, foundation-model benchmark referenced for the Gemini-vs-ChatGPT prompt-format anecdote.
- [[Tokenization]] / [[Tokenizer]] — *engaged*, GPT-4's 100,256 vocab; Mixtral 8x7B's 32,000; "100 tokens ≈ 75 words".
- [[LanguageModel]] — *engaged*, statistical definition extended into LLMs.
- [[maskedlanguagemodel]] — *engaged*, BERT as the non-generative MLM exemplar.
- [[bert|BERT]] — *engaged*, the bidirectional encoder reference.
- [[Hallucination]] — *engaged*, named as the "kink" LinkedIn spent four months grinding.
- [[Perplexity]] — *engaged*, as Perplexity-the-product (cited alongside ChatGPT).
- [[rag|RAG]] — *engaged*, named as one of three core adaptation techniques.
- [[FineTuning]] / [[FineTuning]] — *engaged*, weight-update adaptation.
- [[PromptEngineering]] — *engaged*, no-weight-update adaptation.
- [[MultimodalLLM]] — *engaged*, the LMM definition (generative multimodal).
- [[AgenticAI]] / [[llmagents]] — *engaged*, "AIs that can plan and use tools are called agents."
- [[pretraining]] — *engaged*, defined alongside finetuning and post-training; InstructGPT pre-train uses 98% of compute.
- [[posttraining|PostTraining]] — *engaged*, distinguished from finetuning by who does it (model dev vs. application dev).
- [[Quantization]] — *new*, mentioned as weight-modifying but not training.
- [[MLOps]] — *engaged*, contrasted with AI engineering; AI engineering is "less Ops, more engineering."
- [[humanintheloop]] — *engaged*, the AI-human role spectrum.

## Entities Introduced or Engaged

- [[ChipHuyen]] — *new*, author.
- [[OReilly]] — *new*, publisher.
- [[ChatGPT]] — *new*, the canonical foundation-model consumer application.
- [[Sora]] — *new*, OpenAI's video generation product.
- [[Midjourney]] — *new*, image generation startup ($200M ARR by late 2023).
- [[AdobeFirefly]] — *new*, photo-editing AI product.
- [[Runway]] / [[PikaLabs]] — *new*, video-generation startups.
- [[GitHubCopilot]] — *new*, the first big foundation-model production success ($100M ARR after two years).
- [[Anysphere]] — *new*, AI coding startup ($60M raise, August 2024); maker of [[cursor|Cursor]].
- [[MagicAI]] — *new*, AI coding startup ($320M raise, August 2024).
- [[JensenHuang]] — *new*, NVIDIA CEO; "stop saying kids should learn to code."
- [[SamAltman]] — *new*, OpenAI CEO; on the model-adaptation opportunity for non-FM-builders.
- [[MattGarman]] — *new*, AWS CEO; "most developers will stop coding."
- [[Convai]] / [[Inworld]] — *new*, 3D NPC startups; Huyen advises Convai.
- [[KhanAcademy]] — *new*, AI teaching assistant ("Khanmigo").
- [[Duolingo]] — *new*, language-learning app using AI for lesson personalization.
- [[Chegg]] — *new*, homework-help company disrupted by ChatGPT ($28 → $2).
- [[Grammarly]] — *new*, writing-assistant product; finetunes a model for fluency/coherence.
- [[Photoroom]] — *new*, image-editing startup (Huyen is an investor).
- [[Perplexity]] — *new*, conversational-search standalone product.
- [[Instacart]] — *new*, used an internal prompt marketplace; "Fast Breakdown" was top template.
- [[Scribd]] — *new*, mentioned via Matt Ross: AI cost dropped 2 orders of magnitude April 2022 → April 2023.
- [[Apple]] — *new*, source of the AI-in-product taxonomy (critical/complementary, reactive/proactive, dynamic/static).
- [[openai|OpenAI]] — *engaged*, GPT family; model-as-a-service originator; CLIP author.
- [[anthropic|Anthropic]] — *engaged*, well-funded FM-builder; Claude family.
- [[google|Google]] — *engaged*, Gemini; CLIP/Bard predecessor.
- [[microsoft|Microsoft]] — *engaged*, Copilot ecosystem; Crawl-Walk-Run framework author; partnered with OpenAI.
- [[meta|Meta]] — *engaged*, foundation-model builder.
- [[NVIDIA]] — *engaged*, GPU substrate; Huang's "stop coding" quote; NPC demos.
- [[Mistral7BInstructV02|Mistral]] — *engaged*, well-funded FM-builder.
- [[HuggingFace]] — *engaged*, Transformers framework.
- [[TensorFlow]] / [[PyTorch]] — *engaged*, modeling frameworks.
- [[stanforduniversity|Stanford]] — *engaged*, Huyen's prior teaching home.
- [[GitHub]] — *engaged*, GitHub-star count as the cited proxy for AI-engineering-tool growth.
- [[Ollama]] / [[StableDiffusion]] / [[AutoGPT]] — *engaged*, four open-source AI tools that surpassed Bitcoin in GitHub stars within two years.
- [[gemini|Gemini]] — *engaged*, the Gemini-vs-ChatGPT MMLU prompt-format anecdote.
- [[bard|Bard]] — *engaged*, Gemini's consumer-product predecessor name.

## Connections

- The chapter is the **first survey-style anchor in the wiki** that frames foundation-model engineering as a discipline. It links to the wiki's existing concept entries: [[rag|RAG]], [[FineTuning|fine-tuning]], [[lora|LoRA]], [[MIPROv2]], [[chainofthought|chain-of-thought]], [[react|ReAct]], [[selfconsistency|self-consistency]], [[Hallucination]], [[MultimodalLLM|MLLM]], [[CLIP]], [[AlexNet]], [[ImageNet]], [[bert|BERT]], [[maskedlanguagemodel]], [[gemini|Gemini]], [[GPT4|GPT-4]], [[LanguageModel]], [[pretraining]], [[posttraining|PostTraining]], [[MLOps]], [[mmlu]], [[humanintheloop|HITL]], [[Tokenization]].
- The **three-layer stack** ([[AIEngineeringStack]]) sets up the rest of the book: Chs 2–4 cover model development + evaluation; Chs 5–6 cover application-layer prompt engineering and RAG/agents; Chs 7–10 cover finetuning, dataset engineering, inference optimization, and architecture/feedback.
- **Definitional contrast with [[AgenticAI|Agentic AI as a paradigm]]**: Chapter 1's "agent" definition is the practical-engineering one ("AIs that can plan and use tools") — narrower than the topology-formalized Agentic-AI definition the wiki already records via [[2605.12966-agentic-ai-to-agi]]. Compatible, but different abstraction levels.
- **[[LanguageModel]] existing page is more technical** (joint-probability formula, n-grams, perplexity, scaling laws); Chapter 1 supplies the historical narrative (Shannon → BERT → autoregressive LMs → LLMs → FMs) and the use-case framing.
- **[[pretraining]] existing page is denser on the empirical recipes** ([[1810.04805-bert|BERT]], [[1910.10683-t5|T5]], [[2001.08361-scaling-laws|Kaplan scaling laws]]); Chapter 1 adds the practical distinction between pre-training, finetuning, and post-training as **training phases** rather than recipes.
- **[[posttraining|PostTraining]] page is a stub** — Chapter 1 supplies the first concrete definition the wiki has recorded.
- **[[humanintheloop|HITL]] page is a stub** — Chapter 1 adds the [[CrawlWalkRun|Crawl-Walk-Run]] gradual-automation framework as a concrete HITL deployment ladder.

## Contradictions

- **"Agent" terminology**: Chapter 1 defines agents as "AIs that can plan and use tools" — narrower than [[AgenticAI]]'s topology-graph formalization (Liao et al.'s $\Psi = (\mathcal{G}, \mathcal{F}, \Lambda)$ DAG). Not a contradiction but an abstraction-level difference; flagged for cross-reference.
- **"LLM" as a term**: Huyen explicitly calls LLM "hardly a scientific term" because "large" is ill-defined. The wiki's existing [[LanguageModel]] page treats LLM as a scale extension of the LM joint-probability framework. Compatible.
- No factual contradictions flagged with existing wiki content.
