---
title: "IIR Ch. 19: Web Search Basics"
type: source
tags: [iir, information-retrieval, textbook, web-search, web-graph, near-duplicates, shingling]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/web-search-basics-1.html"
---

## Summary

Chapter 19 of Manning, Raghavan and Schütze's *Introduction to Information Retrieval* (2008) bridges the gap between classical document retrieval (the prior eighteen chapters) and the realities of running a search engine over a hostile, adversarial, billion-page corpus: the World Wide Web. The chapter is the textbook's foundational treatment of [[WebSearch]] and lays the groundwork for later chapters on crawling (Ch. 20) and link analysis (Ch. 21). It assembles seven loosely coupled topics — pre-Google search history, statistical characteristics of the web corpus, the macroscopic [[BowTie]] graph structure, the spam arms race, the advertising business model, the user query taxonomy, index-size estimation, and near-duplicate detection — that together explain why web IR diverges from the closed-corpus assumptions of earlier chapters. The chapter's two most enduring contributions, frequently cited downstream, are Andrei Broder's tripartite [[QueryIntent]] taxonomy and the shingling/[[MinHash]] sketch technique for scalable [[NearDuplicateDetection]] using [[JaccardSimilarity]].

## Key Claims

- **Web IR is adversarial, not cooperative.** Unlike library or enterprise corpora, web authors actively try to manipulate ranking, so classical relevance ([[TFIDF]], [[VectorSpaceModel]]) must be supplemented with link-based authority signals ([[PageRank]], [[HITS]]) and spam-fighting heuristics.
- **The web is heterogeneous at daunting scale.** Pages vary in language, grammar, styling, encoding, and structure; many are image-only with no indexable text; trustworthiness is user-dependent rather than universal.
- **The web graph follows power laws, not Poisson.** In-degree distribution P(in-degree = i) is proportional to 1/iα with α ≈ 2.1; average in-degree is in the 8–15 range. This contradicts the Erdős–Rényi random-graph model that early researchers expected.
- **The web has a bow-tie macrostructure.** Roughly equal-sized SCC, IN, and OUT components, with tendrils and tubes accounting for the remainder. Roughly a quarter of randomly chosen pages cannot reach another quarter via directed link traversal.
- **Spam is economically motivated and adaptive.** Each ranking signal (term frequency, anchor text, link counts) attracts a corresponding spam technique (keyword stuffing, anchor spam, link farms), spawning the [[SEO]] industry and an ongoing "adversarial IR" cat-and-mouse game.
- **Sponsored search displaced banner advertising.** The Goto/Overture pay-per-click model, later perfected by Google AdWords, links advertiser bids to user click intent, making search the most economically valuable real estate on the Internet.
- **Web queries are short and intent-laden.** The average query has 2–3 keywords; few users employ Boolean operators or other syntax; Broder's taxonomy splits queries into informational, navigational, and transactional intents.
- **Index size is hard to measure honestly.** Capture-recapture using overlap statistics gives relative sizes between two engines; absolute estimates require careful unbiased sampling because the web is not strongly connected and IP/URL/query-based sampling each has structural bias.
- **Near-duplicates are 40% of the web.** Shingling with k-grams and min-wise hashed sketches lets a crawler estimate pairwise Jaccard overlap in linear time without quadratic comparisons.

## Section Notes

### 19.1 Background and History

