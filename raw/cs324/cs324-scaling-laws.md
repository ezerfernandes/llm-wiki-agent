# Stanford CS324 (Winter 2022) — Scaling laws
Source: https://stanford-cs324.github.io/winter2022/lectures/scaling-laws/
Fetched for wiki ingest.

> Note on provenance: the lecture web page itself only states "These slides were delivered in class" and links to a slide deck (PDF) and to the Kaplan et al. 2020 paper as further reading. The full lecture content below was extracted slide-by-slide from the publicly hosted slide deck at
> https://stanford-cs324.github.io/winter2022/assets/pdfs/Scaling%20laws%20pdf.pdf
> (37 slides). The slides are titled "Week 6 — Scaling laws, CS324".

---

## Slide 1 — Title
**Week 6 — Scaling laws** — CS324

## Slide 2 — Motivating problem: hyperparameter costs
- Hyperparameter tuning is a huge cost!
- How can we solve this?
  1. Guess and pray
  2. Exhaustive search
  3. Have simple rules that find optimal hyperparams
- Sidebar (Strubell+ 2019): Estimated CO2 emissions from training common NLP models, compared to familiar consumption (Table 1, CO2e in lbs):
  - Air travel, 1 passenger, NY↔SF: 1,984
  - Human life, avg, 1 year: 11,023
  - American life, avg, 1 year: 36,156
  - Car, avg incl. fuel, 1 lifetime: 126,000
  - Training one model (GPU): NLP pipeline (parsing, SRL): 39; w/ tuning & experimentation: 78,468; Transformer (big): 192; w/ neural architecture search: 626,155

## Slide 3 — Teaser: simple, predictive 'laws' for behaviors of LMs
- What you'll learn today: **scaling laws** which are simple, predictive rules for model performance.
- **Old and unpleasant:** tune hyperparameters on big models.
- **New and exciting:** tune on small models, extrapolate to large ones.
- Figures: validation loss vs compute (PetaFLOP/s-days) with fit line **L = 2.57 · C^(-0.048)**; test loss vs parameters (non-embedding) colored by number of layers (1, 2, 3, 6, >6 layers).

## Slide 4 — Scaling laws: surprisingly clean and robust
- These scaling laws hold on *many* different kinds of phenomena!
- Three fitted laws shown (from Kaplan+ 2020):
  - Compute (PF-days, non-embedding): **L = (C_min / 2.3·10^8)^(-0.050)**
  - Dataset size (tokens): **L = (D / 5.4·10^13)^(-0.095)**
  - Parameters (non-embedding): **L = (N / 8.8·10^13)^(-0.076)**
- They even hold in non-standard settings (when train ≠ test). Figure: test loss vs parameters for WebText2 (Test), Internet Books, Books, Wikipedia, Common Crawl.

## Slide 5 — All you want to know about scaling laws (and more)
Organization: simple to complex:
1. **Data vs performance** — "Are there simple rules that determine how data affects performance?"
2. **Hyper-parameters vs performance** — "Are optimal hyperparameters the same across different data/models?"
3. **Forecasting with scaling laws** — "Does benchmark performance follow predictable trends?"

## Slide 6 — Data vs performance
- What's a data scaling law? **Data scaling laws:** simple formula that maps dataset size (n) to error.
- What do we expect out of scaling laws? Monotonic, logistic-like curves.
- Figure (Hestness+ 2017): generalization error (log-scale) vs training data set size (log-scale) with three regions: **Small Data Region** (Best Guess Error), **Power-law Region**, **Irreducible Error Region** (Irreducible Error).

## Slide 7 — Data scaling laws for language models
- First, an empirical observation: **Loss and dataset size is linear on a log-log plot.**
- Figure: test loss vs dataset size (tokens) with fit **L = (D / 5.4·10^13)^(-0.095)**.
- "Scale-free" or "Power law".
- (For language modeling, from Kaplan+ 2020.)

