---
title: "Co-STORM (Collaborative STORM)"
type: concept
tags: [system, multi-agent, information-seeking, llm-application]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Co-STORM (Collaborative STORM)

**Collaborative STORM** — an [[InformationSeeking|information-seeking]] assistance system that supports **collaborative discourse among users and multiple LM agents**, introduced by [[YuchengJiang|Jiang]], [[YijiaShao|Shao]], [[DekunMa|Ma]], [[SinaSemnani|Semnani]] & [[MonicaLam|Lam]] in [[2408.15232-co-storm]] (2024). Direct successor to the [[STORM]] writing system, adding a **human-in-the-loop discourse layer** and a **dynamically maintained mind map** for tracking shared knowledge.

## What it is

Unlike one-question-one-answer [[QASystem|QA systems]] (which require the user to formulate every query) or non-interactive [[STORM]]-style report generators (which produce a static draft without supporting follow-up), Co-STORM lets users **observe and occasionally participate** in a roundtable discourse among LM agents. The agents ask questions *on the user's behalf*, allowing the user to discover [[UnknownUnknowns|unknown unknowns]] serendipitously — emulating the educational scenario where students learn by listening to and occasionally participating in conversations with parents or teachers ([[Nussbaum2008|Nussbaum 2008]]).

## Architecture

The system maintains a turn-based discourse $\mathcal{D} = \{u_1, u_2, ..., u_n\}$ of textual utterances $u_i$ from one of three roles:

1. **User** — passive observer; can take a turn anytime to inject a question/argument.
2. **[[PerspectiveGuidedExpert|Expert agents]]** $\mathcal{P} = \{p_1, ..., p_N\}$ — each with a distinct expertise/perspective, simulated by an LM prompted with the perspective and a search-engine-grounded answer pipeline. $N=3$ in the default config.
3. **[[ModeratorAgent|Moderator]]** — non-expert facilitator that **reranks uncited information** from prior search calls and generates questions to steer toward unexplored regions.

Each utterance is associated with an **[[UtteranceIntent|intent]]** $a_i \in$ {Original Question, Information Request, Potential Answer, Further Details} (taxonomy from [[QuEtAl2019|Qu et al. 2019]]).

### Turn management

[[TurnManagement|Turn management protocol]]: when the user is idle, experts take turns in sequence. After $L=2$ consecutive expert turns with intent in {Potential Answer, Further Details}, the system invokes the moderator to prevent repetitive niche discussion.

### [[CoSTORMMindMap|Mind map]]

A dynamic tree $\mathcal{M} = (\mathcal{C}, \mathcal{E})$ of concepts $c \in \mathcal{C}$, each storing a subset of retrieved information $I^c \subset \mathcal{I}$. Maintained by two operations:

- **`insert`** — derive candidate concepts via semantic-similarity matching, then prompt the LM to choose the final placement.
- **`reorganize`** — when a concept exceeds $K=10$ pieces of info, the LM generates new sub-topic names and re-inserts each piece into the subtree.

After expansion, bottom-up cleaning prunes single-subtopic chains and concepts with no supporting info.

### Moderator reranking

Choose uncited sources $i$ by ranking them by

$$\cos(\mathbf{i}, \mathbf{t})^\alpha \cdot (1 - \cos(\mathbf{i}, \mathbf{q}))^{1-\alpha}$$

— similarity to **topic** $t$, dissimilarity to **prior question** $q$, $\alpha=0.5$. The form encodes "**on-topic but unexplored**."

## Implementation

- LM: [[gpt-4o|gpt-4o-2024-05-13]], temperature 1.0, top-p 0.9.
- Framework: [[DSPy]] (zero-shot, no automated optimizer applied).
- Search: [[YouCom|You.com]] API, filtered to the [[Wikipedia]] *Reliable sources* whitelist.
- Embeddings: `text-embedding-3-small`.
- Hyperparameters: $N=3$, $K=10$, $L=2$, $\alpha=0.5$.
- Code: <https://github.com/stanford-oval/storm>.
- Live preview: <https://storm.genie.stanford.edu>.

## Evaluation

- **Automatic** on the [[WildSeek]] dataset (100 topic+goal pairs across 24 domains):
  - Report quality (Relevance / Breadth / Depth / Novelty) graded by [[Prometheus2]] on a 5-point rubric.
  - [[InformationDiversity]] computed as $1 - \frac{\sum_{i\neq j}\cos(\mathbf{i},\mathbf{j})}{|\mathcal{I}|(|\mathcal{I}|-1)}$.
  - Co-STORM beats both [[RAGChatbot]] and STORM+QA on every dimension; Depth and Novelty gains statistically significant ($p<0.05$).
- **Human evaluation** ($n=20$):
  - 70% prefer Co-STORM over [[GoogleSearch|Google Search]]; 78% over [[RAGChatbot|RAG Chatbot]].
  - 80% report **less effort** vs Search; 67% vs RAG.

## Ablations

- **w/o Moderator**: Relevance 3.78→3.56, Breadth 3.79→3.69, Depth 3.77→3.41, Novelty 3.05→2.89 — **largest drop**, confirms moderator as the load-bearing role.
- **w/o Multi-Expert** ($N=1$): smaller drop than removing the moderator. *"Having just one expert and one moderator can already provide most of the benefits."*

## Relationship to other wiki concepts

- Direct successor of [[STORM]] (same lab; same DSPy substrate; same You.com search; same Wikipedia-filtered grounding).
- Built on [[DSPy]] but **does not use** an automated optimizer ([[MIPROv2]] / [[BootstrapFewShotWithRandomSearch|BFRS]] / [[2507.19457-gepa|GEPA]]) — uses zero-shot prompting. An open methodological gap: would optimizer-tuned Co-STORM widen its lead further?
- Baseline comparisons frame [[rag|RAG]] chatbots as the *single-question* paradigm Co-STORM extends.
- Mind-map idea inspired by [[Buzan1974]]; turn-management protocol from [[Traum2003]]'s [[MixedInitiativeDiscourse|mixed-initiative]] dialogue framing.

## See also
- [[STORM]] · [[WildSeek]] · [[CoSTORMMindMap]] · [[ModeratorAgent]] · [[PerspectiveGuidedExpert]] · [[UnknownUnknowns]] · [[CollaborativeDiscourse]] · [[UtteranceIntent]] · [[TurnManagement]] · [[Prometheus2]] · [[RAGChatbot]] · [[InformationDiversity]]
