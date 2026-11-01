"""Scout Agent: ICP filter and fit score (max 100). Unknowns are flagged, never guessed."""
from . import config

DORMANT_FSMS = {"servicetitan", "jobber", "housecallpro"}


def employees(p):
    if p.employees_est is not None:
        return p.employees_est
    if p.fleet_signal and (p.review_count or 0) >= 75:
        return 10  # proxy only, flagged as unverified by the caller
    return None


def disqualify(p):
    d = []
    if p.state not in config.BEACHHEAD_STATES:
        d.append("outside ET/CT beachhead")
    if p.rating is not None and p.rating < 3.7:
        d.append("rating under 3.7 (fix operations first)")
    e = employees(p)
    if e is not None and e < 5:
        d.append("under 5 employees")
    if p.residential is False:
        d.append("commercial or new construction only")
    if p.pe_or_franchise:
        d.append("PE platform branch or franchise")
    if p.owner_reachable is False:
        d.append("owner not reachable")
    if p.locations is not None and p.locations > 3:
        d.append("more than 3 locations")
    return d


def score(p, bench):
    p.disqualifiers = disqualify(p)
    p.reasons, p.unverified = [], []
    if p.disqualifiers:
        p.score, p.tier = 0, "DQ"
        return p
    pts = 0

    def add(n, why):
        nonlocal pts
        pts += n
        p.reasons.append(f"+{n} {why}")

    rc = p.review_count
    if rc is None:
        p.unverified.append("review_count")
    elif 50 <= rc <= 500:
        add(15, "review volume in 50 to 500 band")
    elif rc > 500:
        add(8, "over 500 reviews, less headroom")
    elif rc >= 20:
        add(7, "20 to 49 reviews")

    r = p.rating
    if r is None:
        p.unverified.append("rating")
    elif 3.8 <= r <= 4.5:
        add(15, "rating 3.8 to 4.5, winnable")
    elif r < 3.8 or r <= 4.7:
        add(8, "rating at the edge of the target band")
    else:
        add(3, "rating above 4.7, little headroom")

    if p.reviews_last_90d is None:
        p.unverified.append("reviews_last_90d")
    elif p.reviews_last_90d > 0:
        add(10, "active in the last 90 days")

    if bench.velocity_ratio >= 1.5:
        add(20, f"competitors collect {bench.velocity_ratio:.1f}x the new reviews")
    elif bench.velocity_ratio >= 1.0:
        add(10, "slightly behind competitor velocity")
    elif bench.avg_velocity is None:
        p.unverified.append("competitor velocity")

    e = employees(p)
    if p.employees_est is None:
        p.unverified.append("employees_est")
    if e is None:
        add(5, "headcount unknown")
    elif 10 <= e <= 30:
        add(15, "10 to 30 employees")
    elif 31 <= e <= 50:
        add(10, "31 to 50 employees")
    elif e < 10:
        add(4, "5 to 9 employees")

    seg = 0
    if p.fsm == "fieldedge":
        seg, why = 15, "FieldEdge shop, no native review product"
    elif p.fsm in DORMANT_FSMS and p.module_active is False:
        seg, why = 15, f"{p.fsm} review module dormant"
    elif p.pe_rival_in_market and p.has_agency is not True:
        seg, why = 10, "independent facing a PE rival"
    if seg:
        add(seg, why)
    if p.fsm in ("", None):
        p.unverified.append("fsm")

    if p.has_agency is False:
        add(5, "no agency")
    elif p.has_agency is None:
        p.unverified.append("has_agency")

    if p.trade in ("plumbing", "both"):
        add(5, "plumbing weighted")
    else:
        add(2, "hvac only")

    p.score = pts
    p.tier = "A" if pts >= config.TIER_A else "B" if pts >= config.TIER_B else "C"
    return p
