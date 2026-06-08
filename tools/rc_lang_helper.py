#!/usr/bin/env python3
"""Helper for the per-language Rosetta Code ingest (Phase A).

Subcommands:
  pending [N]   print next N languages whose wiki/languages/<page>.md is missing/stub
                (tab-separated: category<TAB>page<TAB>task_entries<TAB>pct)
  count         done / total / remaining

"Done" == wiki/languages/<page>.md exists with a real body (> ~120 bytes).
"""
import os, sys, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "raw", "rosettacode", "lang_manifest.tsv")
LANG_DIR = os.path.join(ROOT, "wiki", "languages")


def load():
    rows = []
    with open(MANIFEST) as f:
        next(f)
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            cat, disp, page, te, pct = (parts + ["", "", "", "", ""])[:5]
            rows.append({"cat": cat, "disp": disp, "page": page, "te": te, "pct": pct})
    return rows


def is_done(page):
    p = os.path.join(LANG_DIR, page + ".md")
    if not os.path.exists(p):
        return False
    txt = open(p, encoding="utf-8").read()
    if "<!--SUMMARY" in txt:
        return False  # summary placeholder not yet filled by the subagent
    body = re.sub(r"(?s)^---.*?---", "", txt, count=1).strip()
    return len(body) > 80


def cmd_pending(n):
    rows = load()
    out = [r for r in rows if not is_done(r["page"])]
    for r in out[:n]:
        print(f"{r['cat']}\t{r['page']}\t{r['te']}\t{r['pct']}")


def cmd_count():
    rows = load()
    done = sum(1 for r in rows if is_done(r["page"]))
    print(f"done={done} total={len(rows)} remaining={len(rows) - done}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "count"
    if cmd == "pending":
        cmd_pending(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    elif cmd == "count":
        cmd_count()
    else:
        print("usage: rc_lang_helper.py [pending N | count]", file=sys.stderr)
        sys.exit(1)
