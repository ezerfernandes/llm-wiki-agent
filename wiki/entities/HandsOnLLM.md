---
title: "Hands-On Large Language Models"
type: entity
tags: [book, oreilly, llm, language-ai, hands-on-llm]
sources: [hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch03-looking-inside-llms, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch07-advanced-text-generation, hands-on-llm-ch08-semantic-search-and-rag, hands-on-llm-ch09-multimodal-llms, hands-on-llm-ch10-creating-text-embedding-models, hands-on-llm-ch11-fine-tuning-representation-models, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Hands-On Large Language Models

**Hands-On Large Language Models: Language Understanding and Generation** — book by [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]], published by [[OReilly|O'Reilly Media]] in 2024 (ISBN 978-1-098-15096-9). The third LLM-engineering / LLM-pedagogy book in the wiki — after [[ai-engineering-chip-huyen|Chip Huyen's *AI Engineering*]] and the [[LLMEngineersHandbook|Iusztin / Labonne / Vesa *LLM Engineer's Handbook*]] (Packt 2024).

## Stance and positioning

Where *AI Engineering* (Huyen) frames the discipline of building applications on top of foundation models, and the *LLM Engineer's Handbook* (Iusztin et al.) follows a single LLM Twin production project end-to-end, *Hands-On LLMs* is the **pedagogical introduction to the model class itself** — the book that walks a reader from [[BagOfWords|bag-of-words]] to [[transformer|Transformers]] to [[bert|BERT]] / [[GPT]] / [[ChatGPT]] with runnable code at every step.

Two structural choices distinguish the book:

1. **The "Language AI" umbrella.** The authors deliberately use [[LanguageAI|Language AI]] (≈ [[NLP|NLP]]) as the parent category — *"we want to focus on the models that have had a major role in shaping the field of Language AI. This means exploring more than just LLMs in isolation."* This admits encoder-only models ([[bert|BERT]]) and even pre-neural ([[BagOfWords|bag-of-words]]) techniques as first-class subjects.

2. **The "GPU-poor" commitment.** The book explicitly targets readers without access to high-end GPUs. *"This book is for the GPU-poor!"* The recurring worked model is [[Phi3Mini|Phi-3-mini]] (`microsoft/Phi-3-mini-4k-instruct`, 3.8B params, MIT-licensed); the assumed compute environment is a [[GoogleColab|Google Colab]] T4 with 16 GB VRAM (free tier); [[Quantization|quantization]] brings the working VRAM under 6 GB.

## Tooling stance

Backend-first, GUI-secondary. The book centers on three packages:

- **[[HuggingFace|Hugging Face]] `transformers`** — the canonical first interface; provides `AutoTokenizer`, `AutoModelForCausalLM`, and the `pipeline()` wrapper.
- **[[llamacpp|llama.cpp]]** — the canonical local-inference backend for quantized models.
- **[[LangChain]]** — the orchestration framework for chaining LLM calls with other tools.

GUI alternatives mentioned (not the book's primary focus): [[TextGenerationWebui|text-generation-webui]], [[KoboldCpp]], [[LMStudio|LM Studio]].

## Chapter scope

| Chapter | Topic |
|---|---|
| Ch 1 | An Introduction to Large Language Models — see [[hands-on-llm-ch01-introduction-to-llms]] |
| Ch 2 | Tokens and Embeddings — see [[hands-on-llm-ch02-tokens-and-embeddings]] |
| Ch 3 | Looking Inside Large Language Models — see [[hands-on-llm-ch03-looking-inside-llms]] |
| Ch 4 | Text Classification — see [[hands-on-llm-ch04-text-classification]] |
| Ch 5 | Text Clustering and Topic Modeling — see [[hands-on-llm-ch05-text-clustering-topic-modeling]] |
| Ch 6 | Prompt Engineering — see [[hands-on-llm-ch06-prompt-engineering]] |
| Ch 7 | Advanced Text Generation Techniques and Tools — see [[hands-on-llm-ch07-advanced-text-generation]] |
| Ch 8 | Semantic Search and Retrieval-Augmented Generation — see [[hands-on-llm-ch08-semantic-search-and-rag]] |
| Ch 9 | Multimodal Large Language Models — see [[hands-on-llm-ch09-multimodal-llms]] |
| Ch 10 | Creating Text Embedding Models *(forward-referenced)* |
| Ch 11 | Fine-Tuning Representation Models for Classification — see [[hands-on-llm-ch11-fine-tuning-representation-models]] |
| Ch 12 | Fine-Tuning Generation Models — see [[hands-on-llm-ch12-fine-tuning-generation-models]] |

**The book is now fully ingested (12/12 chapters).** Third fully-ingested book in the wiki after [[ai-engineering-chip-huyen|*AI Engineering*]] (Chip Huyen, O'Reilly 2024) and [[LLMEngineersHandbook|*LLM Engineer's Handbook*]] (Iusztin, Labonne & Vesa, Packt 2024), alongside [[d2l-attention-and-transformers|*Dive into Systems*]]-style D2L material and the in-progress *Mathematics for Machine Learning* ingest.

## Connections

- [[JayAlammar]] / [[MaartenGrootendorst]] — co-authors.
- [[OReilly]] — publisher.
- [[ai-engineering-chip-huyen]] / [[LLMEngineersHandbook]] — sibling 2024 LLM books in the wiki.
- [[hands-on-llm-ch01-introduction-to-llms]] — the first chapter ingested.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2.
- [[hands-on-llm-ch03-looking-inside-llms]] — Ch 3.
- [[hands-on-llm-ch04-text-classification]] — Ch 4 (text classification — first applications chapter).
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 (unsupervised twin of Ch 4 — BERTopic walkthrough).
- [[hands-on-llm-ch06-prompt-engineering]] — Ch 6 (the book's prompt-engineering chapter; opens Part III on the generative-models half of the two-bucket axis; introduces the seven-component modular prompt + chain prompting + chain-of-thought / self-consistency / tree-of-thought + grammar-constrained decoding via llama-cpp-python).
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7 (advanced text generation techniques and tools; the **wiki's first LangChain-centric source**; walks Model I/O, Chains, Memory, and Agents as four LangChain abstractions; introduces the LangChain-native operationalization of [[react|ReAct]] via `create_react_agent` + `AgentExecutor` running a DuckDuckGo + llm-math agent on GPT-3.5; first runnable LangChain ReAct receipt in the wiki, complementing existing DSPy-native ReAct coverage).
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 (the book's headline **[[rag|RAG]] chapter**; three-category retrieval taxonomy [dense / rerank / RAG]; canonical *Interstellar* worked example via [[Cohere]] `co.embed` + [[FAISS|`faiss.IndexFlatL2`]] + `co.rerank` + `co.chat(documents=...)` with automatic span-level citations; local-RAG replication via [[Phi3Mini|Phi-3]] + [[BGESmallEnV15|`BAAI/bge-small-en-v1.5`]] + [[FAISS]] + [[LangChain|`langchain.RetrievalQA`]]; Advanced-RAG continuum [query rewriting → multi-query → multi-hop → routing → agentic]; Liu / Zhang / Liang 2023 four-axis RAG-evaluation taxonomy; [[RAGAS|Ragas]] as LLM-as-a-judge automation).
- [[hands-on-llm-ch09-multimodal-llms]] — Ch 9 (the book's **vision-language chapter** and the **only chapter that extends the wiki's text-only LLM coverage to multimodal models that accept images**; walks three architecturally distinct moves intuition → mechanism → runnable code — [[VisionTransformer|ViT]] (image-as-patches-tokenized-like-text), [[CLIP|CLIP / OpenCLIP]] (contrastive multimodal *embedding* model on `openai/clip-vit-base-patch32`), and [[BLIP2|BLIP-2]] (`Salesforce/blip2-opt-2.7b` — adapter-style multimodal *generative* model with the [[QFormer|Q-Former]] bridge + frozen ViT + frozen OPT-2.7b); two BLIP-2 use cases — [[ImageCaptioning|image captioning]] (supercar → *"an orange supercar driving on the road at sunset"*) and [[VisualQuestionAnswering|VQA / multimodal chat]] (*"What would it cost me to drive that car?"* → *"$1,000,000"*); the chapter's structural punchline that *"the moment the embeddings are passed to the encoder, they are treated as if they were textual tokens"* — the sameness-after-tokenization that justifies the entire adapter pattern; closes Part II of the book).
- [[Phi3Mini]] / [[HuggingFace]] / [[llamacpp]] / [[LangChain]] / [[GoogleColab]] / [[Cohere]] / [[Salesforce]] — the book's stack (Salesforce added as Ch 9 anchor via `Salesforce/blip2-opt-2.7b`; Cohere added as Ch 8 anchor; was a Ch 4 mention before).
- [[hands-on-llm-ch11-fine-tuning-representation-models]] — Ch 11 (second chapter of Part III — fine-tuning representation models for classification). Walks four fine-tuning regimes for [[bert|BERT]]-class encoders on [[RottenTomatoes|rotten_tomatoes]] and [[CoNLL2003|CoNLL-2003]]: **(1)** full supervised fine-tuning via [[Trainer]] + [[DataCollatorWithPadding]] (F1 = 0.85); **(2)** [[LayerFreezing|layer freezing]] (F1 = 0.63 to 0.80 depending on what's frozen); **(3)** [[SetFit]] for few-shot classification (Tunstall et al. 2022) — 32 labels → F1 = 0.85; **(4)** [[ContinuedPretraining|continued pretraining]] with [[MaskedLanguageModel|MLM]] via `AutoModelForMaskedLM` + [[DataCollatorForLanguageModeling]] (qualitative `fill-mask` shift from `idea/dream/day` to `movie/film/mess`). Then pivots to **token-level classification** for [[NamedEntityRecognition|NER]] — `AutoModelForTokenClassification` + [[DataCollatorForTokenClassification]] + [[BIOTagging]] (`O / B-PER / I-PER / B-ORG / I-ORG / B-LOC / I-LOC / B-MISC / I-MISC`) + [[LabelAlignment]] (word-to-subtoken with `(label + 1) if odd` continuation trick) + [[seqeval]] for span-level F1. Closes with forward-reference to Ch 12 for fine-tuning generative models.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — **Ch 12 (final chapter of the book; third chapter of Part III — fine-tuning generation models)**. Walks the **two-stage fine-tuning pipeline for generative LLMs** end-to-end on [[TinyLlama|TinyLlama-1.1B]] using the Hugging Face stack ([[transformers]] + [[peft|PEFT]] + [[bitsandbytes]] + [[trl|TRL]]). **Stage 1 — [[SupervisedFinetuning|Supervised Fine-Tuning (SFT)]]** via [[QLoRA]]: 4-bit NF4 quantization (`BitsAndBytesConfig`) + LoRA adapter (`r=64`, `α=32`, all 7 Llama-family projection layers) + [[SFTTrainer|`trl.SFTTrainer`]] on 3,000 [[UltraChat]] examples in [[ChatTemplate|`<|user|>...<|assistant|>`]] format → ~1 hour on a free Google Colab Tesla T4. **Stage 2 — [[PreferenceFinetuning|Preference Tuning]]** via [[DPO]]: same QLoRA config + [[DPOTrainer|`trl.DPOTrainer`]] on `argilla/distilabel-intel-orca-dpo-pairs` (~6,000 filtered triples) with `beta=0.1`, `lr=1e-5`, `warmup_ratio=0.1`, 200 steps. Also surveys generative-LLM evaluation (word-level metrics — [[Perplexity]] / [[ROUGE]] / [[bleu|BLEU]] / [[BERTScore]]; public benchmarks — [[MMLU]] / [[GSM8K]] / [[HellaSwag]] / [[TruthfulQA]] / [[HumanEval]] / [[GLUE]]; leaderboards — [[OpenLLMLeaderboard|Open LLM Leaderboard]]; [[LLMAsAJudge|LLM-as-a-judge]] + [[ChatbotArena|Chatbot Arena]] + [[EloRating|Elo]]; [[GoodhartsLaw|Goodhart's Law]]) and the [[RewardModel|reward-model]] + [[PPO]] baseline DPO replaces, with a forward-look at [[ORPO]] as the SFT+DPO collapse.
