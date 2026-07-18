r"""
Build the GitHub repository for the AIGC systematic review references.

This script generates ONLY the bibliographic metadata files.
PDFs are NOT copied into the repository -- the full-text PDFs are
submitted to the journal as supplementary material (per the supervisor's
instruction), and the GitHub repo only hosts the public reference list.

Inputs (under ROOT, edit ROOT below for your local layout):
  - References.html          (Zotero CSL export, 68 entries)

Outputs (into github_repo\):
  - References.html          (original Zotero export, preserved)
  - references.md            (68 entries, each with DOI link)
  - references.csv           (tabular, for editors who prefer Excel)

Usage:
    1) Edit ROOT below to point at your local working directory.
    2) `python build_repo.py`
"""

import csv
import re
import sys
from html import unescape
from pathlib import Path
from typing import List, Dict

# -------- paths (edit ROOT for your machine) --------
ROOT = Path(r"E:\Edu\AAA_SSPU\AIGC综述\最终修改")
SRC_HTML = ROOT / "References.html"
OUT = ROOT / "github_repo"
OUT.mkdir(parents=True, exist_ok=True)


# -------- 1. parse References.html --------
def parse_entries(html: str) -> List[Dict]:
    r"""Extract 68 <div class="csl-entry"> entries from the Zotero export."""
    entry_re = re.compile(r'<div class="csl-entry">(.*?)</div>', re.DOTALL)
    raw = entry_re.findall(html)
    if len(raw) != 68:
        print(f"WARNING: expected 68 csl-entry divs, got {len(raw)}", file=sys.stderr)

    parsed = []
    for i, r in enumerate(raw, 1):
        # plain text (for human display)
        plain = re.sub(r"<[^>]+>", "", unescape(r))
        plain = re.sub(r"\s+", " ", plain).strip()

        # first-author last name
        head = plain.split(" (")[0]
        for sep in [" 和 ", " and ", " & "]:
            if sep in head:
                head = head.split(sep)[0]
                break
        first = re.split(r"[\s\u3000]+", head.strip(), maxsplit=1)[0]
        if "和" in first:
            first = first.split("和", 1)[0]
        first_author = first.rstrip(",").strip()
        first_author = re.sub(r"[\\/:*?\"<>|]", "_", first_author)

        # year
        ym = re.search(r"\((\d{4})\)", plain)
        year = ym.group(1) if ym else "n.d."

        # DOI URL
        dm = re.search(r'href="(https?://doi\.org/[^"]+)"', r)
        doi_url = dm.group(1) if dm else ""

        parsed.append(
            dict(
                idx=i,
                first_author=first_author,
                year=year,
                doi_url=doi_url,
                plain=plain,
            )
        )
    return parsed


# -------- 2. emit references.md / references.csv --------
def emit_md(entries: List[Dict]) -> str:
    lines: List[str] = []
    lines.append("# References (68 entries)\n")
    lines.append(
        "This list mirrors the reference list in the submitted manuscript. "
        "Each entry links to its DOI on the publisher's website. Full-text PDFs "
        "are **not** stored in this repository -- they are submitted to the journal "
        "as supplementary material.\n"
    )
    lines.append("\n---\n")
    for e in entries:
        doi_md = f" [[DOI]({e['doi_url']})]" if e["doi_url"] else ""
        lines.append(f"{e['idx']}. {e['plain']}{doi_md}")
    lines.append("")
    return "\n".join(lines)


def emit_csv(entries: List[Dict]) -> str:
    out_rows = [["No.", "First Author", "Year", "Full Reference", "DOI URL"]]
    for e in entries:
        out_rows.append(
            [
                str(e["idx"]),
                e["first_author"],
                e["year"],
                e["plain"],
                e["doi_url"],
            ]
        )
    from io import StringIO

    buf = StringIO()
    w = csv.writer(buf)
    w.writerows(out_rows)
    return buf.getvalue()


# -------- main --------
def main():
    html = SRC_HTML.read_text(encoding="utf-8")
    entries = parse_entries(html)
    print(f"Parsed {len(entries)} entries from References.html")

    # emit files
    (OUT / "References.html").write_text(html, encoding="utf-8")
    (OUT / "references.md").write_text(emit_md(entries), encoding="utf-8")
    (OUT / "references.csv").write_text(emit_csv(entries), encoding="utf-8-sig")

    print(f"Wrote {OUT / 'references.md'} and {OUT / 'references.csv'}")
    print("No PDFs were copied (PDFs go to journal supplementary material only).")


if __name__ == "__main__":
    main()
