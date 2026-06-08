# Stanford CS324 (Winter 2022) — Data
Source: https://stanford-cs324.github.io/winter2022/lectures/data/
Fetched for wiki ingest.

---

## Overview

This lecture examines the training data behind large language models: data sources and scale, how major datasets are constructed and filtered, the biases introduced by curation, dataset documentation practices (datasheets and data statements), and the broader data ecosystem (data governance and data dignity).

---

## 1. The Data Behind Large Language Models

### Scale and Sources

- Large language models train on "raw text" spanning broad domains, genres, and languages.
- The web is a primary source. Google's search index is **100 petabytes** as a lower bound.
- Private corporate datasets exceed public web data — **Walmart generates 2.5 petabytes hourly**.
- **Common Crawl** is a nonprofit web crawler that provides free snapshots. The **April 2021 snapshot contained 320 terabytes** — orders of magnitude smaller than Google's index.

### Representation Issues

Per **Bender et al. (2021)**, despite scale, large-scale data exhibits uneven population representation:

- Internet data overrepresents younger users from developed countries.
- **GPT-2's** Reddit-based training data: **67% male users, 64% aged 18–29**.
- **8.8–15% of Wikipedians are female**.
- Harassment and content filtering marginalize specific populations.

**Key takeaway:** Dataset composition requires careful understanding and documentation.

### WebText and OpenWebText

**WebText** (GPT-2 training data):
- Scraped Reddit outbound links with **≥3 karma**.
- Filtered out Wikipedia (to keep it clean for benchmark evaluation).
- Result: **40 GB** of text.

**OpenWebText** (open replication):
- Extracted Reddit submission URLs.
- Applied Facebook's **fastText** for English filtering.
- Removed near-duplicates.
- Result: **38 GB** of text.

**Toxicity findings** (Gehman et al. 2020):
- OpenWebText: **2.1%** of documents with toxicity score ≥50%.
- WebText: **4.3%** of documents with toxicity score ≥50%.
- **3% of OpenWebText** came from banned/quarantined subreddits.

### Colossal Clean Crawled Corpus (C4)

Created for training the **T5** model.

**Construction:**
- Started from the **April 2019 Common Crawl snapshot (1.4 trillion tokens)**.
- Removed "bad words," code, non-English text.
- Result: **806 GB (156 billion tokens)**.

**Domain composition analysis** (Dodge et al. 2021):
- Significant data from **patents.google.com**.
- **65% of pages** from the Internet Archive; **92% from the last decade**.
- **51.3% hosted in the United States**.
- Systematic errors observed: machine translation artifacts, OCR artifacts.

**Benchmark contamination:**
- Input-and-output contamination: **1.87–24.88%** (XSum: **15.49%**).
- Input contamination: **1.8–53.6%** (QNLI: derived from Wikipedia).

**Representational harms:**
- Jewish terms: **73.2% positive sentiment**.
- Arab terms: **65.7% positive sentiment** (a **7.5% difference**).
- Variation by news source (NYT: 4.5% difference; Al Jazeera: 0%).

**Allocational harms (filtering bias):**
- Sexual orientation terms more likely filtered; 22–36% of filtered content non-offensive.
- African American English (AAE): **42% filtered rate**.
- Hispanic-aligned English: **32% filtered rate**.
- White American English: **6.2% filtered rate**.

### GPT-3 Dataset

**Construction process:**
1. Selected a Common Crawl subset similar to WebText via a **binary classifier**.
2. Performed **fuzzy deduplication** (13-gram overlap detection).
3. Expanded source diversity: **WebText2, Books1, Books2, Wikipedia**.
4. **Downsampled Common Crawl** during training (82% of the data, ~60% of the contribution).

### The Pile

**EleutherAI's approach:**
- **825 GB** of English text.
- **22 high-quality datasets** from academic and professional sources.
- Emphasizes **curation over indiscriminate web scraping**.

**Comparative analysis:**
- A GPT-2-style model (1.5B parameters) trained on The Pile outperforms GPT-3 (trained on the GPT-3 dataset) for coverage of content not in OpenWebText2.
- The Pile captures information gaps present in GPT-3's dataset.

**Analysis coverage:** Pejorative content and gender/religion bias findings were qualitatively similar to prior work.

### Section Summary

