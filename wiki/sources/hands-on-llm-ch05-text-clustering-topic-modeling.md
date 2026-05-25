---
title: "Hands-On LLMs Ch 5 — Text Clustering and Topic Modeling"
type: source
tags: [book, hands-on-llm, oreilly, llm, text-clustering, topic-modeling, bertopic, umap, hdbscan, embeddings, bag-of-words, c-tf-idf, unsupervised]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch05-text-clustering-topic-modeling.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 5 — Text Clustering and Topic Modeling

## Summary

The fifth chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) — and the **unsupervised counterpart** to [[hands-on-llm-ch04-text-classification|Ch 4]]'s supervised + zero-shot classification — codifies a **three-step text-clustering pipeline** (**embed with [[SentenceTransformers|sentence-transformers]] → reduce dimensionality with [[UMAP]] → cluster with [[HDBSCAN]]**) and then extends it via **[[BERTopic]]**, a modular topic-modeling framework authored by Grootendorst himself ([[2203.05794-bertopic|Grootendorst 2022, arXiv:2203.05794]]). The worked dataset is **[[ArXivNLP|ArXiv's Computation and Language (cs.CL) section]]** — **44,949 abstracts** between 1991 and 2024 from [[HuggingFace|Hugging Face]]'s `maartengr/arxiv_nlp`. Embeddings come from `thenlper/gte-small` (384-dim — chosen via the [[MTEB|MTEB leaderboard]] for its **clustering** score + small size + inference speed, replacing Ch 4's `all-mpnet-base-v2`); UMAP reduces 384 → 5 dimensions with `min_dist=0.0`, `metric='cosine'`, `random_state=42`; HDBSCAN with `min_cluster_size=50`, `metric='euclidean'`, `cluster_selection_method='eom'` produces **156 clusters** plus an outlier bucket (label `-1`, 14,520 abstracts unassigned). Manual inspection of cluster 0 surfaces a sign-language-translation theme — *"interesting!"* — but the chapter then transitions away from manual inspection by introducing **topic modeling** as the automatic-cluster-labeling counterpart.

