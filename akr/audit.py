"""Audit Agent: one-page HTML audit and cold email draft per prospect."""
from html import escape
from datetime import date

CSS = """body{font:16px/1.5 system-ui,sans-serif;max-width:760px;margin:2rem auto;padding:0 16px;color:#1b1f23;background:#fff}
h1{font-size:1.5rem;margin:0}.sub{color:#555;margin:.25rem 0 1.5rem}table{border-collapse:collapse;width:100%}
th,td{padding:.5rem;border-bottom:1px solid #ddd;text-align:left}th{font-size:.85rem;color:#555}
tr.you td{font-weight:600;background:#f3f6fa}.flag{background:#fff6e0;padding:.5rem .75rem;border-radius:6px}
footer{margin-top:2rem;font-size:.85rem;color:#666}@media(prefers-color-scheme:dark){body{background:#14171a;color:#e6e8ea}
th,td{border-color:#333}tr.you td{background:#1e252c}.flag{background:#3a3220}.sub,th,footer{color:#9aa}}"""


def _v(x, fmt="{}"):
    return "not verified" if x is None else fmt.format(x)


def _row(p, you=False):
    rr = None if p.response_rate is None else round(p.response_rate * 100)
    return (f'<tr class="{"you" if you else ""}"><td>{escape(p.name)}</td><td>{_v(p.rating)}</td>'
            f'<td>{_v(p.review_count)}</td><td>{_v(p.reviews_last_90d)}</td>'
            f'<td>{_v(rr, "{}%")}</td></tr>')


def gap_line(p, b):
    if b.avg_velocity is None or p.reviews_last_90d is None:
        return "We could not verify recent review pace for this comparison."
    return (f"Over the last 90 days, {escape(p.name)} added {p.reviews_last_90d} reviews. "
            f"The three shops Google shows next to you averaged {b.avg_velocity:.0f}.")


def audit_html(p, b, as_of=None):
    as_of = as_of or date.today().isoformat()
    flags = list(p.unverified)
    if b.note:
        flags.append(b.note)
    neg = p.unanswered_negatives
    checks = [
        "Whether your review request fires on every completed job, not just some.",
        "Who answers new reviews, and how fast." if (neg or 0) else "Response time on new reviews.",
        "What your Google profile shows a stranger searching at 9pm with a dead AC or a burst pipe.",
    ]
    body = [f"<h1>{escape(p.name)}: Google profile audit</h1>",
            f'<p class="sub">{escape(p.market)} &middot; public data as of {as_of}</p>',
            "<table><tr><th>Business</th><th>Rating</th><th>Reviews</th><th>Last 90 days</th><th>Answered</th></tr>",
            _row(p, True), *[_row(c) for c in b.competitors], "</table>",
            f"<p>{gap_line(p, b)}</p>"]
    if neg:
        body.append(f"<p>{neg} negative review(s) still have no response.</p>")
    if p.fsm in ("servicetitan", "jobber", "housecallpro") and p.module_active is False:
        body.append("<p>Your field software includes review tools that do not appear to be in use.</p>")
    body += ["<h2>What we would look at first</h2><ul>",
             *[f"<li>{escape(c)}</li>" for c in checks], "</ul>"]
    if flags:
        body.append('<p class="flag">Not verified: ' + escape(", ".join(flags)) + "</p>")
    body.append("<footer>Prepared by AKR Operations from public listings. No results are promised or implied.</footer>")
    return (f"<!doctype html><html lang=en><meta charset=utf-8>"
            f"<meta name=viewport content='width=device-width,initial-scale=1'>"
            f"<title>{escape(p.name)} Google Audit</title><style>{CSS}</style>"
            f"<body>{''.join(body)}</body></html>")


def email_text(p, b, sender, postal_address, audit_url="{{AUDIT_URL}}"):
    first = p.owner_name.split()[0] if p.owner_name else "there"
    comp = b.competitors[0].name if b.competitors else "the shops ahead of you"
    return (f"Subject: Your Google reviews vs {comp}\n\n"
            f"Hi {first},\n\n"
            f"I pulled public numbers for {p.name} next to the three shops Google shows around you. "
            f"{gap_line(p, b)}\n\n"
            f"The one page comparison is here: {audit_url}\n\n"
            f"If it is useful, I can walk through it in 20 minutes.\n\n"
            f"{sender}\nAKR Operations\n\n"
            f"{postal_address}\nReply unsubscribe and I will not email again.\n")
