---
title: "Trust Root"
type: concept
tags: [concept]
sources: [2605.00424-skills-as-verifiable-artifacts]
last_updated: 2026-05-10
---

# Trust Root

Append-only set of (keyId, pubKey, maxClearance) signer entries. One-shot lock at host bootstrap; subsequent mutations raise a typed error. Locked state is the production posture; an unlocked trust root is acceptable only before any external input has been read. Adapted from object-capability bootstrap discipline.
