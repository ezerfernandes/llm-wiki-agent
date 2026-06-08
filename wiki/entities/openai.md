---
title: "OpenAI"
type: entity
tags: [organization, ai-lab]
sources: [2001.08361-scaling-laws, 2604.25067-frontier-coding-agents-c4, 2603.19247-prompt-optimization-jailbreaking, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling, ai-engineering-ch08-dataset-engineering, hands-on-llm-ch07-advanced-text-generation, hands-on-llm-ch09-multimodal-llms, agentic-design-patterns-ch05-tool-use, agentic-design-patterns-ch06-planning, agentic-design-patterns-ch11-goal-setting, agentic-design-patterns-ch16-resource-aware]
last_updated: 2026-06-07
---

# OpenAI

AI lab; develops the GPT family of models. OpenAI authors produced [[2001.08361-scaling-laws]] (Kaplan, McCandlish, Henighan, Brown, Chess, Child, Gray, Radford, Wu, Amodei — 2020), the foundational empirical study of [[ScalingLaws]] for neural language models and the quantitative argument behind the lab's subsequent compute-scaling roadmap. Several of those authors (Tom B. Brown, Dario Amodei) went on to co-author GPT-3 and to co-found Anthropic. In the broader corpus, GPT-5.4 surfaces as the agent with anomalous time-budget under-utilization in the C4-AlphaZero benchmark — consistent with but not diagnostic of sandbagging. Codex (the OpenAI coding agent) is also one of the four ADS systems improved by AGENTIC-IMODELS.

## Native function calling (Agentic Design Patterns Ch 5)
[[agentic-design-patterns-ch05-tool-use|Ch 5 (Tool Use)]] of [[AgenticDesignPatterns|*Agentic Design Patterns*]] names the OpenAI series (with [[gemini|Gemini]]) as the modern LLMs whose **native function calling** capability the agent frameworks ([[LangChain]], [[LangGraph]], [[GoogleADK|ADK]], [[CrewAI]]) leverage to emit structured [[ToolUse|tool-use]] requests. The [[CrewAI]] example configures `OPENAI_API_KEY` / `OPENAI_MODEL_NAME = "gpt-4o"`. The chapter's References cite the [OpenAI Function Calling docs](https://platform.openai.com/docs/guides/function-calling). See [[ToolUse]] / [[FunctionCalling]].

[[agentic-design-patterns-ch11-goal-setting|Ch 11 (Goal Setting and Monitoring)]] also runs its hands-on iterative-coding agent on OpenAI: `ChatOpenAI(model="gpt-4o", temperature=0.3)` via `langchain_openai`, keyed by `OPENAI_API_KEY`, with `gpt-4o` doing both code generation and the [[LLMAsAJudge|self-judge]] `goals_met` verdict in the [[GoalSettingAndMonitoring|goal-monitoring]] loop. See [[GoalSettingAndMonitoring]].

## Tiered model selection for cost (Agentic Design Patterns Ch 16)
[[agentic-design-patterns-ch16-resource-aware|Ch 16 (Resource-Aware Optimization)]] uses the OpenAI API for one of its three hands-on [[ResourceAwareOptimization|resource-aware]] examples: a `classify_prompt` step (running `gpt-4o`) sorts each user query into `simple`, `reasoning`, or `internet_search`, and `generate_response` then selects the model by class — **`gpt-4o-mini`** for simple, **`o4-mini`** for reasoning, and **`gpt-4o`** (plus a Google Custom Search call) for internet-search queries. This is OpenAI's model lineup serving as the **cost tier menu** for [[DynamicModelSelection|dynamic model selection]] — *"avoids wasting computational resources on simple requests while ensuring complex queries get the necessary attention."* See [[ResourceAwareOptimization]].

## Deep Research API (Agentic Design Patterns Ch 6)
[[agentic-design-patterns-ch06-planning|Ch 6 (Planning)]] details the **OpenAI Deep Research API** as a real-world exemplar of the [[Planning]] pattern (see [[DeepResearch]]): an agentic model that independently reasons, plans, and synthesizes from web sources, returning a structured, citation-rich report. Models named: `o3-deep-research-2025-06-26` (high quality) and `o4-mini-deep-research-2025-06-26` (faster). Called via `client.responses.create` with a `web_search_preview` tool (optionally `code_interpreter` and custom **MCP** tools). Distinctive vs ChatGPT: it exposes all intermediate steps — reasoning, search queries, code run — and supports the [[ModelContextProtocol|Model Context Protocol]] for private-data extensibility.

