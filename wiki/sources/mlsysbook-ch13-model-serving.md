---
title: "Machine Learning Systems (mlsysbook Vol 1) — Ch 13: Model Serving"
type: source
tags: [book, ml-systems, mlsysbook, serving, inference, deployment, batching, queuing-theory, llm-serving, latency, slo, autoscaling, cost]
date: 2026-06-05
sources: []
source_file: raw/mlsysbook-vol1/mlsysbook-ch13-model-serving.qmd
last_updated: 2026-06-05
---

# Machine Learning Systems (mlsysbook Vol 1) — Ch 13: Model Serving

## Summary

Chapter 13 opens the **Deploy** part (Ch 13–16) of [[VijayJanapaReddi|Vijay Janapa Reddi]]'s *Machine Learning Systems* (Vol 1, [[Harvard]], 2026). Its thesis is **the serving inversion**: serving demands the opposite physics of training. Training maximizes throughput (samples/second) with large batches that absorb latency spikes invisibly; serving minimizes latency ($L_{\text{lat}}$, ms/request) where a single slow response is a broken product, and pays a recurring tax on *every* request. Applying the [[DAMTaxonomy|D·A·M taxonomy]], deployment inverts each priority — Data shifts from Volume to Freshness, Algorithm from Mutable to Frozen, Machine from Utilization (100% GPU) to **Headroom** (40–60% to absorb spikes before tail latency explodes). The [[IronLawOfMLSystems|iron law]]'s overhead term $L_{\text{lat}}$ becomes the dominant constraint rather than a rounding error.