The chapter opens by sketching the pre-Google landscape of the mid-1990s. Two competing models for web discovery emerged: full-text crawlers ([[Altavista]], Excite, Infoseek, Lycos, InfoSeek) and human-curated taxonomies ([[Yahoo]]'s directory). First-generation engines indexed tens of millions of static pages and required novel distributed architectures — "tens of machines to create highly available systems" — well before the term *cloud* existed. The chapter notes that classical IR techniques alone produced "results that left much to be desired," motivating new ranking signals based on the authoritativeness of the *host* rather than just textual relevance of the page. This is the conceptual seed of [[PageRank]] and link analysis that Chapter 21 develops formally.

### 19.2 Web Characteristics

The web's defining property for IR purposes is heterogeneity. Page authoring varies across natural languages, character encodings, HTML quality, and styling conventions. Many pages carry no indexable text (image-only marketing pages, Flash sites, dynamic forms). By 1995 [[Altavista]] indexed roughly 30 million static pages; the additional combinatorial explosion of dynamically generated pages (CGI scripts, query-by-form catalogs, the "deep web") was already a known indexing problem. The chapter emphasizes that trust is not a universal property of a page — a page authoritative for one community (e.g., alternative medicine forums) may be untrustworthy for another (e.g., medical professionals), foreshadowing the eventual rise of personalized and contextual ranking.

### 19.2.1 The Web Graph

Pages are modeled as nodes in a directed graph with hyperlinks as edges. Each link carries [[AnchorText]] that often describes the target page from an external viewpoint, providing a powerful "voted description" that the target's own text cannot offer. Empirical studies (Kumar et al. 2000, Broder et al. 2000) showed:

- **In-degree** averages 8–15 with a heavy-tailed distribution following a power law with exponent α ≈ 2.1. The probability that a randomly chosen page has in-degree exactly *i* is proportional to 1/iα.
- **Out-degree** follows a similar power-law distribution, though with different exponent.
- **Macrostructure is bow-tie shaped** with four major regions:
  1. **SCC** (Strongly Connected Component) — a large set of mutually reachable pages forming the "knot" of the bow tie.
  2. **IN** — pages that can reach SCC via directed links but cannot be reached from SCC.
  3. **OUT** — pages reachable from SCC but with no directed path back into SCC.
  4. **Tendrils** — dead-end branches off IN (cannot reach SCC) and off OUT (not reachable from SCC), plus **tubes** that bridge IN directly to OUT bypassing SCC.

In the Broder et al. (2000) snapshot, SCC, IN, OUT, and tendrils+tubes each accounted for roughly a quarter of the discoverable web. This implies that an estimated 25% of randomly chosen page pairs have no directed path between them, which has direct consequences for crawling completeness and for random-walk-based sampling (see §19.5).

### 19.2.2 Spam

The chapter frames web spam as the inevitable consequence of ranking by document features that authors control. Early term-frequency ranking ([[TFIDF]]) was trivially gamed by keyword stuffing: repeating "maui golf real estate" hundreds of times invisibly (white text on white background, or hidden in meta tags) to capture purchase-intent traffic. Two named techniques are central:

- **[[Cloaking]]:** the spammer's web server inspects the HTTP `User-Agent` header (or originating IP block) and returns one document to search-engine crawlers and a different document to human browsers. Search engines see optimized keyword-rich pages; users see commercial pages they did not search for.
- **[[DoorwayPage]]:** a page hand-crafted to rank highly on a chosen query, containing carefully chosen keywords and metadata, which then redirects (via meta-refresh, JavaScript, or HTTP 302) the human visitor to the actual commercial destination.

The chapter notes that paid inclusion — paying a search engine for guaranteed indexing — emerged as a quasi-legitimate analogue of Yellow Pages advertising and that [[SEO]] grew into a full consulting industry. [[Google]]'s breakthrough was to lean on link analysis rather than on-page text, exploiting a structural signal (other authors' votes) that no single spammer could fully manufacture. This produced the modern adversarial-IR regime where every new ranking signal triggers a counter-optimization wave.

### 19.3 Advertising as the Economic Model

The chapter narrates three economic eras of web advertising. **Banner ads** on portals like [[Yahoo]] and AOL used a [[CPM]] (cost per mille — per thousand impressions) brand-awareness model inherited from print and television. **Cost-per-click ([[CostPerClick]], CPC)** ads shifted payment to engagement: advertisers paid only when a user clicked through to their landing page, aligning advertiser cost with measurable user intent. **Cost-per-action (CPA)** went one step further, charging only on conversion (a sale, a signup).

The pivotal innovation was **sponsored search**, pioneered by Goto.com (later renamed Overture, then acquired by [[Yahoo]]). Goto auctioned ranked positions for query terms to advertisers, with the highest bidder appearing at the top of the sponsored panel and paying only when clicked. This model exploited a unique property of search: queries like "golf clubs" directly reveal purchase intent at the moment of greatest commercial value. [[Google]] later refined the auction with quality-score weighting (bid × click-through-rate) and made it the dominant search-advertising mechanic.

Modern search-engine result pages (SERPs) blend two streams: **algorithmic results** (also called "organic"), which the chapter treats as the IR-proper output, and **sponsored results** (paid placement), which appear in a separate panel with disclosure. The economic incentive sustaining the algorithmic side is preserving user trust so that future queries remain valuable to advertisers. The same incentive structure created **click spam** — competitors or affiliates issuing fraudulent clicks to drain a rival's budget, or affiliate networks inflating their own ad revenue. Search-engine marketing (SEM) emerged as a profession optimizing keyword bidding portfolios.

### 19.4 The Search User Experience

[[Google]]'s competitive success is attributed to two user-experience principles. First, an emphasis on **precision at the top of the ranking** rather than on recall — users almost never scroll past the first ten results, so ranking quality dominates exhaustiveness. Second, a **lightweight, low-graphics interface** that loaded fast on dial-up and presented a single query box, in contrast to portal-style pages cluttered with news, ads, and links.

### 19.4.1 User Query Needs (Broder's Taxonomy)

[[AndreiBroder]]'s 2002 paper *A Taxonomy of Web Search* (then at Altavista) introduced the now-canonical three-way intent classification:

