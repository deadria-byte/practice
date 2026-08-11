# Runbook — How to Run the Content/Offer Pipeline

This file tells Claude Code how to run the four specialist agents in order. You never need to open this file to use the system — just tell Claude what you want (see "How to ask for it" below) and Claude follows these steps.

## The order, and what passes between steps

1. **Market Signal Researcher** — Input: a topic or content pillar (e.g. "Customer Service and Recovery"). Output: verdict on whether real demand exists, plus evidence.
   - If the verdict is "no signal found," stop here and report that back instead of continuing — do not force the pipeline forward on a topic with no evidence.
2. **Offer Architect** — Input: the Market Signal Researcher's findings. Output: one specific, sellable offer tied to the Pro tier.
3. **Content Angle Strategist** — Input: the Offer Architect's offer. Output: 5 ranked content angles/hooks.
4. **Conversion System Builder** — Input: the offer plus the strongest angle (or whichever angle you pick). Output: the exact next-step mechanism after someone engages.

## What Claude does at the end
After all four steps finish, Claude compiles the results into a single file and saves it to `outputs/`, named `YYYY-MM-DD-<topic-slug>.md` (for example `outputs/2026-08-10-food-cost-and-inventory.md`). The compiled file includes all four sections in order: Market Signal → Offer → Content Angles → Conversion System.

Nothing gets published, sent, or spent automatically at any step. The output is a draft for you to read and approve.

## How to ask for it
Just tell Claude, in your own words, something like:
- "Run the pipeline on Labor and Staffing."
- "Do the full content/offer workflow for the AI Business Operations pillar."

Claude will call each agent in order using the Agent tool, feed each one's output into the next, and hand you back the finished file's location when done.

## Rules this runbook enforces
- One topic per run. Don't mix pillars in a single pass — run the pipeline again for the next one.
- Every agent reads `business-brief.md` for shared context; don't skip that step even if it seems redundant.
- If any agent flags a problem (weak signal, vague offer, missing infrastructure), stop and surface it rather than pushing a weak result through the remaining steps.
- Respect the non-negotiables from `business-brief.md` at every step — especially: Basic tier never appears, inbound before outbound, no new channels after Week 18.