## Connections
- [[ResourceAwareOptimization]] / [[DynamicModelSelection]] — Ch 16's cost-tier example (`gpt-4o-mini` / `o4-mini` / `gpt-4o` by query class).
- [[DeepResearch]] / [[Planning]] — the OpenAI Deep Research API (`o3`/`o4-mini` deep-research models), Ch 6.
- [[ModelContextProtocol|MCP]] — the Deep Research API's private-data extensibility mechanism.
- [[ToolUse]] / [[FunctionCalling]] — OpenAI's native function-calling API underpins Ch 5's tool-using agents.
- [[gpt54|GPT54]]
- [[GPT51|GPT-5.1]] — used as the cross-family [[LLMAsAJudge|danger judge]] in [[2603.19247-prompt-optimization-jailbreaking]]; chosen specifically because it is *not* in the same model family as any of the four jailbreak targets.
- [[codex|Codex]]
- [[2001.08361-scaling-laws]]
- [[2604.25067-frontier-coding-agents-c4]]
- [[2605.03808-agentic-imodels]]
- [[2603.19247-prompt-optimization-jailbreaking]]
- [[ScalingLaws]]
- [[ComputeEfficientTraining]]

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]]'s *AI Engineering* Ch 1 attributes several discipline-defining contributions to OpenAI:

