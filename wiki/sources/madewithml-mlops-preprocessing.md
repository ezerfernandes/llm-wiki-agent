---
title: "Made With ML — Data Preprocessing"
type: source
tags: [mlops, made-with-ml, preprocessing, tokenization]
date: 2026-05-15
source_file: raw/madewithml/mlops-preprocessing.md
---

## Summary
The preprocessing lesson splits data preparation into two phases — *preparing* (joins, missing values, outliers, feature engineering, cleaning) and *transforming* (scaling, encoding, extraction). For the text-classification example it concatenates title+description into a `text` feature, applies regex-based lowercase/stopword/non-alphanumeric cleaning, label-encodes `tag` via a `class_to_index` map, and tokenizes with the [[scibert]] BertTokenizer (`allenai/scibert_scivocab_uncased`). The final `preprocess(df, class_to_index)` function bundles all steps for reuse across train/inference.

## Key Claims
- Preprocessing splits into two categories: *global* steps (lowercasing, stopword removal) that don't depend on data, and *local* steps (vocab, standardization) learned only from the training split to avoid leakage.
- Missing-value strategies: omit rows, omit features entirely, fill via domain knowledge/mean, or normalize sentinel values (0/null/NA) to NaN.
- Anomalies are global (point), contextual (conditional), or collective (group); some "outliers" disappear under appropriate transformations (e.g. log/power).
- Scaling options include standardization (mean 0, std 1), min-max rescaling, and binning continuous values into categorical bins.
- Encoding choices: label encoding (unique index), one-hot (binary vector), or learned dense embeddings — the last preserves context.
- Feature extraction patterns: transfer learning, autoencoders, PCA, n-gram counts (CountVectorizer), and similarity-based vectorization.
- For high-cardinality features, hash or substitute proxy attributes (location/favorites instead of user ID) to combat the [[CurseOfDimensionality]].
- The course's tokenizer is BertTokenizer pretrained on scientific text (scibert) with `padding="longest"` to handle variable-length batches.

## Key Quotes
> "Certain preprocessing steps are global (don't depend on our dataset, ex. lower casing text, removing stop words, etc.) and others are local (constructs are learned only from the training split, ex. vocabulary, standardization, etc.)."

> "We'll wrap up by combining all of our preprocessing operations into function. This way we can easily apply it to different datasets (training, inference, etc.)."

## Connections
- [[MadeWithML]] — parent course.
- [[GokuMohandas]] — author.
- [[Anyscale]] — publisher.
- [[pandas]] — DataFrame ops (`apply`, `drop`, `dropna`, `map`).
- [[NumPy]] — `np.nan` and array math.
- [[scikitlearn]] — StandardScaler, MinMaxScaler, KBinsDiscretizer, LabelEncoder, OneHotEncoder, PCA, CountVectorizer.
- [[NLTK]] — stopword list and stemming.
- [[HuggingFaceTransformers]] — `BertTokenizer.from_pretrained`.
- [[SciBERT]] — `allenai/scibert_scivocab_uncased` tokenizer/model.
- [[Tokenization]] — converting text to token ids + attention masks.
- [[FeatureEngineering]] — combining title + description into one feature.
- [[FeatureScaling]] — standardization/min-max techniques.
- [[OneHotEncoding]] — categorical encoding option.
- [[LabelEncoding]] — used for the tag column.
- [[Embeddings]] — `nn.Embedding` and contextual representations.
- [[PCA]] — linear dimensionality reduction.
- [[transferlearning]] — extracting features from a pretrained model.
- [[Autoencoders]] — compressed-representation extraction.
- [[FeatureStore]] — referenced for reusing features over time.
- [[DataLeakage]] — risk addressed by separating local vs global preprocessing.
- [[CurseOfDimensionality]] — addressed via hashing/proxy encoding.
- [[transformer]] — underlying architecture of the scibert model.
- [[bert]] — encoder-only model family used.

## Contradictions
- None identified.
