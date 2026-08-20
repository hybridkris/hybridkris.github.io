# krisrockwell.io

The experiments hub. This repo is the GitHub **user site** for `hybridkris`, which is
why it must keep the name `hybridkris.github.io`, and it holds the `CNAME` for
`krisrockwell.io`.

Because the custom domain sits on the user site, every other repository with Pages
enabled is automatically served beneath it at `krisrockwell.io/<repo>/` — no CNAME in
the project repo, no DNS record, no certificate per experiment.

## Adding an experiment

1. Enable Pages on that repository (source: `main`, path: `/`).
2. Add an entry to `entries.json`.
3. `python3 scripts/build_site.py`, then commit.

`entries.json` is the only file to edit for content — the markup is generated.

## Promotion to a subdomain

Work that earns a separate identity gets `<name>.krisrockwell.io` instead: add a
`CNAME` file to that repo and a DNS `CNAME` record pointing at `hybridkris.github.io`.
This is the pattern already used by `cfp.krisrockwell.org` and
`conscientia.krisrockwell.org`. It is a deliberate promotion, not the default — each
subdomain costs a DNS record and its own certificate.

## Design

`scripts/tokens.css` holds the shared tokens: Univers Next Pro Heavy Condensed for
headings, Plantin for running text, OCR B for labels and figures. All three are
commercial Monotype faces and are **not bundled** — each stack names the real face
first and falls back if it is absent.

The same token file is used by the experiment sites, so the collection reads as one
body of work. It is duplicated rather than shared, because Pages cannot pull a file
across repositories; keep the copies in step when changing either.

## Note on visibility

A Pages site built from a **private** repository is still served **publicly**. Decide
visibility per experiment deliberately — publishing here puts the repo contents on the
open web regardless of the repo's own setting.

## Analytics

These pages carry the Google Analytics (GA4) tag `G-48RJDXZTPJ`. It is the one
external request they make, and the one thing here not served from this repo.
Everything else -- CSS, fonts, figures -- is still inlined.
