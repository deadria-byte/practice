import csv
from dataclasses import dataclass, field
from typing import Optional


def _int(v):
    v = (v or "").strip()
    return int(float(v)) if v else None


def _float(v):
    v = (v or "").strip()
    return float(v) if v else None


def _bool(v):
    v = (v or "").strip().lower()
    if v in ("1", "true", "yes", "y"):
        return True
    if v in ("0", "false", "no", "n"):
        return False
    return None  # unknown stays unknown, never guessed


@dataclass
class Prospect:
    place_id: str
    name: str
    city: str
    state: str
    trade: str  # hvac | plumbing | both
    rating: Optional[float] = None
    review_count: Optional[int] = None
    reviews_last_90d: Optional[int] = None
    response_rate: Optional[float] = None  # share of reviews answered, 0..1
    unanswered_negatives: Optional[int] = None
    employees_est: Optional[int] = None
    locations: Optional[int] = None
    fleet_signal: Optional[bool] = None
    fsm: str = ""  # servicetitan | jobber | housecallpro | fieldedge | none | blank
    module_active: Optional[bool] = None  # is their built-in review module in use
    has_agency: Optional[bool] = None
    pe_or_franchise: Optional[bool] = None
    pe_rival_in_market: Optional[bool] = None
    residential: Optional[bool] = None
    owner_reachable: Optional[bool] = None
    owner_name: str = ""
    email: str = ""
    website: str = ""
    phone: str = ""
    # filled by the pipeline
    score: int = 0
    tier: str = ""
    reasons: list = field(default_factory=list)
    disqualifiers: list = field(default_factory=list)
    unverified: list = field(default_factory=list)

    @property
    def trades(self):
        return {"hvac", "plumbing"} if self.trade == "both" else {self.trade}

    @property
    def market(self):
        return f"{self.city}, {self.state}"


def load_prospects(path):
    out = []
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            out.append(Prospect(
                place_id=r["place_id"].strip(), name=r["name"].strip(),
                city=r["city"].strip(), state=r["state"].strip().upper(),
                trade=r["trade"].strip().lower(),
                rating=_float(r.get("rating")), review_count=_int(r.get("review_count")),
                reviews_last_90d=_int(r.get("reviews_last_90d")),
                response_rate=_float(r.get("response_rate")),
                unanswered_negatives=_int(r.get("unanswered_negatives")),
                employees_est=_int(r.get("employees_est")), locations=_int(r.get("locations")),
                fleet_signal=_bool(r.get("fleet_signal")),
                fsm=(r.get("fsm") or "").strip().lower(),
                module_active=_bool(r.get("module_active")),
                has_agency=_bool(r.get("has_agency")),
                pe_or_franchise=_bool(r.get("pe_or_franchise")),
                pe_rival_in_market=_bool(r.get("pe_rival_in_market")),
                residential=_bool(r.get("residential")),
                owner_reachable=_bool(r.get("owner_reachable")),
                owner_name=(r.get("owner_name") or "").strip(),
                email=(r.get("email") or "").strip(),
                website=(r.get("website") or "").strip(),
                phone=(r.get("phone") or "").strip(),
            ))
    return out
