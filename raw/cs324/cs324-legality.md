# Stanford CS324 (Winter 2022) — Legality
Source: https://stanford-cs324.github.io/winter2022/lectures/legality/
Fetched for wiki ingest.

---

## Course Context

This lecture is part of Stanford's CS324 course ("Large Language Models", Winter 2022). It covers the intersection of law with the development and deployment of large language models, focusing on **copyright**, **fair use**, and the **legality of training data**, with a secondary treatment of **privacy law**.

## Introduction to the Legal Framework

New powerful technologies raise the question of whether existing laws still apply. The concept of "Internet law" emerged similarly when the internet grew prominent, drawing from intellectual property, privacy, and contract law.

Judge **Frank Easterbrook** used the term **"Law of the Horse"** in 1996 to question why Internet law should be its own section of legal studies and litigation — i.e., whether a new technology truly warrants its own distinct legal category, or whether existing legal principles already cover it.

The internet presented unique legal challenges: unclear geographic jurisdiction, the possibility of anonymity, and content accessibility to global audiences.

### Law vs. Ethics Distinction

- **Law** is "enforceable by government."
- **Ethics** is "not enforceable and can be created by any organization."

Examples of non-legal (ethical) codes include: the Hippocratic Oath, the ACM Code of Ethics, the NeurIPS code of conduct, and the Stanford Honor Code.

## Jurisdictional Considerations

Laws vary by:
- **Country** (US, China, EU)
- **Governmental level** (federal, state, local)

The EU's **GDPR** represents more comprehensive data privacy regulation than US law. California's Consumer Privacy Act parallels GDPR at the state level. The lecture focuses primarily on **United States** law while noting EU leadership in data privacy and AI regulation.

## Types of Law

- **Common law** (judiciary): Based on judges referencing precedent from previous cases. Example: *Oracle v. Google*.
- **Statutory law** (legislature): Written law produced through legislative processes. Example: the **Copyright Act of 1976**. Fair use existed as common law since the **1840s** before being codified in 1976.
- **Regulatory law** (executive): Created by executive agencies focusing on procedures. Example: EPA regulations fulfilling legislative mandates.

## LLM Lifecycle and Legal Intersections

The lifecycle consists of: **collecting training data → training models → adapting to tasks → deploying to users.**

Two main legal areas intersect this process:

**Data:**
- Machine learning depends heavily on data, often others' data collected without consent.
- Copyright law protects creators — does training on such data violate copyright?
- Privacy law protects individual privacy rights.
- Collection and aggregation legality questions arise for both public and private data.

**Applications:**
- LLMs enable diverse downstream tasks.
- They can be intentionally misused (spam, phishing, harassment, disinformation), covered by Internet fraud laws.
- High-stakes deployment (healthcare, lending, education) faces existing sector regulation.
- Expanded LLM capabilities introduce novel challenges.

## Copyright Law

### Intellectual Property Law Motivation

Intellectual property law encourages the creation of diverse intellectual goods by protecting creators' work from appropriation.

### Copyright Protection Definition

Copyright protects:

> "original works of authorship **fixed** in any tangible medium of **expression**, now known or later developed, from which they can be perceived, reproduced, or otherwise communicated, either directly or with the aid of a machine or device."

- The **1976 Act** expanded scope from "published" works to "fixed" works, based on the **1886 Berne Convention**.
- Registration is **not required** for protection (unlike patents), though registration is necessary before suing for infringement.
- The copyright threshold is "**extremely low**."
- Protection lasts **75 years** before works enter the public domain.

### Legal Uses of Copyrighted Works

**Licensing:**
- "a **license is a promise not to sue**."
- Creative Commons licenses enable free distribution.
- Examples: Wikipedia, Khan Academy, and **307 million Flickr images**.

**Fair Use (Section 107)** — four factors determine fair use applicability:
1. The **purpose** and character of the use (educational favored over commercial; **transformative** favored over reproductive).
2. The **nature** of the copyrighted work (fictional favored over factual; the degree of creativity).
3. The **amount** and substantiality of the portion of the **original work** used.
4. The **effect** of the use upon the **market** (or potential market) for the original work.

Examples: summarizing a watched movie constitutes fair use; reimplementing an algorithm (an idea) rather than copying code (an expression) qualifies.

### Important Notes on Copyright

- Facts and ideas are **not** copyrightable.
- Curated fact databases may be copyrightable if the curation/arrangement constitutes expression.
- Copying data for training violates copyright **before any downstream use**.
- Statutory damages reach **up to $150,000 per work** (Section 504).
- Plaintiffs are typically small rights-holders; defendants are large companies.

### Terms of Service Restrictions

Terms of service impose additional restrictions beyond copyright law. For example, **YouTube's terms** prohibit downloading even Creative Commons-licensed videos.

## Key Copyright Cases

