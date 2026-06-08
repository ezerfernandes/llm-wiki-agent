---
title: "Agentic AI"
type: concept
tags: [paradigm, multi-agent, ml-architecture, agi]
sources: [2605.12966-agentic-ai-to-agi, hands-on-llm-ch07-advanced-text-generation, agentic-design-patterns-00-frontmatter]
last_updated: 2026-06-07
---

# Agentic AI

**Agentic AI** denotes systems of specialized, autonomous learnable mappings composed through a topology — formally a topologically-sorted Directed Acyclic Graph (DAG) — rather than a single dense parameterization. Per Liao et al. (Def. 4.1 in [[2605.12966-agentic-ai-to-agi]]), an Agentic AI system is a tuple $\Psi = (\mathcal{G}, \mathcal{F}, \Lambda)$ where:

- $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ is a DAG of $K = |\mathcal{V}|$ nodes representing information flow.
- $\mathcal{F} = \{f_1,\dots,f_K\}$ is a set of heterogeneous, learnable local mappings (agents). Each $f_i: \mathcal{H}_{in}^{(i)} \times \Theta_i \to \mathcal{H}_{out}^{(i)}$.
- $\Lambda$ is a composition operator mapping parent outputs to a child's input: $x_i = f_i(\Lambda(\{x_j\}_{j\in Pa(i)}); \theta_i)$.

## Why the paradigm matters

The position paper proves that — under the [[StructuredRealWorldDistribution]] assumption (data supported on a union of low-dimensional manifolds $\bigcup_k \mathcal{M}_k$ with $d_k \ll D$) — Agentic AI achieves an *exponential* sample-efficiency gain over a monolithic learner:

$$\mathcal{E}_{\text{R-Agentic}}(N) \approx \mathcal{O}\!\left(K \cdot N^{-1/d_{\max}}\right), \qquad \mathcal{E}_{\text{mono}}(N) \approx \mathcal{O}\!\left(N^{-1/D}\right).$$

The ratio collapses to zero as $N\to\infty$ since $d_{\max} \ll D$. The monolith additionally pays the [[AverageTrap]] penalty — an irreducible quadratic compromise from conflicting per-task gradients (Prop. 3.3) — which Agentic AI avoids by aligning architecture with the manifold structure.

## Three axes generalizing [[MixtureOfExperts]]

Per §5 of the paper, Agentic AI generalizes MoE in:

1. **Scope** — MoE uses fixed expert sub-networks within a forward pass; Agentic AI uses autonomous agents with independent parameters and multi-step reasoning.
2. **Topology** — MoE is single-layer router → expert; Agentic AI extends to arbitrary DAGs.
3. **Routing mechanism** — MoE uses differentiable gating trained end-to-end; agentic routing accommodates iterative refinement, external tools, and dynamic retrieval.

## Generalization governance

Theorem 4.3: $\mathcal{E}_{\text{Agentic}} \approx C(\mathcal{G}) \cdot \mathcal{O}\!\left((N/K)^{-1/d_{\text{eff}}}\right)$. Two factors govern the bound:

- The **effective intrinsic dimension** $d_{\text{eff}}$ governs the *convergence rate*.
- The **[[CompositionalCapacity]]** $C(\mathcal{G}) = \sum_u \omega_u$ (the Topology Factor, sum of per-agent [[TopologicalWeight|Topological Weights]]) governs the *error magnitude*.

Agentic AI succeeds when the topology minimizes $C(\mathcal{G})$ while maximizing the dimensionality gap $D - d_{\text{eff}}$.

## Edge engineering

Per Lemma 4.4 and the [[TopologicalEdgeWeight]] decomposition, edges in a well-designed agentic DAG act as **active variational filters**, not passive pipes:

- Edges after long upstream chains should be **contractive** ($\|J_{e^*}\| < 1$) — typical of critic / judge edges.
- Edges preceding high-sensitivity downstream decisions should satisfy $\|J_{e^*}\| \ll 1$ — typical of voting / verification edges that collapse multiple paths into a stable signal.

## Position relative to other 2026 corpus papers

- The [[2402.01817-llm-modulo|LLM-Modulo Framework]] is an instance of Def. 4.1 (LLM-as-generator + external sound critic, both as nodes in a 2-node DAG).
- The Conductor of [[2512.04388-conductor]] is a *learned* router operating in the §3.2 routing regime.
- The architectural-layer position of [[2605.03310-coordination-architectural-layer]] empirically studies what this paper formalizes via $\mathcal{W}(e^*)$.
- The OneManCompany framework of [[2604.22446-onemancompany]] is a hand-designed instance with HR-style organizational topology.
- [[2605.02396-heavyskill|HEAVYSKILL]] takes the opposite direction (collapse to monolith inner skill) — sacrificing the exponential routing advantage in exchange for inference-time simplicity.

## Connections
- [[2605.12966-agentic-ai-to-agi]] — formal definition.
- [[StructuredRealWorldDistribution]]
- [[AverageTrap]]
- [[RoutingBasedAgenticAI]]
- [[CompositionalCapacity]]
- [[TopologicalWeight]]
- [[TopologicalEdgeWeight]]
- [[MixtureOfExperts]]
- [[MultiAgentSystems]]
- [[llmagents|LLMAgents]]
- [[agenticharness|AgenticHarness]]

## Agentic Design Patterns (Gulli) perspective

[[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[AntonioGulli|Gulli]], Google) supplies the **practitioner-level** definition that sits beneath the formal DAG-of-mappings framing above:

> *"An AI agent is a system designed to perceive its environment and take actions to achieve a specific goal. It's an evolution from a standard Large Language Model (LLM), enhanced with the abilities to plan, use tools, and interact with its surroundings."*

Equivalently: *"a computational entity designed to perceive its environment, make informed decisions based on those perceptions and a set of predefined or learned goals, and execute actions to achieve those goals autonomously."* The book enumerates the defining **characteristics**: [[Autonomy]], [[Proactiveness]], [[Reactiveness]], [[GoalOriented|goal-orientation]], [[ToolUse|tool use]], [[MemoryManagement|memory]], and [[AgentCommunication|communication]]. Operationally an agent runs a five-step loop — *Get the Mission → Scan the Scene → Think It Through → Take Action → Learn and Get Better*.

Gulli organizes agentic systems on a four-level [[AgentComplexitySpectrum|complexity spectrum]] (Level 0 reasoning engine → Level 1 connected → Level 2 strategic → Level 3 collaborative multi-agent), echoing the paradigm shift this page formalizes: Gulli's Level-3 collaborative systems are an informal, hand-designed instance of Def. 4.1's DAG of agents, and his patterns ([[AgenticDesignPattern]]) are reusable blueprints for the topology this page argues should minimize $C(\mathcal{G})$.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

[[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]] uses *"agents"* in the **everyday-LLM-engineering sense** rather than the formal DAG-of-mappings sense of Liao et al. 2026 (the parent paper this page anchors to). Ch 7's framing — *"systems that leverage a language model to determine which actions they should take and in what order"* — fits as a **special case** of Def. 4.1: a 2-node DAG (LLM planner → tool inventory) operating in the [[react|ReAct]] regime.

The Ch 7 [[LangChainAgent|`create_react_agent` + `AgentExecutor`]] receipt is the **operational shape** that makes this paper's formalism legible at code level — the *"composition operator $\Lambda$"* is `AgentExecutor`'s scratchpad accumulation, and the *"learnable local mappings"* are the LLM (planner) + tools (deterministic external functions). Ch 7 stays at the simplest topology; the paper's exponential-sample-efficiency arguments require richer DAGs.
