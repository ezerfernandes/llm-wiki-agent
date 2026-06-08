# Stanford CS324 (Winter 2022) — Security
Source: https://stanford-cs324.github.io/winter2022/lectures/security/
Fetched for wiki ingest.

> Note: The lecture page itself contains only a pointer to the slide deck (titled "Privacy pdf.pdf") plus one "Further reading" citation. The substantive content below was extracted from the slide deck PDF (`/winter2022/assets/pdfs/Privacy%20pdf.pdf`, 41 slides) using `pdftotext -layout`. Headline numbers from the core cited paper (Carlini et al. 2021) were supplemented from the paper abstract.

---

## Week 4 — Security and Privacy (CS324)

### Goals for today
- Security implications of large language models
- Data poisoning — existing work and language models
- Privacy — risks and opportunities

### Security: the CIA model
We view security problems through the **"CIA triad"**:
- **Confidentiality**: Prevent unauthorized disclosure of information
- **Integrity**: Maintain accuracy of outputs
- **Availability**: System is available for use

### Why do LMs matter for security and privacy?
"Aren't language models like any other kind of generative model?"

**Language models are a single point of failure.**
- **Confidentiality**: data stored in a LM is accessible to any downstream application.
- **Integrity**: a backdoored LM can affect all downstream models.
- **Availability**: attacking a LM-based API can cause widespread outages.

### What we're going to cover today (we won't cover everything)
- **Confidentiality**: Avoid backdoors planted in training data
- **Integrity**: Keep training data private
- **Availability**: Not covered

---

## Part 1: Integrity and data poisoning

Framing questions:
- What's data poisoning?
- How is it dangerous for language models?
- What can we do against it?

### Integrity: data poisoning
Classic data poisoning example: **adding a backdoor**. Example given: **face recognition**.

### Data poisoning is a real concern
Do people care about data poisoning? **Data poisoning is the highest concern among practitioners.** [Shankar+ 2021]

### What are the main kinds of attacks?
Two categories:
- **Backdoor with trigger**
  - Goal: Attack any image with a 'trigger'.
  - Allows attackers to get desired predictions.
- **Triggerless**
  - Goal: Attack specific images.
  - Attacker can degrade performance.

### Construction and properties of poisoning attacks
Reference: **Concealed Data Poisoning Attacks** [Wallace+ 2021]. "How can we construct these examples?"

### Mathematical setup of how to perform attacks
Data poisoning is expressed as a **bilevel optimization problem**:
- ℒ_adv is how well we do at attacking our targets x_t.
- X_p is the poisoned data that we add.
- The model is the result of minimizing loss on the training set.
- "These are hard optimization problems."

### Approximating solutions to bilevel opt problems
How can we solve this?
- **Idea**: instead of the argmin, write down the gradient descent updates and **"unroll"** the stochastic gradient descent updates.
- Now θ is a (differentiable) function of X_p and we can take gradients.
- This is called the **"Metapoison" attack**. [Huang+ 2020]

### How good are these attacks?
Reference: **Concealed Data Poisoning Attacks** [Wallace+ 2021].

### Aside: What's the state of empirical results in data poisoning? (vision)
Data poisoning is actually **pretty brittle**. What breaks data poisoning attacks:
- Data augmentation / changing to SGD / transfer / ResNets
- Constraining for imperceptibility via l∞
- Black box attacks
- Flipping the target image

"Attacks are viable, but not as good as we had seen." [Schwarzschild+ 2020]

### Aside: Provable methods for data poisoning mitigation
Can we be truly secure (via provable guarantees)?
- We say that P is **ε-contaminated** with clean distribution P_clean if there exists some Q such that:
  - **P = (1 − ε) P_clean + ε Q**
- Data poisoning equivalent: An adversary arrives and adds samples from an arbitrary distribution Q, with the number of samples up to ε times the clean dataset.
- Teaser: There's ongoing work like **SEVER** that achieves this guarantee.

### Final Aside: trigger-like sequences exist without poisoning
Existing NLP models are sufficiently brittle that you can find **"natural" triggers**. Reference: **Universal Adversarial Triggers** [Wallace+ 2021].

