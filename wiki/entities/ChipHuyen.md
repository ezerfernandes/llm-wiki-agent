---
title: "Chip Huyen"
type: entity
tags: [person, author, ml-engineer, ai-engineer]
sources: [ai-engineering-chip-huyen, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch05-prompt-engineering, ai-engineering-ch06-rag-agents, ai-engineering-ch07-finetuning, ai-engineering-ch08-dataset-engineering, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Chip Huyen

Vietnamese-American AI engineer, author, and educator. Author of *AI Engineering: Building Applications with Foundation Models* ([[OReilly|O'Reilly]], December 2024 — see [[ai-engineering-chip-huyen]]) and its predecessor *Designing Machine Learning Systems* ([[OReilly]], 2022). Previously taught machine-learning systems design at [[stanforduniversity|Stanford]], worked at [[NVIDIA]] and Netflix (Snorkel AI affiliations), and founded an AI-infrastructure startup that was later acquired.

## Voice and method

Throughout Ch 1 of *AI Engineering*, Huyen frames the discipline through three lenses:

- **Empirical surveys**: she interviewed 50 enterprises and read 100+ case studies for the use-case taxonomy, and tracked 205 open-source AI applications with 500+ GitHub stars for consumer-side patterns.
- **Practitioner conversations**: she relays direct quotes from sources like Matt Ross (Scribd, on inference-cost collapse), Anton Bacaj (on AI engineering as full-stack engineering), and senior heads of AI at Fortune 500 companies.
- **Disclosure of investments and advisorship**: she explicitly notes her relationships with [[Convai]] (advisor) and [[Photoroom]] (investor) where these companies appear in the book.

## Positions taken in Ch 1

- **AI engineering ≠ ML engineering**, but evolved from it — see [[AIEngineeringVsMLEngineering]].
- **Start simple**: prompt before RAG, RAG before agents, prompt before finetuning, finetuning before training-from-scratch.
- **Evaluation is the hardest problem in AI engineering** — devotes Chapters 3–4 to it.
- **"Foundation model" is the right term** once modality expands beyond text; "LLM" is "hardly a scientific term" because "large" is ill-defined.
- **The model-as-a-service API tier is what makes AI engineering possible** for non-frontier-lab teams.

## Connections

- [[ai-engineering-chip-huyen]] — the parent source page for the book.
- [[ai-engineering-ch01-intro]] — Chapter 1, surveys the use-case landscape and stack.
- [[ai-engineering-ch02-foundation-models]] — Chapter 2, the deep technical anatomy of foundation models.
- [[OReilly]] — publisher.
- [[stanforduniversity]] — prior teaching home.
- [[NVIDIA]] — prior employer.
- [[AIEngineering]] — the discipline the book defines.
- [[FoundationModel]] — central concept.

## Positions taken in Ch 2

- **Sampling is the most underrated concept in AI.** *"Not only does sampling explain many seemingly baffling AI behaviors, including hallucinations and inconsistencies, but choosing the right sampling strategy can also significantly boost a model's performance with relatively little effort."*
- **Featured [[rlhf|RLHF]] over [[DPO|DPO]]** in the chapter on the grounds that RLHF is more flexible to tweak — even though DPO is simpler and gaining traction (Llama 3 switched).
- **[[Inconsistency|Inconsistency]] and [[Hallucination|hallucination]] are the twin probabilistic-failure modes** — both rooted in the same probabilistic sampling substrate.
- **Two-hypothesis explanation for [[Hallucination|hallucination]]**: [[SelfDelusion|self-delusion]] (self-supervision side) + [[InternalKnowledgeMismatch|internal-knowledge mismatch]] (supervision side). Complementary, not contradictory.
- **The [[ChinchillaScalingLaw|Chinchilla recipe]] (≈20 tokens/param) is the practitioner-grade scaling rule** — but inference economics ([[meta|Meta]]'s Llama choice) often justifies departing from it.

## Positions taken in Ch 4

- **[[EvaluationDrivenDevelopment|Evaluation-driven development]]** — TDD for AI engineering. Define criteria before building. *"I believe that evaluation is the biggest bottleneck to AI adoption."*
- **Four-bucket criteria taxonomy** — domain capability / generation (factual consistency + safety) / instruction-following / cost & latency.
- **"You don't really care about which model is the best. You care about which model is the best for your applications."** — the central thesis of the model-selection section.
- **A benchmark stops being useful as soon as it becomes public** (attributed to a friend; agrees).
- **Build [[CustomLeaderboard|custom leaderboards]] for your applications** — public leaderboards can only filter out bad models.
- **Map evaluation metrics to [[BusinessMetric|business metrics]]** — factual consistency 80% → automate 30% of support; 98% → 90%. Plan around the gradient.
- **[[DataSlicing]] is non-negotiable.** *"If you care about something, put a test set on it."* Includes [[OutOfScopeEvaluation|out-of-scope sets]].
- **Use [[BootstrapEvaluation|bootstrap]] to size evaluation sets.**
- **Human evaluation is the north star, even in production.** LinkedIn manually evaluates up to 500 conversations daily.
- **Anecdote-driven case studies.** Voiceflow ↓10%, GoDaddy ↑ on same GPT-3.5 update. LinkedIn's *"You are a terrible fit"* example. Ello's reading vocabulary constraint. Convai's NPCs needing physical abilities. Samsung's ChatGPT leak. Italy banning OpenAI.
- **Reuses [[SimpsonsParadox|Simpson's paradox]]** from *Designing Machine Learning Systems* as the canonical reason to slice evaluation data.

## Positions taken in Ch 5

- **Prompt engineering is the easiest and most common [[ModelAdaptation|model adaptation]] technique** — *"You should make the most out of prompting before moving to more resource-intensive techniques like finetuning."*
- **Prompt-engineering rigor is non-optional.** *"Prompt experiments should be conducted with the same rigor as any ML experiment, with systematic experimentation and evaluation."*
- **Prompt engineering is human-to-AI communication.** *"Anyone can communicate, but not everyone can communicate effectively."*
- **[[PromptRobustness|Robustness scales with model capability]].** Stronger models reduce prompt-engineering toil — *"working with stronger models can often save you headaches and reduce time wasted on fiddling."*
- **[[ChatTemplate|Chat templates]] are silent-failure surfaces.** Print the prompt before sending it; verify third-party tools use the right template.
- **[[PromptDecomposition|Prompt decomposition]] is one of the few practices that improves both performance *and* cost.** [[GoDaddy]] case study: 1,500-token prompt → decomposed → better.
- **[[chainofthought|CoT]] reduces hallucinations** (LinkedIn finding).
- **Inspect the prompts your tools generate.** Quotes Hamel Husain's *"Show Me the Prompt"* essay; uses a [[LangChain]] typo screenshot as evidence.
- **Separate prompts from code, version them in a [[PromptCatalog|prompt catalog]] rather than in Git when prompts are shared across applications.**
- **Three prompt-attack families** ([[PromptExtraction]] / [[Jailbreak|Jailbreaking + PromptInjection]] / [[InformationExtraction]]) — the chapter's defensive-prompt-engineering taxonomy.
- **"Write your system prompt assuming that it will one day become public."** Proprietary prompts are more liability than moat.
- **As models get better at following instructions, they get better at following *malicious* instructions.** The cat-and-mouse framing for AI safety.
- **[[NeedleInAHaystack|NIAH]] / [[RULERBenchmark|RULER]] tests for *practical* context length** — the advertised number is not the usable number.

## Positions taken in Ch 6

- **RAG = per-query context construction.** *"Context construction for foundation models is equivalent to feature engineering for classical ML models."*
- **Long context does not kill RAG.** Application data grows faster than fixed context limits ([[ParkinsonsContextLaw|Parkinson's Law for context]]); long contexts have efficiency penalties.
- **Term-based vs embedding-based, not sparse vs dense.** The [[SPLADE]] counterexample motivates the new division.
- **BM25 is a formidable baseline.** Quoting [[AravindSrinivas|Aravind Srinivas]] (CEO of [[Perplexity]]): *"Making a genuine improvement over BM25 or full-text search is hard."*
- **Vector DB spending can match API spending.** *"It's not uncommon to see a company's vector database spending be one-fifth or even half of their spending on model APIs."*
- **A RAG system should be evaluated three ways**: retrieval quality, final outputs, embeddings.
- **An agent = environment + tool inventory + AI planner.** Inherited from [[StuartRussell|Russell]] & [[PeterNorvig|Norvig]]'s *AIMA* definition.
- **[[CompoundErrorAccumulation|Compound mistakes]] are the planning tax.** 95% per-step → 60% over 10 steps → 0.6% over 100 steps.
- **Decouple planning from execution.** Validate before executing — avoids 1,000-step fruitless loops.
- **Agnostic on LLMs-can-plan.** Records [[YannLeCun|LeCun]] and [[SubbaraoKambhampati|Kambhampati]]'s skeptic positions alongside [[ReasoningWithLanguageModelIsPlanningWithWorldModel|Hao et al. 2023]]; doesn't adjudicate.
- **Reflection is cheap relative to plan generation and brings large gains.** [[react|ReAct]] / [[reflexion|Reflexion]].
- **Use natural-language plans + translator over exact-function-call plans.** More robust to tool-API changes.
- **Memory has three tiers**: [[InternalKnowledgeMemory|internal knowledge]], [[ShortTermMemory|short-term]], [[LongTermMemory|long-term]].
- **[[FIFOMemory|FIFO]] memory loses purpose-stating messages.** Reflection-based ([[ReflectionMemory|Liu et al. 2023]]) and summarization-based ([[SummarizationMemory|Bae et al. 2022]]) are stronger.
- **RAG is a special case of agent.** *"The RAG pattern can be seen as a special case of agent where the retriever is a tool the model can use."*

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* cross-references Huyen's [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]] as the **discipline-framing companion** to its own runnable-code recipe layer. The wiki records the pairing on the Ch 12 source page:

> *"[[ai-engineering-ch07-finetuning|AI Engineering Ch 7]] — Huyen's most thorough fine-tuning treatment; Ch 12 of Hands-On LLMs is the **runnable-code companion** to Huyen Ch 7's frameworks-and-trade-offs framing."* — Ch 12 wiki source page

The two chapters cover the same surface area (LoRA / QLoRA / PEFT / preference tuning / RLHF / DPO) at **complementary granularities** — Huyen frames the trade-offs, Alammar & Grootendorst walk the actual `bitsandbytes` + `peft` + `trl` code path. Ch 12 is also where Huyen's α:r-ratio framing (*"typically 1:8 to 8:1"* in Ch 7) meets the chapter's `α=32 / r=64 = 0.5×` worked recipe — inside Huyen's framing but contradicting Ch 12's own inline *"twice the size of r"* rule. The convergence completes the wiki's three-book finetuning curriculum: Huyen Ch 7 (discipline) + [[leh-ch05-supervised-fine-tuning|LEH Chs 5–6]] (production pipeline) + Hands-On LLMs Ch 12 (GPU-poor runnable recipe).
