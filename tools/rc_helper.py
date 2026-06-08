#!/usr/bin/env python3
"""Helper for the bulk Rosetta Code task ingest.

Subcommands:
  pending [N]   print the next N pending tasks (title<TAB>slug) not yet ingested
  count         print done / total / remaining
  reindex       rebuild the "Rosetta Code Tasks" section of wiki/index.md and
                append any missing ingest entries to wiki/log.md, from the
                rc-*.md source files actually present on disk.

"Done" == wiki/sources/rc-<slug>.md exists and is non-trivial (> frontmatter).
"""
import os, sys, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "raw", "rosettacode", "manifest.tsv")
SRC_DIR = os.path.join(ROOT, "wiki", "sources")
INDEX = os.path.join(ROOT, "wiki", "index.md")
LOG = os.path.join(ROOT, "wiki", "log.md")


def load_manifest():
    rows = []
    with open(MANIFEST) as f:
        next(f)  # header
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            title, slug = line.split("\t")
            rows.append((title, slug))
    return rows


def is_done(slug):
    p = os.path.join(SRC_DIR, slug + ".md")
    if not os.path.exists(p):
        return False
    # guard against empty/stub files (rate-limit damage)
    txt = open(p, encoding="utf-8").read()
    body = re.sub(r"(?s)^---.*?---", "", txt, count=1).strip()
    return len(body) > 80


def cmd_pending(n):
    rows = load_manifest()
    out = [(t, s) for (t, s) in rows if not is_done(s)]
    for t, s in out[:n]:
        print(f"{t}\t{s}")


def cmd_count():
    rows = load_manifest()
    done = sum(1 for (_, s) in rows if is_done(s))
    total = len(rows)
    print(f"done={done} total={total} remaining={total - done}")


def read_front(path):
    txt = open(path, encoding="utf-8").read()
    m = re.search(r"(?s)^---(.*?)---", txt)
    fm = m.group(1) if m else ""
    def field(name):
        mm = re.search(rf'^{name}:\s*"?(.*?)"?\s*$', fm, re.M)
        return mm.group(1).strip() if mm else ""
    # one-line summary = first non-empty line after a "## Summary" header
    summ = ""
    sm = re.search(r"##\s*Summary\s*\n+(.*?)(\n\n|\n##|$)", txt, re.S)
    if sm:
        summ = " ".join(sm.group(1).split())[:160]
    return field("title"), field("date"), summ


def cmd_reindex():
    rows = load_manifest()
    # ---- index section ----
    lines = ["## Rosetta Code Tasks",
             "*Programming tasks from [rosettacode.org](https://rosettacode.org/wiki/Category:Solutions_by_Programming_Task) — each page summarizes one task and its cross-language solution coverage.*",
             ""]
    done_rows = []
    for title, slug in rows:
        p = os.path.join(SRC_DIR, slug + ".md")
        if not is_done(slug):
            continue
        t, d, summ = read_front(p)
        disp = t or title
        summ = summ or "Rosetta Code programming task."
        lines.append(f"- [{disp}](sources/{slug}.md) — {summ}")
        done_rows.append((title, slug, disp, d))
    section = "\n".join(lines) + "\n"

    idx = open(INDEX, encoding="utf-8").read()
    marker = "## Rosetta Code Tasks"
    if marker in idx:
        # replace from marker up to next top-level "## " or EOF
        pat = re.compile(r"## Rosetta Code Tasks.*?(?=\n## (?!Rosetta)|\Z)", re.S)
        idx = pat.sub(section, idx, count=1)
    else:
        idx = idx.rstrip() + "\n\n" + section
    open(INDEX, "w", encoding="utf-8").write(idx)

    # ---- log entries (only those not already present) ----
    log = open(LOG, encoding="utf-8").read() if os.path.exists(LOG) else ""
    appended = 0
    new_lines = []
    for title, slug, disp, d in done_rows:
        # disp already ends in "(Rosetta Code)" (from the page title), so no suffix here
        entry = f"## [{d or '2026-05-30'}] ingest | {disp}"
        if entry not in log:
            new_lines.append(entry)
            appended += 1
    if new_lines:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(new_lines) + "\n")
    print(f"reindex: {len(done_rows)} tasks in index; {appended} new log entries")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "count"
    if cmd == "pending":
        cmd_pending(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    elif cmd == "count":
        cmd_count()
    elif cmd == "reindex":
        cmd_reindex()
    else:
        print("usage: rc_helper.py [pending N | count | reindex]", file=sys.stderr)
        sys.exit(1)
