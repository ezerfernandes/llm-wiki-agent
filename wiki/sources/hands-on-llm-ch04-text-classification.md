---
title: "Hands-On LLMs Ch 4 — Text Classification"
type: source
tags: [book, hands-on-llm, oreilly, llm, text-classification, sentiment-analysis, zero-shot, embeddings, generative, t5, flan-t5, chatgpt]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch04-text-classification.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 4 — Text Classification

## Summary

The fourth chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) — the **wiki's first applications chapter** from the book — runs a single binary [[SentimentAnalysis|sentiment-analysis]] task (the [[RottenTomatoes|`rotten_tomatoes`]] [[HuggingFace|Hugging Face]] dataset, 5,331 positive + 5,331 negative movie reviews from Pang and Lee 2005) across **four progressively more permissive pretrained-LLM classification regimes** and records the resulting weighted-average [[F1Score|F1]] scores side by side: (1) a **task-specific fine-tuned [[RepresentationModel|representation model]]** — `cardiffnlp/twitter-roberta-base-sentiment-latest` ([[TwitterRoBERTa|Twitter-RoBERTa]]) — wrapped by `transformers.pipeline(...)`, F1 = **0.80**; (2) a **frozen [[Embedding|embedding]] model + [[LogisticRegression|logistic regression]] classifier head** — [[SentenceTransformers|sentence-transformers]] `all-mpnet-base-v2` (768-dim) → [[sklearn|scikit-learn]] `LogisticRegression`, F1 = **0.85**; (3) **[[ZeroShotClassification|zero-shot classification]] via [[LabelEmbedding|label embeddings]] + [[CosineSimilarity|cosine similarity]]** — embed `["A negative review", "A positive review"]`, compute cosine similarity to each test document, `argmax`, F1 = **0.78**; (4) **[[GenerativeClassification|generative classification]] via instruction prompts** — `google/flan-t5-small` ([[FLANT5|Flan-T5-small]], encoder-decoder, F1 = **0.84**) and `gpt-3.5-turbo-0125` ([[ChatGPT|ChatGPT]] / GPT-3.5, decoder-only via OpenAI API, F1 = **0.91**). The chapter is structured as **two halves: representation models** ("Text Classification with Representation Models") covering regimes (1)–(3) and **generative models** ("Text Classification with Generative Models") covering regime (4).

The chapter's central pedagogical move is to **decouple the embedding step from the classification step**: by keeping the embedding model frozen, the per-task work collapses from full BERT fine-tuning (requiring GPUs, costly) to training a logistic regression on CPU over a 768-dim feature vector — a recipe the chapter calls *"a major benefit of this separation"* and the lightweight default for practitioners without GPU access. The chapter then generalizes this to the **no-labels** case via zero-shot label embeddings — describe each label as a sentence (*"A negative review"*), embed the description with the same model, and assign labels by cosine similarity between document and label embeddings; this works because the embedding space is shared across both documents and label descriptions, and gives **F1 = 0.78 with zero labeled examples**, only 7 points below the supervised logistic-regression baseline. The chapter explicitly contrasts this with **[[NaturalLanguageInference|NLI-based zero-shot classification]]** (the dominant prior approach) — *"natural language inference models are amazing for zero-shot classification, the example here demonstrates the flexibility of embeddings for a variety of tasks"* — and uses the embedding approach precisely to demonstrate **embeddings as a versatile but underestimated component** of Language AI pipelines.

