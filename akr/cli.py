"""python -m akr run --input data/sample_prospects.csv --out out"""
import argparse, csv, os, re
from . import audit, benchmark, config, qa, scoring
from .models import load_prospects


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def run(input_path, out_dir, as_of=None, postal=None, audit_url_base=""):
    postal = config.POSTAL_ADDRESS if postal is None else postal
    pool = load_prospects(input_path)
    for sub in ("audits", "emails"):
        os.makedirs(os.path.join(out_dir, sub), exist_ok=True)
    for p in pool:
        scoring.score(p, benchmark.build(p, pool))
    ranked = sorted(pool, key=lambda p: -p.score)
    with open(os.path.join(out_dir, "scored.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["place_id", "name", "market", "tier", "score", "disqualifiers", "unverified", "reasons"])
        for p in ranked:
            w.writerow([p.place_id, p.name, p.market, p.tier, p.score, "; ".join(p.disqualifiers),
                        "; ".join(p.unverified), "; ".join(p.reasons)])
    qa_rows, sendable = [], 0
    for p in ranked:
        if p.tier not in ("A", "B"):
            continue
        b = benchmark.build(p, pool)
        s = slug(p.name)
        html = audit.audit_html(p, b, as_of)
        with open(os.path.join(out_dir, "audits", s + ".html"), "w") as fh:
            fh.write(html)
        url = f"{audit_url_base}/{s}.html" if audit_url_base else "{{AUDIT_URL}}"
        mail = audit.email_text(p, b, config.SENDER_NAME, postal or "{{POSTAL_ADDRESS}}", url)
        with open(os.path.join(out_dir, "emails", s + ".txt"), "w") as fh:
            fh.write(mail)
        found = qa.check(mail, "cold_email", postal) + qa.check(html)
        sendable += not found
        qa_rows.append([p.name, "BLOCK" if found else "PASS",
                        "; ".join(f"{f.rule}: {f.excerpt}" for f in found)])
    with open(os.path.join(out_dir, "qa_report.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["name", "verdict", "findings"])
        w.writerows(qa_rows)
    tiers = {t: sum(p.tier == t for p in pool) for t in ("A", "B", "C", "DQ")}
    return {"total": len(pool), "tiers": tiers, "audited": len(qa_rows), "sendable": sendable}


def main():
    ap = argparse.ArgumentParser(prog="akr")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--input", required=True)
    r.add_argument("--out", default="out")
    r.add_argument("--date")
    r.add_argument("--audit-url-base", default="")
    a = ap.parse_args()
    print(run(a.input, a.out, a.date, audit_url_base=a.audit_url_base))


if __name__ == "__main__":
    main()
