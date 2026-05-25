---
title: "Anchor Text"
type: concept
tags: [web-search, information-retrieval, link-analysis]
sources: [iir-ch21-link-analysis, iir-ch19-web-search-basics]
last_updated: 2026-05-23
---

The visible click-target text of a hyperlink — the phrase a page uses to describe the page it points at. In HTML: `<a href="https://example.com/">click here</a>` has anchor text *"click here"*.

**Why it matters for retrieval**: anchor text written by *other* authors is often a better description of a page than the page's own text. A page may not contain the word *"computer"* anywhere in its body, but if hundreds of other pages link to it with anchor *"computer"*, the inbound anchor consensus is strong evidence the page is about computers. This is one of the founding insights of web search: the link graph carries lexical signal as well as authority signal.

**How it's used**:
- **Indexing**: each anchor's terms are added to the target page's posting lists (often with a higher weight than body text and lower than title).
- **Combating spam**: a page whose body text disagrees with the inbound anchor consensus is suspect (potentially a [[Cloaking|cloaked]] page serving different content to crawlers).
- **Bootstrap discovery**: pages that have no body content (image galleries, PDFs) are still indexable via their anchors.

**Limitations** and counter-trends:
- **Anchor spam**: link farms, Google bombs (*"miserable failure"* → George W. Bush biography, 2003).
- Sites often link with semantically-empty anchors (*"click here"*, *"more info"*).
- Modern ranking uses anchor text as one signal among many — neural retrieval supersedes it for surface-form matching but anchor signal remains useful for authority.

Originated as a retrieval signal at [[WorldWideWebWorm]] / [[Altavista]] / [[google|Google]]. Combined with [[PageRank]] in early Google's ranking. Full treatment in [[iir-ch21-link-analysis]] §21.1.1.
