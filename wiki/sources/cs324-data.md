---
title: "CS324 — Data"
type: source
tags: [cs324, llm, course-lecture, data]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/data/
---

## Summary
This Stanford CS324 lecture examines the training data behind large language models: where it comes from and at what scale, how flagship corpora ([[WebText]], [[OpenWebText]], [[C4]], the [[GPT-3]] dataset, [[ThePile]]) are constructed and filtered, and the biases that scale and curation both introduce. It then argues for systematic dataset documentation ([[Datasheets]], [[DataStatements]]) and situates data within a broader ecosystem of [[DataGovernance]] and [[DataDignity]].

## Key Claims
- The web is the primary data source for LLMs: [[GoogleSearchIndex]] is ~100 PB (a lower bound), while [[CommonCrawl]]'s April 2021 snapshot was only 320 TB; private corporate data can dwarf public web data (Walmart generates ~2.5 PB/hour).
- Scale does not guarantee representativeness ([[BenderEtAl2021]]): internet data overrepresents younger users from developed countries; [[GPT-2]]'s Reddit-derived data skewed 67% male and 64% aged 18–29; only 8.8–15% of Wikipedians are female.
- [[WebText]] (GPT-2 training data) scraped Reddit outbound links with ≥3 karma, excluded Wikipedia, and yielded ~40 GB; [[OpenWebText]] replicated it via Reddit submission URLs + fastText English filtering + dedup, yielding ~38 GB.
- Toxicity (Gehman et al. 2020): ~2.1% of OpenWebText and ~4.3% of WebText documents scored ≥50% toxicity; ~3% of OpenWebText came from banned/quarantined subreddits.
- [[C4]] (built for [[T5]]) started from the April 2019 [[CommonCrawl]] snapshot (1.4T tokens) and, after removing bad words/code/non-English text, produced 806 GB (156B tokens).
- C4 analysis ([[DodgeEtAl2021]]): heavy patents.google.com content; 65% of pages from the Internet Archive (92% from the last decade); 51.3% US-hosted; benchmark contamination ranged 1.87–24.88% (input+output) and 1.8–53.6% (input only).
- C4 filtering produced allocational harms: African American English was filtered at 42%, Hispanic-aligned English at 32%, vs only 6.2% for White American English — and 22–36% of filtered sexual-orientation content was non-offensive.
- The [[GPT-3]] dataset was built by classifier-selecting WebText-like Common Crawl, fuzzy-deduplicating (13-gram overlap), and mixing in WebText2, Books1, Books2, and Wikipedia; Common Crawl was downsampled (82% of data → ~60% of contribution).
- [[ThePile]] ([[EleutherAI]]) is 825 GB assembled from 22 curated high-quality academic/professional datasets, arguing for curation over indiscriminate scraping; it covers information gaps left by the GPT-3 dataset.
- Lessons: total data is massive, training on everything is ineffective, filtering itself biases data, curated non-web datasets show promise, and documentation/inspection are essential.
- ML treats datasets as fixed objects; the databases community studies data as an ecosystem — motivating [[DataGovernance]] (organizational creation, quality, and security of data), exemplified by the [[BigScience]] data governance working group.
- [[Datasheets]] (Gebru et al., 2018) and [[DataStatements]] (Bender & Friedman, 2018) provide documentation frameworks spanning the dataset lifecycle (motivation, composition, collection, preprocessing, uses, distribution, maintenance), analogous to electronics datasheets and FDA nutrition labels.
- [[DataDignity]] (Microsoft + [[RadicalxChange]]) reframes data as collective, group-owned, and labor-like rather than individual property, proposing data coalitions for collective bargaining; [[DataShapley]] (Ghorbani & Zou, ICML 2019) gives a complementary way to value individual data points.

## Key Quotes
> "Documentation is important, but within the machine learning community, it has been a fairly ad-hoc process." — motivation for datasheets/data statements
> "In machine learning research, we tend to think of datasets as fixed objects that you collect and you feed into a training algorithm. In the databases community, there is whole subfield thinking about the ecosystem in which data comes to be and is used." — framing data ecosystems
> "Individually, data does not have value, but collectively, it has a lot of value." — Data Dignity premise
> "People give away their data for free, and big corporations derive tons of value and power from it." — the systemic problem motivating Data Dignity
> "Alice and Bob are both writers. Alice provide examples of writing for free. This can be used to train a language model that can replace Bob." — illustrative example of data-as-labor harm

## Connections
- [[CS324]] — this is the "Data" lecture in the Stanford CS324 (Winter 2022) Large Language Models course
- [[CommonCrawl]] — primary raw web source feeding C4, the GPT-3 dataset, and others
- [[WebText]] — GPT-2's curated Reddit-link corpus, the quality benchmark later datasets emulate
- [[OpenWebText]] — open replication of WebText used in toxicity/quality analysis
- [[C4]] — the Colossal Clean Crawled Corpus built for T5; central case study in filtering bias
- [[T5]] — the model C4 was created to train
- [[GPT-3]] — its training dataset is dissected as a classifier-filtered + deduplicated + mixed corpus
- [[GPT-2]] — trained on WebText; its data demographics illustrate representation skew
- [[ThePile]] — EleutherAI's curated 825 GB corpus offered as a curation-first alternative
- [[EleutherAI]] — creator of The Pile
- [[Datasheets]] — Gebru et al. documentation framework for datasets
- [[DataStatements]] — Bender & Friedman NLP-specific documentation framework
- [[ModelCards]] — related model-reporting documentation framework (Mitchell et al., 2018)
- [[DataGovernance]] — organizational framing of data creation, quality, and security
- [[BigScience]] — Hugging Face initiative with a responsible data governance working group
- [[DataDignity]] — Microsoft/RadicalxChange concept reframing data ownership and value
- [[DataShapley]] — method for ascribing value to individual data points
- [[RadicalxChange]] — co-origin of Data Dignity and the Data Freedom Act
- [[DataFiltering]] — the curation step shown to introduce representational and allocational harms
- [[Deduplication]] — fuzzy/n-gram dedup used in GPT-3 data construction and shown to improve models
- [[BenchmarkContamination]] — training-data overlap with evaluation benchmarks quantified in C4
- [[Toxicity]] — measured across WebText/OpenWebText
- [[DataDocumentation]] — overarching theme uniting datasheets, data statements, and model cards
- [[TimnitGebru]] — lead author of "Datasheets for Datasets"
- [[EmilyBender]] — co-author of Data Statements and of the representation-harms analysis

## Contradictions
- None identified. The lecture's curation-over-scraping argument (favoring The Pile) complements rather than contradicts scaling-focused material elsewhere in the course; it qualifies the "more data is better" view by noting filtering harms and the value of curated, well-documented corpora.
