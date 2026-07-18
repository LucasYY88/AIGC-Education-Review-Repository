# Data Availability — AIGC in Education: A Systematic Review

This repository supports the manuscript submitted to *Humanities and Social Sciences Communications*:

> **AIGC in education: a systematic review of applications, challenges and pathways**
> [Ye Zhang], [Shuo Zhang], & [Xinrong Chen]

It contains the bibliographic metadata (reference list) for all 68 peer-reviewed studies included in the systematic review. The full-text PDFs of these 68 studies are **not** stored here — they are submitted to the journal as supplementary material so that the editorial office can verify the included studies.

---

## 📚 Quick links

| What you want | Where to go |
| --- | --- |
| Read the reference list online | [`references.md`](./references.md) |
| Open it in Excel / a spreadsheet | [`references.csv`](./references.csv) |
| See the original Zotero export | [`References.html`](./References.html) |

For the full-text PDFs, please refer to the journal's supplementary material associated with the submitted manuscript.

---

## 📂 Repository contents

```
.
├── README.md              ← this file
├── references.md          ← 68 entries, each linked to its DOI on the publisher's website
├── references.csv         ← same 68 entries in spreadsheet form (UTF-8 BOM)
├── References.html        ← original Zotero "Better CSL" export
├── scripts/               ← build script (regenerates the reference list)
│   └── build_repo.py
└── LICENSE                ← CC BY 4.0
```

The 68 entries are numbered in the same order as the reference list in the submitted manuscript.

---

## 🧭 How reviewers can use this repository

1. **Browse or search** the reference list in `references.md`. Every entry has a clickable link to the publisher's DOI page.
2. **Open in a spreadsheet** via `references.csv` (Excel, Numbers, Google Sheets — all open UTF-8 BOM files correctly).
3. **Re-import into Zotero** by opening `References.html` (Zotero imports the COinS metadata embedded in the file).

For access to the full-text PDFs, please use the journal's supplementary material.

---

## 🔁 Reproducibility

- The reference list (`references.md` / `references.csv`) is generated from the Zotero export `References.html` by [`scripts/build_repo.py`](./scripts/build_repo.py). Edit the `ROOT` path at the top of that script and re-run it to regenerate everything.
- DOIs are preserved verbatim from the original Zotero entries; clicking the *DOI* link in `references.md` takes the reader to the publisher's landing page for that article.

---

## 📄 License

The reference list and the structure of this repository are released under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)** — see [`LICENSE`](./LICENSE).

The full-text PDFs of the included studies are **not** part of this repository. Copyright of each individual article remains with its original publisher. Please consult each publisher's policy before redistributing or reusing any article.

---

## ✉️ Contact

For questions about this repository, please contact the corresponding author: *yezhang@sspu.edu.cn*.