The chapter is built around the **[[LatencyBudget|latency budget]]** framework and runs a single ResNet-50 example through every layer: serving architectures across the [[DeploymentSpectrum|deployment spectrum]] (cloud/edge/mobile/TinyML), [[InferenceServer|inference-server]] anatomy, [[REST]]-vs-[[gRPC]] protocols, the request lifecycle (preprocessing/inference/postprocessing — where preprocessing often dominates), [[QueuingTheory|queuing theory]] ([[LittlesLaw|Little's Law]], M/M/1, the tail-latency explosion at ~70% utilization), [[TailLatency|tail-tolerant]] techniques (hedged/tied/canary requests, [[GracefulDegradation|graceful degradation]], [[AdmissionControl|admission control]]), model-lifecycle hazards ([[TrainingServingSkew|training-serving skew]], [[ColdStart|cold start]], multi-model serving via [[MIG]]/[[CUDAMPS]]), and **throughput optimization** via [[DynamicBatching|dynamic batching]] (the latency-throughput Pareto frontier, the "batching tax").

The back half is the **[[LLMServing|LLM-serving]]** deepening: autoregressive generation makes decode **[[MemoryWall|memory-bandwidth bound]]** (one full weight read per token), measured by **[[TTFT]]/[[TPOT]]**; [[ContinuousBatching|continuous batching]] (Orca) and **[[PagedAttention]]** (vLLM) cut the 40–60% KV-cache fragmentation waste to <4%; [[PrefixCaching|prefix caching]] and KV-cache offloading manage memory pressure. The chapter closes with [[InferenceRuntime|runtime selection]] ([[PyTorch]]/[[ONNXRuntime|ONNX Runtime]]/[[TensorRT]], 2–9× spread), precision selection (FP16 free 2×, INT8 ~3×), node-level optimization ([[OperatorFusion|fusion]], constant folding, [[Safetensors]] zero-copy loading), serving economics ([[CostPerInference|cost per inference]], GPU-vs-CPU crossover, [[CapacityPlanning|capacity planning]]), an end-to-end **8-billion-parameter [[Llama3|Llama 3]] case study** on an H100, and seven fallacies/pitfalls. Motivating economics: Facebook's 2018 "inference tax" (~4.5B translations/day, tens of trillions of ops/day) and **intelligence deflation** — public API token prices fell ~5.8× per 18 months (2020–2025), shrinking per-inference margins ([[JevonsParadox|Jevons paradox]] then expands aggregate demand).

## Key Claims

- **Serving inverts training's physics.** Training maximizes throughput with large batches; serving minimizes per-request latency and pays a tax on every request. The [[IronLawOfMLSystems|iron law]] $L_{\text{lat}}$ term — request scheduling, network round-trips, orchestration — becomes dominant. Definition: serving is "the operational phase that provides model predictions under strict latency constraints," and the common pitfall is treating it as "just the forward pass" rather than a distributed-systems problem (routing, load balancing, transformation).
- **Run at 40–60% utilization, not 100%.** The **tail-latency explosion** (M/M/1: p99 ≈ 4.6× mean) shows latency stays manageable until utilization crosses the **~70% "knee,"** then diverges nonlinearly. The "Black Friday" example: a 10× traffic spike (1,000→10,000 QPS) does not slow the system 10× — it *collapses* (latency hits 10 s, requests time out, servers 100% loaded but useful throughput near zero). Fixes: load shedding, autoscaling before the knee, graceful degradation.
- **SLO ≠ SLA.** An SLO is an *internal* target (e.g., "p99 < 50 ms"); an SLA is an *external* contractual commitment with penalties. SLOs are set tighter for safety margin. ML SLOs are multi-dimensional (accuracy *and* latency), so a larger model for accuracy can violate the latency SLO.
- **The latency budget is zero-sum and the model usually gets <50% of it.** ResNet-50 breakdown (≈10.1 ms total): JPEG decode 3 ms (30%), resize 1 ms, normalize 0.5 ms, CPU→GPU 0.5 ms, **forward pass 5 ms (~50%)**, softmax+top-5 0.1 ms. Preprocessing ≈ 45%; with TensorRT cutting inference to 2 ms, preprocessing would dominate at ~63%. By **[[AmdahlsLaw|Amdahl's Law]]**, a 10× model speedup yields only ~1.8× end-to-end. "Profile before optimizing; if preprocessing dominates, GPU pipelines (NVIDIA DALI) beat model quantization."
- **The bottleneck shifts by model class.** ResNet-50 is compute-bound (CNN forward pass); **DLRM** is memory-bandwidth/capacity-bound — embedding lookups (fetch 100+ dense 128-dim vectors from terabyte tables) consume ~67% of a 10 ms budget while the MLP is ~17%. "Adding compute does not help once embedding-table bandwidth is the binding constraint."
- **The "serving tax" compounds.** Network I/O 1–5 ms, serialization 50–500 μs, queuing 0.1–10 ms (exponential w/ load), dispatch 10–50 μs, data copy 100–500 μs. The **"killer microseconds"** regime (Barroso/Patterson): too short for OS scheduling, too long to spin-wait. Named μs overheads alone consume ~3–21% of a 5 ms budget before network/queuing.
- **gRPC ≈ 10× cheaper serialization than REST/JSON.** A 1,000-float payload: JSON ~9 KB / ~50 μs parse vs Protobuf ~4 KB / ~5 μs. Use REST for public APIs (accessibility), gRPC+HTTP/2+Protobuf for internal high-QPS service-to-service. FlatBuffers enables true zero-copy (TF Lite's model format).
- **Little's Law sets the memory floor.** $N_{\text{req}} = \lambda \cdot T_{\text{lat}}$ holds for any stable system regardless of arrival/service distribution. 1,000 QPS at a 50 ms SLO ⇒ 50 concurrent slots ⇒ a hard RAM floor for activation storage. If the GPU OOMs at batch 32, the system *physically cannot* hit 1,000 QPS at 50 ms.
- **M/M/1 quantifies the utilization-latency curve.** Time in system = service/(1−ρ): 50% ⇒ 2×, 70% ⇒ 3.3×, 80% ⇒ 5×, 90% ⇒ 10×, 95% ⇒ 20×. M/M/1 over-predicts vs the more realistic M/D/1 (deterministic service, ~half the wait) — a *feature* for capacity planning (built-in ~2× safety margin). p99 ≈ 4.6 × service/(1−ρ).
- **Worked capacity plan: 12 V100s for 5,000 QPS @ 50 ms p99.** Safe utilization ρ ≤ 1 − (4.6×5 ms)/50 ms = 0.54; required μ = 5,000/0.54 ≈ 9,259 req/s; ÷ 1,143 img/s (V100 batch-16) = 8.1 → 9 GPUs; ×1.3 headroom → 12; losing one leaves 11 at ~40% util (N+1 satisfied).
- **The batching tax: throughput vs latency Pareto frontier.** Total batched latency ≈ (B−1)/(2λ) formation delay + $T_{\text{inf}}(B)$. ResNet-50/V100 sweep: batch-1 = 200 img/s @ 15% util; batch-32 = 1,280 img/s @ 95% util (**6.4× throughput**) but inference stretches 5 ms→25 ms. Avg batching-window wait = window/2. Static batching fails under variable traffic; dynamic batching (5–50 ms windows, max batch 8–32) bounds wait. Counterintuitively, **as traffic rises the optimal window shrinks while batch size grows** (law of large numbers).
- **LLM serving is qualitatively different.** Three new properties: autoregressive (serial) generation, variable-length output, stateful KV cache. Decode is **memory-bandwidth bound** (arithmetic intensity ≈ 1 FLOP/byte): "Adding compute cores yields *zero* latency improvement; only faster memory or smaller models help." Metrics split into **TTFT** (prefill, compute-bound) and **TPOT** (decode, bandwidth-bound). Production targets: TTFT < 500 ms, TPOT < 50 ms (~20 tok/s), >1,000 tok/s aggregate.
- **Continuous batching + PagedAttention are the LLM throughput levers.** With variable lengths, static batching wastes ~90% of a finished slot's compute. Continuous (iteration-level / in-flight) batching reschedules per token; PagedAttention (vLLM, SOSP 2023) borrows OS virtual-memory paging (16-token pages) to cut KV-cache waste from 40–80% to <4%, enabling 2–4× higher throughput (>95% memory utilization vs 50–60%). Sarathi-Serve adds chunked prefill + stall-free batching. Speculative decoding gives ~2–3× via draft+verify.
- **Runtime and precision selection are as impactful as architecture.** ResNet-50/V100 batch-1: PyTorch eager 8.5 ms (1×) → TorchScript 6.2 → ONNX 5.1 → TensorRT FP32 2.8 (3×) → FP16 1.4 (6×) → **INT8 0.9 (≈9×)**. FP16 is a near-free 2× (no accuracy loss); INT8 is ~3× over FP32 at <0.4 pp accuracy loss (PTQ) — meaning a 30-GPU FP32 fleet shrinks to 10 at INT8. ONNX Runtime trades 5–15% throughput vs TensorRT for cross-platform portability.
- **Cold start and skew are deployment-time, not edge cases.** Cold start (cloud, first deploy) ≈ 35 s, dominated by 15–30 s TensorRT compilation; precompiling + warm container drops it to ~1.5 s. The first un-warmed request runs >100× slower. **Training-serving skew** silently degrades accuracy (PIL vs OpenCV resize = 0.5–1 pp; BGR vs RGB ≈ random; wrong normalization shifts out of distribution) — invisible to latency/exception monitoring. Fix: identical preprocessing code paths or distribution monitoring.
- **8B Llama 3 / H100 case study.** 4-bit AWQ weights ≈ 3.5 GB; prefill 10,000 tok/s ⇒ TTFT ≈ 120 ms (< 200 ms SLO); decode theoretical ≈ 1.0 ms/token, realized TPOT ~few ms (< 20 ms SLO). ~72 GB free VRAM holds ~2.2M KV-cache tokens ⇒ concurrent batch ~1,700+ requests; prefill-limited throughput ⇒ ~$ fractions per million tokens. KV-cache memory (not compute) bounds concurrency; at 70B-class scale, batch-32 hits the 80 GB OOM zone at just 8k context.
- **Serving cost scales with request volume, not dataset size.** ResNet-50 AWS 2026: c5.xlarge CPU ($0.17/h, 50 img/s) vs g4dn T4 GPU ($0.53/h, 400 img/s, **lowest cost per inference**) vs p3 V100 ($3.06/h, 1,200 img/s, only worth it at very high sustained traffic). GPU startup (2–5 min) >> CPU (30–60 s) suggests hybrid scaling: always-on GPU baseline + CPU overflow for spikes.

## Key Quotes

> "Why does serving invert every optimization priority that made training successful?" — chapter's framing question; training maximizes throughput, serving minimizes latency.

> "Machine (Physics): In training, the goal is Utilization (keeping GPUs at 100 percent). In serving, the goal is Headroom (keeping GPUs at 40–60 percent to absorb traffic spikes before tail latency explodes)." — the serving inversion via the [[DAMTaxonomy|D·A·M taxonomy]].

> "Training creates the model; serving pays the recurring bill. At fleet scale, a model architecture that is cheap to train can still be too expensive, too memory-bound, or too variable in tail latency to serve." — the Facebook "inference tax" war story (Hazelwood et al., 2018).

> "A frequent misconception is that the 'model' has the entire budget. In reality, the model often has less than 50 percent of the total budget; the remainder is consumed by the request lifecycle (DNS, TLS, load balancing, serialization)." — the [[LatencyBudget|latency budget]] definition.

> "Adding more *compute cores* yields *zero* latency improvement; only *faster memory* (Physics) or *smaller models* (Algorithm) can speed up generation." — the memory wall for generative AI / decode phase.

> "Average latency is a vanity metric; tail latency is the user experience." — the percentile-monitoring imperative (echoing Dean & Barroso's tail-at-scale).

> "A system achieving 10,000 QPS but violating the p99 SLO on 5 percent of requests is actually serving 9,500 valid QPS and failing on the rest." — capacity planning: throughput is only real if requests meet the latency SLO (the MLPerf Server rule).

> "Each 10× cost reduction opens application classes that were economically infeasible at the previous price point... cheaper inference reliably increases, not decreases, total GPU fleet demand." — [[JevonsParadox|Jevons paradox]] applied to inference.

## Connections

- [[VijayJanapaReddi]] — author; [[Harvard]] — host institution; mlsysbook.ai/vol1 (2026). This chapter opens the **Deploy** part.
- [[mlsysbook-ch12-benchmarking|Ch 12 (Benchmarking)]] — measured performance under controlled conditions; this chapter faces uncontrolled production traffic. Shares [[TailLatency]], [[MLPerfScenarios]], [[InferencePerformanceMetrics]].
- [[mlsysbook-ch11-hardware-acceleration|Ch 11 (Hardware Acceleration)]] — [[RooflineModel]], [[ArithmeticIntensity]], [[TensorCore]], the [[MemoryWall]] that bounds decode; serving's DSA-efficiency argument (CPUs hit 1–2% of peak at batch-1).
- [[mlsysbook-ch10-model-compression|Ch 10 (Model Compression)]] — [[Quantization]] (FP32/FP16/INT8, QAT vs PTQ) inherited as serving's precision-selection lever.
- [[mlsysbook-ch02-ml-systems|Ch 2 (ML Systems)]] — the [[DeploymentSpectrum|four deployment paradigms]] (Cloud/Edge/Mobile/TinyML), [[CloudML]]/[[EdgeML]], and the physical walls (light/power/memory) that *intensify* at serving time.
- [[IronLawOfMLSystems]] — serving promotes the $L_{\text{lat}}$ overhead term to dominance; batching amortizes it; the energy tax ($E_{move} \gg E_{compute}$) drives the decode memory wall.
- [[DAMTaxonomy]] — the data/algorithm/machine inversion that frames the whole chapter.
- [[LatencyBudget]] — the central organizing framework; zero-sum allocation across phases.
- [[QueuingTheory]] / [[LittlesLaw]] — capacity-planning mathematics; the utilization-latency curve and the ~70% knee.
- [[TailLatency]] — p95/p99 as the binding SLO; tail-at-scale (Dean & Barroso 2013).
- [[ServiceLevelObjective]] — the latency target shaping every architectural decision; SLO vs SLA.
- [[DynamicBatching]] / [[Batching]] / [[StaticBatching]] — the core throughput lever and its Pareto frontier; the batching tax.
- [[ContinuousBatching]] / [[PagedAttention]] / [[KVCache]] — LLM throughput trifecta (Orca; vLLM).
- [[LLMServing]] — the chapter's autoregressive deepening; [[TTFT]]/[[TPOT]], prefill vs decode.
- [[PrefixCaching]] / [[SpeculativeDecoding]] / [[GroupedQueryAttention]] — KV-cache and decode optimizations.
- [[Autoregressive]] / [[GreedyDecoding]] / [[BeamSearch]] / [[NucleusSampling]] — decoding strategies and their latency cost.
- [[InferenceServer]] — Triton/TF Serving/TorchServe anatomy; the scheduler as the throughput-latency brain.
- [[NVIDIATriton]] / [[TensorFlowServing]] / [[TorchServe]] / [[vLLM]] — production inference servers.
- [[InferenceRuntime]] / [[ONNXRuntime]] / [[TensorRT]] / [[OpenVINO]] / [[ONNX]] — the runtime-selection spectrum (portability vs raw speed).
- [[OperatorFusion]] / [[LayerFusion]] — node-level graph optimization; 2–5× speedups.
- [[Safetensors]] — zero-copy fast model loading (30–100× faster than pickle), cuts cold start.
- [[ColdStart]] / [[TrainingServingSkew]] — model-lifecycle hazards solved before queuing optimization matters.
- [[GracefulDegradation]] / [[AdmissionControl]] / [[LoadBalancing]] — overload-handling and tail-tolerant techniques.
- [[MIG]] / [[CUDAMPS]] / [[PinnedMemory]] / [[NUMA]] / [[SIMD]] / [[CUDA]] — multi-model serving and node-level isolation.
- [[CapacityPlanning]] / [[CostPerInference]] — serving economics; GPU-vs-CPU crossover.
- [[MLPerfScenarios]] — Server/MultiStream/SingleStream/Offline map traffic patterns to batching strategies.
- [[BatchInference]] / [[OnlineInference]] / [[StaticInference]] / [[DynamicInference]] — the precompute-vs-on-demand axis.
- [[ModelServing]] / [[InferenceOptimization]] — the practice and discipline this chapter formalizes.
- [[NVIDIA]] / [[Meta]] / [[Google]] / [[OpenAI]] / [[Anthropic]] / [[Llama3]] — hardware vendors, the Facebook case study, and the API-price trajectory.
- [[GPU]] / [[GPUUtilization]] / [[NeuralProcessingUnit]] / [[AmdahlsLaw]] / [[RooflineModel]] — hardware/analysis tools the chapter reuses.

### Contrast with prior wiki serving sources

- [[dmls-ch07-model-deployment|DMLS Ch 7 (Huyen, 2022)]] — the traditional-ML predecessor. DMLS frames batch-vs-online and cloud-vs-edge axes with model-compression/compiler detail; this chapter sharpens the *systems* view (queuing theory, the latency budget, inference-server anatomy) and adds the full LLM-serving story DMLS predates. Both agree preprocessing/network often dominate; both stress that throughput is meaningless without a latency constraint.
- [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9 (Huyen, 2024)]] — the FM-era serving deepening. Heavy overlap on [[ContinuousBatching]], [[PagedAttention]], [[TTFT]]/[[TPOT]], prefill/decode disaggregation. This chapter adds the queuing-theory foundation and a first-principles cost/energy model (J/token, capacity planning) that Ch 9 largely assumes.

## Contradictions

- **No direct contradictions** with [[dmls-ch07-model-deployment]] or [[ai-engineering-ch09-inference-optimization]]; this chapter is a *quantitative-foundations* layer beneath both, not a revision.
- **Latency-scale reconciliation.** Like prior sources, this chapter uses "latency" at two scales — fixed-output end-to-end (tens of ms) vs LLM streaming (TTFT/TPOT). It resolves the ambiguity explicitly by decomposing the budget into prefill (compute-bound TTFT) and decode (bandwidth-bound TPOT) phases, and via a "Notation alert" separating queuing-theory $N_{\text{req}}/T_{\text{lat}}$ from the iron-law $L_{\text{lat}}$ subscripts.
- **Batch-vs-online cost framing (vs DMLS Ch 7).** DMLS argued batch prediction wastes compute when request density is low (Grubhub 2%); this chapter reframes the same axis as **[[StaticInference|static]] vs [[DynamicInference|dynamic]] inference** and recommends a *hybrid* (cache popular precomputed results, dynamic-serve the tail) — a refinement, not a conflict.
- **"100% utilization is efficient" is explicitly listed as a pitfall** here, contradicting naive cost-efficiency intuition (and any wiki page implying max utilization is the goal): M/M/1 shows 70→90% util cuts cost ~22% but triples average latency and pushes p99 from ~77 ms toward ~230 ms. Target 60–70% at peak.