The generative-models half introduces **[[GenerativeClassification|generative classification]] via [[PromptEngineering|prompt engineering]]**: instead of taking the model's class logits, prefix each input with a natural-language instruction (*"Is the following sentence positive or negative? "*) and parse the model's free-text output back to a class label (`"negative"` → 0, `"positive"` → 1). [[FLANT5|Flan-T5]]'s instruction-tuning recipe is sketched (mask-span pretraining → multi-task instruction fine-tuning per Chung et al. *"Scaling instruction-finetuned language models"* with 1,800+ tasks); the chapter notes Flan-T5 is an [[encoderdecoder|encoder-decoder]] model (12 encoder + 12 decoder layers per the [[t5|T5]] paper) and uses Hugging Face's `"text2text-generation"` pipeline. For [[ChatGPT|ChatGPT]] / GPT-3.5 the chapter switches from local inference to the [[openai|OpenAI]] API (`openai.OpenAI(api_key=...)`, `client.chat.completions.create(..., temperature=0)`), describes [[PreferenceFinetuning|preference tuning]] as the third training step beyond pretraining + instruction tuning (forward-referencing Ch 12), and warns about **rate limits and exponential backoff** for API-based inference. The chapter's closing observation — *"since we do not know what data the model was trained on, we cannot easily use these kinds of metrics for evaluating the model. For all we know, it might have actually been trained on our dataset!"* — flags **[[BenchmarkContamination|benchmark contamination]] / [[DataContamination|data contamination]]** as the irreducible epistemological limit of evaluating closed-source LLMs on public datasets.

The chapter sits at the application layer above [[hands-on-llm-ch01-introduction-to-llms|Ch 1]]'s representation-vs-generative taxonomy, [[hands-on-llm-ch02-tokens-and-embeddings|Ch 2]]'s tokenizer/embedding plumbing, and [[hands-on-llm-ch03-looking-inside-llms|Ch 3]]'s Transformer-internals deep-dive. It is **Part II, Chapter 1** of the book — the first chapter where the runnable code does something a practitioner would actually deploy. It forward-references **Ch 10** (creating embedding models), **Ch 11** (fine-tuning representation models — the alternative to using a pretrained task-specific model), and **Ch 12** (fine-tuning generation models — where preference tuning is taught) repeatedly. The chapter's advisory note — *"it is highly advised to compare these examples against classic, but strong baselines such as representing text with TF-IDF and training a logistic regression classifier on top of that"* — is the book's first explicit endorsement of [[TFIDF|TF-IDF]] + [[LogisticRegression|logistic regression]] as the **classical baseline every neural model must beat to justify itself**, echoing [[ai-engineering-ch04-evaluate-ai-systems|Huyen's AI Engineering Ch 4]] discipline on baselining.

## Key Claims

- **The chapter compares four pretrained-LLM classification regimes on a single binary task** ([[RottenTomatoes|rotten_tomatoes]] sentiment; 5,331 positive + 5,331 negative reviews from Pang & Lee 2005, split into train (8,530) / validation (1,066) / test (1,066) — loaded via the [[HuggingFace|Hugging Face]] `datasets` package). The weighted-average [[F1Score|F1]] scores on the test split are:

  | Regime | Model | F1 | Source training data |
  |---|---|---|---|
  | Task-specific representation | `cardiffnlp/twitter-roberta-base-sentiment-latest` | **0.80** | RoBERTa fine-tuned on tweets |
  | Embedding + logistic regression | `sentence-transformers/all-mpnet-base-v2` + sklearn LogisticRegression | **0.85** | Frozen embedding + supervised head |
  | Zero-shot embedding (label embeddings + cosine) | `sentence-transformers/all-mpnet-base-v2` | **0.78** | No labels — only label descriptions |
  | Generative open-source (Flan-T5) | `google/flan-t5-small` (text2text-generation pipeline) | **0.84** | Instruction-tuned encoder-decoder |
  | Generative closed-source (ChatGPT) | `gpt-3.5-turbo-0125` via OpenAI API | **0.91** | Preference-tuned decoder-only |

