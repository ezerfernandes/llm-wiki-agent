---
title: "Dive into Systems — Ch 2.6 Strings and the String Library"
type: source
tags: [dive-into-systems, c-language, strings, standard-library, security, buffer-overflow]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/strings.html
sources: []
last_updated: 2026-05-17
---

# Dive into Systems — Ch 2.6 Strings and the String Library

## Summary

The sixth section of [[DiveIntoSystems]] Ch 2 *A Deeper Dive Into C* — by [[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]] — **returns to [[CString|C strings]] with the full [[Pointer|pointer]] / [[Malloc|dynamic-memory]] toolkit Ch 2.2–2.5 supplied**, deepening the [[dis-1-5-arrays-strings|Ch 1.5]] three-function introduction ([[Strlen|`strlen`]] / [[Strcpy|`strcpy`]] / [[Sprintf|`sprintf`]]) into the full [[StringLibrary|`<string.h>`]] surface area. Three subsections — (1) **statically allocated strings** restates the [[CArray|`char` array]] + [[NullTerminator|`'\0'`]] convention with the headline warning *"failure to allocate enough memory will yield undefined results that range from program crashes to major security vulnerabilities"*; (2) **dynamically allocated strings** plugs the [[dis-2-4-dynamic-memory|Ch 2.4]] [[Malloc|`malloc`]] machinery into the [[CString|C-string]] world, emphasising the `strlen(s) + 1` byte-count discipline; (3) **libraries for manipulating C strings and characters** opens up the comparison family ([[Strcmp|`strcmp`]] / [[Strncmp|`strncmp`]]), the bounded-copy family ([[Strncpy|`strncpy`]] / [[Strlcpy|`strlcpy`]]), concatenation ([[Strcat|`strcat`]] / [[Strncat|`strncat`]]), search ([[Strchr|`strchr`]] / [[Strstr|`strstr`]]), tokenization ([[Strtok|`strtok`]] / `strtok_r`), and the supporting [[CtypeLibrary|`<ctype.h>`]] character-class library + the [[Atoi|`atoi`]] / `atof` numeric-conversion family. Codifies the **caller-owns-the-destination-size** safety contract that [[dis-1-5-arrays-strings|Ch 1.5]] flagged but deferred, and introduces the [[Strncpy|`strncpy`]] *non-termination footgun* + the [[Strlcpy|`strlcpy`]] (glibc 2.38, 2023) modern fix.

## Key Claims

