---
title: "AI Engineering Ch 10 — AI Engineering Architecture and User Feedback"
type: source
tags: [book, architecture, observability, user-feedback, ai-engineering, oreilly, ai-engineering-book]
date: 2024-12-04
source_file: raw/papers/ai-engineering/ch10-architecture-feedback.md
parent_source: ai-engineering-chip-huyen
---

# AI Engineering Ch 10 — AI Engineering Architecture and User Feedback

## Summary

Chapter 10 of [[ChipHuyen|Chip Huyen]]'s *AI Engineering* ([[OReilly|O'Reilly Media]], December 2024) is the book's **synthesis chapter**, structured in two halves: (1) a **step-by-step reference architecture** for production AI applications, built up component by component starting from a raw model call; and (2) a treatment of **user feedback** as both a product/UX surface and an evaluation/training signal. The architecture half walks five additive steps — [[ContextConstruction|context construction]] → [[Guardrail|guardrails]] → [[ModelRouter|router]] + [[ModelGateway|gateway]] → [[SemanticCache|caches]] → agentic patterns + [[WriteAction|write actions]] — interleaved with monitoring/[[observability|observability]] and [[AIPipelineOrchestration|pipeline orchestration]] as cross-cutting concerns. The chapter is unusual for being **anti-architecture-up-front**: each component is introduced only when the failure mode it solves becomes acute, and Huyen explicitly warns that adding components increases failure surface — *"each additional component can potentially make your system more capable, safer, or faster but will also increase the system's complexity."*

The **guardrails** subsection extends the [[ai-engineering-ch05-prompt-engineering|Ch 5]] [[InputGuardrail|input]] / [[OutputGuardrail|output]] dichotomy with concrete production tradeoffs: a **reliability-vs-latency tradeoff** that leads some teams to skip guardrails entirely (a stance Huyen says *"gave [early readers] nightmares"*); a stream-completion blind spot (output guardrails can't evaluate partial responses); a self-host vs API split (third-party APIs ship many guardrails out of the box); and an enumeration of named out-of-the-box solutions — [[PurpleLlama|Meta's Purple Llama]], [[NeMoGuardrails|NVIDIA NeMo Guardrails]], [[AzurePyRIT|Azure PyRIT]], Azure AI content filters, [[PerspectiveAPI|Perspective API]], [[openai|OpenAI]]'s content moderation API. The **[[PIIReverseDictionary|PII reverse dictionary]]** pattern is named explicitly: mask `[PHONE NUMBER]` before sending to a third-party API; restore from a reverse map on the response side. **Failure-handling policies** named: **retry** (cost: extra latency), **parallel calls** (cost: redundant API calls), and **human fallback** (transfer on anger/sentiment, transfer after N turns, transfer on sentinel phrases).

The **router** subsection introduces [[ModelRouter|model routing]] as cost-and-specialization optimization: an [[IntentClassifier|intent classifier]] (often a small adapted GPT-2 / BERT / Llama 7B, sometimes trained from scratch) dispatches to specialized models, declines out-of-scope queries with stock responses, and asks for clarification on ambiguous queries. Routers also act as **next-action predictors** in agentic settings — *"should the model use a code interpreter or a search API next?"* — or as **memory-tier selectors** for long-conversation memory hierarchies. The canonical AI-app pipeline is named: **routing → retrieval → generation → scoring**. The **[[ModelGateway|model gateway]]** subsection promotes the gateway to a first-class architectural component: a **unified-interface layer** wrapping self-hosted models and commercial APIs. Five gateway responsibilities are enumerated: unified interface (swap models without code change), access control / cost management (don't hand out org-wide API tokens), **fallback policies** (retry, route to alternate model, graceful degradation on API failure), load balancing / logging / analytics, and sometimes caching + guardrails. Named gateways: **[[Portkey|Portkey AI Gateway]]**, **MLflow AI Gateway**, **[[WealthsimpleLLMGateway|Wealthsimple's LLM Gateway]]**, **[[TrueFoundry|TrueFoundry]]**, **[[Kong|Kong]]**, **[[Cloudflare|Cloudflare]]**.

