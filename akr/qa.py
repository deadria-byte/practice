"""QA / Compliance Agent: pre-send checker with blocking authority."""
import re
from dataclasses import dataclass

RULES = [
    ("gating", r"only ask (your )?(happy|satisfied)|happy customers only|filter(ing)? (out )?negative|review gating"),
    ("incentive", r"gift card|(discount|coupon|free \w+) (for|in exchange for) (a |an |your )?review|in exchange for (a |an |your )?review"),
    ("fake or removal", r"fake review|buy(ing)? reviews|remove (your |the )?(bad|negative) reviews|delete (your |the )?negative"),
    ("guarantee", r"\bguarantee[sd]?\b"),
    ("naming lock", r"reputation management"),
    ("confidential", r"charter communications|merger"),
    ("placeholder", r"\{\{[^}]*\}\}|\[\[[^\]]*\]\]|\bTODO\b"),
]


@dataclass
class Finding:
    rule: str
    excerpt: str


def check(text, kind="general", postal_address=""):
    """Return findings. Any finding blocks the send."""
    out = []
    for rule, pat in RULES:
        for m in re.finditer(pat, text, re.IGNORECASE):
            out.append(Finding(rule, m.group(0)))
    if kind == "cold_email":
        if "unsubscribe" not in text.lower():
            out.append(Finding("CAN-SPAM", "missing unsubscribe line"))
        if not postal_address or postal_address not in text:
            out.append(Finding("CAN-SPAM", "missing postal address"))
    return out
