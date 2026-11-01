# AKR Operations lead machine

Phase 0 build of the Scout, Audit and QA agents from `docs/build-list.md`, using the locked decisions in `docs/decision-log.md`. Stdlib Python only.

```
python3 -m akr run --input data/sample_prospects.csv --out out --date 2026-12-01
python3 -m unittest discover -s tests
```

Pipeline: scraped CSV -> competitor benchmark (top 3 in market and trade) -> ICP score and disqualifiers (ET/CT beachhead, rating, headcount, PE, owner access) -> one page HTML audit and cold email draft -> QA gate (gating, incentives, guarantees, naming lock, confidential terms, unresolved placeholders, CAN-SPAM).

Outputs in `out/`: `scored.csv`, `audits/`, `emails/`, `qa_report.csv`.

Rules: unknown data is flagged "not verified" in the audit, never guessed. Cold email is blocked until `AKR_POSTAL_ADDRESS` is set and the audit URL is resolved. `data/sample_prospects.csv` is synthetic.

Not built here (needs accounts, keys or your decisions): Outscraper pull, GHL, Smartlead, Stripe, secondary domains, dashboards.
