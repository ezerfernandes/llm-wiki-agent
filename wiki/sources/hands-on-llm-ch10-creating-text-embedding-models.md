---
title: "Hands-On LLMs Ch 10 — Creating Text Embedding Models"
type: source
tags: [book, hands-on-llm, oreilly, llm, embeddings, sentence-embedding, contrastive-learning, sbert, sentence-transformers, siamese-network, bi-encoder, cross-encoder, mean-pooling, cls-pooling, mnr-loss, cosine-similarity-loss, softmax-loss, multiple-negatives-ranking, in-batch-negatives, hard-negatives, semi-hard-negatives, nli, mnli, stsb, mteb, augmented-sbert, tsdae, simcse, contrastive-tension, gpl, domain-adaptation, adaptive-pretraining, masked-language-modeling, fine-tuning, unsupervised-learning]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch10-creating-text-embedding-models.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 10 — Creating Text Embedding Models

## Summary

The tenth chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) and the **opener of Part III ("Training and Fine-Tuning Language Models")** — the first chapter in the book that crosses from *using* pretrained models to *creating* them. Ch 10 is the **runnable-code resolution of every forward reference** prior chapters parked on it: [[hands-on-llm-ch02-tokens-and-embeddings|Ch 2]]'s *"contrastive training is the prototype of any model that takes two vectors and predicts a relation,"* [[hands-on-llm-ch04-text-classification|Ch 4]]'s embedding-as-feature pipeline that relies on `all-mpnet-base-v2`'s contrastive pretraining, [[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]'s *"choose your embedding model from MTEB's clustering column"* discipline, [[hands-on-llm-ch08-semantic-search-and-rag|Ch 8]]'s *"language models need to be trained on question-answer pairs to become better at retrieval — explained in Chapter 10,"* and [[hands-on-llm-ch09-multimodal-llms|Ch 9]]'s *"we will go in depth into [contrastive learning's] inner workings in Chapter 10 where we will create our own embedding model."* The chapter is the **end-to-end recipe** for building a [[SentenceTransformers|sentence-transformers]]-style [[BiEncoder|bi-encoder]] from scratch on [[bert|BERT]]-base-uncased, fine-tuning a pretrained `all-MiniLM-L6-v2` on domain data, and then handling the two real-world data-scarcity regimes that production embedding-model work actually encounters: **few labels available** ([[AugmentedSBERT]]) and **no labels available** ([[TSDAE]]).

Ch 10 walks **five training/fine-tuning regimes** on the same [[MNLI]] subset (50,000 sentence pairs from [[GLUE]]) with the same [[STSB|STS-B]] evaluator (Pearson cosine on `glue/stsb/validation` rescaled to `[0,1]`), so the reader can read the regime's recipe and its STS score side by side as a ladder:

| Regime | Loss | Base model | Data | STS-B Pearson cosine |
|---|---|---|---|---|
| Train-from-scratch | [[SoftmaxLoss]] | `bert-base-uncased` | 50k MNLI | **0.59** |
| Train-from-scratch | [[CosineSimilarityLoss]] | `bert-base-uncased` | 50k MNLI (relabeled 0/1) | **0.72** |
| Train-from-scratch | [[MultipleNegativesRankingLoss\|MNR loss]] | `bert-base-uncased` | 16,875 entailment triplets | **0.80** |
| Fine-tune | [[MultipleNegativesRankingLoss\|MNR loss]] | `all-MiniLM-L6-v2` | 50k MNLI | **0.85** |
| Data augmentation | [[CosineSimilarityLoss]] | `bert-base-uncased` | 10k gold + 40k silver ([[AugmentedSBERT]]) | **0.71** |
| Unsupervised | [[DenoisingAutoEncoderLoss]] | `bert-base-uncased` ([CLS] pooling) | 50k unlabeled MNLI sentences ([[TSDAE]]) | **0.70** |

The ladder is **the chapter's central pedagogical claim**: loss-function choice can move STS-B by **20+ points** on the same data (softmax 0.59 → MNR 0.80), and fine-tuning a pretrained model on a small subset (0.85) outperforms training-from-scratch on the full dataset — but **even unsupervised TSDAE with no labels reaches 0.70**, which is within striking distance of supervised cosine-loss training (0.72). The order of effect-sizes is: **loss function > base model > supervision level > data quantity**.

The chapter introduces **the [[SBERTArchitecture|SBERT architecture]] as the modern default**: a [[SiameseNetwork|siamese / bi-encoder]] of two weight-tied [[bert|BERT]] models, [[MeanPooling|mean-pooled]] over the final layer, optimized with a contrastive objective. The architectural contrast is the [[CrossEncoder|cross-encoder]] — *"a cross-encoder allows two sentences to be passed to the Transformer network simultaneously to predict the extent to which the two sentences are similar"* — which is more accurate but **does not produce reusable embeddings** and scales as $n(n-1)/2$ inference calls for $n$ sentences (49,995,000 for $n=10{,}000$). Sentence-BERT's elegant alternative: drop the classification head, [[MeanPooling|mean-pool]] the final layer, train siamese — *"this ensures a fixed-size embedding."*

