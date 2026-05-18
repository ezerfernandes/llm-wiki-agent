---
title: "scanf Character Class (%[...] / %Ns, C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# scanf Character Class (`%[...]` / `%Ns`)

The **character-class** and **max-width** [[FormatSpecifier|format specifiers]] are the [[Scanf|`scanf`]] / [[Fscanf|`fscanf`]] extensions that fix the unbounded / whitespace-stops-at-space fragility [[dis-1-2-input-output|Ch 1.2]] flagged. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.4 — the **robustness fix** for the §2.8 deepening.

## The forms

| Specifier | Reads |
|---|---|
| `%[abc]` | a string of characters **in** the set `{a, b, c}`; stops at the first character outside the set |
| `%[a-z]` | a range (where supported — typically GNU libc extension) |
| `%[^abc]` | a string of characters **not in** the set; stops at the first character in the set |
| `%[^\n]` | everything up to (but **not including**) the next newline — the "rest of line" reader |
| `%Ns` (e.g. `%20s`) | at most `N` characters into the buffer ([[NullTerminator|`\0`]] still written) — the **buffer-overflow fix** for `%s` |
| `%N[...]` (e.g. `%20[0-9]`) | combined: at most `N` characters from the set |

## Worked examples (per Ch 2.8 §2.8.4)

```c
char array[MAX];

/* string of digits 0..5, max 20 chars */
fscanf(infile, "%20[012345]", array);

/* string of everything except punctuation marks */
fscanf(infile, "%[^.,:!;]", array);

/* rest of line up to newline */
fscanf(infile, "%[^\n]", array);
```

## Why this fixes [[Scanf|`scanf`]]'s flaws

- **No more unbounded `%s` writes.** `%20s` caps the read at 20 bytes — paired with a `char buf[21]` (the extra byte holds `'\0'`), [[BufferOverflow|buffer overflow]] is impossible. The [[Scanf|`scanf`]] equivalent of [[Strlcpy|`strlcpy`]].
- **No more "I want a whole line including spaces."** `%[^\n]` reads everything to the newline — what `%s` notoriously refuses to do.
- **Bounded vocabulary parsing.** `%[0-9]` reads only digits — useful for token boundaries in hand-rolled parsers.

The remaining limitation is the **trailing-newline footgun**: `%[^\n]` consumes everything up to `\n` but **leaves the `\n` on the stream**, so a follow-up call sees it. The fix is the explicit-`%c`-after pattern:

```c
fscanf(infile, "%[^\n]%*c", array);   /* %*c reads and discards the newline */
```

## Connections

- [[Scanf]] / [[Fscanf]] — the functions this extends.
- [[FormatSpecifier]] — the broader specifier vocabulary.
- [[BufferOverflow]] — the failure mode `%Ns` prevents.
- [[Fgets]] — the alternative robust-input recipe; `fgets` + `sscanf` is more common in production than `%[^\n]`.
- [[Strlcpy]] — the [[StringLibrary]] analog of `%Ns`.
- [[CString]] — the result type.
- [[dis-2-8-io]] — introducing source.
