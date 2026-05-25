---
title: "Designing ML Systems — Ch 7: Model Deployment and Prediction Service"
type: source
tags: [book, mlops, deployment, prediction-service, batch-prediction, online-prediction, model-compression, edge-ml, dmls, oreilly]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch07-model-deployment.txt
last_updated: 2026-05-23
---

# Designing ML Systems — Ch 7: Model Deployment and Prediction Service

## Summary

Chapter 7 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly|O'Reilly Media]], 2022) is the engineering core of the book — the chapter that takes a trained model from a notebook to a production prediction service. Huyen opens by debunking four deployment myths (one or two models, model performance stays constant, infrequent updates, scale doesn't matter), then frames the central design axes: **[[BatchInference|batch prediction]] vs [[OnlineInference|online prediction]]** (with the further distinction between online-with-batch-features and online-with-streaming-features = *streaming prediction*), and **[[ModelServing|cloud vs edge]]** computation. Each axis comes with a checklist of trade-offs — latency, throughput, cost, responsiveness to user preference shifts, network reliability, privacy/[[GDPR]], compute and battery on consumer devices.

The chapter's technical second half covers **[[ModelCompression|model compression]]** (low-rank factorization, [[KnowledgeDistillation|knowledge distillation]], [[Pruning|pruning]], [[Quantization|quantization]] — Huyen flags quantization as the most generally applicable and easiest to deploy), then turns to **compiling and optimizing models for edge devices**: framework-to-hardware support matrices, **[[IntermediateRepresentation|intermediate representations]] (IRs)** as the bridge between many frameworks and many hardware backends, **[[Lowering|lowering]]** from high-level computation graphs to hardware-native code, four standard local optimizations (**[[Vectorization|vectorization]], parallelization, [[LoopTiling|loop tiling]], [[OperatorFusion|operator fusion]]**), and the use of **ML to optimize ML** (cuDNN autotune, [[TVM|autoTVM]]) when hand-tuned heuristics scale poorly. The chapter closes with **[[WebAssembly|WebAssembly (WASM)]]** as a hardware-agnostic browser deployment target — performant relative to JavaScript but ~45–55% slower than native code (Jangda et al.). Huyen's thesis: as hardware specializes, **online prediction on-device** will become the default; today's batch-prediction architectures are largely a legacy artifact of MapReduce-era big data systems.

## Key Claims

