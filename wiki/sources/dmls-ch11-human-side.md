---
title: "Designing ML Systems — Ch 11: The Human Side of Machine Learning"
type: source
tags: [book, mlops, user-experience, team-structure, responsible-ai, fairness, privacy, model-cards, oreilly, dmls-book]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch11-human-side.txt
last_updated: 2026-05-23
---

# Designing ML Systems Ch 11 — The Human Side of Machine Learning

## Summary

Chapter 11 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly|O'Reilly Media]], 2022) breaks from the prior eight technical chapters to treat ML as a **sociotechnical** system, organized around three axes: (1) **user experience** under probabilistic, "mostly correct," and high-latency model behavior; (2) **team structure** — cross-functional collaboration with [[AnnotationGuidelines|subject matter experts]] and the debate over whether data scientists should own the end-to-end MLOps pipeline; and (3) **Responsible AI** — co-written with Abhishek Gupta (Montreal AI Ethics Institute) — covering the Ofqual A-level grading scandal, the Strava heatmap anonymization failure, and a six-step practitioner framework (discover bias sources, understand data limits, surface trade-offs, act early, create [[ModelCard|model cards]], establish bias-mitigation processes). The chapter names three signature UX trade-offs — **consistency vs. accuracy**, **speed vs. accuracy**, and **privacy vs. accuracy** — and a fourth, **compactness vs. fairness**, that ties model compression back to algorithmic harm. Its central reframe: ML production is "not just an ML problem but also an infrastructure problem," and ethics is "not a checkbox-ticking activity" but a design constraint that must be acted on early because the cost of fixing bias grows by an order of magnitude at each project lifecycle stage (NASA error-cost study).

## Key Claims