### Recap and future threats (Part 1)
- Practical, easy poisoning attacks exist for **downstream, fine-tuned models**.
- **Metapoison-style attacks work for fine-tuned models.**
- Defenses (provable and otherwise) are still an **open problem**.
- Data poisoning of LMs — **not yet seen, but likely in the future**.

---

## Part 2: Confidentiality and privacy

Framing questions:
- What are privacy threats for language models?
- Should we care about privacy on public data?
- Opportunities for improving privacy?

### On to privacy: why are LMs a privacy risk?
- Continued progress in NLP relies on **ever larger datasets**.
- Example scaling curve from **Hestness 2017**, machine translation error rates.
- **Data requirements conflict with privacy needs.**

### Hard tradeoffs for data-collection (e.g. dialogue generation)
- Public data (low quality, large quantity)
- Annotator-driven data (high quality, costly)
- Private, user data (high quality, large quantity?)

"This line of thinking has already led to real-world harms": **10 billion conversations from a dating app fed into a chatbot** — predictably, it **leaked intimate information directly to the public**.

### Detour: isn't pretraining data in public domain?
Privacy harms aren't just about revealing information to the public. Reference: **A Taxonomy of Privacy** [Solove 2006].

### Aggregation + accessibility of public data can harm privacy
- **Aggregation**: combining multiple, public sources of information. "The point of a language model is to aggregate and generalize from public data."
- **Accessibility**: making sensitive, public information more available.

What's wrong with aggregation?
- Aggregation can violate expected privacy (e.g. a 'synthetic biography').
- (Even accurate) inferences can be harmful (asking GPT-2 for sexual orientation).
- Accessibility can harm expectations of privacy (e.g. API keys left public on GitHub).

### Legal views of aggregation and accessibility
Aggregation and accessibility have been discussed by the **Supreme Court**, in **DOJ v. Reporters Comm. for Free Press**.

> On accessibility: "In an organized society, there are few facts that are not at one time or another divulged to another. Thus the extent of the protection accorded a privacy right at common law rested in part on the degree of dissemination of the allegedly private fact and the extent to which the passage of time rendered it private. […]"

> On aggregation: "But the issue here is whether the compilation of otherwise hard-to-obtain information alters the privacy interest […]. Plainly there is a vast difference between the public records that might be found after a diligent search of courthouse files, county archives, and local police stations throughout the country and a computerized summary located in a single clearinghouse of information."

### Are privacy attacks real and practical?
"With language models, privacy attacks are very easy." Reference: **Extracting Training Data from Language Models** [Carlini+ 2021].