1. **[[InformationalQuery]]** — the user seeks broad knowledge about a topic, expecting to read multiple pages. Examples: "leukemia," "Provence," "neural network." Quality metric: recall at top-k and topical diversity.
2. **[[NavigationalQuery]]** — the user wants a specific known site. Example: "Lufthansa." The single correct answer is the Lufthansa homepage; precision@1 is the entire metric.
3. **[[TransactionalQuery]]** — the user intends to perform an action online (buy, download, book, register). Example: "buy iPod nano." The engine should surface pages with transaction interfaces.

Broder noted that real queries are messy: some belong to multiple categories, some to none. The taxonomy nonetheless became the foundation for query-intent classification in modern engines, influencing both ranking (different signals matter for different intents) and ad placement (transactional queries justify sponsored slots; informational queries less so). The chapter also reports that the **average web query has 2–3 keywords** and that operators (Boolean AND/OR, phrase quotes, `site:`) are used by a small minority of power users.

### 19.5 Index Size and Estimation

Search engines historically competed on index size, advertising claims of "X billion pages indexed." The chapter discusses how to measure such claims honestly given that the true denominator (the size of the web) is unknown and unknowable. Several sampling strategies are surveyed, each biased:

- **Random queries** from a dictionary, conjunctively combined, then sampling one result — biased toward long documents and dependent on ranking.
- **Random IP addresses**, then crawling all hosted pages — biased toward small sites because pages are unevenly distributed across hosts.
- **Random walks** on the web graph — broken because the web is not strongly connected (only the SCC component supports stationary random walks).
- **Document random-walk sampling** (Bar-Yossef and Gurevich, 2006) — builds a virtual undirected graph on documents sharing terms and walks that instead; the state of the art at publication.

Once an unbiased sample is in hand, the relative size of two engines can be compared by **capture-recapture** (the classical ecology technique for estimating wildlife populations). See the formula below.

### 19.6 Near-Duplicates and Shingling

Duplication is endemic on the web: mirror sites, syndication, content scraping, boilerplate templates. The chapter cites the figure that "as many as 40% of pages on the web are duplicates of other pages." Beyond exact byte-identical copies (easy to detect via SHA hash), the harder problem is **near-duplicates** that differ only in timestamps, ad rotations, navigation menus, or session IDs.

The chapter introduces **[[Shingling]]** as the standard solution. A *k-shingle* of document *d* is the set S(*d*) of all contiguous *k*-term subsequences. For "a rose is a rose is a rose" with *k*=4, the shingles are {"a rose is a", "rose is a rose", "is a rose is"}. The similarity of two documents is then the [[JaccardSimilarity]] of their shingle sets: J(S(d₁), S(d₂)) = |S(d₁) ∩ S(d₂)| / |S(d₁) ∪ S(d₂)|.

Computing Jaccard over billions of documents pairwise would be O(N²) and infeasible. The chapter develops the [[MinHash]] sketching trick: for each document, apply many independent random permutations π to its shingles (after hashing them to integers) and record the minimum value min π(S(d)). Probabilistic theorem: **Pr[min π(S(d₁)) = min π(S(d₂))] = J(S(d₁), S(d₂))**. Thus the fraction of permutations on which two documents agree on their minimum hash is an unbiased estimator of their Jaccard similarity. Practically, a sketch of 200 min-hashes per document supports near-duplicate detection by simple counting, and super-shingles further collapse the sketch for fast clustering with a union-find structure. The technique scales to web-corpus sizes and underpins both crawler de-duplication and copyright/plagiarism detection.

## Algorithms & Formulas

**Bow-tie components.** For the web graph G = (V, E) viewed as directed:

- SCC = maximal strongly connected subgraph (every pair u,v has directed paths u→v and v→u)
- IN  = { v ∈ V \ SCC : v has a directed path into SCC }
- OUT = { v ∈ V \ SCC : SCC has a directed path into v }
- Tendrils = pages in V \ (SCC ∪ IN ∪ OUT) reachable from IN forward or reaching OUT backward
- Tubes = paths from IN directly to OUT not passing through SCC

In Broder et al. (2000) snapshot: |SCC| ≈ |IN| ≈ |OUT| ≈ |tendrils+tubes| ≈ 25% each of the connected portion.

**Power-law in-degree.** P(in-degree = i) ∝ 1/iα with α ≈ 2.1 (Kumar et al. 1999).

**k-shingle set.** For document d with token sequence t₁, t₂, …, t_n, define S_k(d) = { (t_j, t_{j+1}, …, t_{j+k−1}) : 1 ≤ j ≤ n − k + 1 }. Typical k = 5–9 tokens.

