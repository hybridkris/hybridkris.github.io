#!/usr/bin/env python3
"""Build index.html for krisrockwell.io, the experiments hub.

Entries live in entries.json so adding an experiment is a data edit, not a
markup edit. Deterministic: no build date, no clock -- rerunning reproduces the
file byte-for-byte.
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

entries = json.load(open(os.path.join(ROOT, "entries.json")))
TPL = open(os.path.join(ROOT, "scripts", "site_template.html")).read()
TOKENS = open(os.path.join(ROOT, "scripts", "tokens.css")).read()


def esc(s):
    return html.escape(s).encode("ascii", "xmlcharrefreplace").decode("ascii")


blocks = []
for e in entries:
    meta = " <span class=\"dot\">&middot;</span> ".join(esc(m) for m in e.get("meta", []))
    blocks.append(
        f'<a class="entry" href="/{e["repo"]}/">'
        f'<h2>{esc(e["title"])}</h2>'
        f'<span class="path">/{esc(e["repo"])}/</span>'
        f'<p>{esc(e["blurb"])}</p>'
        + (f'<span class="meta">{meta}</span>' if meta else "")
        + '</a>')

out = TPL.replace("/*TOKENS*/", TOKENS).replace("<!--ENTRIES-->", "\n".join(blocks))

for marker in ("/*TOKENS*/", "<!--ENTRIES-->"):
    assert marker not in out, f"unfilled placeholder {marker}"
non_ascii = sorted({c for c in out if ord(c) > 127})
assert not non_ascii, f"non-ASCII characters present: {non_ascii}"

path = os.path.join(ROOT, "index.html")
open(path, "w").write(out)
print(f"wrote {path}  {len(out)} bytes  ({len(entries)} entries)")