- **The Ch 1.5 string convention still holds.** A [[CString|C string]] is a [[CArray|`char` array]] terminated by a [[NullTerminator|`'\0'`]]; not all `char` arrays are C strings, but every C string is a `char` array. The chapter reiterates that *"all C strings are character arrays, but not all character arrays are C strings."*
- **The destination-size discipline is the chapter's load-bearing rule.** Many [[StringLibrary|`<string.h>`]] functions (notably [[Strcpy|`strcpy`]] and [[Strcat|`strcat`]]) write into a destination pointer parameter and **assume the destination has enough room**. Per the chapter: *"failure to allocate enough memory will yield undefined results that range from program crashes to major security vulnerabilities."* Three common failure modes: writing past the end of a fixed-size array, passing [[NullPointer|`NULL`]] as destination, attempting to modify a string-literal constant.
- **Dynamic-string allocation needs `strlen(s) + 1`.** When duplicating a string with [[Malloc|`malloc`]], the byte count must include the trailing `'\0'`: `new_str = malloc(sizeof(char) * (strlen(src) + 1));`. The `+1` is the same byte-counting trap [[dis-1-5-arrays-strings|Ch 1.5]] surfaced, now operationalized with [[dis-2-4-dynamic-memory|Ch 2.4]]'s [[Malloc|`malloc`]] / [[Free|`free`]] machinery and the [[NullPointer|`NULL`]]-check / [[Exit|`exit`]] guard.
- **`strncpy` does not always null-terminate — the chapter's most-emphasized footgun.** *"When the length of the src string is greater than or equal to size, [[Strncpy|`strncpy`]] copies the first size characters from src to dst and does **not** add a null character to the end of the dst."* The discipline: *"the programmer should explicitly add a null character to the end of dst after calling [[Strncpy|`strncpy`]]"* (`dst[size-1] = '\0';` is the idiom).
- **`strlcpy` is the modern fix.** *"The [[Strlcpy|`strlcpy`]] function is similar to [[Strncpy|`strncpy`]], except it always adds the `'\0'` character to the end of the destination string."* Added to GNU [[CLanguage|C]] library version 2.38 (mid-2023, long present in BSD libcs); not yet portable. Removes the post-call `dst[size-1] = '\0';` line.
- **`strcmp` has tri-valued return.** *"returns 0 if s1 and s2 are the same strings / a value < 0 if s1 is less than s2 / a value > 0 if s1 is greater than s2"* — comparison is byte-by-byte on ASCII values. `strncmp` is the bounded variant. The chapter restates *"the [[Strcmp|`strcmp`]] function compares strings character by character based on their ASCII representation."* This is the answer to the classic *why `s1 == s2` doesn't work* question — `==` on two `char *` compares **base addresses**, not contents.
- **Concatenation echoes copy's safety story.** [[Strcat|`strcat`]] appends `src` to the end of `dst` and shares [[Strcpy|`strcpy`]]'s destination-size assumption; [[Strncat|`strncat`]] is the bounded variant. Same memory-allocation discipline applies — `dst` must have room for *both* the original contents *and* the appended bytes *and* the new `'\0'`.
- **Search functions return pointers into the original string.** [[Strchr|`strchr`]] returns a pointer to the first occurrence of a character or [[NullPointer|`NULL`]] if absent; [[Strstr|`strstr`]] returns a pointer to the first occurrence of a substring or [[NullPointer|`NULL`]]. **The returned pointer aliases the input** — both functions hand back an address *inside* the original buffer, not a copy. Idiomatic use: *"if `strstr` returns non-`NULL`, that's a pointer to the start of the match within the original string."*
- **Tokenization with `strtok`.** *"A **token** refers to a subsequence of characters in a string separated by any number of delimiter characters of the programmer's choosing."* [[Strtok|`strtok`]] *destructively* tokenizes — it writes `'\0'` over delimiter bytes — and keeps **internal static state** between calls (subsequent calls pass `NULL` as the first argument). Not thread-safe; `strtok_r` is the reentrant variant.
- **`sprintf` constructs formatted strings.** The [[Printf|`printf`]] family member that writes formatted output into a [[CString|C string]] buffer instead of [[StandardOutput|stdout]]: `sprintf(str, "%s is %d years old and in grade %d", "Henry", 12, 7);`. Same unbounded-write hazard as [[Strcpy|`strcpy`]]; `snprintf` is the bounded substitute.
- **`<ctype.h>` is the character-class library.** Predicate functions return *nonzero for true*: `islower`, `isupper`, `isalpha`, `isdigit`, `isalnum`, `ispunct`, `isspace`. Conversion functions return the converted ASCII value: `tolower`, `toupper`. Returning *nonzero* (not necessarily `1`) is the boolean convention.
- **`<stdlib.h>`'s string-to-number family.** [[Atoi|`atoi`]] (ASCII to int) and `atof` (ASCII to float / double) parse leading numeric prefixes of a string. Modern code increasingly prefers `strtol` / `strtod` for their error-reporting capability; the chapter introduces `atoi` / `atof` as the simple-but-quiet entry point.
- **`char []` vs `char *` in parameters — both decay to base address.** *"Both statically declared and dynamically allocated arrays of characters can be passed to a `char *` parameter because the name of either type of variable evaluates to the base address of the array in memory."* This is the [[ArrayDecay|array-decay]] rule from [[dis-2-5-arrays|Ch 2.5]], now restated for strings specifically.
- **Return-value asymmetry — a `char *` return can't go into a `char []`.** *"If a function returns a string (its return type is a `char *`), its return value can only be assigned to a variable whose type is also `char *`; it cannot be assigned to a statically allocated array variable. This restriction exists because the name of a statically declared array variable is not a valid [[LValue|lvalue]] (its base address in memory cannot be changed)."* — the [[dis-1-6-structs|Ch 1.6]] [[LValue|lvalue]] story applied to strings.
- **`free` and `NULL` discipline carries over.** Dynamically allocated strings follow the [[dis-2-4-dynamic-memory|Ch 2.4]] pattern: `free(new_str); new_str = NULL;`.
- **Manual pages are the canonical reference.** *"For more information about these and other C library functions … see their man pages. For example, to view the [[Strcpy|`strcpy`]] man page, run: `$ man strcpy`."* Introduces the [[ManPages|`man`]] system as the textbook's recommended discovery surface for parameter formats, return values, and required headers.