[[BERTopic]] is the chapter's flagship pipeline: a **two-stage modular architecture** where Stage 1 (embed → UMAP → HDBSCAN) is exactly the clustering pipeline above, and Stage 2 represents each cluster via **class-based [[TFIDF|TF-IDF]] (c-TF-IDF)** — a bag-of-words variant that **counts term frequency per cluster** (not per document) and reweights by IDF computed across clusters. The chapter's framing: *"You can think of this modularity as building with Lego blocks; each part of the pipeline is completely replaceable with another, similar algorithm."* Each cluster becomes a topic ranked by c-TF-IDF-weighted vocabulary. For the ArXiv NLP corpus this produces 155 topics (after the outlier topic `-1`) including: topic 0 (speech, asr, recognition, end, acoustic — *automatic speech recognition*), topic 1 (medical, clinical, biomedical, patient — *medical NLP*), topic 2 (sentiment, aspect, analysis, reviews — *sentiment / aspect-based sentiment analysis*), topic 3 (translation, nmt, machine, neural, bleu — *neural machine translation*), topic 22 (topic, topics, lda, latent, dirichlet — *topic modeling*; the BERTopic paper's own abstract is assigned to this topic). The chapter also walks `topic_model.get_topic_info()`, `get_topic(0)`, `find_topics("topic modeling")` (returns topic 22 with similarity 0.95), and a `visualize_documents()` 2D interactive Plotly view backed by a separate UMAP `n_components=2` projection of the same embeddings.

The chapter's **second pedagogical move** is the **representation model** abstraction: BERTopic treats topic-keyword refinement as a **reranking step** on top of c-TF-IDF's initial distribution, applied **once per topic** (not once per document) — a major efficiency claim: *"if we have millions of documents and a hundred topics, the representation block only needs to be applied once for every topic instead of for every document."* Three representation-model families are demonstrated side by side: (1) **[[KeyBERTInspired]]** — embed candidate keywords + per-topic "average document embedding," rerank keywords by cosine similarity, modeled after [[KeyBERT]] (Grootendorst's other open-source NLP package); (2) **[[MaximalMarginalRelevance|Maximal Marginal Relevance (MMR)]]** — iteratively choose the next keyword that is **diverse from already-chosen keywords** yet **relevant to the topic** via a `diversity` parameter; the chapter uses MMR to filter 30 candidate keywords down to 10 diverse ones (e.g. removing the redundant *"summary"* / *"summaries"* / *"summarization"* triple); (3) **[[GenerativeTopicLabeling|text-generation labeling]]** — feed each topic's keywords + 4 most-representative documents (top documents by c-TF-IDF cosine similarity) into a prompt template (`[DOCUMENTS]` / `[KEYWORDS]` tags) and have an LLM **emit a short label** for the topic. The chapter demonstrates this with both [[FLANT5|Flan-T5-small]] via `transformers.pipeline("text2text-generation")` (produces labels like *"Speech-to-description"*, *"Science/Tech"*, *"Summarization"* — some good, some too generic) and [[ChatGPT|GPT-3.5-turbo]] via the [[openai|OpenAI]] API (produces stronger labels like *"Advancements in Aspect-Based Sentiment Analysis"*, *"Neural Machine Translation Enhancements"*). The chapter closes with a `datamapplot` visualization of the top 20 GPT-3.5-labeled topics over the 2D UMAP projection.

The chapter sits at the application layer above [[hands-on-llm-ch01-introduction-to-llms|Ch 1]]'s LLM-history overview, [[hands-on-llm-ch02-tokens-and-embeddings|Ch 2]]'s embedding plumbing ([[SentenceTransformers|sentence-transformers]] + [[BagOfWords|bag-of-words]]), [[hands-on-llm-ch03-looking-inside-llms|Ch 3]]'s Transformer internals, and [[hands-on-llm-ch04-text-classification|Ch 4]]'s classification regimes. It is **Part II Ch 2** of the book — the **unsupervised twin of Ch 4** that **operationalizes the embedding-versatility argument** Ch 4 articulated. It explicitly forward-references **Ch 8** (semantic search) for the **reranking-an-initial-set-of-results** pattern (*"this idea of reranking an initial set of results is a main staple in neural search, a subject that we cover in Chapter 8"*), and closes with a forward-reference to **Ch 6** (prompt engineering — the topic-labeling prompt is its first complex prompt template). The chapter's structural innovation in the wiki: where classical [[LatentDirichletAllocation|LDA]] characterizes each topic by *"a probability distribution of words in a corpus's vocabulary"* via **bag-of-words on the whole corpus**, BERTopic preserves bag-of-words *only for the topic-representation step* and replaces the **topic-discovery step** with embedding-based density clustering — *"our text clustering example does take both [context and meaning] into account as it relies on Transformer-based embeddings that are optimized for semantic similarity and contextual meaning through attention."*

## Key Claims

- **The chapter codifies a three-step text-clustering pipeline that has become the modern default**:
  1. **Embed documents** with an embedding model (Ch 5 uses `thenlper/gte-small` → 384-dim; chosen from the [[MTEB|MTEB leaderboard]] for clustering performance + small size).
  2. **Reduce dimensionality** with [[UMAP]] (384 → 5 dimensions; `n_components=5`, `min_dist=0.0`, `metric='cosine'`, `random_state=42`; *"generally, values between 5 and 10 work well to capture high-dimensional global structures"*). Reduction is needed because *"as the number of dimensions increases, there is an exponential growth in the number of possible values within each dimension. Finding all subspaces within each dimension becomes increasingly complex"* — i.e. the [[CurseOfDimensionality|curse of dimensionality]].
  3. **Cluster** with [[HDBSCAN]] (`min_cluster_size=50`, `metric='euclidean'`, `cluster_selection_method='eom'`). HDBSCAN is a **density-based** algorithm that does not require choosing the number of clusters and explicitly marks unclustered points as **outliers** (label `-1`).
- **The chapter chose density-based clustering ([[HDBSCAN]]) over centroid-based clustering ([[KMeansClustering|k-means]]) because**: (a) the number of clusters is unknown in advance, and (b) ArXiv contains niche papers that should be flagged as outliers rather than forced into a cluster. *"As a density-based method, HDBSCAN can also detect outliers in the data, which are data points that do not belong to any cluster. These outliers will not be assigned or forced to belong to any cluster. In other words, they are ignored."*
- **The default `gte-small` model produces 156 clusters on 44,949 ArXiv NLP abstracts** with the parameters above; 14,520 abstracts are flagged as outliers (topic `-1`). Reducing `min_cluster_size` produces more clusters.
- **Dimensionality reduction is information-lossy**: *"Dimensionality reduction techniques, however, are not flawless. They do not perfectly capture high-dimensional data in a lower-dimensional representation. Information will always be lost with this procedure. There is a balance between reducing dimensionality and keeping as much information as possible."* The chapter uses a separate UMAP `n_components=2` projection for visualization, distinct from the `n_components=5` projection used for clustering.
- **Cosine metric is preferred over Euclidean for UMAP on high-dimensional embeddings**: *"We set metric to 'cosine' as Euclidean-based methods have issues dealing with high-dimensional data."* Inside HDBSCAN, however, the chapter switches back to Euclidean because the UMAP output is already low-dimensional (5D).
- **[[Reproducibility]] tradeoff in UMAP**: *"Setting a random_state in UMAP will make the results reproducible across sessions but will disable parallelism and therefore slow down training."*
- **[[BERTopic]] is a modular topic modeling framework** authored by [[MaartenGrootendorst]] himself ([[2203.05794-bertopic|Grootendorst 2022]]). Its underlying algorithm has two stages: (1) the three-step clustering pipeline above; (2) topic-keyword extraction via **class-based [[TFIDF|TF-IDF]] (c-TF-IDF)**.
- **Class-based TF-IDF (c-TF-IDF)** is the chapter's central technical contribution: instead of TF-IDF on individual documents, BERTopic concatenates all documents in a cluster, computes term frequency **per cluster** (the "c-TF" term), and reweights by an **IDF computed across clusters** (downweighting words that appear across many clusters — e.g., generic stopwords or domain-wide vocabulary). *"BERTopic uses a class-based variant of term frequency–inverse document frequency (c-TF-IDF) to put more weight on words that are more meaningful to a cluster and put less weight on words that are used across all clusters."* Implementation uses `sklearn`'s `CountVectorizer` for the bag-of-words step.
- **The c-TF-IDF formula sketched in the chapter**: *"the IDF value is calculated by taking the logarithm of the average frequency of all words across all clusters divided by the total frequency of each word."* Each word's bag-of-words count in a cluster is multiplied by its IDF weight.
- **Classical [[LatentDirichletAllocation|LDA]] is contrasted with BERTopic on two axes** (Blei, Ng & Jordan 2003): LDA *"assumes that each topic is characterized by a probability distribution of words in a corpus's vocabulary"* — i.e., it operates **on bag-of-words alone**, ignoring word context and semantic meaning. BERTopic preserves bag-of-words only at the topic-representation stage and **replaces the topic-discovery stage** with embedding-based clustering that captures context via Transformer attention.
- **BERTopic's modularity allows each pipeline stage to be swapped independently**: embedding model (sentence-transformers default, replaceable), UMAP (replaceable with PCA), HDBSCAN (replaceable with k-means if outliers are unwanted), c-TF-IDF representation (extensible via representation models). *"You can think of this modularity as building with Lego blocks; each part of the pipeline is completely replaceable with another, similar algorithm."*
- **BERTopic supports many algorithmic variants** sharing the same modular base: guided topic modeling, (semi-)supervised topic modeling, **hierarchical topic modeling**, **dynamic topic modeling** (topics over time), **multimodal topic modeling**, multi-aspect topic modeling, online/incremental topic modeling, zero-shot topic modeling.
- **Outlier handling in BERTopic**: HDBSCAN's outlier label `-1` propagates into BERTopic. To eliminate outliers, the chapter notes two options — (a) swap HDBSCAN for k-means in the pipeline, or (b) use BERTopic's `reduce_outliers()` function to reassign outliers to topics post-hoc.
- **Inspecting BERTopic output**: `topic_model.get_topic_info()` returns a per-topic table with Topic ID, Count, Name (top 4 keywords concatenated with `_`), and full Representation list. `topic_model.get_topic(topic_id)` returns ranked keyword list with c-TF-IDF weights. `topic_model.find_topics("query")` returns the topic IDs most similar to a search query (cosine similarity of query embedding against topic embeddings). `topic_model.topics_[doc_index]` returns the topic assigned to a specific document.
- **Topics found in the ArXiv cs.CL corpus** (selected examples from the chapter):
  | Topic | Count | Top Keywords | Theme |
  |---|---|---|---|
  | -1 | 14,520 | the, of, and, to | Outliers (unclustered) |
  | 0 | 2,290 | speech, asr, recognition, end | Automatic speech recognition |
  | 1 | 1,403 | medical, clinical, biomedical, patient | Medical NLP |
  | 2 | 1,156 | sentiment, aspect, analysis, reviews | Sentiment / aspect-based |
  | 3 | 986 | translation, nmt, machine, neural | Neural machine translation |
  | 22 | — | topic, topics, lda, latent, dirichlet | Topic modeling |
  | 150 | 54 | coherence, discourse, paragraph, text | Discourse coherence |
  | 151 | 54 | prompt, prompts, optimization, prompting | Prompt engineering / optimization |
  | 152 | 53 | sentence, sts, embeddings, similarity | Sentence embeddings / STS |
  | 153 | 53 | counseling, mental, health, therapy | Mental-health NLP |
  | 154 | 50 | backdoor, attacks, attack, triggers | Adversarial / backdoor attacks |

  The total of 155 clusters (0–154) plus topic `-1` matches the 156 unique labels HDBSCAN produced.
- **The BERTopic paper's own abstract is assigned to topic 22** (the topic modeling topic): `topic_model.topics_[titles.index("BERTopic: Neural topic modeling with a class-based TF-IDF procedure")] == 22`. The chapter uses this as a sanity-check vignette.
- **Representation models in BERTopic are reranking blocks layered on top of c-TF-IDF**. Three representative families are demonstrated:
  1. **[[KeyBERTInspired]]** — modeled after Grootendorst's [[KeyBERT]] package. Computes an average document embedding per topic, then reranks candidate keywords by cosine similarity to that topic embedding. Pulls keywords that are semantically related to the cluster.
  2. **[[MaximalMarginalRelevance|MMR (Maximal Marginal Relevance)]]** — Carbonell & Goldstein 1998. Iteratively chooses keywords that are **simultaneously diverse from already-chosen keywords and relevant to the topic**, controlled by a `diversity` parameter (default `0.2`). Used to filter ~30 candidate keywords down to a smaller, diverse ~10-keyword set; removes redundancy (e.g., *"summary"* / *"summaries"* / *"summarization"* → keep one).
  3. **[[GenerativeTopicLabeling|Generative LLM-based topic labeling]]** — feed each topic's top keywords + 4 most-representative documents (top by c-TF-IDF cosine similarity) into a prompt template with `[DOCUMENTS]` and `[KEYWORDS]` placeholders. The model emits a short natural-language label. *"We only need to use the generative model once for every topic, of which there could be potentially hundreds, instead of once for each document, of which there could potentially be millions."*
- **Representation models are applied per topic, not per document** — a major efficiency property: scaling cost is `O(n_topics × representation_cost)` not `O(n_documents × representation_cost)`. This is the same **reranking-an-initial-set** pattern as in [[NeuralSearch|neural search]] (cf. Ch 8) — generate cheap candidates broadly, refine expensively on a small set.
- **Multiple representation models can be stacked or run side by side**. *"You could, for example, use KeyBERTInspired, MMR, and GPT-3.5 side by side to get different perspectives on the same topic."* BERTopic stores `topic_model.topic_representations_` so original c-TF-IDF labels are preserved when representation models are applied.
- **Tradeoffs between representation models**:
  - **c-TF-IDF alone** is fast and preserves domain abbreviations (e.g., *"nmt"* for neural machine translation) but contains redundancy and some stopwords.
  - **KeyBERTInspired** removes nearly all stopwords (because they have weak embedding-similarity signal) but **drops domain abbreviations** the embedding model can't represent — *"words in the original model, like nmt (topic 3), which stands for neural machine translation, are removed as the model could not properly represent the entity. For domain experts, these abbreviations are highly informative."*
  - **MMR** trades top-of-list redundancy for top-of-list breadth; better representations at the cost of small relevance loss.
  - **Flan-T5 labeling** is cheap and local but **prone to overgeneric labels** (e.g., *"Science/Tech"* for medical NLP).
  - **GPT-3.5 labeling** is far more descriptive (*"Advancements in Aspect-Based Sentiment Analysis"*) but requires an [[openai|OpenAI]] API key and tokens.
- **Both KeyBERTInspired and MMR are dimensionality-reduction-free, clustering-free updates** to topic representations. Since they only update the representation step, *"we can update our initial topic representations with KeyBERTInspired without needing to perform the dimensionality reduction and clustering steps."* This is a direct consequence of BERTopic's modular two-stage architecture.
- **The chapter uses scikit-learn's `CountVectorizer`** as the bag-of-words generator under c-TF-IDF — the **second wiki appearance of `sklearn` as an LLM-stack dependency** after [[hands-on-llm-ch04-text-classification|Ch 4]]'s use of `LogisticRegression` / `classification_report` / `cosine_similarity`.
- **`thenlper/gte-small` is the chapter's chosen embedding model** (Li et al., Alibaba DAMO Academy — General Text Embeddings) — 384-dim, faster + higher clustering score than `all-mpnet-base-v2` per the MTEB leaderboard at time of writing. The chapter explicitly recommends checking MTEB for clustering-specific scores.
- **The `[DOCUMENTS]` / `[KEYWORDS]` template** for LLM topic labeling:
  ```
  I have a topic that contains the following documents:
  [DOCUMENTS]

  The topic is described by the following keywords: '[KEYWORDS]'.

  Based on the documents and keywords, what is this topic about?
  ```
  For Flan-T5. For GPT-3.5 the prompt asks for the label in a structured format: *"extract a short topic label in the following format: topic: <short topic label>"*.
- **Visualization options in BERTopic**: `visualize_documents()` (2D Plotly scatter with hover), `visualize_barchart()` (ranked keyword bars per topic), `visualize_heatmap(n_clusters=30)` (inter-topic similarity), `visualize_hierarchy()` (hierarchical topic relationships), `visualize_document_datamap()` (via the `datamapplot` package — labeled 2D landscape).
- **The chapter forward-references reranking as a "main staple in neural search"** — the representation-model abstraction is the topic-modeling instance of the same pattern Ch 8 will use for retrieval.
- **Bag-of-words is not obsolete** — the chapter operationalizes Ch 1's claim *"although bag-of-words is a classic method, it is by no means completely obsolete. In Chapter 5, we will explore how it can still be used to complement more recent language models."* BERTopic is precisely this complement — embeddings for clustering + bag-of-words (c-TF-IDF) for interpretable topic representation.

## Key Quotes

> "Text clustering aims to group similar texts based on their semantic content, meaning, and relationships. ... The recent evolution of language models, which enable contextual and semantic representations of text, has enhanced the effectiveness of text clustering." — Ch 5

> "Language is more than a bag of words, and recent language models have proved to be quite capable of capturing that notion. Text clustering, unbound by supervision, allows for creative solutions and diverse applications, such as finding outliers, speedup labeling, and finding incorrectly labeled data." — Ch 5

> "Although there are many methods for text clustering, from graph-based neural networks to centroid-based clustering techniques, a common pipeline that has gained popularity involves three steps and algorithms: (1) Convert the input documents to embeddings with an embedding model. (2) Reduce the dimensionality of embeddings with a dimensionality reduction model. (3) Find groups of semantically similar documents with a cluster model." — Ch 5

> "Choosing embedding models optimized for semantic similarity tasks is especially important for clustering as we attempt to find groups of semantically similar documents." — Ch 5

> "As the number of dimensions increases, there is an exponential growth in the number of possible values within each dimension. Finding all subspaces within each dimension becomes increasingly complex. As a result, high-dimensional data can be troublesome for many clustering techniques as it gets more difficult to identify meaningful clusters." — Ch 5 (the chapter's [[CurseOfDimensionality|curse-of-dimensionality]] framing)

> "Dimensionality reduction techniques, however, are not flawless. They do not perfectly capture high-dimensional data in a lower-dimensional representation. Information will always be lost with this procedure. There is a balance between reducing dimensionality and keeping as much information as possible." — Ch 5

> "Although a common choice is a centroid-based algorithm like k-means, which requires a set of clusters to be generated, we do not know the number of clusters beforehand. Instead, a density-based algorithm freely calculates the number of clusters and does not force all data points to be part of a cluster." — Ch 5

> "HDBSCAN is a hierarchical variation of a clustering algorithm called DBSCAN that allows for dense (micro)-clusters to be found without having to explicitly specify the number of clusters. As a density-based method, HDBSCAN can also detect outliers in the data, which are data points that do not belong to any cluster." — Ch 5

> "Using any dimensionality reduction technique for visualization purposes creates information loss. It is merely an approximation of what our original embeddings look like. Although it is informative, it might push clusters together and drive them further apart than they actually are. Human evaluation, inspecting the clusters ourselves, is therefore a key component of cluster analysis!" — Ch 5

> "These approaches generally use a bag-of-words technique for the main features of the textual data, which does not take the context nor the meaning of words and phrases into account. In contrast, our text clustering example does take both into account as it relies on Transformer-based embeddings that are optimized for semantic similarity and contextual meaning through attention." — Ch 5 (on classical LDA vs the embedding-based pipeline)

> "BERTopic uses a class-based variant of term frequency–inverse document frequency (c-TF-IDF) to put more weight on words that are more meaningful to a cluster and put less weight on words that are used across all clusters." — Ch 5

> "A major advantage of this pipeline is that the two steps, clustering and topic representation, are largely independent of one another. ... This allows for significant modularity throughout every component of the pipeline." — Ch 5

> "You can think of this modularity as building with Lego blocks; each part of the pipeline is completely replaceable with another, similar algorithm. Through this modularity, newly released models can be integrated within its architecture. As the field of Language AI grows, so does BERTopic!" — Ch 5

> "A major benefit of this approach is that the optimization of topic representations only needs to be done as many times as we have topics. For instance, if we have millions of documents and a hundred topics, the representation block only needs to be applied once for every topic instead of for every document." — Ch 5 (the chapter's representation-model efficiency claim)

> "Note that this idea of reranking an initial set of results is a main staple in neural search, a subject that we cover in Chapter 8." — Ch 5 (forward-reference to Ch 8)

> "Words in the original model, like nmt (topic 3), which stands for neural machine translation, are removed as the model could not properly represent the entity. For domain experts, these abbreviations are highly informative." — Ch 5 (on KeyBERTInspired's domain-abbreviation blind spot)

> "We can use maximal marginal relevance (MMR) to diversify our topic representations. The algorithm attempts to find a set of keywords that are diverse from one another but still relate to the documents they are compared to. ... It filters out redundant words and only keeps words that contribute something new to the topic representation." — Ch 5

> "Both KeyBERTInspired and MMR are amazing techniques for improving the first set of topic representations. KeyBERTInspired especially tends to remove nearly all stop words since it focuses on the semantic relationships between words and documents." — Ch 5

> "We only need to use the generative model once for every topic, of which there could be potentially hundreds, instead of once for each document, of which there could potentially be millions." — Ch 5 (on LLM-based topic labeling)

> "No model is perfect and it is generally advised to generate multiple topic representations. BERTopic allows for all topics to be represented by different representations. You could, for example, use KeyBERTInspired, MMR, and GPT-3.5 side by side to get different perspectives on the same topic." — Ch 5

> "Despite supervised methods like classification being prevalent in recent years, unsupervised approaches such as text clustering hold immense potential due to their ability to group texts based on semantic content without prior labeling." — Ch 5 (closing summary)

## Concepts Introduced or Engaged

- [[TextClustering|Text clustering]] — *new*, the chapter's primary subject.
- [[TopicModeling|Topic modeling]] — *new*, the cluster-labeling counterpart.
- [[DimensionalityReduction|Dimensionality reduction]] — *new*, the chapter's step-2 abstraction.
- [[UMAP|Uniform Manifold Approximation and Projection (UMAP)]] — *new*, the chapter's chosen dimensionality reducer.
- [[HDBSCAN|Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN)]] — *new*, the chapter's chosen clustering algorithm.
- [[DBSCAN|DBSCAN]] — *new*, HDBSCAN's parent algorithm.
- [[DensityBasedClustering|Density-based clustering]] — *new*, the algorithm family HDBSCAN belongs to.
- [[CentroidBasedClustering|Centroid-based clustering]] — *new*, the contrasted clustering family (k-means).
- [[ClassBasedTFIDF|Class-based TF-IDF (c-TF-IDF)]] — *new*, BERTopic's topic-keyword weighting scheme.
- [[BERTopic|BERTopic]] — *new*, the chapter's flagship framework.
- [[KeyBERTInspired|KeyBERTInspired]] — *new*, BERTopic's KeyBERT-inspired keyword-reranker.
- [[MaximalMarginalRelevance|Maximal Marginal Relevance (MMR)]] — *new*, the diversity-vs-relevance keyword selector.
- [[GenerativeTopicLabeling|Generative topic labeling]] — *new*, LLM-based topic-label generation.
- [[LatentDirichletAllocation|Latent Dirichlet Allocation (LDA)]] — *new*, the classical bag-of-words topic model contrasted with BERTopic.
- [[GuidedTopicModeling|Guided topic modeling]] / [[SeededTopicModeling|seeded topic modeling]] — *new*, BERTopic variant.
- [[DynamicTopicModeling|Dynamic topic modeling]] — *new*, BERTopic variant (topics over time).
- [[HierarchicalTopicModeling|Hierarchical topic modeling]] — *new*, BERTopic variant.
- [[SemiSupervisedTopicModeling|Semi-supervised topic modeling]] — *new*, BERTopic variant.
- [[ZeroShotTopicModeling|Zero-shot topic modeling]] — *new*, BERTopic variant.
- [[OnlineTopicModeling|Online / incremental topic modeling]] — *new*, BERTopic variant.
- [[MultimodalTopicModeling|Multimodal topic modeling]] — *new*, BERTopic variant.
- [[Outlier|Outlier detection / handling]] — *engaged*, HDBSCAN label `-1`.
- [[CurseOfDimensionality|Curse of dimensionality]] — *engaged*, the chapter's motivation for UMAP.
- [[BagOfWords|Bag-of-words]] — *engaged*, the foundation of c-TF-IDF.
- [[TFIDF|TF-IDF]] — *engaged*, the foundation of c-TF-IDF.
- [[ReRanking|Reranking]] — *engaged*, the representation-model abstraction.
- [[CosineSimilarity|Cosine similarity]] — *engaged*, used at every stage (UMAP metric, KeyBERTInspired, BERTopic `find_topics`).
- [[Embedding|Embedding]] — *engaged*, the pipeline's input.
- [[SentenceEmbedding|Sentence embedding]] — *engaged*, the embedding granularity.
- [[UnsupervisedLearning|Unsupervised learning]] — *engaged*, the chapter's paradigm.
- [[PCA|PCA]] — *engaged via contrast*, the linear alternative to UMAP.
- [[KMeansClustering|k-means clustering]] — *engaged via contrast*, the centroid-based alternative.
- [[Reproducibility|Reproducibility]] — *engaged via the UMAP `random_state` tradeoff*.

## Entities Introduced or Engaged

- [[JayAlammar]] / [[MaartenGrootendorst]] — *engaged*, co-authors.
- [[HandsOnLLM]] — *engaged*, the book.
- [[OReilly]] — *engaged*, the publisher.
- [[HuggingFace]] — *engaged*, source of the ArXiv NLP dataset (`maartengr/arxiv_nlp`) + all pretrained models.
- [[ArXivNLP]] — *new*, the chapter's dataset (44,949 cs.CL abstracts, 1991–2024; `maartengr/arxiv_nlp` on Hugging Face).
- [[ArXiv]] — *new*, the parent open-access preprint platform.
- [[BERTopic]] — *new*, Grootendorst's modular topic-modeling framework ([[2203.05794-bertopic|Grootendorst 2022, arXiv:2203.05794]]).
- [[KeyBERT]] — *new*, Grootendorst's keyword-extraction package (Grootendorst 2020).
- [[2203.05794-bertopic|BERTopic paper]] — *new*, *"BERTopic: Neural topic modeling with a class-based TF-IDF procedure"* (arXiv:2203.05794).
- [[UMAPLibrary|umap-learn]] — *new*, the Python library implementing UMAP ([[LelandMcInnes|Leland McInnes]] et al.).
- [[HDBSCANLibrary|hdbscan]] — *new*, the Python library implementing HDBSCAN ([[LelandMcInnes|Leland McInnes]], John Healy, Steve Astels — *J. Open Source Softw.* 2.11 (2017): 205).
- [[LelandMcInnes]] — *new (passing reference)*, lead author of UMAP + HDBSCAN.
- [[HaroldHotelling]] — *new (passing reference)*, original PCA author (1933 footnote 1).
- [[MartinEster]] — *new (passing reference)*, DBSCAN author (KDD '96 footnote 4).
- [[DavidBlei]] — *new (passing reference)*, lead LDA author (Blei, Ng & Jordan 2003 footnote 5).
- [[AndrewNg]] — *engaged (passing reference)*, LDA co-author (already a major wiki entity).
- [[MichaelJordan]] — *new (passing reference)*, LDA co-author.
- [[GTESmall|thenlper/gte-small]] — *new*, the chapter's chosen embedding model (Alibaba DAMO General Text Embeddings; 384-dim).
- [[AlibabaDAMOAcademy]] — *new (passing reference)*, the research lab behind GTE.
- [[SentenceTransformers]] — *engaged*, the library used for embeddings (already on wiki from Ch 2 / Ch 4).
- [[FLANT5]] — *engaged*, the encoder-decoder LLM used for topic labeling.
- [[ChatGPT]] / [[GPT35Turbo|gpt-3.5-turbo]] — *engaged*, the closed-source LLM used for topic labeling.
- [[openai|OpenAI]] — *engaged*, the API provider.
- [[google|Google]] — *engaged*, Flan-T5's provider.
- [[sklearn|scikit-learn]] — *engaged*, the library providing `CountVectorizer` for c-TF-IDF.
- [[Plotly]] — *new*, the interactive visualization library powering `visualize_documents()`.
- [[matplotlib]] — *engaged*, used for static 2D scatter plots of clusters.
- [[Datamapplot]] — *new*, the labeled-2D-landscape visualization library used at chapter close.
- [[pandas]] — *engaged*, used to construct the DataFrame for the cluster/outlier 2D plot.
- [[NumPy|numpy]] — *engaged*, used to slice cluster labels with `np.where`.
- [[Gensim]] — *engaged via contrast*, the classical Python topic-modeling library for LDA.

## Connections

- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1's bag-of-words section forward-references this chapter as the place where bag-of-words *"can still be used to complement more recent language models"*; Ch 5 fulfils that promise via c-TF-IDF.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2's [[SentenceTransformers|sentence-transformers]] + 768-dim text-embedding worked example is the direct precursor to Ch 5's embedding step.
- [[hands-on-llm-ch03-looking-inside-llms]] — Ch 3's Transformer-attention treatment is the **why** behind embeddings being able to capture semantic similarity (the load-bearing assumption for the clustering pipeline).
- [[hands-on-llm-ch04-text-classification]] — Ch 4 is the supervised + zero-shot counterpart; Ch 5 is the unsupervised twin. Both use `sentence-transformers` + cosine similarity + `sklearn`. Ch 4's MTEB-leaderboard recommendation is reused in Ch 5 (this time for clustering scores).
- [[hands-on-llm-ch06-prompt-engineering]] — Ch 6 forward-reference (topic-labeling prompt is the chapter's first complex prompt template).
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 forward-reference (representation-model reranking is *"a main staple in neural search"*).
- [[BERTopic]] / [[KeyBERT]] / [[MaartenGrootendorst]] — the author-pipeline thread: Grootendorst's open-source packages are the chapter's core tools.
- [[BagOfWords]] / [[TFIDF]] / [[ClassBasedTFIDF]] — the pre-neural representation lineage culminating in BERTopic's c-TF-IDF.
- [[LatentDirichletAllocation]] / [[Gensim]] — the classical topic-modeling baseline.
- [[UMAP]] / [[HDBSCAN]] / [[DBSCAN]] / [[PCA]] / [[KMeansClustering]] — the clustering/reduction algorithm landscape.
- [[CosineSimilarity]] / [[Embedding]] / [[SentenceEmbedding]] — the embedding stack the chapter operates over.
- [[ReRanking]] — the representation-model abstraction is reranking applied to topic keywords.
- [[MTEB]] — the embedding-model selection rubric the chapter uses (now applied to the **clustering** column of the MTEB leaderboard).
- [[sklearn]] — provides `CountVectorizer` for the c-TF-IDF bag-of-words step.
- [[TopicClustering]] — the existing wiki page (from [[leh-ch05-supervised-fine-tuning|LEH Ch 5]]) — gets substantially expanded here with the BERTopic-specific pipeline.
- [[UnsupervisedLearning]] / [[CurseOfDimensionality]] — engaged as foundational concepts.
- [[HierarchicalClustering]] / [[Dendrogram]] — sibling clustering concepts.

## Contradictions

No direct contradictions with existing wiki content. **Soft consistency notes worth flagging**:

- **[[TopicClustering|Existing TopicClustering page]]** (from [[leh-ch05-supervised-fine-tuning|LEH Ch 5]]) names the same pipeline (sentence-transformers → UMAP → HDBSCAN → LLM auto-label) but in a single paragraph; Ch 5 is the **full pedagogical walkthrough** of that pipeline. Both sources agree on the pipeline; LEH Ch 5 names Hugging Face's `text-clustering` package, [[NomicAtlas]], BunkaTopics, and Lilac as tools, while Ch 5 names [[BERTopic]] (Grootendorst's own framework). **Not a contradiction** — they cover different tooling for the same underlying pipeline.
- **[[BagOfWords|Existing BagOfWords page]]** (from [[hands-on-llm-ch01-introduction-to-llms|Ch 1]]) closes with *"Although bag-of-words is a classic method, it is by no means completely obsolete. In Chapter 5, we will explore how it can still be used to complement more recent language models."* Ch 5 **fulfils** this forward-reference via c-TF-IDF. Consistent.
- **[[TFIDF|Existing TF-IDF page]]** (from [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]) treats TF-IDF as a **retrieval scoring function** (`Score(D, Q) = Σ IDF(t) × f(t, D)`); Ch 5's **class-based variant** (c-TF-IDF) computes term frequency **per cluster** instead of per document and computes IDF **across clusters** instead of across documents. The IDF formula sketched in Ch 5 (*"logarithm of the average frequency of all words across all clusters divided by the total frequency of each word"*) is a BERTopic-specific reformulation; this is **a different application** of TF-IDF, not a contradiction. A new [[ClassBasedTFIDF]] page captures the BERTopic variant.
- **[[MTEB|MTEB]] use in Ch 4 vs Ch 5**: Ch 4 used `all-mpnet-base-v2` based on MTEB; Ch 5 uses `thenlper/gte-small` based on MTEB's **clustering** column specifically. The chapter explicitly notes *"It is a more recent model that outperforms the previous model on clustering tasks."* This is consistent — both chapters use MTEB as the selection rubric; the **task-specific column** matters.
- **[[KMeansClustering|Existing k-means page]]** — Ch 5 contrasts k-means (centroid-based, requires `K`, forces every point into a cluster) with HDBSCAN (density-based, finds `K` automatically, marks outliers). Both characterizations match the existing page. The chapter's added wrinkle: HDBSCAN can be *swapped out for k-means* in the BERTopic pipeline if outliers are undesired.
- **[[HierarchicalClustering|Existing HierarchicalClustering page]]** — this is agglomerative clustering with dendrograms ([[islr-seventh-printing|ISLR]] Ch 10). HDBSCAN's *"hierarchical"* refers to a different mechanism (hierarchy of density-based clusters at varying scales, condensed to flat clusters). **No contradiction**, but worth flagging that the two senses of *"hierarchical clustering"* differ — one is agglomerative-bottom-up-with-linkage, the other is density-based-with-condensed-tree.
- **Reranking** ([[ReRanking|existing page]] from [[leh-ch04-rag-feature-pipeline|LEH Ch 4]] / [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]) is treated there as **post-retrieval cross-encoder rescoring**; Ch 5 uses *"reranking"* for **representation-model refinement of topic keywords**. Both are instances of the same pattern — *"generate cheap candidates broadly, refine expensively on a small set"* — but apply at different granularities. The Ch 5 framing makes this connection explicit: *"this idea of reranking an initial set of results is a main staple in neural search."*

## Position in the wiki

This is the **fifth chapter from *Hands-On Large Language Models*** ingested (after Chs 1–4) and the **wiki's first end-to-end pedagogical walkthrough of modern unsupervised text analysis** — embed → reduce → cluster → represent. It complements rather than replaces the wiki's existing clustering and topic-modeling coverage:

- The existing [[TopicClustering|TopicClustering page]] (from [[leh-ch05-supervised-fine-tuning|LEH Ch 5]]) named the same pipeline in a single paragraph; Ch 5 is the **chapter-length walkthrough**, with a runnable worked example on a real dataset.
- The existing [[HierarchicalClustering|HierarchicalClustering]] / [[KMeansClustering|k-means]] / [[PCA]] / [[CurseOfDimensionality]] pages cover the **classical-ML side**; Ch 5 connects these to the **modern LLM-embedding side** for the first time.
- [[Gensim|Gensim page]] (from Ch 2) covered LDA / word2vec as **classical Python NLP**; Ch 5 introduces [[LatentDirichletAllocation|LDA]] as the **explicit baseline contrasted with BERTopic**.
- **First wiki coverage of [[BERTopic]]** as a named framework (previously only mentioned in passing on [[MaartenGrootendorst|Grootendorst's entity page]]).
- **First wiki coverage of [[KeyBERT]]** as a named keyword-extraction package.
- **First wiki coverage of [[UMAP]] and [[HDBSCAN]]** as named concepts (previously only mentioned in passing on the [[TopicClustering]] page).
- **First wiki coverage of [[ClassBasedTFIDF|c-TF-IDF]]** as a topic-representation weighting scheme.
- **First wiki coverage of [[MaximalMarginalRelevance|MMR]]** as a diversity-vs-relevance ranking algorithm.
- **First wiki coverage of [[KeyBERTInspired]]** as a BERTopic representation block.
- **First wiki coverage of [[GenerativeTopicLabeling]]** as the per-topic prompt-engineering pattern.
- **First wiki coverage of [[DensityBasedClustering]]** as a clustering family.
- **First wiki coverage of [[Outlier|outlier handling]] in clustering** as an explicit pipeline-output concern.
- **First wiki appearance of the [[ArXivNLP|ArXiv NLP dataset]] (`maartengr/arxiv_nlp`)** as a benchmark for clustering / topic modeling.
- **First wiki appearance of [[GTESmall|gte-small]]** as a clustering-optimized embedding model alternative to `all-mpnet-base-v2`.
- **Second wiki appearance of [[sklearn|scikit-learn]] as an explicit LLM-stack dependency** (after Ch 4) — this time providing `CountVectorizer` for c-TF-IDF.

Subsequent chapters build on this foundation:
- **Ch 6** (prompt engineering) generalizes the `[DOCUMENTS]` / `[KEYWORDS]` topic-labeling prompt pattern.
- **Ch 8** (semantic search + RAG) uses the same **reranking-an-initial-set** pattern that Ch 5's representation-model abstraction operationalizes.
- **Ch 10** (creating text embedding models) is the upstream of Ch 5's embedding step — once you can train your own embedding model, your clustering pipeline's quality ceiling rises.
- **Ch 11** (fine-tuning representation models) shows how to fine-tune the [[RepresentationModel|representation model]] feeding the clustering pipeline for domain-specific clustering.