- **Pretrained representation models for classification come in two flavors**: *task-specific models* (representation model already fine-tuned for the task, e.g. sentiment) and *embedding models* (representation model producing general-purpose embeddings that feed a separate classifier). Both keep the underlying model frozen — fine-tuning is covered in Ch 11 (representation models) and Ch 10 (embedding models).
- **The Hugging Face Hub hosts over 60,000 text-classification models and more than 8,000 embedding models at time of writing**. Model selection is multi-axis: language compatibility, underlying architecture, size, performance. The chapter lists six [[bert|BERT]]-family baselines: BERT base (uncased), [[RoBERTa]] base, [[DistilBERT]] base (uncased), [[DeBERTa]] base, bert-tiny, ALBERT base v2.
- **[[RepresentationModel|Encoder-only models]] ([[bert|BERT]] family) excel at task-specific use cases and are significantly smaller than [[GenerativeModel|generative models]]** like the GPT family. *"While generative models, like the GPT family, are incredible models, encoder-only models similarly excel in task-specific use cases and tend to be significantly smaller in size."*
- **[[TwitterRoBERTa|Twitter-RoBERTa]] (cardiffnlp/twitter-roberta-base-sentiment-latest) achieves F1 = 0.80 on Rotten Tomatoes movie reviews despite being trained on tweets** — generalization across domain (Twitter → movie reviews) costs ~5 F1 points vs an in-domain alternative like `DistilBERT base uncased finetuned SST-2`. The chapter uses this gap to motivate **embedding models as the more general second flavor**.
- **The embedding + logistic regression recipe (F1 = 0.85)** uses `sentence-transformers/all-mpnet-base-v2` to convert 8,530 training reviews into a `(8530, 768)` feature matrix, then trains `sklearn.linear_model.LogisticRegression(random_state=42)`. *"A major benefit of this separation is that we do not need to fine-tune our embedding model, which can be costly. In contrast, we can train a classifier, like a logistic regression, on the CPU instead."* The chapter chose `all-mpnet-base-v2` per the **MTEB leaderboard** — *"a great place to start"* — emphasizing inference speed alongside performance.
- **Zero-shot classification via label embeddings**: describe each label as a natural-language sentence (e.g. *"A negative review"* / *"A positive review"*), embed the descriptions with the same model used for documents, and assign labels by cosine similarity:
  ```python
  label_embeddings = model.encode(["A negative review", "A positive review"])
  sim_matrix = cosine_similarity(test_embeddings, label_embeddings)
  y_pred = np.argmax(sim_matrix, axis=1)
  ```
  F1 = 0.78 with **zero labeled training examples** — *"An F1 score of 0.78 is quite impressive considering we did not use any labeled data at all!"*