(From the paper: researchers extracted **hundreds of verbatim text sequences** from **GPT-2**'s training data — including (public) personally identifiable information [names, phone numbers, email addresses], IRC conversations, code, and 128-bit UUIDs. Each extracted sequence appeared in **just one document** in the training data. **Larger models are more vulnerable than smaller models.**)

### Large language models more aggressively memorize
Case study from **Reddit URL memorization**. Reference: **Extracting Training Data from Language Models** [Carlini+ 2021].

### Memorization is closely tied to model goodness-of-fit
- Memorization of data and minimum training loss happen at the same time.
- "Is memorization necessary? That's an open question."
- Reference: **The Secret Sharer …** [Carlini+ 2019].

### Privacy risks of large language models
- Large language models incentivize large-scale public data collection.
- Which can cause harms via: **memorization of public facts and aggregation across an entire corpus**.
- This is hard to avoid because **models seem to prefer to memorize data**.

### How can we prevent memorization?
- Q: Can simple privatization schemes prevent this?
- Even well-meaning, well-designed heuristics can be attacked.
- A proposed privacy heuristic (2/21) was later proven to be broken (4/21).
- What we need: **provable guarantees** that we will not leak data.

### Gold standard — differential privacy (DP)
- **Differential privacy**: a formal privacy guarantee for a randomized algorithm.
- The gap between adjacent datasets is **ε, the privacy level**. [from Hsu '14]
- This is the gold standard for statistics (used in the **2020 census**), but **hard to achieve**.

### Differential privacy with deep learning (DP-SGD)
- Q: How can we apply this to deep neural networks?
- **SGD**: Compute gradients → Sum and update.
- **Differentially private SGD (DP-SGD)**: Compute gradients → **Clipping** → Sum, **add noise**, and update.

### Mixed results for DP with deep neural nets in NLP
Prior attempts to apply DP to large neural models in NLP (via DP-SGD) have often failed.

Example: **Kerrigan et al.** — trained language generation models on Reddit data.
- Input: "Bob lives close to the.."
- Non-private output: "station and we only have two miles of travel left to go"
- Private output (ε = 100): "along supply am certain like alone before decent exceeding"

**Why did things fail? (The dimensionality hypothesis)**
1. Large language models have ~300 million parameters — that's a lot of things to privatize.
2. Theory says differential privacy performance should degrade with dimension (d/n).
3. Most (if not all) successful DP methods relied on low-dimensional statistics.

### Differential privacy with large language models
- Training large language models from scratch with DP: **open problem** — large model size poses statistical + computational issues.
- Using a **public language model to build a private downstream model**: **This is possible!** (Public data → Large LM; then Private data → private model via differential privacy.)

### Opportunities for private NLP with language models
- Fine-tuning large language models has led to huge gains in NLP (gains from pretrained language models).
- These models capture useful generic structures about language (e.g. syntax). [Hewitt and Manning '19; Zhang and Hashimoto '21; Wei, Xie and Ma '21]
- "It's wasteful to spend our private data learning this type of public information."

### Language model performance — fine if tuned right
- Problem: using non-private hyperparameters for private optimization.
- Solution: a way of predicting DP-SGD performance via **'signal-to-noise' ratios**.
- Optimal hyperparameters found via a 'signal-to-noise ratio' analysis vs. typical hyperparameters.
- **'Naive' choices were almost 100x off!** [Li+ 2021]

### Bigger models are better private learners
- DP-SGD (which people ruled out) **beats non-private baselines + heuristic privacy notions**.
- Ordering shown: heuristic privacy method < … < DP-SGD < non-private baseline.

### Pre-trained, large language models are key to privacy
- In the **non-private** case, pre-training is a small gain (**5 BLEU points on E2E**).
- For **private learning**, the difference is huge:
  - **unusable (15 BLEU)** when trained from scratch
  - **usable (61.5 BLEU)** when privately fine-tuning a base LM.

### DP-NLP is bottlenecked by computational challenges
"Is the problem solved? Not quite."
- Subtlety: Differential privacy (via DP-SGD) is **extremely memory intensive**.
- How many examples can we process on a **Titan RTX GPU**?

| | 'medium' model (~300M params) | 'large' model (~700M params) |
|---|---|---|
| Non-private | 34 examples | 10 examples |
| Private | 6 examples | 0 examples |

"New, DP-specific methods (or brute force compute power) are needed."

### Breaking the memory barrier for DP-SGD
- Optimizing gradient computations: nearly non-private levels of memory consumption.
- (Caveat: implementation dependent, extra backpropagation pass.)

### Can we build useful, private language generation systems?
- Restaurant review generation (**E2E**).
- Wikipedia table descriptions (**DART**).

### Recap: Privacy
- Even public data can be a privacy risk.
- Large language models love to memorize training data.
- Opportunities for privacy: language models can help build private models.

### Takeaways: security
**Risks**
- Large datasets: easier to poison, more private data.
- Centralization: more determined adversaries.

**Opportunities**
- Privacy: enables easy private NLP.

---

## Further reading (from lecture page)
- **Extracting Training Data from Large Language Models.** USENIX Security Symposium 2020 / arXiv:2012.07805. Authors: Nicholas Carlini, Florian Tramèr, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom B. Brown, D. Song, Ú. Erlingsson, Alina Oprea, Colin Raffel. (https://arxiv.org/pdf/2012.07805.pdf)