The **caching** subsection distinguishes [[KVCache|KV caching]] / [[PromptCaching|prompt caching]] (covered in [[ai-engineering-ch09-inference-optimization|Ch 9]], implemented by model providers) from **system caching**, which Huyen splits into [[ExactCache|exact caching]] and [[SemanticCache|semantic caching]]. Exact caching hits only on identical queries; storage options range from in-memory to Redis / Postgres / tiered with [[CacheReplacementPolicy|LRU/LFU/FIFO]] eviction. Many teams **train a classifier to predict whether a query should be cached** — user-specific (`"status of my recent order?"`) and time-sensitive (`"how's the weather?"`) queries shouldn't be. A footnote-grade **data-leak warning** is reproduced: if a cached "what is the return policy?" answer was personalized to user X's membership, returning it to user Y leaks X's information. **Semantic caching** uses embedding + vector search + a similarity threshold to match near-duplicate queries; Huyen is **explicitly skeptical** of it — *"semantic caching's value is more dubious because many of its components are prone to failure"* — citing embedding-quality risk, similarity-threshold tuning, and vector-search overhead (which can rival the cost of a fresh inference if the cache is large).

The **agent patterns** subsection collapses [[ai-engineering-ch06-rag-agents|Ch 6]] into a single architectural beat: feedback loops (response fed back into the system), parallel execution, conditional branching, and [[WriteAction|write actions]] (compose email, place order, initiate transfer) — and reiterates the Ch 6 safety warning that write actions *"should be done with the utmost care."* The **monitoring/observability** subsection borrows three DevOps metrics — **[[MTTD|MTTD]]** (mean time to detection), **[[MTTR|MTTR]]** (mean time to response), **[[ChangeFailureRate|CFR]]** (change failure rate) — and lays down a hard line: *"if you don't know your CFR, it's time to redesign your platform to make it more observable."* Huyen distinguishes **monitoring** (external-state tracking) from **observability** (internal-state inferrable from outputs) following the standard mid-2010s DevOps reframe. **Metrics** are split into format failures (easiest), open-ended generation quality (factual consistency, conciseness, creativity, positivity — often computed by [[LLMAsAJudge|AI judges]]), safety (toxicity, [[FalseRefusalRate|refusal rate]], abnormal queries), conversational signals (early-termination rate, average turns, average input/output tokens, output token distribution drift), latency ([[TTFT]] / [[TPOT]] / total), and cost (token volume, TPS, RPS). The **logs and traces** subsection lays down the rule *"the general rule for logging is to log everything"* — model API endpoint, model name, sampling settings (temperature, top-p, top-k, stopping), prompt template, user query, final prompt, output, intermediate outputs, tool calls and outputs, component start/end/crash events, all tagged with IDs. **[[RequestTrace|Traces]]** reconstruct request execution paths across components, surfaced in tools like [[LangSmith|LangSmith]] (visualized in Figure 10-11). **[[DriftDetection|Drift detection]]** is split into three sources: **system-prompt drift** (template updated by a coworker), **user-behavior drift** (users adapting their prompting style — the *self-driving-car-bullying* analogy), and **[[SilentModelUpdate|silent underlying-model drift]]** — Chen et al. (2023) on GPT-4 March/June diffs; [[Voiceflow]] reported a **10% performance drop** switching from `gpt-3.5-turbo-0301` to `gpt-3.5-turbo-1106`.