- **The label description is itself a hyperparameter.** The chapter suggests replacing *"A negative/positive review"* with *"A very negative/positive movie review"* to bias the embedding toward the movie-review domain and the polarity extremes — *"this way, the embedding will capture that it is a movie review and will focus a bit more on the extremes of the two labels."* This is **[[PromptEngineering|prompt engineering]] for label descriptions** — the same iterative-refinement discipline applied to label-text rather than instruction-text.
- **NLI-based zero-shot classification is the prior dominant approach** — the chapter explicitly contrasts it with the embedding approach: *"if you are familiar with zero-shot classification with Transformer-based models, you might wonder why we choose to illustrate this with embeddings instead. Although natural language inference models are amazing for zero-shot classification, the example here demonstrates the flexibility of embeddings for a variety of tasks."*
- **[[GenerativeModel|Generative LLMs]] are sequence-to-sequence models**: they take in text and produce text, regardless of the task. For classification, the model output must be **parsed back to a class label** (`"negative"` → 0, `"positive"` → 1). The chapter calls this the **prompt-engineering pattern for classification**: *"we will have to instruct the model to do so. Thus, we prefix each document with the prompt 'Is the following sentence positive or negative?'"*
- **[[t5|T5]] (Text-to-Text Transfer Transformer) is an encoder-decoder generative model** — *"its architecture is similar to the original Transformer where 12 decoders and 12 encoders are stacked together"* (per Raffel et al. 2020). T5 was pretrained with **span-corruption masked language modeling** (masking *sets* of tokens / token spans, not individual tokens), then fine-tuned multi-task by **converting each task to a sequence-to-sequence task** and training all simultaneously.
- **[[FLANT5|Flan-T5]] extends T5 with 1,800+ instruction-tuning tasks** per Chung et al. *"Scaling instruction-finetuned language models"* (arXiv:2210.11416, 2022). *"This resulted in the Flan-T5 family of models that benefit from this large variety of tasks."* Flan-T5 comes in five sizes — `flan-t5-small/base/large/xl/xxl` — and the chapter uses **flan-t5-small** for speed (F1 = 0.84). Loaded via Hugging Face Transformers as `"text2text-generation"` task.
- **[[ChatGPT|ChatGPT]] (GPT-3.5) is a closed-source decoder-only model** — *"although the underlying architecture of the original ChatGPT model (GPT-3.5) is not shared, we can assume from its name that it is based on the decoder-only architecture."*
- **ChatGPT was trained in three steps**: (1) base pretraining (next-token prediction), (2) **instruction tuning** on manually-created (instruction, output) pairs, (3) **[[PreferenceFinetuning|preference tuning]]** — generate multiple outputs, have humans rank them best-to-worst, train on the resulting preference data. *"A major benefit of using preference data over instruction data is the nuance it represents. By demonstrating the difference between a good and better output the generative model learns to generate text that resembles human preference."* Forward-references Ch 12 for the mechanisms ([[rlhf|RLHF]] / [[DirectPreferenceOptimization|DPO]]).
- **ChatGPT achieves F1 = 0.91 on Rotten Tomatoes** with the prompt template *"Predict whether the following document is a positive or negative movie review: [DOCUMENT] If it is positive return 1 and if it is negative return 0. Do not give any other answers."* Used `gpt-3.5-turbo-0125`, `temperature=0`, system prompt *"You are a helpful assistant."*
- **Closed-source LLM evaluation is epistemologically limited by [[DataContamination|training-data contamination]]**: *"since we do not know what data the model was trained on, we cannot easily use these kinds of metrics for evaluating the model. For all we know, it might have actually been trained on our dataset!"*
- **OpenAI API usage cost data**: running the 1,066-row Rotten Tomatoes test set on `gpt-3.5-turbo-0125` cost **3 cents** at time of writing (covered by free credits). Rate limits require **[[ExponentialBackoff|exponential backoff]]** — *"performs a short sleep each time we hit a rate limit error and then retries the unsuccessful request."*
- **The chapter's evaluation metric is the weighted-average F1 score from `sklearn.metrics.classification_report`** — chosen to *"make sure each class is treated equally"* on a balanced dataset. The chapter walks through [[ConfusionMatrix|confusion matrix]] → [[Precision|precision]] / [[Recall|recall]] / [[Accuracy|accuracy]] / [[F1Score|F1]] for binary classification.
- **The chapter explicitly endorses [[TFIDF|TF-IDF]] + [[LogisticRegression|logistic regression]] as the baseline**: *"although this book focuses on LLMs, it is highly advised to compare these examples against classic, but strong baselines such as representing text with TF-IDF and training a logistic regression classifier on top of that."*

## Key Quotes

> "A common task in natural language processing is classification. The goal of the task is to train a model to assign a label or class to some input text. ... The impact of language models, both representative and generative, on classification cannot be understated." — Ch 4

> "Classification with pretrained representation models generally comes in two flavors, either using a task-specific model or an embedding model." — Ch 4

> "Although this book focuses on LLMs, it is highly advised to compare these examples against classic, but strong baselines such as representing text with TF-IDF and training a logistic regression classifier on top of that." — Ch 4

> "While generative models, like the GPT family, are incredible models, encoder-only models similarly excel in task-specific use cases and tend to be significantly smaller in size." — Ch 4

> "A major benefit of this separation is that we do not need to fine-tune our embedding model, which can be costly. In contrast, we can train a classifier, like a logistic regression, on the CPU instead." — Ch 4

> "To test this, we can perform zero-shot classification, where we have no labeled data to explore whether the task seems feasible. Although we know the definition of the labels (their names), we do not have labeled data to support them." — Ch 4

> "To perform zero-shot classification with embeddings, there is a neat trick that we can use. We can describe our labels based on what they should represent. ... By describing and embedding the labels and documents, we have data that we can work with." — Ch 4