## Slide 8 — Scaling laws: past works and other areas
- Scaling laws hold in many domains:
  - **Machine translation** (Hestness et al. 2017): token error rate, ε(m) = 3.87 m^(-0.13)
  - **Speech** (Hestness et al. 2017): DS2 ε(m) = 1.36 m^(0.39) [as printed; trend lines for DS2 and Attention], Attention ε(m) = 0.95 m^(0.30)
  - **Language modeling** (Kaplan et al. 2020): L = (D / 5.4·10^13)^(-0.095)
  - **Object recognition** (Rosenfeld 2020)
- Data scaling has been known for a while: Kolachina+ 2012 for machine translation, Hestness+ 2017 for neural.

## Slide 9 — Conceptual foundations of data scaling laws
- **Q:** Why do scaling laws show up? We know error should be monotone. But why is it a power law / linear in log-log?
- **A:** Estimation error naturally decays polynomially.
- This may take a moment to understand. Let's work through an example.
- **Example:** If our task is to estimate the mean of a dataset, what's the scaling law?

## Slide 10 — Toy example: mean estimation
- **Input:** x_1 … x_n ~ N(μ, σ²)
- **Task:** estimate the average as μ̂ = (Σ_i x_i) / n
- **What's the error?** By standard arguments: E[(μ̂ − μ)²] = σ² / n
- **This is a scaling law!!** log(Error) = −log n + 2 log σ
- More generally, any polynomial rate 1/n^α is a scaling law.

## Slide 11 — Scaling law exponents: an intriguing mystery
- **Fact:** Similar arguments show most 'classical' models (regression, etc.) have 1/n scaling.
- This means we should see y = −x + C.
- What do we find in neural scaling laws? (figures: machine translation ε(m)=3.87 m^(-0.13); speech ε(m)=1.36 m^(0.39) and ε(m)=0.95 m^(0.30); language modeling L=(D/5.4·10^13)^(-0.095))
- Very different from predictions.. Why might this be?

## Slide 12 — Detour: scaling laws for (nonparametric) learning
- Neural nets can approximate arbitrary functions. Let's turn that into an example.
- **Input:** x_1 … x_n uniform in 2D unit box. y_i = f(x_i) + N(0,1)
- **Task:** estimate f(x)
- **Approach:** cut up the 2D space into boxes with length n^(−1/4), average in each box.
- **What's our estimation error?** Informally, we have √n boxes, each box gets √n samples. Error ≈ 1/√n + (other smoothness terms)
- In d-dimensions, this becomes **Error = n^(−1/d)** — This means scaling is **y = −(1/d) x + C**.
- **Takeaway:** flexible 'nonparametric' learning has dimension-dependent scaling laws.

## Slide 13 — Intrinsic dimensionality theory of data scaling laws
In case that was a bit too low-level:
1. Scaling laws arise due to polynomial rates of learning 1/n^α.
2. The slope α is closely connected to the **intrinsic dimensionality** of the data.
- Figure: 4/α_D vs Dimension, with reference lines 4/α_D and 2/α_D; datasets Teacher-Student, CIFAR-10, CIFAR-100, SVHN, FashionMNIST, MNIST.
- Some recent work (Bahri+ 2021) have tried to verify this empirically.

## Slide 14 — Other advanced data scaling law: distribution shift
- **Data scaling thus far:** how does dataset size relate to performance?
- **Related question:** how does dataset *composition* affect performance?
- **A:** Data composition affects the offset, not the slope.
- Figure (Kaplan+ 2021): test loss vs parameters (non-embedding) for WebText2 (Test), Internet Books, Books, Wikipedia, Common Crawl.
- These 'distribution shift' scaling laws can tell us about the importance of collecting diverse data!
- Figure (Hashimoto 2021): excess error vs training data size for q = 0.00, 0.22, 0.56; and expected error intercept log C(q) vs data source proportion (U-shaped, minimized around 0.4–0.5).

