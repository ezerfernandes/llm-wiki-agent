#!/usr/bin/env python3
"""Phase B: add a 'Solved in (Rosetta Code languages)' relationship section to
task pages, listing [[Language]] backlinks for every language that solves the task.

Source of truth = the task page's own section headings on Rosetta Code (each
top-level heading is a language). Headings are mapped to our language pages via
lang_manifest (so links resolve to wiki/languages/<page>.md). Idempotent: an
existing section is replaced.

Usage: rc_link_languages.py <count>   # process the first <count> task pages
                                       # (manifest order) lacking the section
       rc_link_languages.py all        # process all task pages
"""
import subprocess, json, sys, os, re, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
API = "https://rosettacode.org/w/api.php"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASK_MAN = os.path.join(ROOT, "raw", "rosettacode", "manifest.tsv")
LANG_MAN = os.path.join(ROOT, "raw", "rosettacode", "lang_manifest.tsv")
SRC = os.path.join(ROOT, "wiki", "sources")

SECTION_MARKER = "## Solved in (Rosetta Code languages)"


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


def lang_sections(title):
    d = api({"action": "parse", "page": title, "prop": "sections", "format": "json"})
    return [s["line"] for s in d["parse"]["sections"] if s.get("toclevel") == 1]


def load_lang_map():
    """heading-name -> language page-name (filename stem). Keyed by category and display."""
    m = {}
    with open(LANG_MAN) as f:
        next(f)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            cat, disp, page = (parts + ["", "", ""])[:3]
            if cat:
                m[cat] = page
            if disp:
                m.setdefault(disp, page)
    return m


def task_rows():
    rows = []
    with open(TASK_MAN) as f:
        next(f)
        for line in f:
            if line.strip():
                t, s = line.rstrip("\n").split("\t")
                rows.append((t, s))
    return rows


def build_section(title, langmap):
    headings = lang_sections(title)
    pages, unknown = [], 0
    for h in headings:
        if h in langmap:
            pages.append(langmap[h])
        else:
            unknown += 1
    pages = sorted(set(pages), key=str.lower)
    links = ", ".join(f"[[{p}]]" for p in pages) if pages else "_none in the wiki's language set_"
    note = f" ({unknown} further RC language section(s) are outside the wiki's popularity-list language set.)" if unknown else ""
    return (f"{SECTION_MARKER}\n"
            f"Solved in **{len(pages)}** of the wiki's catalogued languages (Rosetta Code shows "
            f"{len(headings)} language sections for this task).{note}\n\n{links}\n")


def upsert(path, section):
    txt = open(path, encoding="utf-8").read()
    if SECTION_MARKER in txt:
        txt = re.sub(rf"{re.escape(SECTION_MARKER)}.*?(?=\n## |\Z)", section, txt, count=1, flags=re.S)
    elif "## Contradictions" in txt:
        txt = txt.replace("## Contradictions", section + "\n## Contradictions", 1)
    else:
        txt = txt.rstrip() + "\n\n" + section
    open(path, "w", encoding="utf-8").write(txt)


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "1"
    rows = task_rows()
    langmap = load_lang_map()
    limit = None if arg == "all" else int(arg)
    processed = 0
    for title, slug in rows:
        if limit is not None and processed >= limit:
            break
        path = os.path.join(SRC, slug + ".md")
        if not os.path.exists(path):
            continue
        if SECTION_MARKER in open(path, encoding="utf-8").read():
            continue  # already linked; skip (idempotent)
        section = build_section(title, langmap)
        upsert(path, section)
        processed += 1
        print(f"[{processed}] {slug}  <- {title}")
    print(f"DONE: linked {processed} task page(s)")


if __name__ == "__main__":
    main()
