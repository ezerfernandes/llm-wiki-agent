#!/usr/bin/env python3
"""Phase-A worker core: given a Rosetta Code language CATEGORY name, fetch every
task that language solves, intersect with the wiki's 1350 ingested tasks, and
write wiki/languages/<page>.md (structural content + all [[rc-...]] task links),
leaving a <!--SUMMARY--> placeholder for the opus subagent to fill.

Usage: rc_lang_fetch.py "<Category name>"
Prints: MATCHED=<m> TOTAL=<n> PAGE=<page>
"""
import subprocess, json, sys, os, re, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
API = "https://rosettacode.org/w/api.php"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG_MAN = os.path.join(ROOT, "raw", "rosettacode", "lang_manifest.tsv")
TASK_MAN = os.path.join(ROOT, "raw", "rosettacode", "manifest.tsv")
LANG_DIR = os.path.join(ROOT, "wiki", "languages")


def api(params):
    cmd = ["curl", "-s", "-G", "-A", UA, API]
    for k, v in params.items():
        cmd += ["--data-urlencode", f"{k}={v}"]
    for _ in range(4):
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=90).stdout
        try:
            return json.loads(out)
        except Exception:
            time.sleep(1.5)
    raise RuntimeError("api fail")


def category_pages(cat):
    cont = None
    titles = []
    while True:
        p = {"action": "query", "list": "categorymembers", "cmtitle": f"Category:{cat}",
             "cmnamespace": "0", "cmtype": "page", "cmlimit": "500", "format": "json"}
        if cont:
            p["cmcontinue"] = cont
        d = api(p)
        titles += [m["title"] for m in d["query"]["categorymembers"]]
        cont = d.get("continue", {}).get("cmcontinue")
        if not cont:
            break
    return titles


def main():
    cat = sys.argv[1]
    # manifest row for this category
    disp = page = te = pct = ""
    with open(LANG_MAN) as f:
        next(f)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if parts and parts[0] == cat:
                _, disp, page, te, pct = (parts + ["", "", "", "", ""])[:5]
                break
    if not page:
        print(f"ERROR: category {cat!r} not in lang_manifest", file=sys.stderr)
        sys.exit(2)

    title2slug = {}
    with open(TASK_MAN) as f:
        next(f)
        for line in f:
            if line.strip():
                t, s = line.rstrip("\n").split("\t")
                title2slug[t] = s

    members = category_pages(cat)
    matched = sorted({title2slug[t] for t in members if t in title2slug})
    m, n = len(matched), len(members)

    if matched:
        task_lines = "\n".join(f"- [[{s}]]" for s in matched)
    else:
        task_lines = "_No tasks from the wiki's ingested set are solved by this language._"

    te_disp = te if te else "?"
    pct_disp = pct if pct else "?"
    body = f"""---
title: "{disp} (programming language)"
type: entity
tags: [programming-language, rosetta-code]
date: 2026-05-31
rc_category: "Category:{cat}"
rc_task_entries: {te_disp}
rc_tasks_done_pct: "{pct_disp}"
wiki_tasks_solved: {m}
---

## Summary
<!--SUMMARY: replace this line with a 2-4 sentence description of the {disp} programming language (paradigm, typing, origin/era, typical use). Plain prose, no markup headers.-->

## Rosetta Code Coverage
Solves **{m}** of the wiki's 1350 ingested Rosetta Code tasks. Rosetta Code's popularity ranking credits **{disp}** with **{te_disp}** task entries ({pct_disp} of all tasks).

## Tasks Solved
{task_lines}

## Connections
- [[RosettaCode]] — tasks sourced from the Rosetta Code project
"""
    os.makedirs(LANG_DIR, exist_ok=True)
    with open(os.path.join(LANG_DIR, page + ".md"), "w", encoding="utf-8") as f:
        f.write(body)
    print(f"MATCHED={m} TOTAL={n} PAGE={page}")


if __name__ == "__main__":
    main()
