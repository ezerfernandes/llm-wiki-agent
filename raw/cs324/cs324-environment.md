# Stanford CS324 (Winter 2022) — Environmental impact
Source: https://stanford-cs324.github.io/winter2022/lectures/environment/
Fetched for wiki ingest.

---

## Learning Goals

The lecture states three explicit learning objectives:

1. Gain a **holistic understanding** of how large language models fit into the larger environmental story.
2. Be able to **calculate the emissions** impact of training a particular language model.
3. Gain an **awareness** and even personal responsibility towards monitoring and mitigating (negative) environmental impact.

---

## Key Framing: The Climate Crisis Context

- Current warming: **1.2°C** above pre-industrial levels.
- Safety threshold: remain below **1.5°C**.
- Current trajectory: **2.7°C** within decades.

LLM scale examples used to set the stage:

- Strubell et al. (2019): training BERT ≈ **626,000 lbs CO2eq** (presented as ≈ the lifetime emissions of 5 cars).
- DeepMind **Gopher**: ~**380 net metric tons CO2eq**.

---

## Life Cycle Assessment (LCA)

Following **ISO 14040 / 14044** standards, the framework examines three phases.

### Production Phase
- Raw material extraction and metal conversion.
- Manufacturing processes.
- Transportation / shipping.
- For CPU-only data centers, **40%** of emissions come from production (Berthoud et al. 2020).
- iPhone 5 manufacturing: **75%** of total lifecycle emissions come from the production phase.

### Use Phase
- Data acquisition, production, storage.
- Model training — a one-time cost until updates are needed, including experimentation / hyperparameter tuning.
- Inference in production (e.g., Google processes **5.6 billion** search queries daily).

### End-of-Life Phase
- Dismantling, recycling, disposal.
- **80%** of electronic equipment lacks formal collection.

---

## Environmental Impact Categories (beyond greenhouse gases)

- **Water footprint:** Data center cooling consumes freshwater; electricity generation ranks second in water consumption.
- **Human toxicity:** Chemicals from chip manufacturing create toxic waste sites.
- **Abiotic resource depletion:** Fossil fuels; rare minerals such as lithium and cobalt.

---

## Climate Change Mechanics

### Temperature Trends
- Surface temperature has risen **2.14°F (1.19°C)** since 1900.
- The 10 warmest years on record have occurred since 2005.

### Greenhouse Gas Global Warming Potential (GWP, 100-year horizon)
- **CO2:** GWP = 1 (reference standard).
- **Methane:** GWP = 25.
- **Nitrous oxide:** GWP = 300 (atmospheric lifetime: 121 years).

### Emission Sources
- Fossil fuel burning (electricity generation, manufacturing, transportation).
- Agricultural practices (fertilizers).
- Deforestation.

**Trend:** Greenhouse gas emissions have increased **90%** since 1970.

---

## Energy Use and Greenhouse Gas Emissions

### Carbon Intensity (emissions per kWh)
Varies dramatically by location and energy source:
- **Quebec** (hydroelectric): low-carbon baseline reference.
- **Estonia** (coal): ~**30x** higher carbon intensity than Quebec.

### Data Center Energy Statistics
- Global data centers: **205 billion kWh** in 2018 (**1%** of total worldwide electricity).
- United States data centers: **1.8%** of US electricity (2014).
- US data center emissions: **0.5%** of total US greenhouse gas emissions.
- **30%** of global data centers are located in the United States.

**Positive Efficiency Trend:** Computing workloads increased **550%** (2010–2018) while electricity consumption rose only **6%**.

### Temporal and Geographic Accounting Factors
- Season and time-of-day variations in grid carbon intensity.
- Cross-border electricity exchanges obscure actual emission locations.
- California receives **40%** of its (electricity-related) emissions from other regions.

---

## Estimating Emissions for Training Models

### Strubell et al. (2018/2019)

**Formula:**

emissions = R_{power → emit} × PUE × (p_cpu + p_gpu + p_dram)

Where:
- **p_cpu** = average CPU power (watts)
- **p_gpu** = average GPU power (watts)
- **p_dram** = average DRAM power (watts)
- **PUE** = Power Usage Effectiveness = total data center power / IT equipment power
- **R_{power → emit}** = emissions per kWh

**Parameters used:**
- PUE = **1.58** (2018 global data center average)
- R_{power → emit} = **0.954 lbs CO2eq per kWh** (2018 average)

**Results:**
- **BERT-base** (110M parameters): **1,438 lbs CO2eq** (79.2 hours on 64 V100 GPUs).
- **Neural Architecture Search for Evolved Transformer** (213M params): **626,155 lbs CO2eq**.
  - Proxy task: 10 hours on 1 TPUv2.
  - Full search: 32,623 hours (979M steps).
