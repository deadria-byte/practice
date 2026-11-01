"""Budget report: pre-revenue spend (capped) and operating expense, tracked separately.

Ledger CSV columns: date,item,amount,status,bucket
  status: planned | paid     bucket: pre_revenue | operating (blank = auto)
Auto rule: dated on or after the first setup fee date -> operating, else pre_revenue.
"""
import csv
from . import config


def report(path, first_setup_fee_date=None):
    out = {"pre_revenue": {"paid": 0.0, "planned": 0.0}, "operating": {"paid": 0.0, "planned": 0.0}}
    with open(path, newline="") as fh:
        for r in csv.DictReader(fh):
            b = (r.get("bucket") or "").strip()
            if not b:
                b = "operating" if first_setup_fee_date and r["date"] >= first_setup_fee_date else "pre_revenue"
            out[b][r["status"].strip()] += float(r["amount"])
    pre = out["pre_revenue"]
    out["cap"] = config.PRE_REVENUE_CAP
    out["pre_revenue_remaining_if_all_planned_paid"] = config.PRE_REVENUE_CAP - pre["paid"] - pre["planned"]
    out["over_cap"] = pre["paid"] + pre["planned"] > config.PRE_REVENUE_CAP
    return out
