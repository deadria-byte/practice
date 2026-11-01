import os, tempfile, unittest
from akr import benchmark, qa, scoring
from akr.cli import run
from akr.models import load_prospects

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "sample_prospects.csv")


class T(unittest.TestCase):
    def setUp(self):
        self.pool = load_prospects(DATA)
        self.by = {p.place_id: p for p in self.pool}

    def score(self, pid):
        p = self.by[pid]
        return scoring.score(p, benchmark.build(p, self.pool))

    def test_benchmark_top3_excludes_self(self):
        b = benchmark.build(self.by["c1"], self.pool)
        self.assertEqual([c.place_id for c in b.competitors], ["c2", "c3", "c4"])
        self.assertGreater(b.velocity_ratio, 1.5)

    def test_priority_prospect_is_tier_a(self):
        p = self.score("c1")
        self.assertEqual(p.tier, "A", p.reasons)

    def test_disqualifiers(self):
        self.assertIn("rating under 3.7 (fix operations first)", self.score("d1").disqualifiers)
        self.assertIn("outside ET/CT beachhead", self.score("p1").disqualifiers)
        self.assertEqual(self.score("p1").score, 0)

    def test_agency_shop_scores_lower(self):
        self.assertLess(self.score("c2").score, self.score("c1").score)

    def test_qa_blocks_bad_copy(self):
        for bad in ("We offer reputation management", "get a gift card for a review",
                    "We guarantee 50 reviews", "Hi {{name}}", "only ask happy customers"):
            self.assertTrue(qa.check(bad), bad)
        self.assertFalse(qa.check("Plain note about your reviews."))

    def test_cold_email_needs_address_and_unsubscribe(self):
        r = qa.check("hello", "cold_email", "1 Main St")
        self.assertEqual({f.rule for f in r}, {"CAN-SPAM"})

    def test_pipeline_blocks_without_postal_address_then_passes(self):
        with tempfile.TemporaryDirectory() as d:
            res = run(DATA, d, "2026-12-01", postal="")
            self.assertGreater(res["audited"], 0)
            self.assertEqual(res["sendable"], 0)
        with tempfile.TemporaryDirectory() as d:
            res = run(DATA, d, "2026-12-01", postal="1 Main St, Louisville, KY 40202", audit_url_base="https://example.test/a")
            self.assertEqual(res["sendable"], res["audited"])


if __name__ == "__main__":
    unittest.main()