- Round-trip flight NYC–SF: **1,984 lbs CO2eq** (comparison point).
- Car lifetime emissions: **126,000 lbs CO2eq** (comparison point).

### Patterson et al. (2021), Google — "Carbon Emissions and Large Neural Network Training"

**Overall formula:**

emissions = R_{power → emit} × [Energy_train + (queries × Energy_inference)]

**Training formula:**

emissions = hours-to-train × num-processors × power-per-processor × PUE × R_{power → emit}

**Key insight:** NVIDIA reports that **80% of the ML workload is inference, not training.**

**Design variables that drive emissions:**
- Model architecture (Transformer vs. Evolved Transformer).
- Processor type (NVIDIA P100 vs. Google TPUs).
- Data center PUE (average 1.58 vs. Google **1.11**).
- Energy mix (average 0.429 vs. Google **0.080 kg CO2eq/kWh** net, after clean energy credits).

**Per-model training estimates:**

| Model | Energy (MWh) | CO2eq |
|-------|--------------|-------|
| T5 | 86 | 47 tCO2eq |
| GShard | 24 | 4.3 net tCO2eq |
| Switch Transformer | 179 | 59 tCO2eq |
| GPT-3 | 1,287 | 552 tCO2eq |

**Key critique of prior work (Strubell):**
- The neural architecture search estimate was overstated — Patterson et al. argue it was overestimated by a large factor (the lecture cites figures of ~18.7x / ~88x in re-examining the NAS / Evolved Transformer numbers).
- Architecture search is conducted once; the resulting Evolved Transformer is reusable across many applications, so amortizing the search cost over one model is misleading.
- Google's four largest models consumed **< 0.005%** of the company's **12.2 TWh** usage.
- Bitcoin mining consumes approximately **10x** more compute than these four models.

---

## Caveats and Limitations

- Lack of monitoring and transparency in data center operations.
- Proprietary information restrictions.
- Difficulty assigning costs across amortized infrastructure (building construction + multiple models + downstream adaptation).
- **All presented numbers are estimates, not measurements.**
- Benefits are often distributed globally while costs fall "disproportionately on the poor and vulnerable."

---

## Second-Order Effects

- **Rebound effect / Jevons paradox:** efficiency gains increase demand.
- Environmental feedback loops: melting permafrost accelerates emissions.
- Supply chain disruptions: chip shortages affect automobile manufacturing.
- Accelerated desertification and extinction rates.

---

## Mitigation Strategies

### Carbon-Focused
- Train on cleaner energy grids.
- Carbon offsets (used with caution — forest planting can yield monocultures).
- Efficient architectures, training procedures, and hardware (monitor for rebound effects).

### Behavioral / Institutional Incentives
- Mandatory emissions reporting raises awareness.
- Reporting norms shift evaluation criteria beyond accuracy alone.

---

## Python Monitoring Tools (Packages)

- **Environment Impact Tracker** (Henderson et al. 2020)
- **Carbon Tracker**
- **CodeCarbon**

---

## Key Tensions and Trade-offs

- Small current footprint, but rapidly expanding.
- General-purpose models enable "train once, deploy widely" efficiency but require expensive retraining.
- Trade-offs between centralized large models versus distributed smaller models remain unclear.
- Inference dominates training in real-world deployments (~80/20 split).

---

## Summary Conclusions

Environmental impact assessment requires systems-level thinking across full lifecycles. While the current LLM training footprint remains modest, the growth trajectory is steep. Primary mitigation paths include location selection for cleaner energy, architectural efficiency, and institutional norms around emissions reporting.

---

## Major Section Headers (verbatim)

- Life cycle assessment
- Climate change
- Energy use and greenhouse gas emissions
- Estimating emissions for training models
- Python packages
- Summary
- Further reading

---

## Notable Quotes (verbatim)

> "NVIDIA: 80% of the ML workload is inference, not training"

> costs fall "disproportionately on the poor and vulnerable"

---

## Primary References / Further Reading

- **Strubell et al. (2019)** — "Energy and Policy Considerations for Deep Learning in NLP"
- **Lacoste et al. (2019)** — introduces the ML CO2 Impact / Carbon Emissions Calculator
- **Patterson et al. (2021)** — "Carbon Emissions and Large Neural Network Training" (Google)
- **Ligozat et al. (2021)** — "Unraveling the hidden environmental impacts of AI solutions"
- **Henderson et al. (2020)** — Environment Impact Tracker tool
- **Berthoud et al. (2020)** — data center production-phase emissions analysis