- **"Deploy" is loose, but production is a spectrum.** The naive deployment (wrap a `predict()` in [[FastAPI]]/[[Flask]] POST endpoint, containerize, push to AWS/GCP) takes hours; the hard parts — millisecond latency for millions of users, 99% uptime, observability, rapid update cadence — take years.
- **Production typically involves dozens-to-thousands of models, not one.** Uber has thousands in production; Booking.com has 150+; in the 2021 Algorithmia survey, 41% of organizations with > 25,000 employees run > 100 models. A single ride-sharing app may need separate models per country × per use case (demand, ETA, pricing, fraud, churn).
- **ML systems degrade ("software/bit rot" + [[DataDistributionShift|data distribution shift]]).** Performance peaks right after training and decays — the right question is *"how often can I update?"*, not *"how often should I?"* Etsy deployed 50×/day in 2015; Netflix thousands/day; AWS every 11.7 seconds; Weibo's ML iteration cycle is **10 minutes**.
- **Three prediction modes matter:** (1) batch prediction using only batch features, (2) online prediction using only batch features (e.g., precomputed embeddings fetched at request time), (3) online prediction using both batch and streaming features = *streaming prediction*.
- **Batch vs online is fundamentally a latency-vs-throughput trade-off.** Batch (asynchronous) optimizes for throughput, runs periodically on accumulated data, requires knowing inputs in advance, and is well-suited to recommender systems. Online (synchronous) optimizes for low latency, generates predictions on arrival, and is required for cases (fraud detection, autonomous driving, voice assistants, translation, face/fingerprint unlock, fall detection, high-frequency trading) where late or precomputed predictions either fail catastrophically or can't be enumerated.
- **Online prediction is not necessarily more expensive than batch.** A common myth: vectorization makes batch cheaper. Counter: with online you don't generate predictions for absent users — Grubhub had 31M users but only 622K daily orders, so batch wastes 98% of compute. As hardware improves, **online prediction is on track to become the default**.
- **Two pipelines (batch training + streaming inference) is the single most common source of ML production bugs.** Companies like Uber and Weibo have unified pipelines via Apache Flink; [[FeatureStore|feature stores]] (Ch 10) help ensure batch/streaming feature consistency.
- **Model compression has four common families: [[LowRankFactorization|low-rank factorization]], [[KnowledgeDistillation|knowledge distillation]], [[Pruning|pruning]], [[Quantization|quantization]].** Originally aimed at edge deployment, but smaller models also run faster on the cloud. Quantization is the most general and easiest; the others are model/architecture-specific.
- **Knowledge distillation case study: [[DistilBERT]] is 40% smaller, 60% faster, and retains 97% of [[bert|BERT]]'s language understanding capability** (Sanh et al. 2019). The student/teacher framework is architecture-agnostic but depends on having a trained teacher.
- **Pruning has two senses (remove nodes vs. zero out weights).** Frankle & Carbin's lottery-ticket hypothesis shows pruning can remove > 90% of non-zero parameters without accuracy loss; Liu et al. (2018) argued the pruned *architecture* matters more than the *weights*; Zhu et al. (2017) found pruned-then-retrained still outperforms dense baselines. Huyen flags (Ch 11) that pruning can introduce bias.
- **Quantization (lower bit precision) is the dominant compression lever.** [[FP32]] → [[FP16]] (half precision) halves memory; INT8 ("fixed point") quarters it; 1-bit ([[BinaryConnect]], [[XnorNet]]) is extreme. The Roblox case study scaled BERT to 1+ billion daily CPU requests with 25K inferences/s under 20ms latency; **quantization (FP32 → INT8) gave a 7× latency reduction and 8× throughput increase** — the largest single boost in their pipeline.
- **Quantization Aware Training (QAT) vs Post-Training Quantization (PTQ).** QAT trains in lower precision and supports larger effective batch sizes; PTQ quantizes after training (free in TensorFlow Lite / PyTorch Mobile / TensorRT, a few lines of code). [[NVIDIA]] Tensor Cores enable mixed-precision; Google TPUs train with [[BF16|Bfloat16]] ("the secret to high performance on Cloud TPUs").
- **Cloud bills can break companies.** Pinterest, Infor, Intuit spent hundreds of millions per year on cloud (2018); small/medium companies $50K–$2M/year; a single misconfigured Firebase/Cloud Run instance has burned $72K. This cost pressure is the primary driver pushing computation to the edge.
- **Edge computing's appeal goes beyond cost:** offline operation (rural areas, no-internet policies), lower network latency (often a bigger bottleneck than inference latency — ResNet-50 inference might be 30 ms but network round-trip seconds), privacy/[[GDPR]] compliance (no data transfer over the network), and reduced blast radius for breaches ("Nearly 80% of companies experienced a cloud data breach in past 18 months").
- **Edge constraints are compute + memory + battery.** Running a full BERT on a phone kills the battery fast. > 30 billion active edge devices projected by 2025 (Statista). Established players (Google, Apple, Tesla) and well-funded startups are designing custom ML chips.
- **Framework × hardware support is N×M expensive.** A framework must be ported per hardware backend; vendors must support per framework. **Intermediate representations (IRs)** are the middleman: high-level IR = computation graph; **lowering** generates a series of high- and low-level IRs down to hardware-native code (no one-to-one mapping — hence "lowering," not "translating").
- **Four standard local kernel optimizations: vectorization, parallelization, loop tiling, operator fusion.** Loop tiling is hardware-dependent (a good CPU access pattern is bad on GPU). Operator fusion reduces memory access by combining loops over the same array. Vertical/horizontal fusion of a CNN computation graph can compound these gains.
- **Hand-designed heuristics for compiler optimization are nonoptimal and nonadaptive.** ML-based compilers like **[[TVM|autoTVM]]** break the computation graph into subgraphs, predict subgraph cost with a model trained on runtime measurements, search per-subgraph for the fastest path, then stitch the results. Autotuning can take hours to days — but it's a one-time cost per (model, hardware) pair and the result is cached. AutoTVM beats cuDNN on ResNet-50 / NVIDIA TITAN X after ~70 trials.
- **[[WebAssembly|WebAssembly (WASM)]] is the most promising hardware-agnostic deployment target.** Compile a [[scikitlearn|scikit-learn]]/[[PyTorch]]/[[TensorFlow]] model to WASM and run it in any browser-capable device. As of September 2021, WASM is supported by **93% of devices worldwide**. Trade-off: WASM is faster than JavaScript but ~45% (Firefox) to ~55% (Chrome) slower than native code (Jangda et al.).

