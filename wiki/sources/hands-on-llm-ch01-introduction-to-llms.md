---
title: "Hands-On LLMs Ch 1 — An Introduction to Large Language Models"
type: source
tags: [book, hands-on-llm, oreilly, llm, language-ai, introduction]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch01-introduction-to-llms.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 1 — An Introduction to Large Language Models

## Summary

The opening chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) frames **[[LanguageAI|Language AI]]** — the authors' preferred umbrella term for "the subfield of AI focused on developing technologies capable of understanding, processing, and generating human language" — as the discipline within which large language models sit, then traces a compressed history from **[[BagOfWords|bag-of-words]]** (1950s; popularized in the 2000s) through **[[Word2Vec|word2vec]]** (Mikolov et al., 2013), recurrent **[[encoderdecoder|encoder-decoder]]** machine translation with **[[Attention|attention]]** (Bahdanau, Cho & Bengio, 2014), the **[[transformer|Transformer]]** ([[1706.03762-attention-is-all-you-need|Vaswani et al., 2017]]), and the split between **[[bert|BERT]]** (encoder-only, 2018) representation models and the **[[GPT|GPT]] family** (decoder-only, 2018→) generative models. The chapter culminates in **2023 as "the Year of Generative AI"** — [[ChatGPT]]'s explosive adoption (1M users in 5 days, 100M in 2 months) and the open-source-vs-proprietary [[FoundationModel|foundation-model]] arms race.

The chapter also adopts a deliberately permissive definition of "LLM" — the authors include **non-generative encoder-only models** ([[bert|BERT]]-style) and explicitly **sub-billion-parameter representation models** under the umbrella, because *"'Large' is arbitrary and what might be considered a large model today could be small tomorrow."* This positions the book against pure-decoder-LLM treatments. It introduces the **two-step training paradigm** (**[[pretraining|pretraining]]** as the next-token-prediction language-modeling phase that produces a **[[FoundationModel|foundation / base model]]**, then **[[FineTuning|fine-tuning]]** / post-training on narrower data), surveys **applications** (supervised + unsupervised classification, semantic search + RAG, agentic chatbots, vision-language multimodal use cases), names the **societal and ethical considerations** (bias, transparency, harmful content, IP, regulation — citing the **[[EuropeanAIAct|European AI Act]]**), and closes with a *Generating Your First Text* worked example using **[[Phi3Mini|Phi-3-mini]]** (`microsoft/Phi-3-mini-4k-instruct`, 3.8B params, MIT-licensed) via the **[[HuggingFace|Hugging Face]] `transformers`** pipeline on a Google Colab T4 (16 GB VRAM minimum). The "GPU-poor" framing — *"this book is for the GPU-poor"* — anchors the book's whole pedagogical stance.

## Key Claims

