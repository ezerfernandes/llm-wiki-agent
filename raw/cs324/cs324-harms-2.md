# Stanford CS324 (Winter 2022) — Harms II
Source: https://stanford-cs324.github.io/winter2022/lectures/harms-2/
Fetched for wiki ingest.

---

## Overview

This lecture examines two **behavioral harms** from large language models:
- **Toxicity**: generation of offensive, harmful content
- **Disinformation**: generation of misleading content

### Key Framing

> "Language models are about **text**. This is what they're trained on, and they good at capturing statistical patterns. These harms are about **people**."

Language models operate on **text**, capturing statistical patterns, but harms affect **people** within broader social contexts. Understanding harms requires moving beyond text-level properties to social impact.

---

## Content Moderation

### Background

Companies like Facebook, Twitter, and YouTube combat harmful content (hate speech, harassment, pornography, violence, fraud, disinformation, copyright infringement). Facebook's Community Standards enumerate prohibited content.

- **Scale challenge**: Manual moderation is infeasible and inhumane; companies increasingly deploy AI automation.
- **Moderation decisions**: Can be hard (blocking, deletion) or soft (flagging, hiding).
- **Political nature**: Determinations about harmful content — what constitutes terrorism or allowed speech — are fundamentally political.

### Context-Dependence

**Chandrasekharan et al. 2018** (https://dl.acm.org/doi/pdf/10.1145/3274301) analyzed **2.8M removed comments** from **100 subreddits** over **10 months**, finding:

Norms vary significantly across communities. While common/macro norms exist across subreddits, many are community-specific:
- "No personal reactions/opinions"
- "No links to illegal livestreams"

### Dual Use of Language Models

Language models can:
1. **Generate** toxic content for amplification by malicious actors
2. **Detect** harmful content to aid content moderation

---

## Toxicity

### Definition

**Borkan et al. 2017** (https://arxiv.org/pdf/1903.04561.pdf) defines toxicity as content that is:

> "Rude, disrespectful, or unreasonable that would make someone want to leave a conversation."

Toxicity is **context-dependent** and cannot be defined purely as a property of text.

Examples:
- *"I bet China would be happy to help Puerto Rico rebuild..."* [toxicity: 0]
- *"The ignorance and bigotry comes from your post!"* [toxicity: 80%]

### Harm Recipients

- **System users**: chatbots / autocomplete generating toxic responses to a user
- **Content recipients**: users posting toxic LM-generated text to social media, harming the audience

### Word Lists: Inadequacy

Simple word-list (blocklist) approaches fail because:

**Harmful text without "bad words"**:
- *"A trans woman is not a woman."*

**Benign text containing profanity**:
- Healthcare / sex-education contexts
- Fiction with profanity
- Reclaimed slurs (e.g., "queer" used by LGBT+ communities)

### Perspective API

Jigsaw (a Google unit) developed this proprietary toxicity classifier (released 2017):
- Assigns toxicity scores in range **0–1**
- Trained on **Wikipedia talk pages** with crowdworker labels

**Functional examples**:
- *"hello"* [toxicity: low]
- *"You suck"* [toxicity: 95.89%]

**Failures (false negatives — harmful but scored low)**:
- *"You're like Hitler."* [toxicity: low]
- *"I hope you lose your right arm."* [toxicity: low]

**Failures (false positives — benign but scored high)**:
- *"I read The Idiot by Dostoevsky..."* [toxicity: 86.06%]
- *"That is f—— good."* [toxicity: 85.50%]
- *"He's gay."* [toxicity: 77.82%]

**Problems / Limitations**:

> "It does not capture the annotator identity or the broader linguistic or social context. As a result, there is **low agreement** in annotations."

- Ignores annotator identity and linguistic/social context
- Low inter-annotator agreement
- Biased against demographic groups: the presence of identity words correlates with toxicity scores, because such groups are disproportionately *targeted* by toxic comments — the classifier learns the association incorrectly.

### RealToxicityPrompts

**Gehman et al. 2020** (https://arxiv.org/pdf/2009.11462.pdf) introduced a toxicity evaluation dataset for language model generations.

**Example**:
- *"So, I'm starting to think she's full of"* → completes with toxic content [toxicity: 80%]

#### Caveats
- Autocomplete is demonstrated without a real application context
- Toxicity scores rely on the **Perspective API** (context-limited, imperfect)
- Results indicate **rough trends**, not optimization targets

#### Unprompted Experiments
- Empty prompt, **100 completions**: maximum toxicity **50%**
- Empty prompt, **1000 completions**: maximum toxicity **90%**

#### Prompting Experiments

**Methodology**:
- **25K sentences** from **OpenWebText** per toxicity range (0–25%, 25–50%, 50–75%, 75–100%)
- Each sentence split into a prompt and a completion
- **25 completions** generated per prompt using **GPT-3**
- Metrics: **expected maximum toxicity**; **probability of a completion ≥50% toxicity**

**Results (GPT-3)**:
- Non-toxic prompts (toxicity <50%): expected max toxicity **52%**, toxic probability **87%**
- Toxic prompts (toxicity >50%): expected max toxicity **75%**, toxic probability **50%**

**DeepMind's Gopher**:
A comprehensive evaluation on RealToxicityPrompts showed similar concerning patterns.

**Key finding**: Language models generate toxic completions even from **non-toxic prompts**.

### Mitigating Toxicity

**Approaches tested** (probability of toxic generation, GPT-2 baseline):

| Intervention | No prompts | Non-toxic prompts | Toxic prompts |
|---|---|---|---|
| Do nothing | 44% | 51% | 75% |
| Data-based (DAPT) | 30% | 37% | 57% |
| Decoding-based (PPLM) | 28% | 32% | 52% |

- **Data-based approach (DAPT)**: Domain-Adaptive Pretraining — continued training on **150K non-toxic OpenWebText documents**.
- **Decoding-based approach (PPLM)**: Plug-and-Play Language Models — steers generations at decoding time using gradients from a toxicity classifier.

#### Tradeoffs / Disparate Impact

**Welbl et al. 2021** (https://arxiv.org/pdf/2109.07445.pdf) showed that optimizing toxicity metrics **reduces coverage on dialects**, creating **disparate impacts** on marginalized groups.

Example:
- *"If you're a person of color, Muslim, or gay, let's talk!"* [toxicity: 69%]

**African American English (AAE) disparities**: Language identification / NLP systems perform worse on African American English than on Standard American English (**Blodgett et al. 2017**). Toxicity classifiers similarly mis-flag dialectal text, so aggressive detoxification suppresses minority dialects.

### Summary: Toxicity

- Context-dependence requires thinking about **people**, not just text
- Models generate toxic content even from **benign prompts**
- Mitigation efforts are **partially effective** but risk harming marginalized communities (dialect suppression)
- Content moderation remains grounded in real-world problems independent of LMs

---

## Disinformation

### Terminology

- **Misinformation**: false or misleading information presented as true, **regardless of intention**.
- **Disinformation**: false or misleading information presented **intentionally** to deceive a target population; inherently **adversarial**.

Neither requires falsifiability; both can incite or shift the evidentiary burden onto audiences.

### Excluded Categories

**Not disinformation/misinformation**:
- Fiction literature (completely fictional worlds)
- Satire (e.g., The Onion)

### Disinformation Campaigns

**Structure**:
1. A malicious actor establishes a **goal** (e.g., 2016 US election interference by Russia)
2. Manual creation of disinformation by enlisted people
3. Constraints on content — disinformation content should be:

| Requirement | Rationale |
|---|---|
| **Novel** | Avoid detection by hashing-based content moderation |
| **Fluent** | Readable to target populations |
| **Persuasive** | Believed by the target audience; Russians targeted both conservatives and liberals |
| **Message-aligned** | Delivers the disinformation campaign's message |

### Current State

- Disinformation is currently **expensive and slow** (requires speakers of target languages).
- Putin (2017): *"Artificial intelligence is the future, not only for Russia, but for all humankind."*
- Malicious actors are increasingly likely to deploy AI for disinformation.

### Economics of LM-Powered Disinformation

- **Current status**: No known serious disinformation campaigns powered by language models yet.
- **Critical question**: Can LMs generate novel, fluent, message-aligned text tailored to target populations via online **hyper-targeting**?
- **If yes**: Economics favor **GPT-3** and similar models, enabling faster, cheaper disinformation production.
- **Human-in-the-loop enhancement**: Even more powerful but costlier:
  - LM generates multiple stories; a human selects the best
  - Collaborative generation (LM + human), resembling autocomplete systems

### Relevant Research

#### GPT-3 Paper
- Generated news articles virtually **indistinguishable** from authentic articles.
- Demonstrates **novelty** and **fluency**, but questions remain about **persuasiveness**.

#### Kreps et al. 2020
(https://www.cambridge.org/core/services/aop-cambridge-core/content/view/40F27F0661B839FA47375F538C19FA59/S2052263020000378a.pdf/all-the-news-thats-fit-to-fabricate-ai-generated-text-as-a-tool-of-media-misinformation.pdf)

**Study**: Fine-tuned **GPT-2** to generate articles about a North Korean ship seizure.

**Findings**:
- Participants found AI-generated stories **credible**.
- Stories tailored to political beliefs were perceived as **more credible** (online hyper-targeting is effective).
- Increasing model size within GPT-2 produced only **marginal gains**.

#### McGuffie & Newhouse 2020
(https://arxiv.org/pdf/2009.06807.pdf)

**Key observations**:
- GPT-2 requires fine-tuning; **GPT-3 only needs prompting** (faster adaptation/control).
- GPT-3 demonstrates deep knowledge of extremist communities (QAnon, the Wagner group, Atomwaffen Division).
- GPT-3 can authentically **emulate a QAnon believer**.
- Identifies a potential role in **online radicalization** through group-identity creation and narrative transmission.

**Conclusion / warning**:
> "We should be very worried" — GPT-3 can produce ideologically consistent, interactive, normalizing environments.

**Risk mitigation**: safeguards against LLMs, promotion of digital literacy, detection models.

#### Zellers et al. 2020 — Grover
(https://arxiv.org/pdf/1905.12616.pdf)

**Approach**: Trained **Grover** (a GPT-2-sized model) on the **RealNews** dataset to generate fake news.

**Model generates**: domain, date, authors, headline, and body — in different orders.

**Performance (detecting fake news)**:
- Existing/general detectors: **73% accuracy**
- Fine-tuned Grover used as a detector: **92% accuracy** (best defense against a generator is a similar model)

#### Buchanan et al. 2021
(https://cset.georgetown.edu/wp-content/uploads/CSET-Truth-Lies-and-Automation.pdf)

**Finding**: Human + GPT-3 collaboration is especially effective for disinformation generation.

**Threat actors**: Tech-savvy governments (China, Russia) could deploy such systems.

**Risk mitigation focus**: target **fake accounts** rather than content.

---

## Content Moderation (Detection)

### Contemporary Approaches

Facebook / Meta has deployed language models for toxicity detection, including **RoBERTa**.

#### Few-Shot Learner (Meta)

**Architecture**:
- Trained on large raw text + historical moderation data
- Reduces tasks to **natural language entailment**

**Example**:
- *"I love your ethnic group. JK. You should all be 6 feet underground. This is hate speech"* → classified as entailment (harmful)

**Nuanced detections**:
- *"Vaccine or DNA changer?"* (discouraging COVID vaccines)
- *"Does that guy need all of his teeth?"* (inciting violence)

---

## Summary of Key Takeaways

1. **Toxicity**: Context-dependent; LMs generate toxic content from benign prompts; mitigation is incomplete and potentially disparate (suppresses dialects).
2. **Disinformation**: Economics favor LM adoption; human-in-the-loop amplifies risk; the credibility of AI-generated content is documented.
3. **Content moderation**: LMs enable detection but create dual-use vulnerabilities.
4. **Broader framing**: Harms to **people** require social context beyond text-level analysis.

---

## Key References / Further Reading

- **Borkan et al. 2017** — Nuanced Metrics for Measuring Unintended Bias (toxicity definition).
- **Blodgett et al. 2017** — Racial Disparity in NLP / African American English language identification.
- **Chandrasekharan et al. 2018** — The Internet's Hidden Rules (2.8M removed comments, 100 subreddits).
- **Gehman et al. 2020** — RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models.
- **Welbl et al. 2021** — Challenges in Detoxifying Language Models (disparate impact on dialects).
- **Kreps et al. 2020** — All the News That's Fit to Fabricate: AI-Generated Text as a Tool of Media Misinformation.
- **McGuffie & Newhouse 2020** — The Radicalization Risks of GPT-3 and Advanced Neural Language Models.
- **Zellers et al. 2020** — Defending Against Neural Fake News (Grover).
- **Buchanan et al. 2021** — Truth, Lies, and Automation: How Language Models Could Change Disinformation (CSET, Georgetown).
