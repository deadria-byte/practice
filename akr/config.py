"""Locked decisions from docs/decision-log.md, kept in one place."""
import os

BRAND = "AKR Operations"
SENDER_NAME = "Robert Davis"  # decision 6: outreach goes out under Robert's name
OFFER_PRICE = {"setup": 995, "monthly": 497}  # decision 2: no pilot pricing

# Decision 16: beachhead is ET/CT only (simplified by state; split states
# such as KY, TN, IN, MI, FL, TX are placed by where most of the state sits).
EASTERN = {"CT", "DE", "DC", "FL", "GA", "IN", "KY", "ME", "MD", "MA", "MI",
           "NH", "NJ", "NY", "NC", "OH", "PA", "RI", "SC", "VT", "VA", "WV"}
CENTRAL = {"AL", "AR", "IL", "IA", "KS", "LA", "MN", "MS", "MO", "NE", "ND",
           "OK", "SD", "TN", "TX", "WI"}
BEACHHEAD_STATES = EASTERN | CENTRAL

# CAN-SPAM postal address. Left unset on purpose: the QA gate blocks any
# cold email until this is provided.
POSTAL_ADDRESS = os.environ.get("AKR_POSTAL_ADDRESS", "")

TIER_A, TIER_B = 70, 50
