"""Competitor benchmark: the top 3 in-market competitors per prospect."""
from dataclasses import dataclass
from statistics import mean


@dataclass
class Benchmark:
    competitors: list
    avg_velocity: float = None
    velocity_ratio: float = 0.0  # competitor avg / prospect (higher = further behind)
    note: str = ""


def build(prospect, pool):
    """Top 3 by review count in the same city, state and trade."""
    comps = [p for p in pool
             if p.place_id != prospect.place_id
             and p.market == prospect.market
             and p.trades & prospect.trades
             and p.review_count is not None]
    comps.sort(key=lambda p: p.review_count, reverse=True)
    comps = comps[:3]
    b = Benchmark(competitors=comps)
    vel = [c.reviews_last_90d for c in comps if c.reviews_last_90d is not None]
    if len(comps) < 3:
        b.note = f"Only {len(comps)} comparable competitor(s) found in {prospect.market}."
    if vel and prospect.reviews_last_90d is not None:
        b.avg_velocity = mean(vel)
        b.velocity_ratio = b.avg_velocity / max(prospect.reviews_last_90d, 1)
    return b