- Total available data (web + private) is massive.
- Training on all available data is ineffective.
- Filtering / curation itself introduces biases.
- Non-web high-quality datasets (e.g., The Pile) show promise.
- Careful documentation and inspection are essential.

---

## 2. Documentation for Datasets

### Core Premise

> "Documentation is important, but within the machine learning community, it has been a fairly ad-hoc process."

Parallels to other fields:
> "Electronics industry has a well-established protocol where every component has a datasheet" with operating characteristics.

- The FDA mandates nutrition labels for food products.

### Two Influential Frameworks

**Datasheets for Datasets** (Timnit Gebru et al., 2018):
- Establishes community norms; emphasizes **transparency**.
- Dual purpose: enables dataset creators to "reflect on decisions, potential harms (e.g., social biases) when creating the dataset," and helps consumers "know when the dataset can and can't be used."

**Data Statements** (Emily M. Bender and Batya Friedman, 2018):
- "More tailored to language datasets."
- Covers curation rationale, language variety, and speaker/annotator demographics.

### Two Purposes

1. **Creators:** Reflect on decisions and potential harms.
2. **Consumers:** Understand appropriate and inappropriate uses.

### Dataset Lifecycle Questions (Datasheets framework)

- **Motivation:** Purpose, creators, funding sources.
- **Composition:** What instances represent, missing information, confidential data.
- **Collection process:** Data acquisition methods, personnel involved, compensation, ethical reviews.
- **Preprocessing/cleaning/labeling:** Methods used and software availability.
- **Uses:** Prior applications/tasks and prohibited uses.
- **Distribution:** Access/distribution methods and IP restrictions.
- **Maintenance:** Support, hosting, and update plans.

### Data Statements (NLP-specific) Coverage

- Curation rationale.
- Language variety (using the **BCP 47** schema).
- Speaker demographics (age, gender, race/ethnicity).
- Annotator demographics.

**Example:** The Pile includes comprehensive datasheet documentation.

---

## 3. Data Ecosystems

### Data Management & Governance

> "In machine learning research, we tend to think of datasets as fixed objects that you collect and you feed into a training algorithm. In the databases community, there is whole subfield thinking about the ecosystem in which data comes to be and is used."

- **Data governance** addresses "how an organization can create data, maintain its quality and security."
- **BigScience data governance working group** (Hugging Face initiative): "developing a framework to responsibly curate quality data sources, in contrast to the indiscriminate scraping of the web."

### Data Dignity Framework

Originated out of **Microsoft and RadicalxChange**. Reframes data fundamentally:

- "People create data."
- Because "people live in social environments, data also is a property not of individuals, but of groups of people" (examples: emails, genetic data).
- "Individually, data does not have value, but collectively, it has a lot of value."

**Systemic problem:**
> "People give away their data for free, and big corporations derive tons of value and power from it."

**Illustrative example:**
> "Alice and Bob are both writers. Alice provide examples of writing for free. This can be used to train a language model that can replace Bob."

### Proposed Solutions

- **Data as Labor:** Think about data as "labor rather than property rights," recognizing that "data privacy works on the individual level, and doesn't work."
- **Data Coalitions:** "Intermediate organizations that represent between data producers and data buyers (think about collective bargaining)."
- **Data Shapley** (Amirata Ghorbani, James Y. Zou, ICML 2019): A "framework for ascribing value to a given data point in the context of machine learning."

For deeper engagement, the lecture references the **Data Freedom Act** (RadicalxChange).

---

## Further Reading

**Documentation:**
- "Datasheets for datasets" (Gebru et al., 2018)
- "Data Statements for Natural Language Processing" (Bender & Friedman, 2018)
- "Model Cards for Model Reporting" (Mitchell et al., 2018)

**Datasets:**
- Common Crawl
- OpenWebText
- C4 (Raffel et al., 2020)
- CCNet
- The Pile (Gao et al., 2020)
- XLM-R corpus (Conneau et al., 2019)

**Analysis:**
- "Documenting Large Webtext Corpora" (Dodge et al., 2021)
- "Quality at a Glance" (Caswell et al., 2021)
- "An Empirical Exploration in Quality Filtering of Text Data" (Gao, 2021)
- "Deduplicating Training Data Makes Language Models Better" (Lee et al., 2021)

**Ecosystems:**
- Foundation Models Report (data section)
- BigScience data governance working group
- "Data Shapley" (Ghorbani & Zou, 2019)
- "Data Freedom Act" (RadicalxChange)