- **[[ChatGPT|ChatGPT]] (Nov 2022)** — the launch that ignited the [[AIEngineering|AI engineering]] discipline. The "ChatGPT moment" marks when [[SelfSupervision|self-supervised]] [[LargeLanguageModel|LLMs]] crossed into mainstream consciousness.
- **[[ModelAsAService|Model-as-a-service]] approach** — OpenAI popularized the API-served foundation-model business model, *"making it easier to leverage AI to build applications."* This is one of three structural factors enabling AI engineering.
- **[[CLIP]] (2021)** — pioneered [[NaturalLanguageSupervision|natural language supervision]] at 400M (image, text) pairs (400× [[ImageNet]]) → the first model to zero-shot generalize across image classification tasks.
- **GPT scaling milestones**: first GPT (June 2018, 117M params); GPT-2 (Feb 2019, 1.5B params); GPT-4 vocab 100,256 tokens. Ch 1 uses these to anchor the historical scale evolution of LLMs.
- **InstructGPT compute-allocation data**: pre-training takes up to 98% of compute and data resources — the canonical citation for how dominated by pre-training the FM compute budget is.
- **[[SamAltman|Sam Altman's]] thesis** (Sep 2022): the biggest opportunity for most people is adapting these models for specific applications — effectively the founding argument for AI engineering as a discipline.
- **[[Sora]]** — OpenAI's text-to-video product, cited in the image/video use case category.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 adds five OpenAI-specific data points:

1. **[[GPT2|GPT-2]] data filter.** OpenAI used **Reddit links with ≥3 upvotes** to filter [[CommonCrawl|Common Crawl]] for GPT-2's training data — a crude but practical signal of "links people care about."
2. **[[GPT3|GPT-3] scale**: 175B params, 300B training tokens, **3.14 × 10²³ [[FLOPs|FLOPs]]**. The canonical scale data point for the chapter's compute-budgeting examples.
3. **[[PPO]] (2017).** Released by OpenAI; the dominant RL backbone of [[rlhf|RLHF]].
4. **[[Verifier]] result** (Cobbe et al. 2021): math-problem verifier ≈ **30× model-size increase** in capability — the chapter's strongest argument for [[TestTimeCompute|test-time compute]].
5. **[[Logprobs]] API constraints.** Ch 2: *"OpenAI API only shows you the logprobs of up to the 20 most likely tokens. It used to let you get the logprobs of arbitrary user-provided text but discontinued this in September 2023."* Cited as a likely **model-replication-security** measure.

Plus the **OpenAI internal contradiction on RLHF and hallucination**: [[JohnSchulman]] (UC Berkeley 2023 talk) said RLHF reduces hallucinations; the InstructGPT paper (Ouyang et al. 2022) shows RLHF *worsened* hallucination vs SFT alone. Recorded as an open question on the [[Hallucination]] and [[InternalKnowledgeMismatch]] pages.

[[LeoGao]] (OpenAI researcher) is also the originator of the **[[InternalKnowledgeMismatch|internal-knowledge-mismatch]] hypothesis** for why LMs hallucinate.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

OpenAI is the principal entity through which Ch 1 narrates the rise of large generative language models:

- **[[GPT|GPT-1]] (2018, [[AlecRadford|Radford]] et al.)** — 117M params, trained on 7,000 books + [[CommonCrawl|Common Crawl]]; the original decoder-only [[GenerativeModel|generative model]].
- **[[GPT2|GPT-2]] (2019)** — 1.5B params.
- **[[GPT3|GPT-3]] (2020, Brown et al., *"Language Models are Few-Shot Learners"*)** — 175B params.
- **[[ChatGPT]] (Nov 2022, powered initially by GPT-3.5)** — *"reaching one million active users in five days and then one hundred million active users in two months"* — the chapter's anchor for 2023 as "the Year of Generative AI."
- **[[GPT4|GPT-4]] (2023, OpenAI 2023 *"GPT-4 Technical Report"*, arXiv:2303.08774)** — the more performant ChatGPT-backing variant.

Ch 1 also names OpenAI as the canonical example of a **[[ProprietaryLLM|proprietary-LLM]] provider** — *"Closed source LLMs are models that do not have their weights and architecture shared with the public. ... Examples of such models include OpenAI's GPT-4 and Anthropic's Claude."*

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 surfaces OpenAI in **six specific roles** beyond being the dominant commercial model API provider:

1. **[[OpenAIEvals|OpenAI Evals]]** — OpenAI's evaluation harness for ~500 benchmarks plus user-registered ones.
2. **[[OpenAIModeration|Moderation endpoint]]** — content-moderation API and a canonical harm taxonomy (alongside Meta's [[LlamaGuard]]).
3. **[[OpenSourceModel|Open-sourced]] some models** — GPT-2 and [[CLIP]] are open-source. *"Typically, model providers open source weaker models and keep their best models behind paywalls."*
4. **GPT-3 contamination disclosure** (Brown et al. 2020) — **13 benchmarks ≥40% contaminated** in GPT-3's training data. Canonical practitioner data point on the prevalence of [[DataContamination|data contamination]].
5. **Version drift case study** — GPT-3.5-turbo-0301 → 1106 migration dropped [[Voiceflow]]'s intent classification 10% but improved [[GoDaddy]]'s customer support. Stanford/Berkeley's Chen et al. 2023 documented similar GPT-3.5/GPT-4 performance shifts between March-June 2023.
6. **De-facto API standard** — *"Many API providers mimic OpenAI's API"* — the swap-compatibility interface for the ecosystem.

Plus the **Italy ban (2023)** as a country-level access-loss case study. OpenAI is also one of the few API providers Anthropic credits with publishing a useful moderation-prompts tutorial.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 features OpenAI in **four distinct roles**:

1. **The [[InContextLearning|in-context learning]] paper.** Brown et al. 2020 (the GPT-3 paper) *"Language Models Are Few-shot Learners"* is the founding work for in-context learning as a paradigm.
2. **The [[InstructionHierarchy|Instruction Hierarchy]] post-training scheme.** [[WallaceEtAl2024|Wallace et al. 2024]] — *"The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions"* — is Ch 5's load-bearing structural defense against [[PromptInjection|prompt injection]] and [[IndirectPromptInjection|indirect prompt injection]]. Also the source of the email-assistant worked example.
3. **Prompt-position preference.** *"Most models, including GPT-4, empirically perform better when the task description is at the beginning of the prompt."* — the canonical contrast with Llama 3's end-bias.
4. **Customer-support decomposition example.** Ch 5's worked example of [[PromptDecomposition|prompt decomposition]] (intent classification + per-intent response prompts) is drawn directly from OpenAI's prompt-engineering guide.

The OpenAI research-manager quote in Ch 5's opening — *"The problem is not with prompt engineering. It's a real and useful skill to have. The problem is when prompt engineering is the only thing people know."* — is the chapter's load-bearing framing.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses **OpenAI's Chat Completions API** (`openai.OpenAI(api_key=...)` → `client.chat.completions.create(...)`) as the chapter's closed-source [[GenerativeClassification|generative-classification]] demo with `gpt-3.5-turbo-0125` — the first end-to-end OpenAI-API worked example in the *Hands-On LLMs* book:

```python
import openai
client = openai.OpenAI(api_key="YOUR_KEY_HERE")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt.replace("[DOCUMENT]", document)}
    ],
    model="gpt-3.5-turbo-0125",
    temperature=0
)
```

Ch 4 reports specifically:
- **Cost**: the 1,066-row Rotten Tomatoes test sweep cost **3 cents** at time of writing, covered by the free-tier OpenAI credit allowance.
- **F1 on [[RottenTomatoes|Rotten Tomatoes]]**: **0.91** weighted average — the chapter's best result across all four classification regimes.
- **Rate-limit mitigation**: the chapter names **[[ExponentialBackoff|exponential backoff]]** as the standard remedy for `RateLimitError`, with a forward reference to OpenAI's cookbook backoff guide.
- **Cohere as alternative**: in the embedding section, the chapter names *"Cohere's and OpenAI's offerings"* as the production-grade alternatives to local sentence-transformers — *"this would allow the pipeline to run entirely on the CPU."*

Plus Ch 4's **three-step OpenAI training pipeline sketch** for ChatGPT (pretraining → instruction tuning → preference tuning) — see [[ChatGPT]] for the full treatment.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

OpenAI surfaces in Ch 8 across multiple data-engineering threads:

### The finetuning-data-quantity experiment

OpenAI's published experiment varied the number of training examples (100 → 550,000) across five models from the OpenAI lineup:

| Data size | Result |
|---|---|
| 100 examples | More advanced models (e.g., GPT-4) **dramatically outperform** weaker ones (Babbage) after finetuning |
| 550,000 examples | **All five models converge** to similar performance |

This is the chapter's core evidence for the **"small data → PEFT on big model; large data → full FT on small model"** heuristic.

### text-davinci-003 as the canonical teacher for distillation

- **[[AlpacaDataset|Alpaca]]** — 175 seeds + text-davinci-003 → 52K examples; Llama-7B student is 4% the size of teacher.
- **[[BuzzFeed]]** — Flan-T5 + LoRA on text-davinci-003-generated examples; 80% inference cost reduction.

text-davinci-003 is the GPT-3 variant most widely used as a teacher in the open synthetic-data ecosystem.

### [[OpenAIDota2|OpenAI Dota 2]] — the canonical self-play project

- 180 game-years/day of simulated training.
- Top-professional-human Dota 2 performance.
- The chapter's headline [[SelfPlay|self-play]] example for AI agents.

### [[GregBrockman]] — manual-data-inspection quote

OpenAI co-founder quoted in Ch 8:

> "Manual inspection of data has probably the highest value-to-prestige ratio of any activity in machine learning."

The Ch 8 anchor for **stare-at-your-data discipline** as a non-glamorous-but-high-leverage practice.

## From [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]]

Ch 7 uses OpenAI's API (specifically **`gpt-3.5-turbo`** via `ChatOpenAI`) as the **agent-capable LLM** when the local [[Phi3Mini|Phi-3-mini]] proves insufficient. The chapter's framing of OpenAI's role:

> *"These autonomous processes generally require an LLM that is powerful enough to properly follow complex instructions. The LLM that we used thus far is relatively small and not sufficient to run these examples. Instead, we will be using OpenAI's GPT-3.5 model as it follows these complex instructions more closely."* — Ch 7

The structural point: OpenAI is Ch 7's **honest fallback** when the GPU-poor / Phi-3-local commitment hits its capability ceiling at agents. The [[LangChainAgent|LangChain `create_react_agent` + `AgentExecutor`]] worked example (MacBook Pro price + EUR conversion via DuckDuckGo + llm-math) runs on GPT-3.5-turbo. This is the wiki's first runnable [[LangChain]] ReAct agent and the first place OpenAI's API serves an *agent* role in the [[HandsOnLLM]] book (Chs 1–6 used OpenAI for classification + topic-labeling only).

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 puts OpenAI in two new wiki-relevant roles centered on **[[CLIP|CLIP / Contrastive Language-Image Pre-training]]** (Radford et al. 2021):

1. **Author lab of CLIP** — *"the most well-known and currently most-used"* multimodal embedding model. OpenAI's contribution is the original training recipe (400M image-text pairs harvested from the web via [[NaturalLanguageSupervision|natural language supervision]]) and the `openai/clip-vit-base-patch32` checkpoint Ch 9 loads via Hugging Face `transformers`. **[[AlecRadford|Alec Radford]]** is the same first author Ch 1 cited for [[GPT2|GPT-2]] — CLIP and the GPT family share a research lead.
2. **Source of the [[ClsToken|`[CLS]` token convention inversion]]** — CLIP's distinguishing-feature against BERT is that *"in CLIP, the [CLS] token is actually used to represent the image embedding, not the text embedding"* (the inverse of BERT's convention) — Ch 9 codifies this convention shift as a CLIP-specific override.

CLIP positions OpenAI as the **multimodal-embedding-foundation lab** in addition to its frontier-LLM role; the chapter does not call out a downstream OpenAI generative multimodal model (GPT-4V / GPT-4o would qualify but are not the chapter's focus — Ch 9's worked generative multimodal model is [[Salesforce]]'s [[BLIP2|BLIP-2]]).
