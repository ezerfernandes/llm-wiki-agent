---
title: "Human-in-the-Loop"
type: concept
tags: [concept, hitl, deployment, planning]
sources: [2605.00424-skills-as-verifiable-artifacts, ai-engineering-ch01-intro, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Human-in-the-Loop

HITL: operator-approval gate before irreversible side-effects. The Metere paper argues HITL is the universal default for unverified skills, and the only sustainable policy at scale is to make verification (not gate weakening) the path off it. Four-state lifecycle: request → decide → execute → audit. Broker policies: deny-all / policy / interactive / webhook.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] in *AI Engineering* Ch 1 defines HITL more broadly as **"involving humans in AI's decision-making processes"** and gives a worked customer-support example with three HITL configurations:

1. AI shows several responses; human agents reference them while writing.
2. AI responds to simple requests; routes complex ones to humans.
3. AI responds to all requests directly, with no human in the loop.

The chapter pairs HITL with [[microsoft|Microsoft's]] **[[CrawlWalkRun|Crawl-Walk-Run]] framework** as a *graduation ladder*: start with mandatory human review (Crawl), progress to AI-with-internal-users-only (Walk), reach full external automation (Run). Acceptance-rate metrics (e.g., "95% of AI suggestions used verbatim") become the criterion for moving up the ladder.

This is the wiki's first record of HITL as a **deployment-ladder planning framework** rather than (only) a per-action authorization gate. The Metere framing (deny/policy/interactive/webhook) and the Crawl-Walk-Run framing are complementary — Metere is the runtime-policy mechanism; Crawl-Walk-Run is the longitudinal product-strategy framework on top.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 of *Hands-On LLMs* invokes *"no human in the loop"* as **the closing safety caveat** on autonomous [[LangChainAgent|LangChain ReAct agents]] — the chapter's parting wisdom after walking through the worked MacBook-Pro price + EUR-conversion agent:

> *"By creating this relatively autonomous behavior, we are not involved in the intermediate steps. As such, there is no human in the loop to judge the quality of the output or reasoning process. This double-edged sword requires a careful system design to improve its reliability. For instance, we could have the agent return the website's URL where it found the MacBook Pro's price or ask whether the output is correct at each step."* — Ch 7

Ch 7's two concrete suggestions for **partial HITL** in the LangChain agent path:

1. **Provenance return** — have the agent surface the source URL alongside the retrieved fact so a human can verify.
2. **Step-level approval** — interactively ask the user whether the output is correct at each ReAct cycle.

Both are concrete versions of Huyen Ch 1's HITL configurations and the Metere broker policies — the **LangChain-agent specific operationalization** of *"keep the human in the loop somewhere"*. The chapter pairs this caveat with the implicit [[CompoundErrorAccumulation|compound-error-accumulation]] argument (the more autonomous the agent, the higher the variance in correctness).