- **Authors Guild v. Google** (2013, District Court): Google scanned books and made them searchable with snippets (launched 2002). The court granted summary judgment for Google, deeming it **fair use**.
- **Google v. Oracle** (April 2021, Supreme Court): Google replicated **37 Java APIs** in Android. The Supreme Court ruled Google's use was covered by **fair use**.
- **Fox News v. TVEyes** (2018, 2nd Circuit): TVEyes recorded television and created a searchable text-clip service. The court ruled against TVEyes — **not fair use** — because it deprived Fox News of revenue despite being transformative.
- **Kelly v. Arriba** (2003, 9th Circuit): Arriba's search engine showed thumbnails of Kelly's photographs. The court ruled for Arriba, deeming it **fair use**.
- **Sega v. Accolade** (1992, 9th Circuit): Accolade reverse-engineered Sega Genesis code to make new games. The court ruled for Accolade as **fair use**, emphasizing it was mostly original content benefiting competition without diminishing Sega's market. The court distinguished "**non-expressive**" access to ideas and facts from protectable expression.

## Fair Learning Argument for ML as Fair Use

The "**Fair Learning**" theory (Lemley & Casey) argues machine learning qualifies as fair use because ML use is "**transformative**, doesn't change [the] work, but changes [the] purpose." ML systems extract **ideas** (e.g., the concept of a stop sign) rather than concrete **expression** (the artistic choices in a specific image).

**Arguments supporting ML as fair use:**
- Broad training data access creates better societal systems.
- Licensing from all creators is impractical.
- Using copyrighted data can be fairer to all parties.

**Arguments against:**
- ML systems produce no creative end product but generate profit.
- Generative models compete with creative professionals.
- ML problems (disinformation, surveillance) warrant denying fair use benefits.
- Separating protectable expression from unprotectable ideas is challenging.

The lecture questions whether copyright is even the **appropriate tool** to regulate ML problems.

## Three Historical Phases of Information Technology

- **First phase**: Text data mining (search engines) via simple pattern matching.
- **Second phase**: Classification and recommendation systems.
- **Third phase**: Generative models mimicking expression.
  - Training-data extraction from **GPT-2** raises privacy concerns.
  - LLMs potentially generating copyrighted works verbatim presents fair use problems.
  - Even non-verbatim output still uses copyrighted training material.
  - LLMs can **compete** with writers — e.g., an LLM trained on three books could auto-generate a fourth.

**Conclusion**: Copyright and ML in the context of large language models remains "**very much open**."

## Privacy Law Examples

**Clearview AI** (founded 2017):
- Scraped **10 billion faces** from Facebook, Twitter, Google, YouTube, and Venmo by October 2021.
- Sold the data to law enforcement and commercial entities.
- Claimed **First Amendment** rights to public information.
- Illinois's **Biometric Information Privacy Act (BIPA, 2008)** regulates private biometric identifiers.
- Clearview was deemed illegal by the EU's **Hamburg data protection authority**.

**California Consumer Privacy Act (CCPA, 2018):**
- Provides California residents the right to know what personal data is collected, whether it's sold, to say no to sales, to access data, to request deletion, and to avoid discrimination for exercising privacy rights.
- Personal data includes real names, aliases, addresses, identifiers, IP addresses, emails, account names, SSNs, driver's license numbers, and passport numbers.
- Applies to businesses operating in California with **$25 million+** revenue.
- **No federal equivalent** exists.
- Unlike GDPR, it does **not** allow data correction.

**California Privacy Rights Act (CPRA, 2020):**
- Creates a **California Privacy Protection Agency**.
- Takes effect **January 1, 2023**, for data collected after **January 1, 2022**.
- Intends to enable: knowing who collects data and how it's used; controlling personal information use; accessing, correcting, deleting, and transferring data; exercising privacy rights without penalty; holding businesses accountable for inadequate security; benefiting from businesses' use of personal data; and protecting employee/contractor privacy.

**GDPR (General Data Protection Regulation):**
- EU law on data privacy **adopted in 2016, enforceable in 2018**.
- Broader than CCPA.
- Data subjects can provide and withdraw consent.
- People retain access rights to their data.
- Google was fined **$57 million** for not obtaining consent for Android ad personalization.

## Other Laws

**California's Bot Disclosure Bill (SB 1001):**
- Illegal to use bots to communicate without disclosure that it's a bot.
- Restrictions: applies only to incentivizing sales or influencing elections; applies only to public websites with **10 million+ monthly US visitors**.

## Summary

Training large language models requires confronting **copyright** and **fair use**. The "**uncurated** nature of web crawls" necessitates appeals to fair use — licensing everyone is impractical. The "**generative** aspect" creates fair use challenges through competition with humans. Regulatory-level questions arise: should regulation target LLMs themselves or downstream applications? This space is "quickly evolving and will require deep legal and AI expertise."

### Key Takeaways
- Copyright law protects creators, but fair use permits certain uses.
- LLMs trained on web-scale data necessarily rely on fair use arguments.
- Generative capabilities create novel copyright tensions.
- Privacy law increasingly restricts data collection and use.
- Legal frameworks remain unsettled for emerging AI technologies.

## Further Reading / Citations

- Mark Lemley, Bryan Casey. "Fair Learning." *Texas Law Review*, 2021.
- Casey & Lemley. "You might be a robot." *Cornell Law Review*.

(No individual instructor/author credits appear in the lecture text.)
