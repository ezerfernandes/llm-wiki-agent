---
title: "CS324 — Environmental Impact"
type: source
tags: [cs324, llm, course-lecture, environment]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/environment/
---

## Summary
This Stanford CS324 (Winter 2022) lecture examines the environmental impact of large language models through a full life-cycle assessment lens: production, use (training and inference), and end-of-life. It surveys two competing emissions accounting methodologies — [[StrubellEtAl]] (2019) and [[PattersonEtAl]] (2021) — that yield very different estimates for the same models, then covers energy/carbon-intensity dynamics, mitigation strategies, and monitoring tooling. The core takeaway is that LLM training's current carbon footprint is modest relative to global activity but growing steeply, with inference (not training) dominating real-world ML workloads.

## Key Claims
- Training [[BERT]] emits ≈ **626,000 lbs CO2eq** per the often-cited [[StrubellEtAl]] framing (compared to ~5 cars' lifetime emissions); DeepMind's [[Gopher]] is estimated at ~**380 net metric tons CO2eq**.
- [[LifeCycleAssessment]] (per ISO 14040/14044) spans production (raw materials, manufacturing, shipping), use (data, training, inference), and end-of-life (recycling, disposal); for CPU-only data centers, ~40% of emissions are from production, and 80% of electronic equipment lacks formal collection.
- [[StrubellEtAl]] emissions formula: `emissions = R_{power→emit} × PUE × (p_cpu + p_gpu + p_dram)`, using [[PowerUsageEffectiveness]] (PUE) = 1.58 (2018 global average) and R = **0.954 lbs CO2eq/kWh**.
- Strubell's specific results: [[BERT]]-base (110M params) ≈ **1,438 lbs CO2eq** (79.2h on 64 V100 GPUs); Neural Architecture Search for the [[EvolvedTransformer]] (213M) ≈ **626,155 lbs CO2eq**.
- [[PattersonEtAl]] (Google, 2021) per-model training estimates: [[T5]] = 86 MWh / 47 tCO2eq; [[GShard]] = 24 MWh / 4.3 net tCO2eq; [[SwitchTransformer]] = 179 MWh / 59 tCO2eq; [[GPT-3]] = **1,287 MWh / 552 tCO2eq**.
- [[PattersonEtAl]] argue [[StrubellEtAl]]'s NAS estimate was overstated by a large factor (cited figures ~18.7x–88x) because architecture search is a one-time cost amortizable across the many downstream uses of the resulting reusable model.
- Emissions depend heavily on four design variables: model architecture, processor type (NVIDIA P100 vs. Google TPUs), data-center PUE (1.58 average vs. Google's **1.11**), and energy mix (0.429 average vs. Google's **0.080 kg CO2eq/kWh** net).
- [[CarbonIntensity]] of electricity varies ~30x by location (e.g., coal-powered Estonia vs. hydroelectric Quebec), and varies by season, time-of-day, and cross-border grid exchanges — so where and when a model trains matters enormously.
- Inference, not training, dominates: NVIDIA reports **80% of the ML workload is inference**; e.g., Google handles ~5.6 billion search queries daily.
- Global data centers used **205 billion kWh** in 2018 (~1% of global electricity); from 2010–2018 computing workloads rose **550%** while data-center electricity rose only **6%**; US data centers are ~0.5% of US greenhouse gas emissions and ~30% of global data centers sit in the US.
- Google's four largest models consumed **<0.005%** of the company's 12.2 TWh usage, and Bitcoin mining uses ~10x more compute than those four models combined.
- All published figures are **estimates, not measurements**, limited by lack of monitoring, proprietary opacity, and the difficulty of amortizing infrastructure costs.
- Mitigation: train on cleaner grids, pursue efficient architectures/hardware (watching for [[ReboundEffect]] / Jevons paradox), use cautious carbon offsets, and mandate emissions reporting to shift evaluation norms beyond accuracy.
- [[CO2]] is the GWP reference (=1); methane GWP = 25; nitrous oxide GWP = 300 (121-year lifetime); global greenhouse gas emissions have risen ~90% since 1970.

## Key Quotes
> "NVIDIA: 80% of the ML workload is inference, not training" — emphasizing that inference, not training, dominates real-world ML carbon cost.

> costs fall "disproportionately on the poor and vulnerable" — on the inequitable distribution of climate harms versus globally distributed benefits.

## Connections
- [[StanfordCS324]] — this is a lecture within the course.
- [[StrubellEtAl]] — origin of the widely cited BERT/NAS emissions estimates and the per-component power formula.
- [[PattersonEtAl]] — Google's competing, lower estimates and critique of Strubell's amortization.
- [[GPT-3]] — largest model in Patterson's table (1,287 MWh / 552 tCO2eq).
- [[BERT]] — anchor example for Strubell's training-emissions calculation.
- [[EvolvedTransformer]] / [[Transformer]] — the architecture whose Neural Architecture Search drove the headline 626k lbs estimate.
- [[T5]], [[GShard]], [[SwitchTransformer]], [[Gopher]] — models with reported energy/CO2eq figures.
- [[CarbonEmissions]] — central metric (CO2eq) the lecture quantifies.
- [[EnergyConsumption]] — kWh/MWh inputs to the emissions calculations.
- [[CarbonIntensity]] — emissions-per-kWh factor that varies by grid and time.
- [[PowerUsageEffectiveness]] — data-center overhead multiplier (PUE) in both formulas.
- [[LifeCycleAssessment]] — the production/use/end-of-life accounting framework.
- [[ReboundEffect]] — second-order risk where efficiency gains increase total demand.
- [[CO2]] — greenhouse gas reference standard for GWP comparisons.

## Contradictions
- [[StrubellEtAl]] and [[PattersonEtAl]] materially disagree on the emissions of Neural Architecture Search for the [[EvolvedTransformer]]; Patterson argues Strubell overstated it by ~18.7x–88x due to ignoring that the search is a one-time, amortizable cost. The lecture presents this as a methodological dispute over amortization rather than a factual error in measurement.