## Slide 15 — Other advanced data scaling laws: fairness + distr. shift
- **Data diversity:** can we use scaling laws to understand fairness impacts of data?
- **Conjecture:** performance for *minority subgroups* also follow a scaling law.
- Figure (Rolfe+ 2021): Goodreads (history vs fantasy), Mooc (edu ≤ secondary vs edu > secondary), Adult (female vs male) — loss vs # training points from each group (n_A = n_B).
- **We can use scaling laws to optimize data collection for fairness.**

## Slide 16 — Recap: data scaling laws
- Remarkably linear relationship between log-data size and log-error.
- Holds across domains and models.
- Theory understanding: similar to generalization bounds; mean estimation example.
- Applications: data collection, fairness.

## Slide 17 — Scaling laws for model engineering
- Now for what I promised at the start: **model scaling!**
- **Our motivation:** how can we efficiently design huge LMs?
  - LSTMs vs Transformers
  - Adam vs SGD
- How should we allocate our limited resources?
  - Train models longer vs train bigger models?
  - Collect more data vs get more GPUs?
- Scaling laws provide a simple procedure to answer these.

## Slide 18 — Cross-model: transformers vs LSTMs
- **Q:** Are transformers better than LSTMs? Brute force way: spend tens of millions to train an LSTM GPT-3.
- **Scaling law way:** Figure (Kaplan+ 2021): test loss vs parameters (non-embedding); Transformers (blue) keep improving with a steeper, sustained slope, while LSTMs (1 Layer, 2 Layers, 4 Layers) plateau/curve upward at large parameter counts.

## Slide 19 — Optimizer choice
- What about ADAM vs SGD?
- Figure (Hestness+ 2017): minimum validation loss (log-scale) vs training data set size (number of chars, log-scale) for Depth-10 RHNs:
  - SGD trend: ε(m) = 5.37 m^(-0.094)
  - Adam trend: ε(m) = 5.25 m^(-0.095)
- (Note, this is in 2017, so pre-transformers. RHN is recurrent highway nets.)

## Slide 20 — Number of layers
- Does depth or width make a huge difference?
- Figure: test loss vs parameters (non-embedding) for 1, 2, 3, 6, >6 layers.
- 1 vs 2 layers makes a huge difference.
- More layers have diminishing returns below 10^7 params.

## Slide 21 — Side note – scaling laws can sometimes lead us astray
- These scaling laws are already used in the design of LMs.
- Figure (a) Kaplan et al., 2020: test loss vs parameters for 1/2/3/6/>6 layers.
- Figure (b) "This work, Section 5": test loss vs parameters for 6 Layers vs 12 Layers, annotated with "Depth ineff." region and "Depth efficiency" region.
- Table 1 (Levine+ 2021): Comparing the architecture of Jurassic-1 models to their GPT-3 counterparts:
  - **GPT-3 6.7B:** n_params 6.7B, n_layers 32, d_model 4096, n_heads 32, d_head 128, n_vocab 50K
  - **J1-Large:** 7.5B, 32, 4096, 32, 128, 256K
  - **GPT-3 175B:** 175B, 96, 12288, 96, 128, 50K
  - **J1-Jumbo:** 178B, 76, 13824, 96, 144, 256K

## Slide 22 — Some surprising takeaways
- The effect of hyperparameters on big LMs can be predicted *before* training!
  - Optimizer choice
  - Model depth
  - Architecture choice
- **The scaling law based design procedure:**
  1. Train a few smaller models
  2. Establish a scaling law (e.g. ADAM vs SGD scaling law)
  3. Select optimal hyperparam based on the scaling law prediction.

## Slide 23 — Model size data joint scaling
- **Q:** Do we need more data or bigger models?
- Clearly, lots of data is wasted on small models. (Figure: Loss vs Model and Dataset Size, params 708M / 302M / 85M / 3M / 25M / 393.2K; loss vs tokens in dataset.)
- **Joint data-model scaling laws** describe how the two relate.
  - From Rosenfeld+ 2020: **Error = n^(−α) + m^(−β) + C**
  - From Kaplan+ 2021: **Error = [m^(−α) + n^(−1)]^β**