The chapter codifies the **[[ContrastiveLearning|contrastive-learning]] data-construction discipline** the wiki had only seen in fragments before: the [[NLI]] dataset structure (premise/hypothesis/entailment-or-contradiction-or-neutral) is itself a **contrastive-learning data source** — entailments are positives, contradictions are negatives, neutrals can be ignored or treated as negatives depending on the loss. This is the [[hands-on-llm-ch09-multimodal-llms|Ch 9]] *"negatives are required"* observation extended to a **specific data-mining recipe** for text-only embeddings.

The **[[HardNegatives|hard-negatives]] taxonomy** the chapter introduces is a wiki-first contribution: **easy negatives** (random documents — what [[InBatchNegatives|in-batch negatives]] from MNR loss actually produce), **semi-hard negatives** (cosine-similar but not the right answer — minable from a pretrained embedding model), **hard negatives** (related-but-wrong — the kind production embedding models actually need; usually require manual labeling or generative-model labeling). Ch 10's canonical worked example: question = *"How many people live in Amsterdam?"* → positive = *"Almost a million people live in Amsterdam"* → hard negative = *"More than a million people live in Utrecht, which is more than Amsterdam"* (related to Amsterdam, related to population, but wrong city).

The **two fine-tuning workhorses** Ch 10 walks at code level fill specific data-availability regimes:

- **[[AugmentedSBERT]]** (Thakur, Reimers et al. 2020, arXiv:2010.08240) — *"a way to augment your data such that an embedding model can be fine-tuned when there is only a little labeled data available."* Train an accurate-but-slow [[CrossEncoder|cross-encoder]] on a small **gold dataset**, use it to label a much larger pool of unlabeled pairs into a **silver dataset**, then train the fast [[BiEncoder|bi-encoder]] (SBERT) on the gold + silver union. Ch 10's worked example uses **10,000 gold + 40,000 silver** and achieves STS-B = 0.71 — *"the original cosine similarity loss example had a score of 0.72 with the full dataset. Using only 20% of that data, we managed to get a score of 0.71!"*
- **[[TSDAE]]** (Wang, Reimers & Gurevych 2021, arXiv:2104.06979) — *"Transformer-based Sequential Denoising Auto-Encoder"* — for **no labels at all**. Add noise to a sentence (delete a percentage of words at random), encode the damaged sentence with [[CLSPooling|[CLS]-token pooling]] (not mean-pooling — *"in the TSDAE paper, this was shown to be more effective since mean pooling loses the position information"*), decode back to the original. Ch 10's TSDAE run with **50,000 unlabeled sentences** reaches STS-B = 0.70 — *"quite impressive considering we did all this training with unlabeled data."*

The chapter closes on **[[DomainAdaptation|domain adaptation]] via [[AdaptivePretraining|adaptive pretraining]]**: when target-domain vocabulary diverges from the source domain (medical, legal, financial), the recipe is to first run **TSDAE** (or [[MaskedLanguageModel|masked language modeling]]) on the target-domain corpus unsupervised, then fine-tune that model on either in-domain or out-of-domain labeled pairs — *"although data from the target domain is preferred, out-domain data also works since we started with unsupervised training on the target domain."* The book promises Ch 11 will walk the [[MaskedLanguageModel|MLM]] half of this recipe.

## Key Claims

### Embedding models and the goal of training them

- **Embedding models convert text to numerical vectors that capture meaning.** *"This process of embedding the input is typically performed by an LLM, which we refer to as an embedding model. The main purpose of such a model is to be as accurate as possible in representing the textual data as an embedding."*
- **Accuracy means semantic similarity is preserved in the geometry.** *"We expect vectors of documents that are similar to one another to be similar, whereas the embeddings of documents that each discuss something entirely different should be dissimilar."* Embeddings live in **high-dimensional space**; 2-D visualizations are pedagogical simplifications.
- **Embedding-model training is steerable to any notion of similarity.** *"By presenting the model with enough examples of semantically similar documents, we can steer toward semantics whereas using examples of sentiment would steer it in that direction."* (Worked example: training on sentiment-paired data produces an embedding model whose geometry clusters by sentiment instead of by topic — useful for downstream sentiment classification.)

### Contrastive learning