> "If you are familiar with zero-shot classification with Transformer-based models, you might wonder why we choose to illustrate this with embeddings instead. Although natural language inference models are amazing for zero-shot classification, the example here demonstrates the flexibility of embeddings for a variety of tasks. As you will see throughout the book, embeddings can be found in most Language AI use cases and are often an underestimated but incredibly vital component." — Ch 4

> "Classification with generative language models, such as OpenAI's GPT models, works a bit differently from what we have done thus far. These models take as input some text and generative text and are thereby aptly named sequence-to-sequence models. This is in stark contrast to our task-specific model, which outputs a class instead." — Ch 4

> "Instead of fine-tuning the model for one specific task, each task is converted to a sequence-to-sequence task and trained simultaneously. ... This method of fine-tuning was extended in the paper 'Scaling instruction-finetuned language models,' which introduced more than a thousand tasks during fine-tuning that more closely follow instructions as we know them from GPT models. This resulted in the Flan-T5 family of models that benefit from this large variety of tasks." — Ch 4

> "A major benefit of using preference data over instruction data is the nuance it represents. By demonstrating the difference between a good and better output the generative model learns to generate text that resembles human preference." — Ch 4 (on ChatGPT training)

> "The F1 score of 0.91 already gives a glimpse into the performance of the model that brought generative AI to the masses. However, since we do not know what data the model was trained on, we cannot easily use these kinds of metrics for evaluating the model. For all we know, it might have actually been trained on our dataset!" — Ch 4

## Concepts Introduced or Engaged

- [[TextClassification|Text classification]] — *engaged*, the chapter's primary subject.
- [[SentimentAnalysis|Sentiment analysis]] — *engaged*, the worked instance.
- [[BinarySentimentClassification|Binary sentiment classification]] — *engaged*, the specific task variant.
- [[RepresentationModel|Representation model]] — *engaged*, the encoder-only category.
- [[GenerativeModel|Generative model]] — *engaged*, the decoder-only / encoder-decoder category.
- [[TaskSpecificModel|Task-specific model]] — *new*, a representation model fine-tuned for one downstream task.
- [[EmbeddingModel|Embedding model]] — *new*, a representation model producing general-purpose embeddings.
- [[ZeroShotClassification|Zero-shot classification]] — *new*, classification without labeled training data.
- [[LabelEmbedding|Label embedding]] — *new*, the embedding of a natural-language label description.
- [[GenerativeClassification|Generative classification]] — *new*, classification via prompt → free-text → parse-back-to-label.
- [[ClassificationHead|Classification head]] — *engaged*, the trainable output layer.
- [[LogisticRegression|Logistic regression]] — *engaged*, the chapter's chosen classifier on top of embeddings.
- [[NaturalLanguageInference|Natural language inference]] — *engaged*, contrasted with embedding-based zero-shot.
- [[FewShotLearning|Few-shot learning]] — *engaged via contrast* (zero-shot setting; few-shot covered in Ch 6).
- [[CosineSimilarity|Cosine similarity]] — *engaged*, the label-assignment metric.
- [[F1Score|F1 score]] — *engaged*, the chapter's evaluation metric.
- [[Precision|Precision]] / [[Recall|Recall]] / [[Accuracy|Accuracy]] — *engaged*, classification metrics.
- [[ConfusionMatrix|Confusion matrix]] — *engaged*, the prediction-vs-truth table.
- [[ClassificationReport|Classification report]] — *new*, sklearn's per-class metric summary.
- [[PromptEngineering|Prompt engineering]] — *engaged*, used for generative classification.
- [[InstructionTuning|Instruction tuning]] — *engaged*, the Flan-T5 / ChatGPT training step.
- [[PreferenceFinetuning|Preference finetuning]] — *engaged*, ChatGPT's third training step.
- [[ExponentialBackoff|Exponential backoff]] — *new*, the API-retry pattern.
- [[DataContamination|Data contamination]] / [[BenchmarkContamination|Benchmark contamination]] — *engaged*, the epistemological limit of closed-source LLM evaluation.
- [[TFIDF|TF-IDF]] — *engaged*, recommended baseline.
- [[encoderdecoder|Encoder-decoder]] — *engaged*, T5's architecture.
- [[texttotextframework|Text-to-text framework]] — *engaged*, the T5 framing the chapter uses.
- [[spancorruption|Span corruption]] — *engaged*, T5's pretraining objective the chapter names.
- [[maskedlanguagemodel|Masked language modeling]] — *engaged*, framed as pretraining for representation models.
- [[FineTuning|Fine-tuning]] — *engaged*, contrasted with frozen-model recipes the chapter uses.