- Provides surprisingly good fits to model-data joint error. (Figure: Wiki103 error (cross entropy) landscape over log2(data fraction) × log2(model fraction).)

## Slide 24 — Model-data joint scaling is accurate
- From Rosenfeld – fit scaling exponents on small data, small models. Predict rest.
- Figures: (a) Illustration of fit (green) vs extrapolated (red) over data fraction × model fraction grid. (b) Extrapolation on ImageNet (μ:-4.5%, σ:4.681%, model fraction 1/16, data fraction 1/8). (c) Extrapolation on WikiText-103 (μ:0.5%, σ:1.689%, model fraction 1/16, data fraction 1/8).
- Trading off data size and model size: optimize **n^(−α) + m^(−β) + C** with your costs.

## Slide 25 — Do we have enough data to feed our models?
- Figures: "Data Size Bottleneck" — test loss vs params (non-embed) for data sizes 21M / 43M / 86M / 172M / 344M / 688M / 1.4B / 22.0B; "Overfitting" — L/L(D=∞) − 1 vs N^(α_N/α_D)/D.
- From Kaplan: Fitted training laws suggest 22B token WebText can fit 10^9 parameters. Model size should scale as **O(m^0.74)**.

## Slide 26 — Compute tradeoffs
- **Q:** what about other resources? Compute vs performance?
- **For a fixed compute budget…** Big model that's undertrained vs small model that's well trained?
- Figures: (Kaplan+ 2021) "Performance vs Compute Budget" — test loss vs parameters (non-embedding), colored by PF-days; (Brown+ 2020) validation loss vs compute (PetaFLOP/s-days) colored by parameters, fit **L = 2.57 · C^(-0.048)**.
- Scaling laws tell us: **properly undertrained models are better.**

## Slide 27 — Compute tradeoffs (2)
- **Q:** as we increase both compute and model size, how should we scale training?
  - Huge batches, same number of steps
  - Fixed batches, more steps
- Figures:
  - Parameters (non-embedding) vs compute (PF-days, non-embedding): **N = (1.3·10^9) · C_min^0.73** (compute-optimal) and **N = (1.6·10^9) · C^0.88** (other line).
  - Steps vs compute (PF-days, excluding embeddings): **S_min = (5.4·10^3) · C_min^0.03** (adjusted) vs S (fixed-batch) which grows much faster.
- Good news for data parallel processing (?).

## Slide 28 — Final detail and remark: 'effective dimensionality'
- We've been thinking about 'parameters' but not all parameters are equal.
- Figures: test loss vs parameters WITH embedding (0, 1, 2, 3, 6, >6 layers) vs test loss vs parameters NON-embedding (1, 2, 3, 6, >6 layers).
- Embedding layer parameters don't behave the same!
- **Related:** recent papers on scaling laws for mixtures of experts.

## Slide 29 — Scaling laws for models and compute
- Log-linearity extends to model parameters and compute!
- Lets us set the following based on small models: Pick optimizer; Pick architecture and model sizes.
- Also lets us make smart resource tradeoffs: Big models vs more data?

## Slide 30 — Scaling laws and the future
- **Q:** Can big language models solve every problem?
- We can use scaling laws to answer this!
  - For each capability (e.g. question answering)..
  - Build a scaling law for compute capacity.
  - Extrapolate the scaling curve.
- Can 'reasonable' amounts of compute solve our problems?
- (Cartoon "STACK MORE LAYERS", from r/programmerhumor.)

## Slide 31 — Forecasting question: will we solve the Winograd schema?
- Classic AI challenge: Winograd schema (twin sentences with pronoun-resolution ambiguity; examples with trophy/suitcase, Ann/Mary, tree/roof, lions/zebras).
- Current GPT-3 performance after seeing 50 examples: **77%**. Can we push this further?