- **[[ContrastiveLearning|Contrastive learning]] is the dominant technique for text embedding models.** *"Contrastive learning is a technique that aims to train an embedding model such that similar documents are closer in vector space while dissimilar documents are further apart. ... it's very similar to the word2vec method from Chapter 2."*
- **The underlying mechanism: similarity is learned by contrast.** *"The best way to learn and model similarity/dissimilarity between documents is by feeding a model examples of similar and dissimilar pairs."* This relates to the philosophical concept of **contrastive explanation** — Tim Miller 2021 (*"Contrastive explanation: A structural-model approach,"* The Knowledge Engineering Review 36: e14): *"understanding a particular case, 'Why P?' in contrast to alternatives, 'Why P and not Q?'"* The chapter's anecdotal frame is the bank robber asked *"Why did you rob a bank?"* who answers *"Because that is where the money is"* — a contrastive question (*"Why rob banks instead of obeying the law?"*) would have produced a more useful answer.
- **The contrast teaches the model both similarity AND dissimilarity.** *"By providing the contrast between two concepts, it starts to learn the features that define the concept but also the features that are not related. We get more information when we frame a question as a contrast."*
- **[[Word2Vec|word2vec]] is the historical predecessor.** *"One of the earliest and most popular examples of contrastive learning in NLP is actually word2vec. ... a word close to a target word in a sentence will be constructed as a positive pair whereas randomly sampled words constitute dissimilar pairs."*

### SBERT architecture

- **[[SBERT]] / [[SentenceTransformers|sentence-transformers]] fixed the computational overhead of BERT-for-similarity.** *"Before sentence-transformers, sentence embeddings often used an architectural structure called cross-encoders with BERT. ... the number of computations rises quickly when you want to find the highest pair in a collection of 10,000 sentences. That would require $n \cdot (n-1)/2 = 49{,}995{,}000$ inference computations and therefore generates significant overhead. Moreover, a cross-encoder generally does not generate embeddings."*
- **The SBERT modification: drop the classification head, mean-pool, train siamese.** *"In sentence-transformers the classification head is dropped, and instead mean pooling is used on the final output layer to generate an embedding. This pooling layer averages the word embeddings and gives back a fixed dimensional output vector. This ensures a fixed-size embedding."*
- **The training uses a Siamese architecture.** *"We have two identical BERT models that share the same weights and neural architecture. These models are fed the sentences from which embeddings are generated through the pooling of token embeddings. Then, models are optimized through the similarity of the sentence embeddings. Since the weights are identical for both BERT models, we can use a single model and feed it the sentences one after the other."*
- **The original SBERT training pass:** *"During training, the embeddings for each sentence are concatenated together with the difference between the embeddings. Then, this resulting embedding is optimized through a softmax classifier."* (This is the *softmax loss* the chapter later names as suboptimal compared to MNR and cosine losses.)
- **The bi-encoder / cross-encoder tradeoff is restated.** *"The resulting architecture is also referred to as a bi-encoder or SBERT for sentence-BERT. Although a bi-encoder is quite fast and creates accurate sentence representations, cross-encoders generally achieve better performance than a bi-encoder but do not generate embeddings."*
- **Reference:** Nils Reimers and Iryna Gurevych. *"Sentence-BERT: Sentence embeddings using Siamese BERT-networks."* arXiv:1908.10084 (2019).

### Data construction — natural language inference

- **[[NLI|Natural language inference (NLI)]] datasets are the standard pretraining-data source for contrastive sentence embeddings.** *"When pretraining your embedding model, you will often see data being used from natural language inference (NLI) datasets. NLI refers to the task of investigating whether, for a given premise, it entails the hypothesis (entailment), contradicts it (contradiction), or neither (neutral)."*
- **NLI labels map directly to contrastive labels.** *"If you look closely at entailment and contradiction, then they describe the extent to which two inputs are similar to one another. As such, we can use NLI datasets to generate negative examples (contradictions) and positive examples (entailments) for contrastive learning."*
- **The chapter uses [[GLUE]]'s [[MNLI|MNLI]] subset.** *"The General Language Understanding Evaluation benchmark (GLUE). This GLUE benchmark consists of nine language understanding tasks. ... One of these tasks is the Multi-Genre Natural Language Inference (MNLI) corpus, which is a collection of 392,702 sentence pairs annotated with entailment (contradiction, neutral, entailment). We will be using a subset of the data, 50,000 annotated sentence pairs."*
- **Smaller datasets make training more unstable.** *"The smaller the dataset, the more unstable training or fine-tuning an embedding model is. If possible, larger datasets are preferred assuming it is still quality data."*

### Train from scratch — code recipe