The **[[AIPipelineOrchestration|AI pipeline orchestration]]** subsection distinguishes AI-app orchestrators from general workflow orchestrators ([[Airflow]], [[Metaflow]]) and names two responsibilities: **components definition** (declare models, retrievers, tools) and **chaining** (function composition: query → retrieve → assemble prompt → generate → evaluate → return or escalate). Named orchestrators: [[LangChain]], [[LlamaIndex]], [[Flowise]], [[Langflow]], [[Haystack]]. Evaluation axes: **integration/extensibility, complex-pipeline support, ease of use/performance/scalability**. Huyen's start-simple stance applies — *"you might want to start building your application without one first … an orchestrator can abstract away critical details of how your system works, making it hard to understand and debug."*

The **user feedback** half opens with a strong product/strategy claim: *"user feedback is proprietary data, and data is a competitive advantage. A well-designed user feedback system is necessary to create the [[DataFlywheel|data flywheel]] discussed in Chapter 8."* The chapter then formalizes the [[ExplicitFeedback]] vs [[ImplicitFeedback]] distinction Huyen's earlier ML systems work already named — but extends it for the **conversational interface**, which makes feedback extractable from the text of dialogue itself. The taxonomy of **[[ConversationalFeedback|conversational feedback]]** has two layers: **[[NaturalLanguageFeedback|natural language feedback]]** (extracted from message content) and **[[ImplicitConversationalSignal|other conversational signals]]** (extracted from user actions). Natural-language signals include **early termination** (stop generation halfway, exit app, leave agent hanging), **error correction** (`"No, …"` / `"I meant, …"`), **rephrase attempts** (Figure 10-12), **action-correcting feedback** (`"Bill is the suspect, not the victim"`; `"you should also check XYZ's GitHub"`), **confirmation requests** (`"Are you sure?"`, `"Show me the sources"`), **user edits** of the model's output (especially strong as preference data — *each user edit makes up a preference example, with the original generated response being the losing response and the edited response being the winning response*), **complaints** (the [[FITSDataset|FITS dataset]] from Xu et al. 2022 has eight clusters: clarify-demand, irrelevant, point-to-sources, suggest-search, factually-incorrect, lacks-specificity, low-confidence, rude/repetitive), **sentiment** (`"Uggh"` — call centers track voice loudness), and the **[[RefusalRate|model's own refusal rate]]** as a feedback signal. Action-side signals include **regeneration** (`Cf. usage-based vs subscription billing — billing model affects signal strength`), **conversation organization** (delete = strong negative; rename = good content + bad title), **conversation length** (positive for AI companions, negative for productivity bots), and **dialogue diversity** (a long conversation with low diversity = stuck in a loop).

