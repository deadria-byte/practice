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

# CAN-SPAM postal address (AKR Mint Hill business address, set by DeAdria 2026-11-01).
POSTAL_ADDRESS = os.environ.get(
    "AKR_POSTAL_ADDRESS",
    "AKR Operations, 11300 Lawyers Rd J #2022, Mint Hill, NC 28227")

TIER_A, TIER_B = 70, 50

# Mountain-time slivers of otherwise ET/CT states, excluded by ZIP prefix when a
# zip column is present. Far west Texas (El Paso, Hudspeth). Other slivers
# (western KS, NE, ND, SD) are small and can be added here as needed.
MOUNTAIN_ZIP_PREFIXES = {"TX": ("799", "885")}

# Budget: the cap covers pre-revenue spend only. Once the first setup fee
# lands, costs are operating expense and tracked separately.
PRE_REVENUE_CAP = 1000