```python
from sentence_transformers import SentenceTransformer, losses
from sentence_transformers.training_args import SentenceTransformerTrainingArguments
from sentence_transformers.trainer import SentenceTransformerTrainer
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator
from datasets import load_dataset

train_dataset = load_dataset("glue", "mnli", split="train").select(range(50_000))
train_dataset = train_dataset.remove_columns("idx")

embedding_model = SentenceTransformer('bert-base-uncased')
train_loss = losses.SoftmaxLoss(
    model=embedding_model,
    sentence_embedding_dimension=embedding_model.get_sentence_embedding_dimension(),
    num_labels=3,
)

val_sts = load_dataset("glue", "stsb", split="validation")
evaluator = EmbeddingSimilarityEvaluator(
    sentences1=val_sts["sentence1"],
    sentences2=val_sts["sentence2"],
    scores=[s/5 for s in val_sts["label"]],
    main_similarity="cosine",
)

args = SentenceTransformerTrainingArguments(
    output_dir="base_embedding_model",
    num_train_epochs=1,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=32,
    warmup_steps=100,
    fp16=True,
    eval_steps=100,
    logging_steps=100,
)

trainer = SentenceTransformerTrainer(
    model=embedding_model,
    args=args,
    train_dataset=train_dataset,
    loss=train_loss,
    evaluator=evaluator,
)
trainer.train()
```

- **By default sentence-transformers unfreezes all layers.** *"By default, all layers of an LLM in sentence-transformers are trainable. Although it is possible to freeze certain layers, it is generally not advised since the performance is often better when unfreezing all layers."*
- **`microsoft/mpnet-base` is the recommended alternative base** to `bert-base-uncased` for word embeddings.

### Evaluation — STS-B + MTEB

- **[[STSB|Semantic Textual Similarity Benchmark (STS-B)]] is the chapter's standard evaluator.** *"A collection of human-labeled sentence pairs, with similarity scores between 1 and 5"* — rescaled to `[0,1]` by dividing by 5.
- **`EmbeddingSimilarityEvaluator` outputs Pearson/Spearman cosine, manhattan, euclidean, and dot.** *"The one we are interested in most is 'pearson_cosine', which is the cosine similarity between centered vectors. It is a value between 0 and 1 where a higher value indicates higher degrees of similarity."*
- **A good embedding model is more than STS-B.** *"To unify this evaluation procedure, the Massive Text Embedding Benchmark ([[MTEB]]) was developed. The MTEB spans 8 embedding tasks that cover 58 datasets and 112 languages."* — Niklas Muennighoff et al. 2022, arXiv:2210.07316.
- **Evaluation time is part of the [[MTEB]] output** alongside accuracy/F1 — *"although many embedding models exist, we typically want those that are both accurate and have low latency."* For Ch 10's worked `Banking77Classification` task, evaluation time = 31.83 s.
- **The chapter uses STS-B (not full MTEB) for illustration** to keep runtimes short — *"testing your model on the entire MTEB can take a couple of hours depending on your GPU."*

### Loss functions — the chapter's central knob

- **Softmax loss was the first sentence-transformers loss but is not advised today.** *"Softmax loss is generally not advised as there are more performant losses."*
- **Two recommended losses:** **[[CosineSimilarityLoss|cosine similarity loss]]** and **[[MultipleNegativesRankingLoss|multiple negatives ranking (MNR) loss]]**.
- **Other notable losses:** `MarginMSE` (for training/fine-tuning [[CrossEncoder|cross-encoders]]).

#### Cosine similarity loss