**Jaccard similarity.** J(A, B) = |A ∩ B| / |A ∪ B|, range [0, 1]; J = 1 iff identical sets; J = 0 iff disjoint.

**Min-hash sketch.** For each of M random permutations π_m on the shingle universe, sketch_m(d) = min{ π_m(s) : s ∈ S_k(d) }. The estimator Ĵ(d₁, d₂) = (1/M) · |{ m : sketch_m(d₁) = sketch_m(d₂) }| converges to J(S(d₁), S(d₂)) by the min-hash collision theorem. M = 200 is typical for web-scale work.

**Capture-recapture index-size estimator.** Given two engines E₁ and E₂ both treated as independent uniform random subsets of the web, let *x* be the fraction of pages sampled from E₁ that are also in E₂, and *y* be the fraction sampled from E₂ that are also in E₁. Then |E₁| / |E₂| ≈ y / x. Proof sketch: |E₁ ∩ E₂| = x · |E₁| = y · |E₂|, so |E₁|/|E₂| = y/x. Practical complication: sampling uniformly is itself the hard problem (see §19.5).

## Key Quotes

> "Web pages exhibited heterogeneity at a daunting scale." — §19.2

> "There may be no universal, user-independent notion of trust; a web page whose contents are trustworthy to one user may not be so to another." — §19.2

> "Spamming is inherently an economically motivated activity, and has sprung into a billion-dollar subindustry." — §19.2.2

> "Clicking on the advertisement leads the user to a web page set up by the advertiser, where the user is induced to make a purchase." — §19.3

> "The very first search result should be the home page of Lufthansa." — §19.4.1 (on navigational queries)

> "As many as 40% of the pages on the Web are duplicates of other pages." — §19.6

> "The Jaccard coefficient equals the probability that two documents share a minimum permuted hash value." — §19.6

## Connections

- [[InformationRetrieval]] — the chapter extends the textbook's core IR framework to web scale and adversarial conditions.
- [[CommonCrawl]] — modern open analogue of the crawls discussed historically here; downstream of all crawling and de-duplication problems described.
- [[google]] — central exemplar throughout the chapter; framed as the engine that solved early ranking, spam, and UX problems simultaneously.
- [[WebSearch]] — the chapter is the textbook's primary entry point to web-search-as-a-discipline.
- [[WebGraph]] — modeled here as a directed graph with power-law degree distribution; underpins later chapters on link analysis.
- [[BowTie]] — the macrostructural model (SCC/IN/OUT/tendrils) introduced in §19.2.1.
- [[WebSpam]] — the adversarial side of web IR; this chapter is the canonical introduction.
- [[Cloaking]] — server-side spam technique discussed in §19.2.2.
- [[DoorwayPage]] — keyword-stuffed redirect pages, §19.2.2.
- [[SEO]] — the consulting industry that emerged from the spam arms race.
- [[PaidPlacement]] — Goto/Overture/Google AdWords sponsored search model from §19.3.
- [[CostPerClick]] — payment model dominating sponsored search; replaces banner CPM.
- [[QueryIntent]] — Broder's three-way taxonomy.
- [[NavigationalQuery]] — "find Lufthansa.com," precision@1 metric.
- [[InformationalQuery]] — broad-topic exploration, recall-oriented.
- [[TransactionalQuery]] — purchase/download/booking intent, drives ad value.
- [[Shingling]] — k-gram set representation for near-duplicate detection.
- [[MinHash]] — sketching technique making Jaccard tractable at web scale.
- [[NearDuplicateDetection]] — the §19.6 problem and its algorithmic solution.
- [[JaccardSimilarity]] — the similarity measure that shingling estimates.
- [[AnchorText]] — link text as voted external description of a target page.
- [[PageRank]] — implied throughout but formally developed in IIR Ch. 21.
- [[TFIDF]] — classical ranking signal that web spam attacked first; motivating context.
- [[VectorSpaceModel]] — same as above; classical baseline against which web ranking is contrasted.
- [[AndreiBroder]] — author of the query-intent taxonomy and co-author of the bow-tie and shingling papers.
- [[Yahoo]] — early human-curated directory and later acquirer of Overture.
- [[Altavista]] — pioneering first-generation full-text engine; Broder worked there.
- [[MinHashDeduplication]] — existing concept page in this wiki; this chapter is its theoretical grounding.
- [[CPM]] — banner-ad pricing model that sponsored search displaced.

## Contradictions

- None identified. The chapter is consistent with later IIR chapters (Ch. 20 on crawling, Ch. 21 on link analysis) and with the wiki's existing pages on [[MinHashDeduplication]] and classical IR ranking. The 40%-duplicates figure is a 2008 estimate; modern crawls (e.g., [[CommonCrawl]]) report similar or higher near-duplicate rates, so the claim has aged well rather than being contradicted.