## Slide 32 — How much more compute for human-level reasoning?
- Just extend the line for the scaling law..
- Figure (Winogrande): accuracy vs parameters in LM (0.1B → 175B) for Zero-Shot, One-Shot, Few-Shot (K=50); reference lines for Human, Fine-tuned SOTA, Fine-tuned RoBERTa-Large, Fine-tuned BERT-Large, Random Guessing.
- If the scaling law holds.. Roughly **64× more parameters** will get us to human-level.

## Slide 33 — Another setting: SAT analogies
- Context → "lull is to trust as"; Correct Answer → "cajole is to compliance"; incorrect options listed.
- **Task:** selecting the correct answer (with highest probability).
- Figure (SAT Analogies): accuracy vs parameters in LM (0.1B → 175B) for Zero-Shot, One-Shot, Few-Shot (K=20).
- **Scaling:** clear linear scaling in log space.

## Slide 34 — Less optimistic scaling curves
- **Word in context dataset** (WiC). Examples with target words bed, land, justify, beat in two contexts (T/F whether same sense).
- Figure (WiC): accuracy vs parameters in LM for Zero-Shot, One-Shot, Few-Shot (K=32); reference lines Fine-tune SOTA, BERT-Large, Random Guessing.
- **Scaling:** near-zero. GPT-3 paper notes 'pairwise comparison' tasks are harder.

## Slide 35 — Phase transitions
- **Thus far:** everything has had linear scaling (with different slopes).
- **Phase transitions** are sudden, discontinuous jumps in performance.
- Figure (Arithmetic, few-shot): accuracy vs parameters in LM (0.1B → 175B) for Two/Three/Four/Five Digit Addition & Subtraction, Two Digit Multiplication, Single Digit Three Ops — sharp jumps around 13B–175B.
- The GPT-3 paper has some intriguing observations on phase transitions..
- **Do we expect to see more phase transitions?** This is probably the 'big unknown' in LM scaling!

## Slide 36 — Scaling laws and the future
- Some tasks will just improve continually via scale (Winograd, SAT etc).
- There are some others that may have 'phase transitions' and emergent behavior.
- Finally, more work to be done on some tasks (WiC?).
- **Scaling laws can help with** a key question: what problems can we brute force?

## Slide 37 — Recap: scaling laws – surprising and useful!
- **Data scaling:** understand how data affects models, clean theory.
- **Model scaling:** dramatically reduce costs for training.
- **Scaling as prediction:** understand what problems can be 'brute forced'.
- Scaling laws are interesting for everyone!
  - Theorists (why do we get scaling laws)
  - Practitioners (lets use scaling laws to optimize)
  - AI enthusiasts (can we get AGI with more gpus?)

---

## References cited in the lecture
- Strubell+ 2019 (energy/CO2 cost of training NLP models)
- Hestness et al. 2017 (deep learning data scaling; machine translation, speech, RHN/Adam vs SGD)
- Kaplan et al. 2020 — "Scaling Laws for Neural Language Models" (arXiv:2001.08361)
- Kaplan+ 2021 (cited on several figures — slide deck attribution; refers to the same Kaplan scaling-law line of work)
- Rosenfeld 2020 / Rosenfeld+ 2020 (object recognition; joint data-model scaling, ImageNet & WikiText-103)
- Kolachina+ 2012 (machine translation data scaling)
- Bahri+ 2021 (intrinsic dimensionality theory of scaling)
- Hashimoto 2021 (distribution-shift scaling laws)
- Rolfe+ 2021 (fairness / minority-subgroup scaling laws)
- Levine+ 2021 (Jurassic-1 / AI21; depth efficiency, J1-Large, J1-Jumbo)
- Brown+ 2020 — GPT-3 paper (compute-vs-loss figure; Winogrande, SAT analogies, WiC, arithmetic few-shot, phase transitions)