## Entities Introduced or Engaged

- [[JayAlammar]] / [[MaartenGrootendorst]] — *engaged*, co-authors.
- [[HandsOnLLM]] — *engaged*, the book.
- [[OReilly]] — *engaged*, the publisher.
- [[HuggingFace]] — *engaged*, source of `datasets`, `transformers`, and all the pretrained models.
- [[RottenTomatoes]] — *new*, the dataset (Pang & Lee 2005; movie reviews; HF `rotten_tomatoes`).
- [[BoPang]] / [[LillianLee]] — *new (passing reference)*, authors of the original Rotten Tomatoes paper *"Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales."*
- [[TwitterRoBERTa]] — *new*, the chapter's task-specific RoBERTa (`cardiffnlp/twitter-roberta-base-sentiment-latest`).
- [[CardiffNLP]] — *new*, the research group behind Twitter-RoBERTa.
- [[RoBERTa]] — *new*, the BERT variant Twitter-RoBERTa is built from.
- [[DistilBERT]] — *new*, the chapter's named alternative task-specific model (SST-2 fine-tuned).
- [[ALBERT]] — *new*, BERT-family baseline named in the model-selection list.
- [[DeBERTa]] — *engaged via passing reference*, also in the BERT-family baseline list (concept page exists from Ch 2).
- [[SentenceTransformers|sentence-transformers]] — *engaged*, the library used for embeddings.
- [[AllMPNetBaseV2|all-mpnet-base-v2]] — *engaged*, the specific embedding model.
- [[MTEB]] — *new*, the Massive Text Embedding Benchmark leaderboard the chapter recommends for model selection.
- [[NilsReimers]] / [[IrynaGurevych]] — *engaged via passing reference*, sentence-transformers authors (Sentence-BERT cited as footnote 6).
- [[sklearn|scikit-learn]] — *new*, the library used for `LogisticRegression` + `classification_report` + `cosine_similarity`.
- [[FLANT5]] — *engaged*, the encoder-decoder generative model.
- [[t5|T5]] — *engaged*, the architecture Flan-T5 is built from.
- [[ColinRaffel]] — *new (passing reference)*, lead T5 author cited as footnote 7.
- [[HyungWonChung]] — *new (passing reference)*, lead Flan-T5 / *"Scaling instruction-finetuned language models"* author cited as footnote 8.
- [[ChatGPT]] — *engaged*, the closed-source decoder-only model.
- [[openai|OpenAI]] — *engaged*, ChatGPT's provider; the chapter uses the OpenAI Python client.
- [[google|Google]] — *engaged*, Flan-T5's provider.
- [[Cohere]] — *engaged via passing reference*, named alongside OpenAI as an embedding-API provider.
- [[microsoft|Microsoft]] — *engaged via passing reference*, MPNet backbone provider (DeBERTa also Microsoft).
- [[bert|BERT]] — *engaged*, the foundational representation model.
- [[GPT3|GPT-3.5]] — *engaged*, ChatGPT's underlying model.

## Connections