The **feedback-design** subsection covers **when** (initial calibration, error events, low-confidence model states) and **how** (Midjourney's upscale/vary/regen as Huyen's exemplar of good implicit-feedback design; [[GitHubCopilot|GitHub Copilot]]'s tab-to-accept as cheap-feedback ergonomics; standalone tools like [[openai|ChatGPT]] and [[anthropic|Claude]] suffering because they're not integrated into user workflow — Gmail can track if a draft was sent, ChatGPT can't). **[[InpaintingFeedback|Inpainting]]** is showcased as a model of **human-AI collaboration that simultaneously generates high-quality feedback**. Two opposing positions on **positive-feedback collection** are aired: Apple's HIG warns against asking for both positive and negative feedback (asking for good feedback signals that good outputs are exceptional); a counter-position holds that **positive feedback reveals which features users love enough to volunteer praise** — concentrating product effort on the small set of high-impact features. The **comparative-evaluation design** discussion notes Google Gemini's partial-response side-by-side (Figure 10-16) vs ChatGPT's full-response side-by-side; the better-or-worse data feeds [[PreferenceFinetuning|preference finetuning]]. **Visibility of signals** materially shapes their quality — public likes draw self-censorship; X (Twitter) making likes private in 2024 produced a reported uptick.

The **feedback limitations** subsection enumerates four bias families: **[[LeniencyBias|leniency bias]]** (Uber: average driver rating 4.8, below 4.6 = deactivation risk — five-star ratings reserved for default, four stars = something went wrong); **[[RandomFeedback|random feedback]]** (users click randomly to dispatch comparative-eval prompts they don't care about reading); **[[PositionBias|position bias]]** (the first suggestion gets clicked more — mitigated by position randomization or position-correcting model); **[[PreferenceBias|preference bias]]** + [[RecencyBias|recency bias]] (long-but-less-accurate wins; last-seen answer wins). The capstone failure mode is **[[DegenerateFeedbackLoop|degenerate feedback loops]]**: predictions influence the feedback that trains the next iteration, amplifying initial biases — *exposure bias / popularity bias / filter bubbles*. The cat-photo example: minor initial preference signal → system biases output → biased users self-select → feedback compounds → product is now a "cat haven." The final feedback-loop warning is **[[Sycophancy|sycophancy]]**: training on user feedback teaches the model to give users *what it thinks they want*, even when that's not what's most accurate or beneficial — Sharma et al. (2023) showed this empirically; Stray (2023) frames it as the **liar pathology** of feedback-trained agents.

The chapter closes with a synthesis statement that the book has been working toward: *"compared to traditional ML engineering, AI engineering is moving closer to product"* — both because the data flywheel makes feedback-system design an engineering responsibility, and because product experience itself becomes a competitive advantage when models are commodity.

## Key Claims

- **Production AI architecture is built additively, not designed up-front.** Huyen builds the reference architecture in five steps — context construction → guardrails → router+gateway → caches → agent patterns + write actions — each justified by a specific failure mode the prior architecture exhibits. Adding components increases capability *and* failure surface; the chapter recommends adding only what's earned.
- **Guardrails come with a reliability-vs-latency tradeoff that some teams refuse.** Output guardrails block streaming (you can't evaluate a partial response); input guardrails add latency. Some teams skip guardrails entirely to preserve TTFT — a stance Huyen flags as nightmare-inducing but real.
- **PII masking with a reverse dictionary is the canonical defense for sending data to third-party APIs.** Replace `phone-number → [PHONE NUMBER]` before egress; restore on ingress via a [[PIIReverseDictionary|reverse PII map]]. Detection tools are themselves often AI-powered (fuzzy match for "looks like an address"). The Samsung-leaked-into-ChatGPT footnote is the canonical motivating incident.
- **A [[ModelRouter|router]] is an [[IntentClassifier|intent classifier]] + dispatcher.** It can be implemented on top of foundation models (adapted GPT-2 / BERT / Llama 7B) or trained from scratch as a small classifier. The canonical AI-application pipeline is **routing → retrieval → generation → scoring**. Routers should be fast and cheap so multiple can be used without significant latency cost.
- **A [[ModelGateway|model gateway]] is a unified-interface layer with five responsibilities**: unified API (swap models without code changes), access control + cost management (don't share org-wide API keys), fallback policies (retry, route to alternate model), load balancing / logging / analytics, optionally caching + guardrails. Named: Portkey, MLflow AI Gateway, Wealthsimple LLM Gateway, TrueFoundry, Kong, Cloudflare.
- **Caching splits into [[ExactCache|exact]] and [[SemanticCache|semantic]]; semantic caching's value is dubious.** Exact caching is well-understood (LRU/LFU/FIFO eviction, Redis/Postgres backends, classifier-based cacheability prediction). Semantic caching depends on embedding quality, similarity-threshold tuning, and vector-search cost — often risk > reward.
- **Cached personalization is a data-leak vector.** Caching a "what's the return policy?" response that was personalized to user X's membership and serving it to user Y leaks X's information. Caching layer must distinguish personalized vs generic responses.
- **Observability requires three DevOps metrics: [[MTTD]], [[MTTR]], [[ChangeFailureRate|CFR]].** *"If you don't know your CFR, it's time to redesign your platform to make it more observable."* Evaluation metrics should translate to monitoring metrics; issues found in monitoring should feed back to evaluation.
- **The logging rule is "log everything."** Model API endpoint, model name, sampling parameters (temperature, top-p, top-k, stopping condition), prompt template, user query, final prompt, output, intermediate outputs, tool calls, tool outputs, component lifecycle events. All tagged with IDs to enable [[RequestTrace|tracing]].
- **Drift comes from three sources: system-prompt drift, user-behavior drift, and silent underlying-model drift.** Voiceflow reported a **10% performance drop** switching from `gpt-3.5-turbo-0301` to `gpt-3.5-turbo-1106`. Chen et al. (2023) documented GPT-4 March vs June 2023 behavior diffs without a version bump on the API.
- **The conversational interface enables a new feedback category: [[NaturalLanguageFeedback|natural-language feedback]].** Extracted from the *content* of user messages — error corrections, rephrases, complaints, confirmation requests, sentiment, action-correcting nudges — and from the model's own behavior (refusal rate). Implicit, abundant, but noisier than explicit feedback.
- **User edits are the strongest implicit signal and double as [[PreferenceData|preference data]].** *"Each user edit makes up a preference example, with the original generated response being the losing response and the edited response being the winning response."*
- **Standalone AI products are at a structural feedback disadvantage.** GitHub Copilot can see whether a suggestion was accepted (tab = yes, continue typing = no); ChatGPT can't see whether a drafted email was actually sent. Integrated products win the feedback flywheel.
- **[[InpaintingFeedback|Inpainting]] is the model design of human-AI collaboration.** Users get a better output and developers get high-quality region-level feedback as a byproduct. Huyen wishes text-to-speech had this affordance for fixing pronunciation in 5% of generations.
- **Apple's HIG warns against asking for positive feedback, but product managers disagree.** Asking for good feedback can imply good outputs are exceptional; alternatively, positive feedback reveals the small set of features users love enough to volunteer praise about — concentrating product investment. The chapter doesn't resolve this — it presents both.
- **The four feedback biases to design around: [[LeniencyBias|leniency]], randomness, [[PositionBias|position]], [[PreferenceBias|preference]] (incl. [[RecencyBias|recency]] and length).** Uber's average driver rating of 4.8 (deactivation below 4.6) is the canonical leniency illustration.
- **[[DegenerateFeedbackLoop|Degenerate feedback loops]] can destroy a product.** Initial small preference signal → system over-amplifies → user base self-selects → preference compounds → product drift. *"Exposure bias / popularity bias / filter bubbles."* Mechanism applies to cat photos and to racism, sexism, explicit content.
- **Feedback-trained models become [[Sycophancy|sycophantic]].** Sharma et al. (2023): models trained on human feedback present user-flattering responses. Stray (2023) frames this as feedback turning a conversational agent into a **liar**. The bias toward what users *want to hear* over what's accurate is the central failure mode of naive feedback-as-training-data.
- **AI engineering is moving closer to product.** The chapter's closing reframe: feedback-system design used to be a product responsibility, ignored by engineers. The data-flywheel logic now makes it an engineering responsibility too — *"more AI engineers are now becoming involved in the process to ensure they receive the data they need."*

## Key Quotes

> "Context construction is like feature engineering for foundation models." — Ch 10 (reprised from Ch 6)

> "A few early readers told me that the idea of ignoring guardrails in favor of latency gave them nightmares." — Ch 10, footnote on the reliability-vs-latency tradeoff

> "If you don't know your CFR, it's time to redesign your platform to make it more observable." — Ch 10

> "The general rule for logging is to log everything." — Ch 10

> "Each user edit makes up a preference example, with the original generated response being the losing response and the edited response being the winning response." — Ch 10

> "User feedback is proprietary data, and data is a competitive advantage. A well-designed user feedback system is necessary to create the data flywheel discussed in Chapter 8." — Ch 10

> "Don't ask users to do the impossible. … For mathematical questions like this, the right answer shouldn't be a matter of preference." — Ch 10, on the design failure of asking users to choose between two math answers they can't evaluate

> "User feedback is crucial for improving user experience, but if used indiscriminately, it can perpetuate biases and destroy your product." — Ch 10

> "Compared to traditional ML engineering, AI engineering is moving closer to product. This is because of both the increasing importance of data flywheel and product experience as competitive advantages." — Ch 10, closing thesis

> "Many AI challenges are, at their core, system problems. To solve them, it's often necessary to step back and consider the system as a whole." — Ch 10, final paragraph

## Concepts

### New (minted by this chapter)

- [[ModelGateway]] — unified-interface layer wrapping model APIs with access control, cost management, fallback, load balancing, logging, optional caching + guardrails
- [[ModelRouter]] — intent-classifier-plus-dispatcher that routes queries to the appropriate model / pipeline / fallback
- [[ExactCache]] — system-cache layer that hits only on identical queries; LRU/LFU/FIFO eviction; Redis/Postgres/in-memory backends
- [[SemanticCache]] — vector-search-based cache that hits on semantically-similar queries; Huyen is skeptical of its cost/benefit
- [[PIIReverseDictionary]] — masking pattern that replaces PII with placeholders (e.g., `[PHONE NUMBER]`) before egress and restores via a reverse map on ingress
- [[RequestTrace]] — reconstructed timeline of a single request's execution path across pipeline components; the trace counterpart to log entries
- [[MTTD]] — mean time to detection; DevOps observability metric
- [[MTTR]] — mean time to response; DevOps observability metric
- [[ChangeFailureRate]] — CFR; percentage of deployments that result in failures requiring fixes or rollbacks
- [[DriftDetection]] — observability sub-discipline catching system-prompt drift, user-behavior drift, and silent underlying-model drift
- [[SilentModelUpdate]] — model-provider behavior change behind a fixed API endpoint (Voiceflow's 10% drop on `gpt-3.5-turbo-0301 → -1106`; Chen et al. 2023 on GPT-4)
- [[AIPipelineOrchestration]] — AI-app-specific pipeline orchestration distinct from general workflow orchestrators like [[Airflow]] / [[Metaflow]]
- [[ConversationalFeedback]] — umbrella for feedback extracted from a conversational interface; covers natural-language and action-side signals
- [[NaturalLanguageFeedback]] — feedback inferred from the content of user messages (corrections, complaints, rephrases, sentiment)
- [[ImplicitConversationalSignal]] — feedback inferred from user actions (regeneration, deletion, conversation length, dialogue diversity)
- [[RephraseAttempt]] — user repeats their request in different wording, signaling that the model misunderstood
- [[ErrorCorrection]] — user starts a follow-up with `"No, …"` / `"I meant, …"`; the strongest natural-language failure signal
- [[ActionCorrectingFeedback]] — user nudges an agent to take a specific additional action (`"check XYZ's GitHub"`)
- [[UserEditFeedback]] — direct user edit of model output; doubles as preference data (original = loser, edit = winner)
- [[RegenerationSignal]] — user requests a fresh generation of the same prompt; weak negative signal, modulated by billing model (usage-based vs subscription)
- [[InpaintingFeedback]] — region-level user edit on image (or any structured) outputs; the chapter's design exemplar of human-AI collaboration producing high-quality feedback as a byproduct
- [[FITSDataset]] — Feedback for Interactive Talk & Search dataset (Xu et al. 2022); eight clustered feedback-complaint types
- [[LeniencyBias]] — feedback bias toward over-positive ratings; Uber's 4.8 average driver rating is the canonical illustration
- [[PositionBias]] — user clicks the first option more often regardless of quality
- [[PreferenceBias]] — feedback bias toward longer / last-seen / familiar options
- [[DegenerateFeedbackLoop]] — predictions influence the feedback that trains the next iteration; exposure bias / popularity bias / filter bubbles
- [[Sycophancy]] — feedback-trained model gives users what it thinks they want over what's accurate; Sharma et al. 2023; Stray 2023 frames as the "liar" pathology

### Existing (referenced, extended where noted)

- [[Guardrail]] / [[InputGuardrail]] / [[OutputGuardrail]] — Ch 5 introduced the dichotomy; Ch 10 extends with reliability-vs-latency tradeoff, stream-completion blind spot, named OOTB solutions
- [[ContextConstruction]] — reprised as Step 1 of the architecture
- [[IntentClassifier]] — Ch 6 introduced; Ch 10 extends with the routing-and-dispatch instantiation
- [[KVCache]] / [[PromptCaching]] — Ch 9 deep-dive; Ch 10 places them as Model-API-layer caching distinct from system caching
- [[WriteAction]] — Ch 6 introduced; Ch 10 reinforces the safety thesis
- [[Agent]] / [[AgenticAI]] — Ch 6 backbone; Ch 10 places agent patterns as the architecture's complexity ceiling
- [[Orchestrator]] — wiki's existing MLOps-pipeline orchestrator page; Ch 10's AI-pipeline orchestrator is the LLM-app-specific sibling
- [[Hallucination]] — recurring failure mode metrics are designed around
- [[FalseRefusalRate]] — Ch 5 introduced; Ch 10 reuses as a monitoring metric
- [[DataFlywheel]] — Ch 8 introduced; Ch 10 supplies the feedback-system mechanics
- [[ExplicitFeedback]] / [[ImplicitFeedback]] — already in wiki from recommender-systems literature; Ch 10 extends to the conversational-interface setting
- [[PreferenceFinetuning]] / [[PreferenceModel]] — feedback-extracted preferences feed here
- [[FirstPositionBias]] / [[RecencyBias]] / [[VerbosityBias]] — wiki's existing bias entries; Ch 10 surfaces the user-facing analogues (position bias, recency bias, preference-for-length)
- [[Latency]] / [[TTFT]] / [[TPOT]] — Ch 9 vocabulary reused as monitoring metrics
- [[BusinessMetric]] / [[EngagementMetric]] / [[StickinessMetric]] — wiki's existing north-star metric pages; Ch 10 advocates correlating model metrics against these
- [[UsagePatternMonitoring]] — Ch 5's behavior-over-time defense; Ch 10's monitoring section is its observability sibling
- [[observability]] / [[Monitoring]] / [[ModelMonitoring]] — wiki stubs filled in by this chapter
- [[Logging]] / [[StructuredLogging]] — wiki stubs the "log everything" rule reinforces

## Entities

### New (minted by this chapter)

- [[Portkey]] — AI Gateway provider
- [[TrueFoundry]] — AI/ML platform with gateway component
- [[Kong]] — API gateway company; can serve as model gateway
- [[Cloudflare]] — CDN/platform with AI gateway product
- [[WealthsimpleLLMGateway]] — Wealthsimple's open-source LLM gateway
- [[PurpleLlama]] — Meta's safety-tools umbrella (Llama Guard + companions)
- [[PerspectiveAPI]] — Jigsaw/Google API for toxicity scoring
- [[Flowise]] — visual LLM-app orchestrator
- [[Langflow]] — visual LLM-app orchestrator
- [[Haystack]] — deepset's RAG/orchestration framework
- [[FITSDataset]] — Xu et al. 2022 feedback dataset (also listed under concepts as a named-dataset concept)
- [[GoogleGemini]] — referenced as showing partial-response side-by-side comparative feedback (Figure 10-16) — minted only if not already present as `gemini`

### Existing (referenced)

- [[ChipHuyen]] — author
- [[OReilly]] — publisher
- [[openai|OpenAI]] — content moderation API; ChatGPT
- [[anthropic|Anthropic]] — Claude
- [[meta|Meta]] — Purple Llama, Llama Guard
- [[NVIDIA]] — NeMo Guardrails
- [[AzurePyRIT]] — Azure red-teaming toolkit
- [[NeMoGuardrails]] — concept + entity
- [[GuardrailsAI]] — concept + entity
- [[LangChain]] / [[LlamaIndex]] — named orchestrators
- [[LangSmith]] — request-trace visualization (Figure 10-11)
- [[MLflow]] — MLflow AI Gateway
- [[Airflow]] / [[Metaflow]] — general workflow orchestrators contrasted with AI-app orchestrators
- [[Midjourney]] — feedback-design exemplar (upscale/vary/regen)
- [[GitHubCopilot]] — feedback-design exemplar (tab-to-accept)
- [[DALLE|DALL-E]] — inpainting example (Figure 10-14)
- [[Voiceflow]] — silent-model-update incident (10% drop on GPT-3.5 turbo version bump)
- [[Spotify]] / [[Amazon]] (Alexa) / Yahoo! — early conversational-AI natural-language-feedback research sites
- [[Apple]] — Human Interface Guidelines stance against asking for both positive and negative feedback
- [[gemini|Google Gemini]] — partial side-by-side comparative feedback (Figure 10-16); existing entity page

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — guardrail dichotomy, refusal-rate / false-refusal-rate metric, PII masking, defensive prompt engineering
- [[ai-engineering-ch06-rag-agents]] — context construction, intent classifier, agent patterns, write actions, tool-output sanitization
- [[ai-engineering-ch08-dataset-engineering]] — data flywheel; feedback-system design supplies the data the flywheel runs on
- [[ai-engineering-ch09-inference-optimization]] — KV cache, prompt cache, TTFT/TPOT, batching; Ch 10's system-cache section explicitly distinguishes itself from Ch 9's inference cache
- [[ai-engineering-ch03-evaluation-methodology]] / [[ai-engineering-ch04-evaluate-ai-systems]] — evaluation-monitoring coupling; *"evaluation metrics should translate well to monitoring metrics"*
- [[ai-engineering-ch01-intro]] — AI engineering moving closer to product is a callback to Ch 1's discipline-definition argument
- [[DataFlywheel]] / [[AIProductDefensibility]] — strategic logic of feedback-as-data-moat
- [[DefensivePromptEngineering]] / [[Jailbreak]] / [[IndirectPromptInjection]] — what the guardrail layer defends against
- [[CustomerServiceAgent]] — Ch 10's router-with-human-fallback worked example is structurally a customer-service agent

## Contradictions

- **Positive-feedback collection**: Apple's HIG says no, the product managers Huyen interviews say yes. Ch 10 *presents the disagreement without resolving it* — this is a contradiction *within the chapter*, not against the prior wiki. Worth flagging because the wiki's [[DataFlywheel]] page leans toward "collect everything" and the Apple-HIG counter-position deserves its own discoverable home.
- **Stream completion + output guardrails**: Ch 10 states output guardrails *"might not work well in the stream completion mode"* because partial responses are hard to evaluate. This is a real practical limit not contradicted but also not surfaced in [[OutputGuardrail]]'s current page (which describes a single-shot evaluation model). Worth appending — see updates below.
- No direct contradictions with prior chapters of the same book. Ch 10's [[ImplicitFeedback]] extension explicitly *extends* the recommender-systems framing already in the wiki rather than overriding it.

## Notable omissions

- **Tool gateway** is named in passing as a useful but uncommon pattern ("not discussed in this book since it's not a common pattern as of this writing") — left to a future revision.
- **Text-to-speech inpainting** is a Huyen wishlist item ("I wish there were inpainting for text-to-speech") rather than an existing technique — noted as an aspirational design direction.
- **Quantitative cost/benefit numbers for guardrails** are not provided. The chapter is qualitative about the latency-vs-reliability tradeoff; teams have to measure on their own workload.
- **Concrete sycophancy mitigation** is left underspecified — Ch 10 names the failure mode (Sharma et al. 2023, Stray 2023) but doesn't prescribe a mitigation beyond "understand the limitations of this feedback before incorporating it."