## Key Quotes

> "Deploying is easy if you ignore all the hard parts." — Huyen (paraphrasing an internet aphorism), Ch 7

> "The right question should be: 'How often can I update my models?'" — on update cadence; cites Etsy 50×/day, Netflix thousands/day, AWS every 11.7s, Weibo 10-min ML iteration

> "Batch prediction is a workaround for when online prediction isn't cheap enough or isn't fast enough. Why generate one million predictions in advance and worry about storing and retrieving them if you can generate each prediction as needed at the exact same cost and same speed?" — on the legacy character of batch prediction

> "Having two different pipelines to process your data is a common cause for bugs in ML production." — on training/serving pipeline divergence; the case for [[FeatureStore|feature stores]] and unified [[ApacheFlink|Flink]]-style pipelines

> "We're always trying to bring new models into production just as fast as humanly possible." — Josh Wills, former Google staff engineer / Slack director of data engineering

> "Nearly 80% of companies experienced a cloud data breach in [the] past 18 months." — *Security* magazine, on the privacy case for edge

> "This process is also called lowering, as in you 'lower' your high-level framework code into low-level hardware-native code. It's not translating because there's no one-to-one mapping between them." — on compiler IR architecture

> "Converting 32-bit floating points to 8-bit integers reduces the latency 7 times and increases throughput 8 times." — Roblox BERT-on-CPU case study; the chapter's strongest quantization data point

## Connections