- [[hands-on-llm-ch01-introduction-to-llms]] / [[hands-on-llm-ch02-tokens-and-embeddings]] / [[hands-on-llm-ch03-looking-inside-llms]] — predecessor chapters; this is **Part II Ch 1**, the first applications chapter.
- [[RepresentationModel]] / [[GenerativeModel]] — the two-bucket axis from Ch 1 the chapter operationalizes for classification.
- [[bert]] / [[t5]] / [[FLANT5]] / [[ChatGPT]] — the four representative model archetypes the chapter compares.
- [[Embedding]] / [[TextEmbedding]] / [[SentenceEmbedding]] / [[SentenceTransformers]] / [[AllMPNetBaseV2]] — the embedding stack from Ch 2 the chapter reuses.
- [[CosineSimilarity]] — used for both label-embedding zero-shot and (later in the book) semantic search.
- [[NaturalLanguageInference]] / [[SNLI]] — the prior dominant zero-shot approach contrasted with embedding-based zero-shot.
- [[F1Score]] / [[Precision]] / [[Recall]] / [[Accuracy]] / [[ConfusionMatrix]] — the metric vocabulary the chapter introduces.
- [[TFIDF]] / [[LogisticRegression]] — the classical baseline the chapter endorses.
- [[texttotextframework]] / [[spancorruption]] — T5's signature contributions the chapter sketches.
- [[InstructionTuning]] / [[PreferenceFinetuning]] / [[rlhf]] — the post-training pipeline that produces Flan-T5 and ChatGPT.
- [[d2l-nlp-applications]] / [[SentimentAnalysis]] — the wiki's prior sentiment-analysis treatment (D2L on [[IMDb]]); Ch 4's [[RottenTomatoes|Rotten Tomatoes]] is the smaller-but-canonical Hugging-Face-distributed alternative.
- Future chapters: **Ch 10** (creating embedding models — the alternative to using a frozen pretrained embedding), **Ch 11** (fine-tuning representation models — the alternative to using a frozen pretrained task-specific model), **Ch 12** (fine-tuning generative models — covers RLHF / DPO that Ch 4 only names).

## Contradictions

None directly conflicting with existing wiki content. **Soft consistency notes worth flagging**:

- **Zero-shot definition.** The existing [[ZeroShotLearning|Zero-Shot Learning page]] (sourced from [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]]) defines zero-shot in the **prompt-engineering sense**: zero examples in the prompt, model uses prior knowledge. Ch 4 uses zero-shot in the **classification-without-labels sense**: no training labels, only label descriptions + cosine similarity. **Both are correct uses of "zero-shot"** — they share the *"no labeled training data"* core but differ on what the model is asked to do (follow an instruction vs match an embedding). Flagged on the new [[ZeroShotClassification]] page as the classification-specific specialization of the broader [[ZeroShotLearning]] concept.
- **Embedding-based vs NLI-based zero-shot.** Ch 4's *"natural language inference models are amazing for zero-shot classification, the example here demonstrates the flexibility of embeddings for a variety of tasks"* is consistent with [[NaturalLanguageInference|the existing NLI page]] (from [[d2l-nlp-applications]]) — which treats NLI as a text-pair classification task that **can be used as the engine for zero-shot text classification** by casting (document, candidate-label-as-hypothesis) pairs into NLI. The chapter intentionally chooses the embedding route to demonstrate embedding versatility, not because NLI is inferior.
- **T5 architecture detail.** The chapter states *"its architecture is similar to the original Transformer where 12 decoders and 12 encoders are stacked together."* The existing [[t5|T5 page]] (sourced from [[1910.10683-t5]]) lists five sizes — T5-Small (60M), Base (220M), Large (770M), 3B, 11B. The chapter's "12+12" describes the T5-Base size. No contradiction.
- **Flan-T5 sources count.** Ch 4 says *"more than a thousand tasks"* in Flan-T5 instruction tuning; the existing [[FLANT5|Flan-T5 page]] says *"1,800+ tasks"* per Chung et al. 2022. Both are loose paraphrases of the same paper figure (the original paper reports 1,836 tasks). No contradiction.
- **ChatGPT training pipeline.** Ch 4's three-step framing (pretraining → instruction tuning → preference tuning with manually-ranked outputs) is consistent with [[PreferenceFinetuning|the existing Preference Finetuning page]] (from [[ai-engineering-ch02-foundation-models|Huyen Ch 2]]) and the [[ChatGPT|ChatGPT page]]'s [[posttraining|post-training]] treatment. Ch 4's specific mechanism description — *"manually ranked from best to worst"* — matches [[rlhf|RLHF]]'s preference-data construction.
- **F1 score reporting.** Ch 4 uses **weighted-average F1** (treating classes equally on a balanced 533/533 test set). The existing [[F1Score|F1 Score page]] (from [[2507.03152-medval|MedVAL]]) emphasizes **macro-F1** for ordinal multi-class. Both are correct reporting choices for their respective settings — weighted-average and macro-F1 coincide on perfectly balanced binary classification, so no numerical conflict.
- **TF-IDF baseline endorsement.** Ch 4's recommendation that LLM examples be compared against TF-IDF + logistic regression is consistent with the wiki's [[TFIDF|TF-IDF page]] (from [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]) which positions TF-IDF as the classical baseline; consistent with [[ai-engineering-ch04-evaluate-ai-systems|Huyen Ch 4]]'s discipline on baselining; consistent with the wider Made With ML / D2L baselining tradition.