- **"Language AI" is a more honest umbrella than "LLM"**, encompassing technologies that "technically might not be LLMs but still have a significant impact on the field, like how retrieval systems can give LLMs superpowers" — the chapter explicitly treats RAG ([[rag|retrieval-augmented generation]]) as Language-AI-but-not-LLM. The terms "Language AI" and **[[NLP|natural language processing]]** can be used interchangeably "with the continued success of machine learning methods in tackling language processing problems."
- **The history-of-Language-AI arc has three structural inflection points**: (1) [[BagOfWords|bag-of-words]] → [[Word2Vec|word2vec]] (2013): from sparse-count to dense-semantic vector representations; (2) [[Word2Vec|word2vec]] → recurrent encoder-decoder + attention (2014, Bahdanau-Cho-Bengio): from static word embeddings to context-sensitive sequence representations; (3) RNN+attention → [[transformer|Transformer]] (2017, [[1706.03762-attention-is-all-you-need|Vaswani et al.]]): removing recurrence entirely, enabling parallel training, unlocking scale.
- **The encoder-only / decoder-only split (2018) is the central architectural divergence in the modern LLM tree.** [[bert|BERT]] ([[JacobDevlin|Devlin]] et al. 2018, 12 encoders, [[maskedlanguagemodel|masked language modeling]] + the `[CLS]` token + fine-tuning for downstream tasks) is the encoder-only **representation model** template; [[GPT|GPT-1]] ([[AlecRadford|Radford]] et al. 2018, 117M params, trained on 7,000 books + [[CommonCrawl|Common Crawl]]) is the decoder-only **generative model** template.
- **Scale matters and scale ran fast.** GPT-1 117M (2018) → [[GPT2|GPT-2]] 1.5B (2019) → [[GPT3|GPT-3]] 175B (2020). *"More parameters greatly influence the capabilities and performance of language models."*
- **The base/foundation model + instruct/chat fine-tune split is what makes ChatGPT possible.** Generative LLMs as text-completion machines can be turned into instruction-following systems by fine-tuning on dialog data: *"By fine-tuning these models, we can create instruct or chat models that can follow directions."* Generative models are thus **"completion models."**
- **[[ContextLength|Context length]] (context window) is a defining LLM property** — the maximum number of tokens the model can process. The chapter notes that due to autoregressive generation, current context length grows as new tokens are emitted.
- **2023 is "the Year of Generative AI."** [[ChatGPT]] (GPT-3.5) and successors crossed into mainstream use; both proprietary and open-source [[FoundationModel|foundation models]] proliferated. *"Open source base models are often referred to as foundation models and can be fine-tuned for specific tasks."*
- **Transformer alternatives emerged in 2023-2024**: [[Mamba]] (Gu & Dao, 2023) and [[RWKV]] (Peng et al., 2023) target Transformer-level performance with advantages like larger context windows or faster inference, though neither has displaced the Transformer at frontier scale.
- **Training paradigm has two principal phases** (vs. classical ML's one):
  1. **Pretraining (language modeling)** — train on a vast corpus of internet text; learn grammar, context, and language patterns by next-token prediction. The resulting model is a **foundation / base model**; it doesn't follow instructions.
  2. **Fine-tuning (post-training)** — further-train on a narrower task. E.g., [[Llama|Llama 2]] was pretrained on **2 trillion tokens** — a compute scale out of reach for most practitioners; fine-tuning is the high-leverage entry point.
- **Proprietary vs. open models** trade off control, fine-tunability, and data privacy against compute requirements and hosting expertise. Examples cited: proprietary — [[openai|OpenAI's]] [[GPT4|GPT-4]], [[anthropic|Anthropic's]] [[claudeopus47|Claude]]; open — [[Cohere|Cohere's]] **Command R**, [[Mistral]] models, [[microsoft|Microsoft's]] **Phi**, [[meta|Meta's]] [[Llama]] models. *"Some publicly shared models have a permissive commercial license, which means that the model cannot be used for commercial purposes. For many, this is not the true definition of open source."*
- **The book's tooling stance**: backend packages without GUI — **[[llamacpp|llama.cpp]]**, **[[LangChain]]**, and **[[HuggingFace|Hugging Face]] Transformers** as the core. The local-GUI alternatives mentioned (but not the book's focus): **[[TextGenerationWebui|text-generation-webui]]**, **[[KoboldCpp|KoboldCpp]]**, **[[LMStudio|LM Studio]]**.
- **The book is "for the GPU-poor."** Examples use **[[GoogleColab|Google Colab]] T4 with 16 GB VRAM** as the minimum target. The main worked model is [[Phi3Mini|Phi-3-mini]] (`microsoft/Phi-3-mini-4k-instruct`, 3.8B params, MIT-licensed, runs in <8 GB VRAM and **<6 GB with quantization**). Llama-2 training-cost anchor: A100-80GB rentals at $1.50/hr × 3,311,616 GPU-hours = **>$5,000,000** to create the Llama 2 family.
- **Five ethical considerations** structure the chapter's responsibility framing: bias and fairness (training-data bias propagates), transparency and accountability (humans may not know they're talking to a model — medical-device regulation cited as a likely outcome), generating harmful content ([[Hallucination|hallucination]] + fake news), intellectual property (training-data provenance is rarely shared), and regulation — naming the **[[EuropeanAIAct|European AI Act]]** as the canonical example of foundation-model-regulating legislation.
- **The chapter's `transformers` worked example** uses the model+tokenizer pair, `device_map="cuda"`, `torch_dtype="auto"`, `trust_remote_code=True`, and the `transformers.pipeline("text-generation", ..., do_sample=False)` wrapper. `do_sample=False` forces greedy decoding; the chapter forward-references Chapter 6 for sampling strategies.

## Key Quotes

> "Language AI refers to a subfield of AI that focuses on developing technologies capable of understanding, processing, and generating human language. The term Language AI can often be used interchangeably with natural language processing (NLP) with the continued success of machine learning methods in tackling language processing problems." — p. 4 (defining the umbrella term)

> "Bag-of-words works as follows: ... we simply count how often a word in each sentence appears, quite literally creating a bag of words." — p. 7 (defining the foundational pre-neural representation)

> "Embeddings are vector representations of data that attempt to capture its meaning." — p. 8 (the word2vec / dense-embedding pivot)

> "Attention selectively determines which words are most important in a given sentence." — p. 14 (Bahdanau-Cho-Bengio attention before the Transformer)

> "The Transformer ... could be trained in parallel, which tremendously sped up training." — p. 15 (the structural reason the Transformer won)

> "BERT is an encoder-only architecture that focuses on representing language ... This means that it only uses the encoder and removes the decoder entirely." — p. 18

> "These generative decoder-only models, especially the 'larger' models, are commonly referred to as large language models (LLMs). ... the term LLM is not only reserved for generative models (decoder-only) but also representation models (encoder-only)." — p. 21–22 (the book's permissive LLM definition)

> "'Large' is arbitrary and what might be considered a large model today could be small tomorrow." — p. 25 (justifying the inclusive definition)

> "For instance, Llama 2 has been trained on a dataset containing 2 trillion tokens. Imagine the compute necessary to create that model!" — p. 26 (anchoring the pretraining/fine-tuning split)

> "This book is for the GPU-poor! We will use models that users can run without the most expensive GPU(s) available or a big budget." — p. 29 (the book's pedagogical commitment)

> "Why don't chickens like to go to the gym? Because they can't crack the egg-sistence of it!" — p. 33 (the chapter's first generated output; Phi-3-mini, greedy decoding)

## Concepts Introduced or Engaged

- [[LanguageAI]] — *new*, the chapter's umbrella term for language-processing AI; positioned as interchangeable with [[NLP]] but slightly broader (encompasses retrieval systems that "give LLMs superpowers").
- [[BagOfWords]] — *new*, the pre-neural sparse-count text-representation technique introduced as the chapter's starting point.
- [[Word2Vec]] — *engaged*, the 2013 dense word-embedding milestone (existing wiki page updated).
- [[WordEmbedding]] / [[Embedding]] — *engaged*, the chapter's embeddings-have-many-types framing (word vs sentence vs document; static vs contextual).
- [[Attention]] — *engaged*, introduced via Bahdanau-Cho-Bengio 2014 before the Transformer.
- [[selfattention]] — *engaged*, the Transformer-specific attention variant.
- [[transformer|Transformer]] — *engaged*, the chapter's architectural pivot.
- [[encoderdecoder|Encoder-Decoder]] — *engaged*, the original Transformer's design pattern.
- [[bert|BERT]] — *engaged*, the encoder-only template introduced 2018.
- [[maskedlanguagemodel]] — *engaged*, the BERT training objective.
- [[RepresentationModel]] — *new*, the chapter's umbrella term for encoder-only models that produce embeddings.
- [[GenerativeModel]] — *new*, the chapter's umbrella term for decoder-only text-generating models.
- [[GPT|GPT-1]] / [[GPT2|GPT-2]] / [[GPT3|GPT-3]] — *engaged*, the decoder-only scaling history (117M → 1.5B → 175B).
- [[LanguageModel]] — *engaged*, the underlying joint-probability framework.
- [[LargeLanguageModel]] — *engaged*, the chapter's permissive definition (includes sub-1B representation models).
- [[AutoregressiveLanguageModel]] — *engaged*, the decoder-only generative paradigm.
- [[FoundationModel]] — *engaged*, the chapter's term for base / pretrained models.
- [[pretraining]] — *engaged*, the language-modeling first step.
- [[FineTuning]] — *engaged*, the second step (instruct / chat tuning).
- [[InstructModel]] — *new*, the chat / direction-following fine-tuned variant.
- [[CompletionModel]] — *new*, the generative-LLM-as-text-completer framing.
- [[ContextLength]] — *new*, the maximum-tokens-processable property; alias [[ContextWindow]].
- [[Tokenization]] / [[Tokenizer]] — *engaged*, splitting text into tokens (sub-words for most modern models).
- [[RNN]] — *engaged*, the pre-Transformer recurrent backbone.
- [[Mamba]] / [[RWKV]] — *engaged*, the 2023 Transformer-alternative architectures mentioned in the "Year of Generative AI."
- [[rag|RAG]] — *engaged*, the chapter forward-references RAG as the canonical example of Language-AI-but-not-LLM.
- [[Hallucination]] — *engaged*, in the ethics section.
- [[Quantization]] — *engaged*, Phi-3-mini quantization gets the model under 6 GB VRAM.
- [[GPU]] / [[VRAM]] — *engaged*, the "GPU-poor" framing's hardware vocabulary.
- [[OpenSourceLLM]] / [[ProprietaryLLM]] — *new*, the open-vs-closed-weights dichotomy.
- [[GreedyDecoding]] — *engaged*, the chapter's `do_sample=False` worked example.
- [[NeuralNetwork]] — *engaged*, defined in the word2vec section as interconnected layers of nodes with weights (parameters).
- [[Parameter]] — *engaged*, defined as the connection weights in a neural network.

## Entities Introduced or Engaged

- [[JayAlammar]] — *new*, co-author (Cohere; well-known for *The Illustrated Transformer*).
- [[MaartenGrootendorst]] — *new*, co-author (creator of BERTopic and KeyBERT).
- [[HandsOnLLM]] — *new*, the book itself.
- [[OReilly]] — *engaged*, publisher.
- [[openai|OpenAI]] — *engaged*, GPT-1 / GPT-2 / GPT-3 / GPT-4 / ChatGPT.
- [[anthropic|Anthropic]] — *engaged*, Claude.
- [[meta|Meta]] — *engaged*, Llama 2 (the chapter's training-cost anchor).
- [[microsoft|Microsoft]] — *engaged*, Phi (the book's main worked model).
- [[google|Google]] — *engaged*, Google Colab (the book's pedagogical compute target).
- [[Cohere]] — *new*, Command R (proprietary-but-open model example); Jay Alammar's employer.
- [[Mistral]] — *engaged*, the open-weights French AI lab.
- [[HuggingFace|Hugging Face]] — *engaged*, the model hub and `transformers` library; "800,000+ models" at time of writing.
- [[ChatGPT]] — *engaged*, the November-2022 ignition event.
- [[GPT4|GPT-4]] — *engaged*, the larger ChatGPT-backing model.
- [[Phi3Mini|Phi-3-mini]] — *new*, the book's main worked model (`microsoft/Phi-3-mini-4k-instruct`).
- [[Llama|Llama 2]] — *engaged*, the 2-trillion-token pretraining anchor.
- [[CommonCrawl]] — *engaged*, GPT-1's training data.
- [[GoogleColab]] — *engaged*, the book's compute target.
- [[AlecRadford]] — *engaged*, first author of GPT-1 / GPT-2.
- [[TomasMikolov]] — *engaged*, first author of word2vec.
- [[JacobDevlin]] — *new*, first author of BERT.
- [[AshishVaswani]] — *new*, first author of "Attention is All You Need".
- [[DzmitryBahdanau]] — *new*, first author of the 2014 attention paper.
- [[YoshuaBengio]] — *engaged*, co-author of the 2014 attention paper.
- [[KyunghyunCho]] — *engaged*, co-author of the 2014 attention paper.
- [[JohnMcCarthy]] — *new*, AI co-founder; quoted on the AI definition.
- [[LangChain]] — *engaged*, named backend tooling.
- [[llamacpp|llama.cpp]] — *engaged*, named backend tooling.
- [[LMStudio]] — *new*, GUI alternative for local LLMs.
- [[KoboldCpp]] — *new*, GUI alternative for local LLMs.
- [[TextGenerationWebui]] — *new*, GUI alternative for local LLMs.
- [[EuropeanAIAct]] — *new*, the foundation-model-regulating EU legislation cited in the responsibility section.
- [[NVIDIA]] — *engaged*, the assumed GPU vendor (`device_map="cuda"`).

## Connections

- [[JayAlammar]] / [[MaartenGrootendorst]] — co-authors of the book.
- [[OReilly]] — publisher.
- [[HandsOnLLM]] — the book this chapter opens.
- [[LanguageAI]] / [[NLP]] — the umbrella terminology.
- [[BagOfWords]] → [[Word2Vec]] → [[Attention]] → [[transformer|Transformer]] → [[bert|BERT]] / [[GPT|GPT-1]] — the chapter's history arc.
- [[RepresentationModel]] vs [[GenerativeModel]] — the encoder-vs-decoder dichotomy this chapter establishes as the book's organizing axis.
- [[ContextLength]] — the chapter introduces the term that becomes load-bearing in later chapters.
- [[FoundationModel]] / [[pretraining]] / [[FineTuning]] / [[InstructModel]] / [[CompletionModel]] — the training-paradigm vocabulary.
- [[Phi3Mini]] — the book's recurring worked model.
- [[HuggingFace]] / [[LangChain]] / [[llamacpp]] — the book's tool stack.
- [[GoogleColab]] / [[GPU]] / [[VRAM]] / [[Quantization]] — the "GPU-poor" hardware vocabulary.
- [[EuropeanAIAct]] — regulation framing.

## Contradictions

None directly conflicting with existing wiki content. **Soft tensions worth flagging** (do not constitute contradictions):

- **The "LLM" definition is more permissive than the wiki's existing [[LargeLanguageModel]] page** ([[ai-engineering-ch01-intro|Chip Huyen Ch 1]] framing). Huyen treats LLM as "scaled language model trained via self-supervision"; Alammar & Grootendorst extend it to include sub-1B encoder-only representation models (e.g., BERT) and explicitly non-generative models. Both stances are defensible; flagged here as a definitional difference, not a contradiction.
- **Layer count for BERT-base.** The chapter says "BERT base model with 12 encoders" (Figure 1-21 caption); the wiki's existing [[bert]] page says "BERT_BASE (110M)" with no explicit layer count, but this is consistent with the 12-layer BERT-base from [[1810.04805-bert]]. No contradiction — both pages reference the same model.
- **The chapter dates word2vec to 2013** (consistent with [[Word2Vec]] page citing Mikolov et al. 2013).
- **The chapter dates GPT-1 to 2018** (consistent with [[AlecRadford]] page and the broader wiki).
- **Attention paper date 2014** (Bahdanau, Cho & Bengio, arXiv 1409.0473) — consistent with the existing wiki ([[encoderdecoder]] / [[transformer]]).
- **The chapter's "117M parameters" for GPT-1 + "1.5B for GPT-2" + "175B for GPT-3"** — fully consistent with [[GPT3]], [[AlecRadford]], and [[LargeLanguageModel]] pages.

## Position in the wiki

This is the **first chapter from *Hands-On Large Language Models*** ingested — a sibling pedagogical anchor to the [[ai-engineering-chip-huyen|Chip Huyen *AI Engineering*]] book (the wiki's other O'Reilly-2024 LLM book) and to the [[LLMEngineersHandbook|Iusztin / Labonne / Vesa *LLM Engineer's Handbook*]] (Packt, 2024). Where Huyen Ch 1 frames AI engineering as a discipline downstream of foundation models, and the LLM Engineer's Handbook Ch 1 frames the LLM Twin project as a production-system anchor, Alammar & Grootendorst Ch 1 is the **pure pedagogical introduction** — the historical arc + architectural taxonomy + responsible-use survey + a runnable first example.

The chapter complements rather than contradicts the existing wiki:

- **Historical narrative**: extends the [[Word2Vec]] / [[bert]] / [[transformer]] / [[GPT|GPT family]] timeline with the explicit BoW → word2vec → attention → Transformer arc that the existing concept pages assume but don't narrate end-to-end.
- **Definitional clarity**: introduces the **representation-model vs generative-model** vocabulary the book uses throughout — a clearer two-bucket split than the wiki had previously codified.
- **Tooling baseline**: anchors `transformers` + `pipeline()` + the Hugging Face Hub as the canonical *first* interface to an LLM (the LLM Engineer's Handbook later builds on top of this).
- **Worked model**: introduces **Phi-3-mini** as the book's recurring small-but-capable model, complementing the wiki's existing emphasis on Llama / Mistral / GPT.

Subsequent chapters (Ch 2: Tokenization & Embeddings; Ch 3: Looking Inside LLMs; Ch 4–11: applications and fine-tuning) will deepen the technical content this chapter sketches.