- [[ChipHuyen]] — author of *Designing Machine Learning Systems* (2022) and the 2024 successor *AI Engineering*; this chapter precedes [[ai-engineering-ch09-inference-optimization|Ch 9 of *AI Engineering*]] by two years and is the LLM-era successor's direct ancestor.
- [[OReilly]] — publisher.
- [[ai-engineering-ch09-inference-optimization]] — the foundation-model-era deepening of this chapter; many concepts (quantization, distillation, pruning, low-rank factorization, batching, model compression, compiler/IR/lowering, operator fusion) are inherited and extended.
- [[BatchInference]] — the asynchronous mode this chapter defines; same vocabulary used in *AI Engineering*.
- [[OnlineInference]] — the synchronous mode; this chapter's framing of streaming-vs-only-batch-features predates and underpins the FM treatment.
- [[ModelCompression]] — the four-family taxonomy (quantization / distillation / pruning / low-rank) crystallized in this chapter.
- [[Quantization]] — covered with FP32/FP16/INT8/binary precision tiers; Roblox case study; QAT vs PTQ.
- [[KnowledgeDistillation]] — student/teacher framework; [[DistilBERT]] as canonical example.
- [[Pruning]] — both senses (node removal vs weight zeroing); lottery ticket; pruning-as-architecture-search debate.
- [[LowRankFactorization]] — depthwise/pointwise separable convolutions in [[MobileNet]] and [[SqueezeNet]]; [[AlexNet]]-level accuracy with 50× fewer parameters.
- [[DistilBERT]] — 40% smaller, 60% faster, 97% capability retention; the cited distillation case study.
- [[bert|BERT]] — the model being compressed in the Roblox case study.
- [[FP16]] / [[FP32]] / [[BF16]] / [[FixedPoint]] / [[FloatingPoint]] — quantization precision tiers; BF16 = TPU-native; FP16 = NVIDIA Tensor Cores.
- [[QuantizationAwareTraining]] / [[PostTrainingQuantization]] — when to apply quantization; PTQ is free in TF Lite / PyTorch Mobile / TensorRT.
- [[NVIDIA]] — Tensor Cores (mixed precision), TITAN X (autoTVM benchmark), DGX A100 (per-model optimization team example).
- [[google|Google]] — TPUs + BF16; TensorFlow / TensorFlow Lite; thousands of models training concurrently.
- [[Apple]] — acquired [[XnorAI|Xnor.ai]] (~$200M, 2020) for on-device compression; custom chip program.
- [[XnorAI]] — XNOR-Net authors; acquired by Apple for ~$200M (Jan 2020); illustrative of compression-research → product pipeline.
- [[Tesla]] — referenced as building custom ML chips for edge inference.
- [[GoogleTPU]] — supports Bfloat16 training; "the secret to high performance on Cloud TPUs."
- [[GPU]] / [[CUDA]] — the dominant ML inference hardware; CPU/GPU/TPU compute-primitive distinction (scalar/vector/tensor) drives why the same kernel is hardware-specific.
- [[TensorRTLLM|TensorRT]] — NVIDIA's on-device inference framework; ships PTQ out of the box; the CBR vertical/horizontal fusion figure originates with the TensorRT team.
- [[TensorFlow]] / [[PyTorch]] — the two frameworks whose model exports (TF SavedModel; PyTorch ONNX) the chapter names; PyTorch's TPU support didn't arrive until September 2020 (illustrating the framework × hardware support cost).
- [[FastAPI]] — the chapter's literal example of how to expose a `predict()` function as a POST endpoint.
- [[AmazonSageMaker]] — named example of a managed cloud inference endpoint.
- [[Kubernetes]] / [[container]] — the containerization layer this chapter assumes (Ch 9 of DMLS covers it more).
- [[ApacheFlink]] — used by Uber and Weibo for unified batch + stream processing pipelines.
- [[ApacheSpark]] / [[MapReduce]] — the batch-system legacy that made batch prediction the historical default.
- [[FeatureStore]] / [[LogicalFeatureStore]] — Ch 10's mechanism for guaranteeing batch/stream feature consistency.
- [[TrainingServingSkew]] — the failure mode that motivates feature stores and unified pipelines.
- [[DataDistributionShift]] / [[DistributionShift]] / [[DataDrift]] — the reason ML models decay in production (next chapter's topic).
- [[continuallearning]] — the response to model decay (Ch 9 of DMLS).
- [[Compiler]] / [[CompilerOptimization]] / [[Lowering]] — the compiler view of ML deployment; Ch 9 of *AI Engineering* deepens this with `torch.compile` / [[XLA]] / [[TVM]] / [[MLIR]].
- [[TVM]] — the open-source ML compiler stack; **autoTVM** is the ML-powered subgraph optimizer covered here.
- [[OperatorFusion]] / [[Vectorization]] / [[LoopTiling]] — three of the four local kernel optimizations.
- [[CNN]] / [[Convolution]] / [[AlexNet]] / [[ResNet]] — context for the SqueezeNet/MobileNet compression claims and the autoTVM ResNet-50 benchmark.
- [[MicroservicesArchitecture]] / [[REST]] / [[RESTAPI]] / [[API]] — the synchronous prediction-service architecture; RESTful APIs over HTTP are the canonical online prediction transport.
- [[GDPR]] — regulatory driver for edge inference.
- [[Latency]] / [[InferencePerformanceMetrics]] — the optimization target for online prediction (and the metric the Roblox case study reports).
- [[AsynchronousInference]] / [[AWSSageMakerInferenceEndpoint]] — adjacent operationalizations.
- [[InferenceOptimization]] — broader discipline this chapter establishes for traditional ML; Ch 9 of *AI Engineering* picks up the LLM-era story.
- [[MLOps]] / [[DevOps]] — Huyen's DevOps-best-practices framing of model update cadence.

## Contradictions

- **Online prediction cost vs batch prediction cost.** Conventional wisdom (still echoed in some wiki pages and in Ch 9's brief side note) holds that batch prediction is strictly cheaper because of vectorization. Huyen here pushes back: when most users don't generate requests on a given day (Grubhub: 622K/31M = 2%), batch wastes 98% of compute. Reconcile by treating batch's cost-efficiency claim as **request-density-dependent**, not universal.
- **No direct contradictions with [[ai-engineering-ch09-inference-optimization]].** Ch 9 of *AI Engineering* is a deepening rather than a revision: the same four model-compression families, the same batch-vs-online vocabulary (with the FM-specific batch-API caveat noted on [[BatchInference]]), the same lowering/IR/compiler architecture. The DMLS 2022 chapter is best read as the **traditional-ML predecessor** to Ch 9 of the 2024 book.
- **Latency vocabulary scale mismatch.** This chapter's "latency" is end-to-end request/response (in the tens to hundreds of ms), distinct from foundation-model TTFT/TPOT/TBT. No conflict, but the wiki's [[Latency]] page should make the multi-scale nature explicit. Already flagged on the Ch 9 source page.