- **The intuitive default.** *"The cosine similarity loss is an intuitive and easy-to-use loss that works across many different use cases and datasets. It is typically used in semantic textual similarity tasks."*
- **Data format: pairs with a similarity score in [0,1].** *"Instead of having strictly positive or negative pairs of sentences, we assume pairs of sentences that are similar or dissimilar to a certain degree. Typically, this value lies between 0 and 1 to indicate dissimilarity and similarity, respectively."*
- **Computation:** Compute cosine similarity of the two sentence embeddings, compare to the labeled similarity score, minimize the deviation. *"The model will learn to recognize the degree of similarity between sentences."*
- **NLI label mapping for cosine loss:** entailment (0) → 1.0; neutral (1) → 0.0; contradiction (2) → 0.0. *"The entailment represents a high similarity between the sentences, so we give it a similarity score of 1. In contrast, since both neutral and contradiction represent dissimilarity, we give these labels a similarity score of 0."*
- **Worked result on 50k MNLI:** STS-B Pearson cosine = **0.72** (vs softmax's 0.59).

#### Multiple negatives ranking (MNR) loss

- **Also known as [[InfoNCE]] / [[NTXentLoss|NT-Xent]] loss.** *"Multiple negatives ranking (MNR) loss, often referred to as InfoNCE or NTXentLoss"* — Henderson et al. 2017 (arXiv:1705.00652, *"Efficient natural language response suggestion for smart reply"*), Oord, Li & Vinyals 2018 (arXiv:1807.03748, *"Representation learning with contrastive predictive coding"*), Chen et al. 2020 (*"A simple framework for contrastive learning of visual representations,"* SimCLR, ICML).
- **Data format: positive pairs (or anchor/positive/negative triplets).** *"You might have pairs of question/answer, image/image caption, paper title/paper abstract, etc. The great thing about these pairs is that we can be confident they are hard positive pairs."*
- **[[InBatchNegatives|In-batch negatives]] are how MNR generates contrasts.** *"Negative pairs are constructed by mixing a positive pair with another positive pair. ... These negatives are called in-batch negatives and can also be used to generate the triplets."*
- **Larger batch sizes make MNR harder (and therefore better).** *"Larger batch sizes tend to work better with multiple negative rankings (MNR) loss as a larger batch makes the task more difficult. ... the model needs to find the best matching sentence from a larger set of potential pairs of sentences."*
- **The classification framing of MNR:** *"After having generated these positive and negative pairs, we calculate their embeddings and apply cosine similarity. These similarity scores are then used to answer the question, are these pairs negative or positive? In other words, it is treated as a classification task and we can use cross-entropy loss to optimize the model."*
- **MNR-loss data construction on MNLI:** filter to entailment-only rows (50k → 16,875), use premise as anchor, entailment hypothesis as positive, **shuffle the hypothesis column** to generate soft random negatives. The downside the chapter flags: in-batch negatives produce **easy negatives** — often completely unrelated to the question — and *"the embedding model's task of then finding the right answer to a question becomes quite easy."*
- **Worked result on 16,875 MNLI entailment triplets:** STS-B Pearson cosine = **0.80**.

#### Easy / semi-hard / hard negatives

- **[[HardNegatives|Hard negatives]] are negatives that are related to the question but are not the right answer.** *"We would like to have negatives that are very related to the question but not the right answer. ... Since this would make the task more difficult for the embedding model as it has to learn more nuanced representations, the embedding model's performance generally improves quite a bit."*
- **Canonical hard-negative example:**
  - Question: *"How many people live in Amsterdam?"*
  - Positive: *"Almost a million people live in Amsterdam."*
  - Easy negative: random unrelated sentence (what in-batch negatives produce).
  - Semi-hard negative: related to Amsterdam OR to population, but not both — *"this does not lead to hard negatives since this method merely finds similar sentences, not question/answer pairs."*
  - Hard negative: *"More than a million people live in Utrecht, which is more than Amsterdam"* (related to Amsterdam, related to population, but wrong city / wrong answer).
- **Three negative-mining recipes:**
  - **Easy negatives** — randomly sample documents (what MNR's in-batch sampling produces by default).
  - **Semi-hard negatives** — *"using a pretrained embedding model, we can apply cosine similarity on all sentence embeddings to find those that are highly related."*
  - **Hard negatives** — *"need to be either manually labeled (for instance, by generating semi-hard negatives) or you can use a generative model to either judge or generate sentence pairs."*

### Fine-tuning a pretrained embedding model

- **Fine-tuning from a pretrained [[SentenceTransformers|sentence-transformers]] model is cheaper than training from scratch.** *"The sentence-transformers framework allows nearly all embedding models to be used as a base for fine-tuning. We can choose an embedding model that was already trained on a large amount of data and fine-tune it for our specific data or purpose."*
- **`all-MiniLM-L6-v2` is the recommended fine-tuning base.** *"All-MiniLM-L6-v2 performs well across many use cases and due to its small size is quite fast."*
- **Worked supervised fine-tune:** swap `bert-base-uncased` for `sentence-transformers/all-MiniLM-L6-v2`, keep MNR loss + 50k MNLI triplets. **Result: STS-B = 0.85** — the highest score in the chapter. *"Although a score of 0.85 is the highest we have seen thus far, the pretrained model that we used for fine-tuning was already trained on the full MNLI dataset, whereas we only used 50,000 examples."*
- **The bottleneck shifts from compute to data quality.** *"The main difficulty of training or fine-tuning your model is finding the right data. With these models, we not only want to have very large datasets, but the data in itself needs to be of high quality."*
- **[[DomainAdaptation|Domain adaptation]] preview:** *"Instead of using a pretrained BERT model like 'bert-base-uncased' or a possible out-of-domain model like 'all-mpnet-base-v2', you can also perform masked language modeling on the pretrained BERT model to first adapt it to your domain. Then, you can use this fine-tuned BERT model as the base for training your embedding model. ... In the next chapter, we will apply masked language modeling on a pretrained model."*

### Augmented SBERT

- **The data-scarcity workhorse.** *"A disadvantage of training or fine-tuning these embedding models is that they often require substantial training data. Many of these models are trained with more than a billion sentence pairs. ... Fortunately, there is a way to augment your data such that an embedding model can be fine-tuned when there is only a little labeled data available. This procedure is referred to as Augmented SBERT."* — Thakur, Reimers et al. 2020, arXiv:2010.08240.
- **The four-step recipe:**
  1. Fine-tune a [[CrossEncoder|cross-encoder]] (BERT) on a small annotated **gold dataset**.
  2. Generate new sentence pairs (or sample unlabeled pairs).
  3. Label the new pairs with the fine-tuned cross-encoder → **silver dataset**.
  4. Train a [[BiEncoder|bi-encoder]] (SBERT) on **gold + silver**.
- **Gold vs silver definitions.** *"A gold dataset is a small but fully annotated dataset that holds the ground truth. A silver dataset is also fully annotated but is not necessarily the ground truth as it was generated through predictions of the cross-encoder."*
- **Two strategies for generating unlabeled pairs to feed the cross-encoder:**
  1. **Random cross-product** — take the premise of row A with the hypothesis of row B. *"This strategy, however, likely generates significantly more dissimilar than similar pairs."*
  2. **Pretrained-embedding-model reranking** — embed all candidate pairs with a pretrained model, take the top-$k$ cosine-similar for each input sentence. *"This rough reranking process allows us to focus on sentence pairs that are likely to be more similar. Although the sentences are still chosen based on an approximation since the pretrained embedding model was not trained on our data, it is much better than random sampling."*
- **Worked result:** 10,000 gold + 40,000 silver MNLI pairs trained with `bert-base-uncased` + cosine similarity loss → STS-B = **0.71** (vs the same model trained on all 50,000 labeled pairs = 0.72). *"Using only 20% of that data, we managed to get a score of 0.71!"*
- **Quality-of-silver diagnostic.** *"You can test the quality of your silver data by also training your embedding model only on the gold dataset. The difference in performance indicates how much your silver dataset potentially adds to the quality of the model."*

### Unsupervised — TSDAE

- **Four unsupervised techniques the chapter names:** **[[SimCSE]]** (Gao, Yao & Chen 2021, arXiv:2104.08821, *"Simple Contrastive Learning of Sentence Embeddings"*), **[[ContrastiveTension|Contrastive Tension (CT)]]** (Carlsson et al. ICLR 2021), **[[TSDAE]]** (Wang, Reimers & Gurevych 2021, arXiv:2104.06979), **[[GPL|Generative Pseudo-Labeling (GPL)]]** (Wang et al. 2021, arXiv:2112.07577).
- **The chapter focuses on TSDAE.** *"It has shown great performance on unsupervised tasks as well as domain adaptation."*
- **TSDAE's core idea: denoising auto-encoder over deleted-word noise.** *"We add noise to the input sentence by removing a certain percentage of words from it. This 'damaged' sentence is put through an encoder, with a pooling layer on top of it, to map it to a sentence embedding. From this sentence embedding, a decoder tries to reconstruct the original sentence from the 'damaged' sentence but without the artificial noise. The main concept here is that the more accurate the sentence embedding is, the more accurate the reconstructed sentence will be."*
- **TSDAE is similar to [[MaskedLanguageModel|MLM]] but at the sentence level.** *"Similar to masked language modeling, where we try to reconstruct and learn certain masked words. Here, instead of reconstructing masked words, we try to reconstruct the entire sentence."*
- **After training, only the encoder is used.** *"We can use the encoder to generate embeddings from text since the decoder is only used for judging whether the embeddings can accurately reconstruct the original sentence."*
- **TSDAE uses [[CLSPooling|[CLS]-token pooling]] (NOT [[MeanPooling|mean-pooling]]).** *"With the [CLS] token as the pooling strategy instead of the mean pooling of the token embeddings. In the TSDAE paper, this was shown to be more effective since mean pooling loses the position information, which is not the case when using the [CLS] token."* (A wiki-first explicit recommendation against mean-pooling for one specific training regime — TSDAE.)
- **Encoder/decoder weights are tied.** *"We tie the parameters of both models. Instead of having separate weights for the encoder's embedding layer and the decoder's output layer, they share the same weights. This means that any updates to the weights in one layer will be reflected in the other layer as well"* — via `losses.DenoisingAutoEncoderLoss(embedding_model, tie_encoder_decoder=True)`.
- **Memory cost is higher than supervised losses — lower the batch size.** Ch 10 drops `per_device_train_batch_size` from 32 to **16** for TSDAE.
- **The denoising tokenizer is NLTK's `punkt`.** *"We start by downloading an external tokenizer, which is used for the denoising procedure"* — `nltk.download("punkt")`.
- **Worked result on 50,000 unlabeled MNLI sentences (premise + hypothesis flattened):** STS-B Pearson cosine = **0.70**. *"Quite impressive considering we did all this training with unlabeled data."*

### Domain adaptation via adaptive pretraining

- **The goal of [[DomainAdaptation|domain adaptation]].** *"To update existing embedding models to a specific textual domain that contains different subjects from the source domain."*
- **Source domain (in-domain) vs target domain (out-domain).** *"The target domain, or out-domain, generally contains words and subjects that were not found in the source domain or in-domain."*
- **[[AdaptivePretraining|Adaptive pretraining]] is the canonical method.** *"You start by pretraining your domain-specific corpus using an unsupervised technique, such as the previously discussed TSDAE or masked language modeling. Then, you fine-tune that model using a training dataset that can be either outside or in your target domain. Although data from the target domain is preferred, out-domain data also works since we started with unsupervised training on the target domain."*
- **The full pipeline Ch 10 recommends:** TSDAE on target-domain unlabeled text → fine-tune with [[MultipleNegativesRankingLoss|MNR loss]] (or [[AugmentedSBERT|Augmented SBERT]]) on whatever labeled pairs are available (in-domain preferred but out-domain works). *"Using everything you have learned in this chapter, you should be able to reproduce this pipeline!"*

## Key Quotes

> "Contrastive learning is a technique that aims to train an embedding model such that similar documents are closer in vector space while dissimilar documents are further apart. ... it's very similar to the word2vec method from Chapter 2." — Ch 10, on the chapter's foundational technique.

> "Before sentence-transformers, sentence embeddings often used an architectural structure called cross-encoders with BERT. ... finding the highest pair in a collection of 10,000 sentences ... would require $n \cdot (n-1)/2 = 49{,}995{,}000$ inference computations and therefore generates significant overhead. Moreover, a cross-encoder generally does not generate embeddings." — Ch 10, on the structural problem SBERT solves.

> "In sentence-transformers the classification head is dropped, and instead mean pooling is used on the final output layer to generate an embedding. ... This ensures a fixed-size embedding." — Ch 10, on the SBERT mechanism.

> "We have two identical BERT models that share the same weights and neural architecture. ... Since the weights are identical for both BERT models, we can use a single model and feed it the sentences one after the other." — Ch 10, on the [[SiameseNetwork|siamese-network]] training construction.

> "If you look closely at entailment and contradiction, then they describe the extent to which two inputs are similar to one another. As such, we can use NLI datasets to generate negative examples (contradictions) and positive examples (entailments) for contrastive learning." — Ch 10, on the NLI-to-contrastive-data mapping.

> "Compared to our previously trained model with softmax loss (0.72), our model with MNR loss (0.80) seems to be much more accurate!" — Ch 10, on the loss-function effect size.

> "Larger batch sizes tend to be better with MNR loss as a larger batch makes the task more difficult. ... the model needs to find the best matching sentence from a larger set of potential pairs of sentences." — Ch 10, on the [[InBatchNegatives|in-batch negatives]] mechanism.

> "These negatives are called in-batch negatives and can also be used to generate the triplets." — Ch 10, naming the [[InBatchNegatives|in-batch negative]] primitive.

> "We would like to have negatives that are very related to the question but not the right answer. These negatives are called hard negatives." — Ch 10, defining [[HardNegatives|hard negatives]].

> "A gold dataset is a small but fully annotated dataset that holds the ground truth. A silver dataset is also fully annotated but is not necessarily the ground truth as it was generated through predictions of the cross-encoder." — Ch 10, on the [[AugmentedSBERT]] gold/silver distinction.

> "The original cosine similarity loss example had a score of 0.72 with the full dataset. Using only 20% of that data, we managed to get a score of 0.71!" — Ch 10, on Augmented SBERT's payoff.

> "We add noise to the input sentence by removing a certain percentage of words from it. ... a decoder tries to reconstruct the original sentence from the 'damaged' sentence but without the artificial noise. The main concept here is that the more accurate the sentence embedding is, the more accurate the reconstructed sentence will be." — Ch 10, on TSDAE's denoising auto-encoder mechanism.

> "In the TSDAE paper, this was shown to be more effective since mean pooling loses the position information, which is not the case when using the [CLS] token." — Ch 10, on the only regime where [CLS]-pooling beats mean-pooling.

> "You can start with TSDAE to train an embedding model on your target domain and then fine-tune it using either general supervised training or Augmented SBERT." — Ch 10, on the closing domain-adaptation recipe.

## Worked-Code Receipts (in chapter order)

| # | Regime | Data | Loss | Base model | Pooling | STS-B Pearson cosine |
|---|---|---|---|---|---|---|
| 1 | From scratch | 50k MNLI | `SoftmaxLoss(num_labels=3)` | `bert-base-uncased` | Mean | **0.59** |
| 2 | From scratch | 50k MNLI (relabel 2:0,1:0,0:1) | `CosineSimilarityLoss` | `bert-base-uncased` | Mean | **0.72** |
| 3 | From scratch | 16,875 entailment triplets | `MultipleNegativesRankingLoss` | `bert-base-uncased` | Mean | **0.80** |
| 4 | Fine-tune | 50k MNLI | `MultipleNegativesRankingLoss` | `all-MiniLM-L6-v2` | Mean | **0.85** |
| 5 | Augmented SBERT | 10k gold + 40k silver | `CosineSimilarityLoss` + `CrossEncoder` labeling | `bert-base-uncased` | Mean | **0.71** |
| 6 | Unsupervised TSDAE | 50k unlabeled MNLI sentences | `DenoisingAutoEncoderLoss(tie_encoder_decoder=True)` | `bert-base-uncased` | **[CLS]** | **0.70** |

All six runs share the same training hyperparameters: `num_train_epochs=1`, `warmup_steps=100`, `fp16=True`, `eval_steps=100`, `logging_steps=100`. Run 6 (TSDAE) lowers `per_device_train_batch_size` from 32 to 16. Run 5 (Augmented SBERT) uses `apply_softmax=True` at cross-encoder inference time and `NoDuplicatesDataLoader` for the gold-dataset loader.

## Connections

- [[ContrastiveLearning]] — the chapter's foundational technique, now finally walked at full code-recipe granularity (the wiki had only seen it in fragments through Chs 1, 2, 9).
- [[SentenceTransformers]] — the library the chapter trains.
- [[SBERTArchitecture]] / [[SBERT]] — the mean-pooled, siamese-BERT, bi-encoder architecture the library implements.
- [[BiEncoder]] / [[CrossEncoder]] — the structural tradeoff the chapter restates and then exploits in Augmented SBERT.
- [[SiameseNetwork]] — the training topology.
- [[MeanPooling]] / [[CLSPooling]] — the two pooling strategies the chapter names; mean-pooling is the default; CLS-pooling is preferred for TSDAE.
- [[NaturalLanguageInference]] / [[SNLI]] / [[MNLI]] / [[GLUE]] — the data source.
- [[STSB]] — the chapter's evaluator.
- [[MTEB]] — the broader evaluator suite.
- [[SoftmaxLoss]] / [[CosineSimilarityLoss]] / [[MultipleNegativesRankingLoss]] / [[DenoisingAutoEncoderLoss]] — the four losses walked.
- [[InfoNCE]] / [[NTXentLoss]] — alternative names for MNR loss.
- [[InBatchNegatives]] / [[HardNegatives]] / [[SemiHardNegatives]] / [[EasyNegatives]] — the negative-mining taxonomy.
- [[AugmentedSBERT]] / [[TSDAE]] / [[SimCSE]] / [[ContrastiveTension]] / [[GPL]] — the named fine-tuning / unsupervised techniques.
- [[GoldDataset]] / [[SilverDataset]] — the data-quality taxonomy the chapter introduces (gold = ground truth; silver = cross-encoder-labeled).
- [[DomainAdaptation]] / [[AdaptivePretraining]] — the closing-section discipline.
- [[MaskedLanguageModel]] — TSDAE's sentence-level analog; Ch 11's main subject.
- [[NilsReimers]] / [[IrynaGurevych]] — Sentence-BERT and TSDAE authors.
- [[NandanThakur]] — Augmented SBERT lead author.
- [[KexinWang]] — TSDAE and GPL lead author.
- [[bert|BERT]] / [[AllMPNetBaseV2|all-mpnet-base-v2]] / [[AllMiniLML6V2|all-MiniLM-L6-v2]] — the base models named.
- [[Word2Vec]] / [[NoiseContrastiveEstimation]] — historical contrastive-learning predecessors the chapter explicitly traces.
- [[hands-on-llm-ch02-tokens-and-embeddings]] / [[hands-on-llm-ch04-text-classification]] / [[hands-on-llm-ch05-text-clustering-topic-modeling]] / [[hands-on-llm-ch08-semantic-search-and-rag]] / [[hands-on-llm-ch09-multimodal-llms]] — Chs 2/4/5/8/9 forward-reference Ch 10; Ch 10 is their resolution.
- [[HandsOnLLM]] — the book.
- [[JayAlammar]] / [[MaartenGrootendorst]] — the authors.

## Contradictions

- **Pooling strategy default contradicts itself across regimes.** The chapter's main thesis is **mean-pooling beats [CLS]-pooling** (citing the Sentence-BERT paper finding that *"averaging output layer or using the [CLS] token ... has shown to be worse than simply averaging word vectors, like GloVe"* in the cross-encoder framing) — but then in the TSDAE section it explicitly recommends **[CLS]-pooling** over mean-pooling because *"mean pooling loses the position information, which is not the case when using the [CLS] token."* No contradiction in fact — the two regimes are distinct (supervised contrastive vs unsupervised denoising) — but it is the **only place in the wiki** where [CLS]-pooling is recommended over mean-pooling, and worth flagging for readers who have internalized the mean-pooling-as-default rule from Chs 2/4/5/8.
- **No book-level contradictions with prior chapters.** Ch 10 is the **resolution** of forward references from Chs 2, 4, 5, 8, and 9 rather than a revision of any of them. The chapter's claim that *"the main difficulty of training or fine-tuning your model is finding the right data"* echoes [[ai-engineering-ch08-dataset-engineering|Huyen Ch 8]]'s data-engineering chapter; the two books agree that data is the bottleneck.
- **No cross-book contradiction with [[d2l-nlp-applications]]'s NLI coverage.** The Ch 10 NLI framing (entailment as positive, contradiction as negative) is the contrastive-data twin of D2L's NLI-as-classification framing. They are complementary, not contradictory.