## Key Quotes

> "Failure to allocate enough memory will yield undefined results that range from program crashes to major security vulnerabilities."

> "When the length of the src string is greater than or equal to size, strncpy copies the first size characters from src to dst and does not add a null character to the end of the dst. As a result, the programmer should explicitly add a null character to the end of dst after calling strncpy."

> "The strlcpy function is similar to strncpy, except it always adds the '\0' character to the end of the destination string."

> "Linux's GNU C library added strlcpy in a recent version (2.38). It's currently only available on some systems, but its availability will increase as newer versions of the C library become more widespread."

> "A token refers to a subsequence of characters in a string separated by any number of delimiter characters of the programmer's choosing."

> "Both statically declared and dynamically allocated arrays of characters can be passed to a char * parameter because the name of either type of variable evaluates to the base address of the array in memory."

> "If a function returns a string (its return type is a char *), its return value can only be assigned to a variable whose type is also char *; it cannot be assigned to a statically allocated array variable. This restriction exists because the name of a statically declared array variable is not a valid lvalue (its base address in memory cannot be changed)."

> "For more information about these and other C library functions … see their man pages."

## Connections

- [[DiveIntoSystems]] — the textbook; this is Ch 2.6 of Ch 2 *A Deeper Dive Into C*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-1-5-arrays-strings]] — the Ch 1 introduction to [[CString|C strings]] that *deferred* the safety-and-bounded-variants discussion to Ch 2.6. Ch 2.6 picks up that thread.
- [[dis-2-4-dynamic-memory]] — the [[Malloc|`malloc`]] / [[Free|`free`]] / [[Exit|`exit`]] / [[NullPointer|`NULL`]]-check machinery the *dynamic strings* section reuses.
- [[dis-2-5-arrays]] — the [[ArrayDecay|array-decay]] mechanism the *parameter-passing* section restates for `char []` vs `char *`.
- [[CString]] — extended here with safety discipline and the dynamic-allocation pattern.
- [[NullTerminator]] — the sentinel the entire library depends on.
- [[StringLibrary]] — expanded from the Ch 1.5 three-function preview to the full surface area.
- [[Strlen]] / [[Strcpy]] / [[Sprintf]] — Ch 1.5 introductions restated with safety context.
- [[Strncpy]] — the bounded-copy variant + the non-termination footgun.
- [[Strlcpy]] — the modern always-terminates variant (glibc 2.38+).
- [[Strcmp]] / [[Strncmp]] — the comparison family.
- [[Strcat]] / [[Strncat]] — the concatenation family.
- [[Strchr]] / [[Strstr]] — the search family.
- [[Strtok]] — destructive tokenization with internal state.
- [[CtypeLibrary]] — `<ctype.h>` character-class predicates + case conversion.
- [[Atoi]] — `<stdlib.h>` ASCII-to-int conversion.
- [[ManPages]] — the recommended documentation surface.
- [[LValue]] — the [[dis-1-6-structs|Ch 1.6]] concept that explains why `char []` cannot be assigned a `char *` return value.
- [[BufferOverflow]] — the security failure mode this chapter's safety story is fighting.
- [[Pointer]] / [[NullPointer]] / [[Malloc]] / [[Free]] — the underlying machinery.

## Contradictions

- None. Ch 2.6 *completes* [[dis-1-5-arrays-strings|Ch 1.5]]'s explicit deferral of safer string functions ([[Strncpy]] / `snprintf`) and the comparison family ([[Strcmp]] / [[Strncmp]] / [[Strchr]] / [[Strstr]]). The chapter ratifies [[dis-1-5-arrays-strings|Ch 1.5]]'s [[Strcpy|`strcpy`]] safety warning, layers on the [[Strncpy|`strncpy`]] non-termination footgun (a *new* hazard introduced precisely because the naive safer choice has its own bug), and supplies the [[Strlcpy|`strlcpy`]] (glibc 2.38) modern fix. No prior claim overturned.