- **ML systems differ from traditional software in three UX-relevant ways: they are probabilistic (same input may yield different outputs at different times), "mostly correct" (predictions are usually right but you don't know for which inputs they'll be wrong), and potentially high-latency.** Each property breaks user expectations carried over from deterministic software.
- **The consistency–accuracy trade-off:** Booking.com's filter-recommendation team had to add a rule-layer specifying when the ML model **must** return the same recommendation (e.g., when the user already applied a filter) and when it can return new ones (e.g., when the user changes destination), because users were getting confused when previously-seen filters disappeared. The accuracy-maximizing recommendation is not always the consistency-preserving one.
- **Combatting "mostly correct" predictions requires either users who can correct outputs or product affordances that let nonexperts evaluate alternatives.** Huyen's worked example: [[GPT3|GPT-3]] generating React code is useful to a React engineer (who can fix bad code) but useless to a no-React user (the app's target audience). The fix is to **show multiple candidate predictions rendered in a form the nonexpert can judge** (rendered web pages, not raw code) — a form of [[humanintheloop|human-in-the-loop]] AI. Huyen cites Jessy Lin's *"Rethinking Human-AI Interaction"* as the reference.
- **The speed–accuracy trade-off motivates "smooth failing" via a backup system.** Some companies route queries to a fast-but-worse backup (heuristic, simple model, or cached predictions) when the main model exceeds a latency budget. More sophisticated setups use a *second model* to predict whether the main model will be slow, then route accordingly — at the cost of adding that predictor's own latency.
- **Subject matter experts (SMEs) — doctors, lawyers, bankers, farmers, stylists — are developers of ML systems, not just labelers.** Their input is needed across problem formulation, [[FeatureEngineering|feature engineering]], error analysis, model evaluation, reranking predictions, and UI design. *"Good luck trying to get your doctor to use Git"* — the practical answer is **no-code/low-code platforms** that let SMEs contribute without engineer-mediated access; most current no-code ML solutions target labeling, QA, and feedback stages.
- **The end-to-end data scientist debate has two organizational answers, each with named drawbacks.** **Approach 1** (separate Ops/platform team productionizes models built by the DS team) creates communication overhead, debugging cross-team blame games, "finger-pointing" failure modes, and narrow-context optimization. **Approach 2** (data scientists own the entire process) creates "grumpy unicorns" expected to know Kubernetes, Airflow, Docker, etc., and writing more boilerplate than data science. Huyen now favors Approach 2 **but only if backed by sufficient internal infrastructure tooling**, citing [[StitchFix|Stitch Fix]]'s Eric Colson and Netflix's full-cycle developer model.
- **Huyen explicitly retracts an earlier position:** her widely-shared 2020 tweet listed Kubernetes as essential to the ML workflow; she now says *"expecting data scientists to know about infrastructure is like expecting app developers to know about how Linux kernels work"* (Erik Bernhardsson's analogy). The answer isn't to require K8s fluency — it's to build abstractions that hide it.
- **The Ofqual A-level grading scandal (UK, summer 2020) is a case study in three concrete failures.** **Failure 1: wrong objective** — Ofqual optimized for "maintaining standards" across schools (fitting predicted grades to historical school-level distributions) rather than grading accuracy for individual students, which downgraded high-performing students from historically low-performing (low-resource, more-underprivileged) schools. **Failure 2: insufficient fine-grained evaluation** — coarse aggregate ~60% accuracy hid bias across school size, teacher-assessment demographics, and protected groups under the 2010 Equalities Act; small schools fell back to teacher grades, which advantaged private-school students who tend to have smaller classes. **Failure 3: lack of transparency** — neither the public nor teachers were told how their inputs would be used until results day, foreclosing external statistical scrutiny (the Royal Statistical Society's inquiry flagged the technical advisory group's composition).
- **The Strava heatmap incident (2018) shows that anonymization is not sufficient.** Strava published a global activity heatmap of 1B activities across 27B km of paths, with PII anonymized and explicit-private activities excluded. Aggregate patterns still **exposed military base locations and patrol routes overseas** (Afghanistan forward operating bases, Turkish patrols in Syria), and analysts argued individual users and heart rates could be inferred. The deeper failure: Strava's privacy default was **opt-out** (users had to actively disable collection, and some settings were only changeable through the website, not the mobile app). *Privacy-respecting defaults should be opt-in.*
- **Disparate impact occurs when a selection process produces different outcomes for different groups even when neutral on its face**, because the model uses features correlated with legally protected classes (e.g., zip code and high-school diploma as proxies for race in hiring). Mitigation tools named: **disparate-impact remover** (Feldman et al., *"Certifying and Removing Disparate Impact"*), [[IBMAIF360|IBM's AI Fairness 360 (AIF360)]]'s `DisparateImpactRemover`, the **Infogram method** for hidden-bias detection in [[H2OAI|H2O]].
- **Two compounding fairness trade-offs that the ML literature usually elides.** (i) **Privacy vs. accuracy via differential privacy** — Bagdasaryan & Shmatikov (2019) found that the accuracy cost of differential privacy is **not uniform**: underrepresented classes and subgroups lose disproportionately more accuracy. (ii) **Compactness vs. fairness** — Hooker et al. (2019, 2020) found that compressed models have similar top-line metrics but diverge on narrow subsets, **amplifying algorithmic harm against protected groups in the long tail**; pruning carries a far higher disparate-impact penalty than the quantization techniques evaluated.
- **Act early: bias remediation cost grows by an order of magnitude per lifecycle stage** (NASA error-cost study, Stecklein et al.). Both Ofqual and Strava illustrate the inverse — cost-saving / time-saving shortcuts in early design produced cascading downstream costs.
- **[[ModelCard|Model cards]] (Mitchell et al., 2018, *"Model Cards for Model Reporting"*) are short documents standardizing ethical disclosure** alongside trained models: model details (developer, date, version, type), intended use (primary use cases, intended users, out-of-scope cases), factors (demographic / phenotypic / environmental), metrics (with decision thresholds), evaluation data, training data, quantitative analyses (unitary and intersectional), ethical considerations, and caveats. Manual maintenance is overhead for frequently-updated models; Huyen predicts model stores will eventually auto-generate them, and lists [[TensorFlow]], [[Metaflow]], and [[scikitlearn|scikit-learn]] as already offering model-card generation features.
- **A six-step framework for Responsible AI in practice:** (1) discover sources of bias across training data, labeling, feature engineering, model objective, and evaluation; (2) understand the limits of the data-driven approach (cross disciplinary/functional lines); (3) understand trade-offs across desiderata (privacy/accuracy, compactness/fairness, latency/accuracy, transparency/IP); (4) act early; (5) create model cards; (6) establish systematic bias-mitigation processes — internal tool portfolios and, where appropriate, third-party audits. Stay current via the **ACM FAccT** conference, the **Partnership on AI**, the Alan Turing Institute's Fairness/Transparency/Privacy group, and the **AI Now Institute**.
- **Responsible AI is not a compliance checkbox.** The framework helps meet compliance, but *"won't be a replacement for critical thinking on whether a product or service should be built in the first place"* — some applications (criminal sentencing, predictive policing) may be inappropriate regardless of the audit framework applied to them.

## Key Quotes

> "ML systems are probabilistic instead of deterministic. Usually, if you run the same software on the same input twice at different times, you can expect the same result. However, if you run the same ML system twice at different times on the exact same input, you might get different results." — Ch 11, opening framing of the UX-vs-software gap

> "Good luck trying to get your doctor to use Git." — Ch 11, on translating SME domain expertise into versionable code

> "Expecting data scientists to know about infrastructure is like expecting app developers to know about how Linux kernels work." — Erik Bernhardsson analogy, quoted in Ch 11; Huyen's retraction of her earlier "data scientists should know Kubernetes" position

> "What one programmer can do in one month, two programmers can do in two months." — Frederick P. Brooks, quoted in Ch 11 on the coordination overhead of separate dev/ops teams

> "Failure 1: setting the wrong objective; Failure 2: insufficient fine-grained model evaluation to discover biases; Failure 3: lack of transparency." — Ch 11, anatomy of the Ofqual A-level grading scandal

> "The accuracy of differential privacy models drops much more for the underrepresented classes and subgroups." — Bagdasaryan & Shmatikov (2019), quoted in Ch 11 on the privacy-accuracy trade-off's disparate impact

> "Compression techniques amplify algorithmic harm when the protected feature (e.g., sex, race, disability) is in the long tail of the distribution." — Hooker et al. (2019), quoted in Ch 11 on the compactness-vs-fairness trade-off

> "It is important to not treat this responsible AI as merely a checkbox ticking activity that we undertake to meet compliance requirements for our organization. … It won't be a replacement for critical thinking on whether a product or service should be built in the first place." — Ch 11, closing thesis on Responsible AI

## Concepts

### New (minted by this chapter, for the parent agent to create)

- **`ConsistencyAccuracyTradeoff.md`** — tension between giving users stable predictions and the most accurate predictions; the Booking.com filter-recommendation case study is the canonical illustration.
- **`SpeedAccuracyTradeoff.md`** — when a worse-but-faster backup model is preferable to the main model for latency-critical queries; rule-based or learned routing between them.
- **`SmoothFailing.md`** — pattern of routing slow main-model inferences to a fast fallback (heuristics, simple models, cached precomputed predictions) once a latency threshold is exceeded.
- **`BackupModel.md`** — the fast/simple companion model used in smooth-failing setups.
- **`MostlyCorrectPredictions.md`** — ML's defining behavior where predictions are usually correct but not deterministically so; productizing this requires correctability affordances or multi-candidate UI.
- **`MultipleCandidatePredictions.md`** — UX pattern of showing N rendered candidates so nonexpert users can pick the best one (e.g., GPT-3 React code rendered as web pages to non-engineers).
- **`SubjectMatterExpert.md`** — domain experts (doctors, lawyers, bankers, etc.) as first-class participants in ML system development, not just labelers.
- **`NoCodeMLPlatform.md`** — tooling pattern enabling SMEs to contribute (labeling, QA, dataset creation, feedback) without engineer-mediated access; most current solutions cluster around labeling/QA.
- **`EndToEndDataScientist.md`** — organizational pattern where data scientists own the full lifecycle from data to production; success conditional on internal abstraction tooling (Stitch Fix / Netflix model).
- **`FullCycleDeveloper.md`** — Netflix's "specialists build tools, generalists use them end-to-end" model, sometimes called the Netflix full-cycle developer pattern.
- **`ResponsibleAI.md`** — practice of designing, developing, and deploying AI with empowerment, trust, fairness, and positive societal impact as first-class goals; consists of fairness, privacy, transparency, accountability.
- **`AlgorithmicFairness.md`** — fairness as both a model property (metrics) and a process property (objective choice, evaluation granularity, transparency).
- **`DisparateImpact.md`** — when an apparently neutral selection process produces widely different outcomes for different groups (Feldman et al., 2015); arises when the model uses features correlated with protected classes.
- **`DisparateImpactRemover.md`** — Feldman et al. technique to repair disparate impact in features, implemented in AIF360.
- **`DifferentialPrivacy.md`** — formal privacy guarantee that single-row substitutions have bounded effect on query results; carries a privacy-vs-accuracy trade-off that is **not uniform across subgroups**.
- **`PIIAnonymization.md`** — the practice (and limits) of stripping personally-identifiable information from datasets before release; the Strava heatmap is the canonical "anonymization is not enough" cautionary case.
- **`OptInVsOptOut.md`** — privacy-default debate; Huyen's prescription is that opt-in should be the default for data collection.
- **`CompactnessFairnessTradeoff.md`** — finding from Hooker et al. (2019, 2020) that model compression amplifies algorithmic harm against long-tail protected groups; pruning is worse than quantization on this axis.
- **`PrivacyAccuracyTradeoff.md`** — differential privacy reduces accuracy non-uniformly, hurting underrepresented subgroups more.
- **`ModelCard.md`** — Mitchell et al. (2018) standardized disclosure document for trained models; intended-use, factors, metrics, evaluation data, training data, ethical considerations.
- **`AIIncidentDatabase.md`** — public registry of AI failures referenced in the Responsible AI section.
- **`FineGrainedEvaluation.md`** — evaluating model performance across slices (school size, demographic group, etc.) rather than only aggregate accuracy; Ofqual's failure to do this hid systemic bias. (Note: distinct from existing `BiasMitigationFinetuning` / `slice-based evaluation` concepts.)
- **`OfqualGradingAlgorithm.md`** — 2020 UK A-level auto-grader case study; canonical illustration of wrong-objective + coarse-evaluation + opaque-process failure modes.
- **`StravaHeatmap.md`** — 2018 fitness-app heatmap incident that exposed US/allied military base activity despite anonymization; canonical illustration of aggregate-patterns-defeat-anonymization.
- **`ConsistencyAccuracyTradeoff.md`** — see above (single entry, not duplicated).

### Reused (existing pages that should reference / be referenced by this chapter)

- [[MLOps]] — "ML production is not just an ML problem but also an infrastructure problem" is the chapter's MLOps thesis.
- [[humanintheloop|Human-in-the-Loop]] — multi-candidate UX and SME involvement are concrete HITL patterns.
- [[HumanInTheLoopApproval]] — adjacent concept on humans-in-the-loop as gatekeepers.
- [[Latency]] / [[InferenceOptimization]] / [[ModelCompression]] / [[Pruning]] / [[Quantization]] — the speed-vs-accuracy and compactness-vs-fairness trade-offs link directly back here.
- [[FeatureEngineering]] — named as a bias-injection point.
- [[AnnotationGuidelines]] / [[DataAnnotation]] — labeling-stage bias source; SMEs as labelers.
- [[Responsibility]] — already-extant short concept; should be cross-linked from the new ResponsibleAI page.
- [[ExplicitFeedback]] / [[ImplicitFeedback]] — Ch 11's UX framing is upstream of Ch 10 of the AI Engineering book's feedback chapter; cross-link.
- [[DegenerateFeedbackLoop]] — Ch 11's bias-amplification mechanism is the same phenomenon DMLS Ch 8 (data) and AI Engineering Ch 10 (feedback) describe.
- [[Monitoring]] / [[observability]] / [[ModelMonitoring]] — fine-grained evaluation feeds into post-deployment monitoring.
- [[GPT3|GPT-3]] / [[LargeLanguageModel]] — GPT-3 React-code example as the "mostly correct" worked example.
- [[stanforduniversity|Stanford]] — Huyen's affiliation when the book was written.
- [[CovariateShift]] / [[DataDrift]] — training/serving distribution mismatch is a bias source upstream of fairness failures.

## Entities

### New (to be created)

- **`AbhishekGupta.md`** — founder & principal researcher, Montreal AI Ethics Institute; co-author of Ch 11's Responsible AI section.
- **`MontrealAIEthicsInstitute.md`** — applied technical-and-policy AI ethics organization; co-author affiliation for the Responsible AI section.
- **`Ofqual.md`** — UK Office of Qualifications and Examinations Regulation; deployer of the failed 2020 A-level auto-grader.
- **`Strava.md`** — fitness-tracking company whose 2018 heatmap publication exposed military base activity patterns despite anonymization.
- **`BookingCom.md`** — travel-accommodation site whose 2020 ML filter-recommendation case study introduced the consistency-accuracy trade-off.
- **`CathyONeil.md`** — mathematician and author of *Weapons of Math Destruction* (Crown Books, 2016).
- **`WeaponsOfMathDestruction.md`** — Cathy O'Neil's 2016 book, named as foundational reading on algorithmic harm.
- **`MargaretMitchell.md`** — first author of *"Model Cards for Model Reporting"* (2018) and ethical-AI researcher.
- **`TimnitGebru.md`** — co-author of the Model Cards paper and named tutorial author on fairness/accountability/transparency/ethics (2020).
- **`EmilyDenton.md`** — co-author of fairness/accountability/transparency/ethics tutorials (2020), named in the Responsible AI further-reading list.
- **`SaraHooker.md`** — first author of *"What Do Compressed Deep Neural Networks Forget?"* (2019) and *"Characterising Bias in Compressed Models"* (2020); named slide-deck author on fairness/security/governance (2022).
- **`EricColson.md`** — Stitch Fix Chief Algorithms Officer (formerly VP Data Science & Engineering at Netflix); author of *"Beware the Data Science Pin Factory"* (2019).
- **`EugeneYan.md`** — author of *"Unpopular Opinion — Data Scientists Should Be More End-to-End"* (2020).
- **`ErikBernhardsson.md`** — engineer-author of the "expecting data scientists to know about infrastructure is like expecting app developers to know about Linux kernels" analogy (2021).
- **`FrederickBrooks.md`** — author of *The Mythical Man-Month*; quoted on coordination overhead between separate teams.
- **`JessyLin.md`** — author of *"Rethinking Human-AI Interaction"*, named as the reference for human-in-the-loop AI design.
- **`IBMAIF360.md`** — IBM's open-source AI Fairness 360 toolkit (metrics, explanations, bias-mitigation algorithms); houses the `DisparateImpactRemover`.
- **`H2OAI.md`** — H2O.ai's ML platform; implements the Infogram method for hidden-bias detection in features.
- **`AdaLovelaceInstitute.md`** — UK think tank; Jones & Safak's analysis of the Ofqual auto-grader is referenced.
- **`RoyalStatisticalSociety.md`** — UK statistical body whose inquiry challenged Ofqual's process.
- **`ACMFAccT.md`** — ACM Conference on Fairness, Accountability, and Transparency; the field's canonical venue.
- **`PartnershipOnAI.md`** — multistakeholder AI-ethics partnership organization.
- **`AlanTuringInstitute.md`** — UK national institute for data science and AI; named for its Fairness/Transparency/Privacy group. (Note: existing `AlanTuring.md` entity is the person, not the institute.)
- **`AINowInstitute.md`** — NYU-based AI policy research institute, named in the further-reading list.
- **`NIST.md`** — US National Institute of Standards and Technology; publisher of *NIST Special Publication 1270* on bias in AI.
- **`TrustworthyML.md`** — community-maintained resource list for trustworthy ML research and practice.
- **`MetaflowModelCards.md`** — (entity or concept) Metaflow's model-card generation feature.

### To update

- **`ChipHuyen.md`** — add Ch 11 as the human-side / Responsible-AI chapter of DMLS; note her self-retraction on the "Kubernetes is essential" position.
- **`OReilly.md`** — add DMLS (2022) as a published title if not yet enumerated.
- **`StitchFix.md`** — add Eric Colson and the "full-stack data science generalist" position as cited in Ch 11.
- **`Kubernetes.md`** — add Huyen's retraction context as a representative MLOps-overreach example.
- **`Airflow.md`** / **`Metaflow.md`** / **`TensorFlow.md`** / **`scikitlearn.md`** — add Ch 11 as a source noting these tools' role in end-to-end DS workflows (and TensorFlow/Metaflow/scikit-learn as having model-card generation features).
- **`Responsibility.md`** — cross-link to the new `ResponsibleAI.md` concept (philosophical vs. practical/engineering framing).
- **`GPT3.md` (or `LargeLanguageModel.md` / `GPT4.md` family)** — add the GPT-3 React-code-generation worked example as one of Huyen's canonical "mostly correct" illustrations.
- **`MLOps.md`** — add the Ch 11 thesis that ML production = ML problem + infrastructure problem; cite the Approach-1-vs-Approach-2 team-structure debate.
- **`humanintheloop.md` / `HumanInTheLoopApproval.md`** — add the Ch 11 multi-candidate-presentation pattern; cite Jessy Lin.
- **`ModelCompression.md` / `Pruning.md` / `Quantization.md`** — add the Hooker et al. compactness-vs-fairness finding (compression amplifies harm on long-tail protected groups; pruning > quantization on disparate-impact penalty).
- **`DataAnnotation.md` / `AnnotationGuidelines.md`** — cross-link Ch 11's labeling-stage bias-source discussion.

## Connections

- [[ChipHuyen]] — author; this is Ch 11 of her *Designing Machine Learning Systems* (DMLS, O'Reilly 2022), the predecessor to her later *AI Engineering* (2024).
- [[OReilly]] — publisher.
- [[MLOps]] — Ch 11 formalizes the "ML = data + infra" framing that underpins MLOps as a discipline.
- [[humanintheloop]] / [[HumanInTheLoopApproval]] — multi-candidate UX, SME involvement, and human correction of "mostly correct" predictions are HITL patterns.
- [[GPT3|GPT-3]] — the React-code-generation worked example for mostly-correct predictions.
- [[Latency]] / [[InferenceOptimization]] / [[ModelCompression]] / [[Pruning]] / [[Quantization]] — speed-accuracy and compactness-fairness trade-offs.
- [[FeatureEngineering]] — named as one of the five bias-injection points in the framework.
- [[AnnotationGuidelines]] / [[DataAnnotation]] — SME-driven labeling and inter-annotator-bias mitigation.
- [[ExplicitFeedback]] / [[ImplicitFeedback]] — DMLS Ch 11's UX framing is upstream of the AI Engineering Ch 10 feedback taxonomy.
- [[DegenerateFeedbackLoop]] — the bias-amplification mechanism that Ch 11's "act early" guidance is designed to forestall.
- [[StitchFix]] — Eric Colson's *"Beware the Data Science Pin Factory"* is one of two named anchors for the end-to-end-DS position.
- [[NetflixPrize]] — same parent org as the full-cycle developer model Ch 11 cites (separate concept but useful corpus neighbor).
- [[Kubernetes]] / [[Airflow]] / [[Metaflow]] / [[TensorFlow]] / [[scikitlearn]] — the infra tools Huyen now argues data scientists should be *abstracted from*, with TensorFlow/Metaflow/scikit-learn singled out for model-card auto-generation.
- [[Monitoring]] / [[observability]] / [[ModelMonitoring]] — fine-grained evaluation and bias auditing extend into post-deployment monitoring.
- [[CovariateShift]] / [[DataDrift]] — bias surfaces in deployed models when serving distributions diverge from training distributions.
- [[Responsibility]] — short existing concept; the new `ResponsibleAI` page is the practitioner-facing extension.
- [[stanforduniversity|Stanford]] — Huyen's affiliation at the time of DMLS.
- [[ai-engineering-chip-huyen]] / [[ai-engineering-ch10-architecture-feedback]] — sibling source pages; DMLS Ch 11 is the conceptual predecessor of AI Engineering Ch 10's feedback / observability / user-experience discussion (often cross-referenced).

## Contradictions

- **Internal retraction (not a wiki contradiction):** Huyen's earlier-tweet position that data scientists should know Kubernetes is **explicitly retracted in this chapter** — *"as I learned more about low-level infrastructure, I realized how unreasonable it is to expect data scientists to know about it."* The retraction is in-chapter and self-acknowledged; downstream wiki pages on Kubernetes / MLOps should reflect the updated stance.
- **Tension with the [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]] discussion of `liked-this-suggestion` / accept-rate feedback signals:** Ch 11 says systems should be transparent and let users understand how their input shapes the model; Ch 10 (and the modern data-flywheel literature) celebrates collecting implicit signals at scale. The two are reconcilable but the wiki should make the trade-off explicit (transparency requires telling users that their edits/likes/acceptances are training data, which can suppress the signals being collected).
- No contradictions with extant wiki pages were detected.

## Bibliographic detail

- **Title**: Designing Machine Learning Systems
- **Author**: [[ChipHuyen|Chip Huyen]]
- **Publisher**: [[OReilly|O'Reilly Media, Inc.]]
- **Edition**: First Edition, May 2022 (Revision: 2022-05-17 First Release)
- **Chapter**: 11 — *The Human Side of Machine Learning*
- **Section co-author**: Abhishek Gupta (Montreal AI Ethics Institute) co-wrote the Responsible AI section.
- **Source**: `raw/books/designing-ml-systems/dmls-ch11-human-side.txt`