## Position in the wiki

This is the **fourth chapter from *Hands-On Large Language Models*** ingested (after Chs 1–3) and the **wiki's first chapter-length walkthrough of all four pretrained-LLM classification regimes side by side on a single binary task**. It complements rather than replaces the wiki's existing classification coverage:

- Where the existing [[TextClassification|Text Classification page]] (from [[d2l-nlp-applications|D2L NLP Applications]]) is the **architecture-survey** treatment (RNN baseline / textCNN / BERT fine-tuning) and the existing [[SentimentAnalysis|Sentiment Analysis page]] is the **D2L worked-example IMDb walkthrough**, Ch 4 is the **practitioner-comparison-table tour** with side-by-side F1 scores across four pretrained-LLM regimes on a single smaller dataset.
- **First wiki coverage of [[ZeroShotClassification|zero-shot classification via label embeddings + cosine similarity]]** as a distinct technique from prompt-engineering zero-shot or NLI-based zero-shot.
- **First wiki coverage of [[GenerativeClassification|generative classification via instruction prompts + label parsing]]** as a distinct technique for using decoder-only and encoder-decoder LLMs as classifiers.
- **First wiki worked example using `transformers.pipeline` for `text-classification` and `text2text-generation` tasks** (Chs 1–3 used `pipeline("text-generation")` only).
- **First wiki worked example using the OpenAI Chat Completions API** (`gpt-3.5-turbo-0125`, `temperature=0`, system prompt + user prompt).
- **First wiki appearance of the [[RottenTomatoes|rotten_tomatoes]] dataset** as a small / balanced / Hugging-Face-distributed alternative to [[IMDb|D2L's IMDb]] for sentiment-analysis benchmarking.
- **First wiki appearance of [[TwitterRoBERTa|Twitter-RoBERTa]] (`cardiffnlp/twitter-roberta-base-sentiment-latest`)** as a representative task-specific RoBERTa for sentiment.
- **First wiki appearance of the [[MTEB|MTEB leaderboard]]** as the canonical embedding-model selection rubric (forward-reference for Ch 10's embedding-creation chapter).
- **First wiki coverage of [[sklearn|scikit-learn]] as an explicit dependency in the LLM-engineering toolchain** — used in Ch 4 for `LogisticRegression`, `classification_report`, and `cosine_similarity` over embeddings.

Subsequent chapters build on this foundation:
- **Ch 5** (text clustering + topic modeling) is the unsupervised counterpart to Ch 4's supervised + zero-shot classification.
- **Ch 6** (prompt engineering) generalizes the generative-classification prompt pattern Ch 4 introduces.
- **Ch 8** (semantic search + RAG) reuses the same `sentence-transformers/all-mpnet-base-v2` + cosine similarity machinery Ch 4 demonstrates.
- **Chs 10–12** are the **fine-tuning trilogy** that Ch 4's "frozen model" recipes forward-reference: Ch 10 (creating embedding models — the alternative to using `all-mpnet-base-v2` frozen), Ch 11 (fine-tuning representation models — the alternative to using Twitter-RoBERTa frozen), Ch 12 (fine-tuning generative models — covers the [[rlhf|RLHF]] / [[DirectPreferenceOptimization|DPO]] preference tuning Ch 4 only sketches).
