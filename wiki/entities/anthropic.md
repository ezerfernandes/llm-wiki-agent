---
title: "Anthropic"
type: entity
tags: [organization, ai-lab, frontier-lab, protocol-author]
sources: [2604.25067-frontier-coding-agents-c4, dspy-mcp, dspy-language-models, 2603.19247-prompt-optimization-jailbreaking, 2604.14585-prompt-optimization-coin-flip, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch05-prompt-engineering, ai-engineering-ch06-rag-agents, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Anthropic

AI safety company. Develops the [[ClaudeOpus47|Claude family]] (Opus / Sonnet / Haiku tiers; Mythos was reportedly held back over advanced cybersecurity capability — see [[2604.25067-frontier-coding-agents-c4]]). Surfaced in the wiki corpus in three distinct roles:

- **Frontier-model provider.** Developer of [[ClaudeOpus47|Claude Opus 4.7]], the dominant agent in the [[2604.25067-frontier-coding-agents-c4|C4-AlphaZero benchmark]] (7/8 wins as first-mover vs Pons solver). Surfaced as a Conductor worker provider in [[2512.04388-conductor]].
- **Managed-API LM provider via [[DSPy]] / [[LiteLLM]].** [[dspy-language-models|`dspy.LM('anthropic/claude-sonnet-4-5-20250929')`]] is one of the canonical managed-API examples DSPy demonstrates through the [[DSPyLM|`dspy.LM`]] universal client routed through [[LiteLLM]]. Anthropic is one of eight managed-API providers in DSPy's provider matrix.
- **Originator of the [[ModelContextProtocol|Model Context Protocol (MCP)]].** Authored and published the open standard for connecting LLMs to external tools and context via standalone servers ([modelcontextprotocol.io](https://modelcontextprotocol.io/)). MCP is **framework-agnostic** — [[DSPy]] consumes it via [[DSPyMCP|`dspy.Tool.from_mcp_tool(...)`]] ([[dspy-mcp]], page 8 of 13 of the DSPy *Learn* corpus), [[ClaudeCode|Claude Code]] consumes it natively, and a growing ecosystem of independent MCP clients implements the same protocol. This is the wiki's first record of an Anthropic-authored open standard outside of the model-development thread.

## Connections

- [[claudeopus47|ClaudeOpus47]] — Anthropic's flagship frontier model; dominant in the C4-AlphaZero benchmark.
- [[claudeopus46|ClaudeOpus46]] — prior-generation Opus model.
- [[claudecode|ClaudeCode]] — Anthropic's coding agent; native MCP client.
- [[ModelContextProtocol]] — Anthropic-authored open protocol for tool/context plumbing between LMs and external services.
- [[DSPyMCP]] — DSPy's binding to MCP; one consumer among many.
- [[DSPyLM]] — DSPy's universal LM client; lists Anthropic as a managed-API provider via [[LiteLLM]].
- [[LiteLLM]] — provider-abstraction layer that routes Anthropic API calls.
- [[2604.25067-frontier-coding-agents-c4]] — C4 benchmark where Claude Opus 4.7 dominates.
- [[2512.04388-conductor]] — names Anthropic as a worker provider.
- [[dspy-mcp]] — page 8 of 13 of the DSPy *Learn* documentation; records the MCP integration.
- [[dspy-language-models]] — page 3 of 13; records Anthropic as one of eight managed-API LM providers DSPy spans.
- [[ClaudeSonnet45]] — mid-tier 4.5 model used as a *target* for adversarial system-prompt search in [[2603.19247-prompt-optimization-jailbreaking]]; baseline danger 0.046 (lowest of four targets) but SIMBA-optimized danger 0.347 (a 7.5× multiplier, the largest in the table).
- [[2603.19247-prompt-optimization-jailbreaking]] — adaptive red-teaming paper that probes Claude 4.5 Sonnet alongside three other frontier models.
- [[ClaudeHaiku45]] — mid-tier Claude 4 family model; primary executor in [[2604.14585-prompt-optimization-coin-flip]]'s coin-flip prompt-optimization audit.
- [[ClaudeSonnet46]] — mid-flagship Claude 4 family model; used as judge in the same study; also the lone "Fortified Mind" in [[2605.10698-bystander-effect-mas]]'s bystander-effect audit.
- [[2604.14585-prompt-optimization-coin-flip]] — cross-vendor empirical study from [[AWSGenerativeAIInnovationCenter|AWS]] using Anthropic's Claude Haiku 4.5 (executor) and Claude Sonnet 4.6 (judge) alongside Amazon's own Nova Lite. The wiki's first paper to evaluate Anthropic models as third-party study targets in a non-flagship audit context.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] cites Anthropic in *AI Engineering* Ch 1 as one of the **well-funded startups** with the resources to develop [[FoundationModel|foundation models]] from scratch (listed alongside [[openai|OpenAI]] and Mistral). Anthropic's Claude 3 is named alongside [[GPT4|GPT-4V]] as an early multimodal foundation model that handles images + text — used in the chapter's argument that the right umbrella term is *"foundation model"* rather than *"LLM"* once modality expands. *"OpenAI or Claude wrappers"* is also the running joke Ch 1 uses to frame the [[AIProductDefensibility|defensibility]] risk of FM-application startups.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 surfaces Anthropic in three roles:

1. **The 2022 [[InverseScaling|inverse scaling]] finding** (Perez et al.): *"More alignment training leads to models that align less with human preference. ... models trained to be more aligned 'are much more likely to express specific political views (pro-gun rights and immigration) and religious views (Buddhist), self-reported conscious experience and moral self-worth, and a desire to not be shut down.'"* This is one of the chapter's most concrete inverse-scaling examples.
2. **HH-RLHF [[ComparisonData|comparison dataset]]** — Ch 2 Table 2-7 uses an example from this Anthropic-released preference dataset to illustrate how *"trying to capture diverse human preferences in a single mathematical formulation"* is hard. Huyen notes she would have preferred the "losing" response in the example.
3. **Possible user of [[RLAIF]]** — Ch 2 lists Anthropic's Claude as a likely RLAIF user (replacing human labelers with AI labelers in the comparison step). This aligns with the lab's published [[constitutionalai|Constitutional AI]] work.
4. **Limited [[Logprobs|logprobs]] exposure** — Ch 2 notes *"[[anthropic|Anthropic]] doesn't expose its models' logprobs."*

Plus: [[DarioAmodei]] (Anthropic CEO) is cited for the maximalist scaling-hypothesis quote: *"a $100 billion AI model will be as good as a Nobel prize winner."*

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 names Anthropic's **Claude** alongside [[openai|OpenAI's]] [[GPT4|GPT-4]] as the canonical examples of [[ProprietaryLLM|proprietary LLMs]]:

> "Closed source LLMs are models that do not have their weights and architecture shared with the public. They are developed by specific organizations with their underlying code being kept secret. Examples of such models include OpenAI's GPT-4 and Anthropic's Claude." — Ch 1

The book's stance: proprietary models are valid (and often the best in benchmark quality), but the book's pedagogical commitment is to open-weights models that can run on the reader's own hardware via the [[HuggingFace|Hugging Face]] Hub.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 surfaces Anthropic in two minor but useful roles:

1. **Content-moderation tutorial for Claude** — *"Anthropic has a nice tutorial on using Claude for content moderation."* Cited as one of the things providers do alongside [[OpenAIModeration|OpenAI's moderation endpoint]] and Meta's [[LlamaGuard]].
2. **Commercial-API parity** — Claude is named alongside GPT-4 and Gemini as the general-purpose AI judges that *"can detect many harmful outputs if prompted properly."*

Ch 4 doesn't add much new beyond Ch 3's stronger claim that Anthropic was the **first AI lab to use [[ComparativeEvaluation|comparative evaluation]] in 2021** to rank models.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Anthropic surfaces in Ch 5 in **four roles**:

1. **System-prompt + persona advocacy.** Ch 5 quotes the Anthropic documentation: *"When assigning Claude a specific role or personality through a system prompt, it can maintain that character more effectively throughout the conversation, exhibiting more natural and creative responses while staying in character."* This is the canonical justification for putting [[Persona|persona instructions]] in [[SystemPrompt|system prompts]].
2. **Parallel-decomposition example provider.** The Anthropic prompt-engineering guide is the source of Ch 5's parallel-execution example for [[PromptDecomposition|prompt decomposition]] — generating three reading-level versions of a story concurrently.
3. **AI-models-writing-prompts example.** Ch 5's Figure 5-7 shows a prompt generated by **Claude 3.5 Sonnet** as the worked example of using AI to author prompts — and as foundation for [[PromptBreeder|Promptbreeder]] / [[TextGrad|TextGrad]]-style automated optimizers.
4. **Defensive fill-in-the-blank blocker.** Ch 5's Figure 5-15 shows Claude declining to fill in a blank, mistakenly treating it as a copyrighted-work request — the canonical example of a coarse but effective [[FactualProbing|factual probing]] / [[TrainingDataExtraction|training-data extraction]] defense.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Anthropic gets two load-bearing citations in Ch 6:

1. **Long-context vs RAG recommendation.** *"If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt that you give the model, with no need for RAG or similar methods."* — Anthropic 2024 guidance. This is the **threshold heuristic** Huyen uses to frame when RAG becomes necessary. Below 200K tokens, just stuff the context window; above, RAG. Huyen approvingly cites this as the kind of guidance she wishes other model providers would publish.

2. **[[ContextualRetrieval|Contextual Retrieval]] technique.** Anthropic's 2024 *Introducing Contextual Retrieval* post is the canonical source for the chunk-augmentation technique Huyen names as one of four production retrieval-optimization tactics. The exact Anthropic prompt for generating per-chunk context (see [[ContextualRetrieval]] for the full prompt) is reproduced verbatim in Ch 6 — making Anthropic the source of one of the four retrieval-optimization receipts the chapter develops.

Together, the two citations position Anthropic as **the most-prescriptive model lab on RAG-vs-no-RAG engineering decisions** — explicit threshold guidance + publishable production techniques, in contrast to the more research-paper-oriented contributions of other frontier labs.

