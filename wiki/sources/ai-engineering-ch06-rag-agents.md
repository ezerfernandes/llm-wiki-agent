---
title: "AI Engineering Ch 6 — RAG and Agents"
type: source
tags: [book, rag, agents, ai-engineering, oreilly, ai-engineering-book]
date: 2024-12-04
source_file: raw/papers/ai-engineering/ch06-rag-agents.md
parent_source: ai-engineering-chip-huyen
---

# AI Engineering Ch 6 — RAG and Agents

## Summary

Chapter 6 of [[ChipHuyen|Chip Huyen]]'s *AI Engineering* ([[OReilly|O'Reilly Media]], 2024) develops the two dominant patterns for **giving foundation models external information at inference time**: [[rag|RAG]] and [[Agent|agents]]. Huyen frames RAG as a *"technique to construct context specific to each query, instead of using the same context for all queries"*, and explicitly positions it as the **foundation-model-era analogue of feature engineering** for classical ML. The chapter rejects the *"long context kills RAG"* thesis on two grounds: (1) application data outgrows any fixed context length (Huyen's *"Parkinson's Law for context"* footnote), and (2) [[ContextLength|long-context]] efficiency degrades — *"the longer the context, the more likely the model is to focus on the wrong part."*

The **RAG architecture** section splits the retriever into **indexing** and **querying** and develops two retrieval-algorithm families. **Term-based retrieval** ([[TermBasedRetrieval]]) — represented by [[TFIDF|TF-IDF]] and [[BM25|Okapi BM25]] (Robertson et al. 1980s), implemented via inverted indexes in [[Elasticsearch]]/[[Lucene]] — scores documents by term-frequency × inverse-document-frequency, with BM25 adding length normalization. **Embedding-based / semantic retrieval** ([[EmbeddingBasedRetrieval]]) maps both queries and documents into a vector space (the [[VectorDatabase]]) and ranks by cosine similarity, with [[ApproximateNearestNeighbor|ANN]] algorithms — [[LSH]], [[HNSW]], [[ProductQuantization]], [[IVF|inverted file index]], [[Annoy]], [[FAISS]], [[ScaNN]], Hnswlib, Milvus — replacing brute-force k-NN at scale. The chapter rejects the textbook **sparse-vs-dense** division (citing [[SPLADE]] as the counterexample — sparse embeddings that behave like dense retrieval) in favor of **term-based vs embedding-based**. **Hybrid search** ([[HybridSearch]]) combines the two — sequentially (cheap term-based fetch → expensive embedding rerank) or in parallel via [[ReciprocalRankFusion|reciprocal rank fusion]] (Cormack et al. 2009).

Retrieval is evaluated by **[[ContextPrecision|context precision]]** (of retrieved, what fraction is relevant?) and **[[ContextRecall|context recall]]** (of relevant, what fraction is retrieved?), with [[NDCG]] / [[MAP]] / [[MRR]] for rank-sensitive evaluation, [[MTEB]] for embedding-quality benchmarking, and [[BEIRBenchmark|BEIR]] (Thakur et al. 2021) for retrieval-system benchmarking across 14 tasks; [[ANNBenchmarks|ANN-Benchmarks]] compares index algorithms by recall / QPS / build-time / index-size.

The **retrieval optimization** section names four production tactics: **[[ChunkingStrategy|chunking strategy]]** (fixed-length / recursive / token-based / language-specific / Q&A-aware; overlap to prevent boundary cutoff), **[[ReRanking|reranking]]** (including [[TimeBasedReranking|time-weighted]] for news / email / stock), **[[QueryRewriting|query rewriting]]** (a.k.a. query reformulation / expansion / normalization — disambiguating *"How about Emily Doe?"* against conversation history, with identity-resolution edge cases), and **[[ContextualRetrieval|contextual retrieval]]** ([[anthropic|Anthropic]] 2024 — augment each chunk with AI-generated 50–100-token explanatory context, plus metadata, tags, and *"questions this chunk can answer"*). **RAG beyond text** covers **[[MultimodalRAG|multimodal RAG]]** (using [[CLIP]]-style joint embeddings to retrieve both text and images for the same query) and **[[RAGOverTabularData|RAG with tabular data]]** via **[[TextToSQL|text-to-SQL]]** (LM generates SQL → SQL executor runs it → LM generates final response).

The **agents** section opens with the [[StuartRussell]]–[[PeterNorvig]] definition (*"anything that can perceive its environment and act upon that environment"*) and decomposes an agent into **environment** + **tool inventory** + **AI planner**. Concrete worked example: a Kitty Vogue ecommerce agent runs an 8-step reason-act-reflect loop against an SQL tool. The chapter introduces two empirical risks for multi-step agents: **[[CompoundErrorAccumulation|compound mistakes]]** (95% per-step → 60% after 10 steps → 0.6% after 100 steps) and **higher stakes** (write actions can do real damage). **Tools** are categorized into three families: **[[KnowledgeAugmentation|knowledge augmentation]]** (retrievers, [[WebBrowsingTool|web browsing]], Slack/email/inventory APIs), **[[CapabilityExtension|capability extension]]** (calculator, code interpreter, image captioner, OCR, [[DALLE|DALL-E]], LaTeX compiler, translator), and **[[WriteAction|write actions]]** (SQL writes, email sends, bank transfers — *"You shouldn't allow an unreliable AI to initiate bank transfers."*). The chapter cites [[Chameleon]] (Lu et al. 2023) — a 13-tool GPT-4 agent that improves [[ScienceQA]] by +11.37% and TabMWP by +17%.

**Planning** is presented as the agent's hardest subsystem. Huyen develops the **decouple-planning-from-execution** pattern (validate the plan before running it; reject invalid-action plans, plans-too-long, or AI-judge-rejected plans), names the **[[IntentClassifier|intent classifier]]** as a planner companion that routes queries and rejects [[IRRELEVANTClass|IRRELEVANT]] tasks, and decomposes the full process into **plan-generate → reflect → execute → reflect**. She surveys the LLMs-can't-plan debate (citing [[YannLeCun|LeCun 2023]] and [[SubbaraoKambhampati|Kambhampati 2023]]'s *"LLMs extract planning knowledge but can't make executable plans"* critique), notes that **planning is fundamentally search with backtracking**, and credits Hao et al. 2023 ([[ReasoningWithLanguageModelIsPlanningWithWorldModel|RAP]]) with showing how an LLM's internal world model can be plumbed into the search. **Foundation Model vs RL planners** are contrasted in a sidebar — RL trains the planner, FM is the planner; the author predicts they'll merge. **Plan generation** receipts include system-prompt examples with `get_today_date()` / `fetch_top_products()` / `fetch_product_info()` / `generate_query()` / `generate_response()` action lists, the **[[FunctionCalling|function-calling]]** API surface (with `required`/`none`/`auto` tool-use modes; the canonical `lbs_to_kg(40)` example), the **[[PlanningGranularity|planning-granularity]] trade-off** (exact-function-name plans vs natural-language plans + translator/program-generator), and **[[ControlFlow|complex control flows]]** (sequential / parallel / if-statement / for-loop — AI-determined, harder than software-engineering control flow).

**Reflection and error correction** introduces [[react|ReAct]] (Yao et al. 2022) as the canonical *Thought-Act-Observation* interleaving pattern (HotpotQA worked example), and [[reflexion|Reflexion]] (Shinn et al. 2023) as the evaluator + self-reflection split that generates new "trajectories" after failure. Huyen notes the [[ActorCriticAgent|actor-critic]] (Konda & Tsitsiklis 1999) RL ancestry. **Tool selection** surveys the wide range of tool-inventory sizes ([[Toolformer]] 5 / [[Chameleon]] 13 / [[Gorilla]] 1,645 APIs), names diagnostic techniques (ablation studies, tool-call-distribution plots, tool-transition trees), and cites [[VoyagerAgent|Voyager]] (Wang et al. 2023) for **AI-created skills** — a skill manager that stores successful action-sequences as reusable code-tools in a vector database.

**Agent failure modes and evaluation** names three families: **[[PlanningFailure|planning failures]]** (invalid tool / valid tool with invalid parameters / valid tool with wrong parameter values; **[[GoalFailure|goal failures]]**; **[[ReflectionFailure|reflection failures]]** — agent insists task is done when it isn't); **[[ToolFailure|tool failures]]** (tool returns wrong output; translation errors; missing tool for the domain); and **[[AgentEfficiency|efficiency failures]]** (step count / cost / per-action latency). The chapter cites the **[[BerkeleyFunctionCallingLeaderboard|Berkeley Function Calling Leaderboard]]**, the **[[AgentOpsEvalHarness|AgentOps evaluation harness]]**, and the **[[TravelPlannerBenchmark|TravelPlanner benchmark]]** as agent benchmarks.

The **memory** section closes the chapter with a three-tier model: **[[InternalKnowledgeMemory|internal knowledge]]** (the model weights — fixed except by retraining), **[[ShortTermMemory|short-term memory]]** (the context window — fast, capacity-limited, per-query), and **[[LongTermMemory|long-term memory]]** (external stores — RAG-retrievable, persistent across sessions). Huyen lists four benefits of an explicit memory system (overflow management, cross-session persistence, consistency, structural integrity), names two operations (memory management = add/delete; memory retrieval = RAG-style query), and surveys management strategies: **[[FIFOMemory|FIFO]]** (OpenAI / [[LangChain]] N-last-messages — fast but loses purpose-of-conversation messages), **[[SummarizationMemory|summarization-based]]** memory (Bae et al. 2022 — classifier decides per-sentence whether to keep summary, original, both, or neither), and **[[ReflectionMemory|reflection-based]]** memory (Liu et al. 2023 — agent decides per-action whether to insert, merge, or replace existing memory, especially on contradictions).

## Key Claims

- **RAG = per-query context construction.** *"You can think of RAG as a technique to construct context specific to each query, instead of using the same context for all queries."*
- **Context construction is the foundation-model equivalent of feature engineering.** Both *"serve the same purpose: giving the model the necessary information to process an input."*
- **Long context does not kill RAG.** Two reasons: data grows faster than context limits ([[ParkinsonsContextLaw|Parkinson's Law for context]]), and long contexts have efficiency penalties — *"the longer the context, the more likely the model is to focus on the wrong part of the context."*
- **[[anthropic|Anthropic]]'s long-context-vs-RAG threshold**: *"if your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt that you give the model, with no need for RAG."*
- **A RAG system has two components: retriever + generator.** Retriever has two functions: **indexing** and **querying**.
- **End-to-end finetuning of RAG can significantly improve performance** — the original Lewis et al. paper trained retriever + generator jointly; today's systems usually train them separately.
- **Term-based vs embedding-based is the right division, not sparse vs dense.** [[SPLADE]] (Formal et al. 2021) is the counterexample — sparse embeddings whose behavior matches dense retrieval.
- **BM25 is a formidable baseline.** Quoting [[AravindSrinivas]] (CEO of [[Perplexity]]): *"Making a genuine improvement over BM25 or full-text search is hard."*
- **The embedding-based-vs-term-based trade-off**: term-based is faster and cheaper out of the box but hard to improve; embedding-based is more expensive but can be finetuned to outperform — at the cost of obscuring keywords like error codes (`EADDRNOTAVAIL`) or product names.
- **Vector DB spending can rival API spending.** *"It's not uncommon to see a company's vector database spending be one-fifth or even half of their spending on model APIs."*
- **A RAG system should be evaluated three ways**: retrieval quality, final RAG outputs, and embeddings (for embedding-based retrieval).
- **Hybrid search = sequential or parallel combination.** Sequential = cheap fetch then expensive rerank; parallel = multiple retrievers → [[ReciprocalRankFusion|RRF]] with `k=60` constant.
- **Chunking trade-offs**: smaller chunks → more diversity but lose continuity; larger chunks → more context but lower recall; no universal best chunk size — experiment.
- **Contextual retrieval** ([[anthropic|Anthropic]] 2024): prepend each chunk with an LM-generated 50–100-token *"situate this chunk within the document"* context before embedding.
- **An agent = environment + tool inventory + AI planner.** ChatGPT, RAG systems, and SWE-agent (Yang et al. 2024) are all agents.
- **Compound mistakes are the planning tax.** At 95% per-step accuracy: 60% after 10 steps, 0.6% after 100 steps. Agents need more powerful models than non-agent applications for this reason.
- **Tool inventory determines capability ceiling, but more tools also means harder selection.** [[Toolformer]] uses 5 tools; [[Chameleon]] 13; [[Gorilla]] 1,645 APIs.
- **Function calling = tool use API.** Most providers expose it with `required` / `none` / `auto` modes. The API guarantees valid function names but not correct parameter values.
- **Planning should be decoupled from execution.** Validate plans (via heuristics or AI judge) *before* executing — avoids 1,000-step fruitless loops.
- **[[YannLeCun|LeCun]] and [[SubbaraoKambhampati|Kambhampati]] argue autoregressive LLMs can't plan.** Huyen's stance: unclear whether LLMs fundamentally can't plan or just haven't been given the right scaffolding (search + world model + state tracking).
- **Planning is fundamentally search with backtracking.** [[ReasoningWithLanguageModelIsPlanningWithWorldModel|Hao et al. 2023]] argue an LLM's internal world model can be plumbed into the search.
- **Reflection is cheap relative to plan generation and brings surprisingly large performance gains.** [[react|ReAct]] (Yao et al. 2022) interleaves Thought-Act-Observation; [[reflexion|Reflexion]] (Shinn et al. 2023) splits reflection into evaluator + self-reflection modules.
- **Use natural-language plans instead of exact function names.** More robust to tool-API changes; weaker translator model converts to executable commands.
- **Different agent frameworks favor different tool categories.** [[AutoGPT]] focuses on social media APIs ([[Reddit]], X, [[Wikipedia]]); [[Composio]] focuses on enterprise APIs ([[google|Google Apps]], [[GitHub]], [[Slack]]).
- **[[VoyagerAgent|Voyager]] (Wang et al. 2023) demonstrates AI-created tools.** Successful skills (coding programs) are added to a skill library and retrieved for reuse — a tool inventory that grows over time.
- **Three agent failure families**: planning failures (invalid tool / invalid params / wrong values / goal failure / reflection error), tool failures (wrong output / translation error / missing tool), efficiency failures (steps / cost / latency).
- **Memory has three tiers**: internal knowledge (weights), short-term (context), long-term (RAG-retrievable external).
- **[[FIFOMemory|FIFO]] memory management is dangerous when early messages carry the purpose** — *"the earliest messages might carry the most information, especially when the early messages state the purpose of the conversation."*
- **RAG is a special case of agent.** *"The RAG pattern can be seen as a special case of agent where the retriever is a tool the model can use."*

## Key Quotes

> "You can think of RAG as a technique to construct context specific to each query, instead of using the same context for all queries." — p. 254

> "Context construction for foundation models is equivalent to feature engineering for classical ML models." — p. 254

> "No matter how long a model's context length is, there will be applications that require context longer than that. ... I have a similar theory that an application's context expands to fill the context limit supported by the model it uses." — Parkinson's-context footnote, p. 255

> "If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt." — [[anthropic|Anthropic]] 2024, quoted p. 256

> "Making a genuine improvement over BM25 or full-text search is hard." — [[AravindSrinivas]] (CEO of [[Perplexity]]), p. 260

> "It's not uncommon to see a company's vector database spending be one-fifth or even half of their spending on model APIs." — p. 265

> "If the model's accuracy is 95% per step, over 10 steps, the accuracy will drop to 60%, and over 100 steps, the accuracy will be only 0.6%." — compound-error math, p. 278

> "Just as you shouldn't give an intern the authority to delete your production database, you shouldn't allow an unreliable AI to initiate bank transfers." — write-action safety, p. 281

> "The agent might assign only 40 people and insist that the task has been accomplished." — reflection-failure illustration, p. 299

> "The RAG pattern can be seen as a special case of agent where the retriever is a tool the model can use." — Summary, p. 305

## Concepts Introduced or Engaged

- [[rag|RAG]] — *engaged*, deep dive of the previously stub-level entry.
- [[Agent]] — *engaged*, the LLM-agent meaning (distinct from the existing OPM-original [[Agent]] page); this chapter populates Huyen's framing.
- [[AgenticAI]] / [[multiagentsystems]] — *engaged*, broader paradigm.
- [[TermBasedRetrieval]] — *new*, the term-frequency family of retrieval algorithms.
- [[EmbeddingBasedRetrieval]] — *new*, the semantic / vector-search retrieval family.
- [[TFIDF]] — *new*, the term-frequency × inverse-document-frequency scoring function.
- [[BM25]] — *engaged*, sharpened (length-normalized TF-IDF; Robertson et al. 1980s).
- [[InvertedIndex]] — *new*, the dictionary-of-term-to-documents data structure under [[Elasticsearch]] / [[Lucene]].
- [[SPLADE]] — *new*, Formal et al. 2021 sparse-lexical retrieval — counterexample to sparse-vs-dense division.
- [[ApproximateNearestNeighbor]] — *new*, ANN family of algorithms.
- [[HNSW]] — *new*, Malkov & Yashunin 2016 multi-layer-graph ANN.
- [[LSH]] — *new*, Indyk & Motwani 1999 locality-sensitive hashing.
- [[ProductQuantization]] — *new*, Jégou et al. 2011.
- [[IVF]] — *new*, Sivic & Zisserman 2003 inverted-file-index ANN.
- [[Annoy]] — *new*, Spotify's tree-based ANN.
- [[FAISS]] — *new*, Facebook's vector-search library (Johnson et al. 2017).
- [[ScaNN]] — *new*, Google's vector-search library (Sun et al. 2020).
- [[ReciprocalRankFusion]] — *new*, Cormack et al. 2009 — combines rankings from multiple retrievers.
- [[HybridSearch]] — *engaged*, sharpened with Huyen's sequential vs parallel framing.
- [[ContextPrecision]] — *new*, retrieval evaluation metric: relevant fraction of retrieved.
- [[ContextRecall]] — *new*, retrieval evaluation metric: retrieved fraction of relevant.
- [[NDCG]] / [[MAP]] / [[MRR]] — *new*, rank-sensitive retrieval metrics.
- [[BEIRBenchmark]] — *new*, Thakur et al. 2021 retrieval-system benchmark across 14 datasets.
- [[ANNBenchmarks]] — *new*, comparison harness for ANN libraries by recall / QPS / build-time / index-size.
- [[MTEB]] — *engaged*, the embedding-quality benchmark.
- [[ChunkingStrategy]] — *engaged*, sharpened with fixed-length / recursive / token-based / language-specific variants.
- [[ReRanking]] — *engaged*, sharpened with time-weighted variant.
- [[QueryRewriting]] — *new*, a.k.a. reformulation / normalization / expansion.
- [[ContextualRetrieval]] — *new*, [[anthropic|Anthropic]] 2024 — prepend LM-generated context to each chunk.
- [[MultimodalRAG]] — *new*, RAG with image/video/audio sources retrieved via joint embeddings (e.g. [[CLIP]]).
- [[RAGOverTabularData]] — *new*, the text-to-SQL-style RAG variant.
- [[TextToSQL]] — *new*, semantic parsing from natural language to SQL.
- [[ToolInventory]] — *new*, the set of tools an agent has access to.
- [[FunctionCalling]] — *new*, the model-provider API surface for tool use.
- [[KnowledgeAugmentation]] — *new*, the tool family that gives the agent access to data.
- [[CapabilityExtension]] — *new*, the tool family that addresses model deficiencies (calculator, code interpreter, OCR, translator).
- [[WriteAction]] — *new*, tools that mutate state (vs read-only).
- [[WebBrowsingTool]] — *new*, the umbrella for internet-access tools.
- [[CodeInterpreter]] — *new*, executes generated code on behalf of the agent.
- [[CompoundErrorAccumulation]] — *new*, the 95%-per-step → 60%-over-10-steps decay.
- [[PlanningGranularity]] — *new*, the level of detail in a generated plan.
- [[ControlFlow]] — *engaged*, generalized to AI-determined sequential / parallel / if-statement / for-loop.
- [[IntentClassifier]] — *new*, planning companion that routes queries and rejects IRRELEVANT tasks.
- [[ReasoningWithLanguageModelIsPlanningWithWorldModel]] — *new*, Hao et al. 2023 — LLM as world model for planning.
- [[Chameleon]] — *new*, Lu et al. 2023 — 13-tool GPT-4-powered agent.
- [[Toolformer]] — *new*, Schick et al. 2023 — GPT-J finetuned for 5 tools.
- [[Gorilla]] — *new*, Patil et al. 2023 — agent that selects from 1,645 APIs.
- [[SWEAgent]] — *new*, Yang et al. 2024 — coding agent over a computer environment.
- [[VoyagerAgent]] — *new*, Wang et al. 2023 — Minecraft agent with persistent skill library.
- [[ToolTransition]] — *new*, the conditional-probability graph of tool-pair usage.
- [[react|ReAct]] — *engaged*, Yao et al. 2022 Thought-Act-Observation pattern.
- [[reflexion|Reflexion]] — *engaged*, Shinn et al. 2023 evaluator + self-reflection split.
- [[ActorCriticAgent]] — *new*, the RL ancestry of agent reflection (Konda & Tsitsiklis 1999).
- [[PlanningFailure]] — *new*, agent failure family: invalid tool / wrong parameters / goal failure / reflection error.
- [[ToolFailure]] — *new*, agent failure family: tool returns wrong output / translation error / missing tool.
- [[AgentEfficiency]] — *new*, agent evaluation: steps / cost / latency per task.
- [[GoalFailure]] — *new*, agent solves a different task or violates constraints.
- [[ReflectionFailure]] — *new*, agent insists task is done when it isn't.
- [[ShortTermMemory]] — *new*, the context window as memory.
- [[LongTermMemory]] — *new*, external persistent memory (RAG-retrievable).
- [[InternalKnowledgeMemory]] — *new*, model weights as memory.
- [[FIFOMemory]] — *new*, first-in-first-out memory management strategy.
- [[ReflectionMemory]] — *new*, Liu et al. 2023 — agent decides per-action add/merge/replace.
- [[SummarizationMemory]] — *new*, Bae et al. 2022 summary-plus-classifier memory.
- [[BerkeleyFunctionCallingLeaderboard]] — *new*, agent benchmark.
- [[TravelPlannerBenchmark]] — *new*, agent benchmark.
- [[AgentOpsEvalHarness]] — *new*, agent evaluation harness.
- [[ScienceQA]] — *new*, Lu et al. — multimodal science question-answering benchmark.
- [[TabMWP]] — *new*, Lu et al. 2022 — tabular math word problems benchmark.
- [[ContextLength]] — *engaged*, the constraint memory + RAG patterns work around.
- [[CLIP]] — *engaged*, the canonical multimodal embedding model for [[MultimodalRAG]].
- [[Hallucination]] — *engaged*, hallucinated tool calls and hallucinated parameter values.

## Entities Introduced or Engaged

- [[ChipHuyen]] — *engaged*, author.
- [[OReilly]] — *engaged*, publisher.
- [[anthropic|Anthropic]] — *engaged*, [[ContextualRetrieval]] technique + 200K-token long-context recommendation.
- [[openai|OpenAI]] — *engaged*, [[ChatGPT]] as the canonical agent example; FIFO memory removal.
- [[meta|Meta]] — *engaged*, [[YannLeCun|Yann LeCun]] (Meta's Chief AI Scientist) on autoregressive-LLMs-can't-plan.
- [[google|Google]] — *engaged*, [[ScaNN]] vector search library.
- [[Elasticsearch]] — *new*, Shay Banon 2010 search engine built on [[Lucene]].
- [[Lucene]] — *new*, the inverted-index search library underlying Elasticsearch.
- [[Perplexity]] — *engaged*, [[AravindSrinivas]] *"BM25 is hard to beat"* quote.
- [[AravindSrinivas]] — *new*, CEO of [[Perplexity]].
- [[StuartRussell]] — *new*, *AI: A Modern Approach* (1995) — agent definition.
- [[PeterNorvig]] — *new*, *AI: A Modern Approach* (1995) co-author.
- [[YannLeCun]] — *engaged*, *autoregressive LLMs can't plan* position (2023).
- [[SubbaraoKambhampati]] — *engaged*, *Can LLMs Really Reason and Plan?* (2023) — LLMs extract planning knowledge but can't generate executable plans.
- [[NLTK]] — *engaged*, NLP toolkit with tokenization functions.
- [[spaCy]] — *new*, classical NLP package with tokenization.
- [[CoreNLP]] — *new*, Stanford's NLP package.
- [[AutoGPT]] — *engaged*, agent framework focused on social-media APIs.
- [[Composio]] — *new*, agent framework focused on enterprise APIs ([[google|Google Apps]], [[GitHub]], [[Slack]]).
- [[LangChain]] — *engaged*, frameworks like LangChain allow N-last-messages FIFO memory.
- [[FAISS]] — *new*, Facebook AI Similarity Search.
- [[Annoy]] — *new*, Spotify open-source tree ANN.
- [[Hnswlib]] — *new*, the reference HNSW implementation.
- [[Milvus]] — *engaged*, vector DB that implements HNSW.
- [[Pinecone]] — *engaged*, the managed-vector-DB peer.
- [[microsoft|Microsoft]] — *engaged*, SPTAG (Space Partition Tree And Graph).
- [[Spotify]] — *new*, Annoy's home.
- [[GitHub]] / [[Slack]] / [[Reddit]] / [[Wikipedia]] — *engaged*, named as tool-API targets.

## Connections

- [[ai-engineering-chip-huyen]] — parent source page.
- [[ai-engineering-ch05-prompt-engineering]] — Ch 5 introduces [[ContextConstruction]] as the umbrella; Ch 6 is the deep dive.
- [[ai-engineering-ch07-finetuning]] — Ch 7 sibling; finetuning is the *non*-prompt-based alternative.
- [[ai-engineering-ch04-evaluate-ai-systems]] — Ch 4's evaluation methodology applies to RAG retrievers and agent planners alike.
- [[ChipHuyen]] — author.
- [[OReilly]] — publisher.

## Contradictions

- **None vs sibling chapters or wiki.** Ch 6 reinforces Ch 1's *"start simple — prompt before RAG, RAG before agents"* progression and Ch 5's [[ContextConstruction]] umbrella. The chapter's *"long context doesn't kill RAG"* position complements (rather than contradicts) [[anthropic|Anthropic]]'s 200K-token *"just use the full context"* recommendation — Huyen quotes Anthropic approvingly, framing the recommendation as a *lower-bound* on when RAG becomes necessary.
- **Internal debate flagged, not contradicted.** Huyen records but does not adjudicate the [[YannLeCun|LeCun]]/[[SubbaraoKambhampati|Kambhampati]] *"LLMs can't plan"* position vs the [[ReasoningWithLanguageModelIsPlanningWithWorldModel|Hao et al. 2023]] *"LLMs contain a world model"* counter. The wiki's existing [[Planning]] page records the LeCun/Kambhampati skepticism via [[2402.01817-llm-modulo|LLM-Modulo]]; this chapter source page records Huyen's more agnostic stance.
