# AKR Operations — Full Build List (SKELETON, 2026-11-01)
Purpose: everything that must exist to execute the HVAC & plumbing reputation business, automation-first. DeAdria's stated build team: Claude Code (builds/runs systems) + Claude (coordination, drafting, analysis) + Muse/Harry (planning, tracking, accountability) + GHL & off-shelf tools where building is wasteful.
Legend: [CC] Claude Code build · [CFG] configure off-shelf · [DOC] write once · [HUMAN] stays human
Phase: 0 = before first outreach · 1 = pilot phase · 2 = scale (10+ clients)

## A. Foundation (legal/admin/finance plumbing)
0 [DOC] Service agreement (compliance, GBP access, no results guarantee, client owns assets)
0 [CFG] Insurance (GL + E&O), business bank/Stripe ACH-first billing setup
0 [DOC] Compliance rulebook (no gating, no incentives, no fake reviews, SMS consent/A2P, CAN-SPAM, Google policy)
0 [CFG] Domains: main brand domain + 6-10 secondary outreach domains (never send cold from main)

## B. Brand & voice system
0 [DOC] Brand voice guide (trade-plain, operator-to-operator, no agency-speak; do/don't phrases)
0 [DOC] Message house: core promise, 3 proof angles (emergency-call moment, PE-rival fight, exit value), objection answers
0 [CFG] Logo/brand kit, email signatures, social profiles
0 [DOC] Naming/tagline lock for the offer ("review engine + CX operations," never "reputation management")

## C. Marketing assets
0 [CC/CFG] Website: home (offer), audit landing page, booking page, sample scoreboard page
0 [CC] Sample/free audit template (the lead magnet — prospect vs 3 named competitors)
1 [DOC] Case-study template (filled by pilots), testimonial capture flow
1 [DOC] Robert intro video + sample client scoreboard (proof assets for remote trust)

## D. Lead machine (data → audit → outreach)
0 [CC] Prospect scraper: national Google Maps pull (Outscraper/API) — rating, review count, velocity, website, phone
0 [CC] ICP filter + scoring engine (10+ employees proxies: review volume, locations, trucks/fleet signals; disqualifiers; FSM detection: ServiceTitan/Jobber/Housecall Pro/FieldEdge)
0 [CC] Competitor benchmark generator (top-3 local competitors per prospect, velocity gap)
0 [CC] Audit generator (auto one-page PDF/page per prospect from scraped data)
0 [CC] Email enrichment + verification flow (business inboxes; named-owner attempt via Apollo/Instantly; MillionVerifier)
0 [CFG] Cold outreach infrastructure: secondary domains, SPF/DKIM/DMARC, warm-up, sequencer (Smartlead/Instantly), sending caps
0 [CC] Sequence system: audit email + bumps + Robert call tasks + video-audit trigger for warm replies
1 [CC] Reply triage (AI classifies: positive/neutral/OOO/not-a-fit → routes to Robert's queue)
1 [CC] List hygiene loop (bounces, unsubscribes, suppression list across campaigns)

## E. Robert's sales system
0 [CFG] CRM pipeline in GHL (stages: audited → contacted → warm → call booked → call held → pilot offered → closed → onboarding gate)
0 [CC] Robert's Scorecard dashboard (today's queue, weekly targets vs actual: replies worked, follow-ups, video audits, calls booked/held, close rate; milestones to $8,333 MRR; streaks)
0 [DOC] Discovery call script + audit walkthrough flow (20-30 min, owner required)
0 [DOC] Office-manager one-page brief (gatekeeper → champion tool)
0 [DOC] Objection playbook ("my software does that," "my agency includes it," price, timing/peak season)
0 [CFG] Scheduling + reminders + no-show re-book flow; business phone (Quo), call recording
1 [CC] Speed-to-lead alerts (warm reply → Robert notified in minutes)

## F. Onboarding system
0 [CC/CFG] Onboarding gate checklist (agreement signed, setup paid, GBP manager access, job-completion data path confirmed — no gate, no start)
0 [CC] Onboarding automation: A2P registration, sub-account creation, QR/review assets generated, kickoff scheduling
0 [DOC] Client kickoff deck/call flow; CSR script + technician ask script (client team training pack)
1 [CC] Access tracker (who owes access/data; auto-nudges)

## Set G. Client delivery engine (per-client, automated)
0 [CC/CFG] Review-request workflow per client (FSM trigger at job completion first; AKR platform where gap: FieldEdge etc.)
0 [CC] Review monitoring + alert system (new review → queue; negative → same-day escalation)
0 [CC] Response engine: AI drafts in client voice → human approve/send; response-time SLA tracker
0 [CFG] GBP management checklist system (categories, services, photos, posts, Q&A)
1 [CC] Ask-rate monitor (requests sent vs jobs completed, by tech/crew where data allows)
1 [CC] Review theme miner (monthly: top complaint/praise themes per client → feeds quarterly fix)

## H. Reporting & dashboards
0 [CC] Customer dashboard (rating + trend, new reviews, velocity vs 3 competitors, response time/% answered, GBP calls/directions, ask-rate, latest reviews, quarterly focus)
0 [CC] Monthly scoreboard auto-builder (dashboard data → owner-readable one-pager + DeAdria insight line)
0 [CC] Internal ops dashboard (all clients: health RAG, ask-rate exceptions, response SLA, churn risk flags)
1 [CC] Business HQ dashboard (MRR, clients, churn, pipeline value, gate tracker vs sprint targets)

## I. Quarterly strategy / process improvement
1 [DOC] Quarterly process-fix playbook (theme → SOP change → client call flow)
1 [CC] Competitor re-benchmark automation (quarterly refresh per client)
1 [DOC] Client strategy call template + notes→actions tracker

## J. Money system
0 [CFG] Stripe products: $995 setup + $497/mo, ACH-first; failed-payment retry + alert flow
1 [CC] Monthly money report (MRR, setups, churn $, stack costs, contribution) — feeds HQ dashboard
1 [CFG] Bookkeeping categories + tax folder rhythm (with AKR books)

## K. Accountability & operating system
0 [DOC] Goal tracker: $100K scoreboard (17 clients / $8,333 MRR) with sprint gates 1-3 and kill rules
0 [CFG] Weekly operating meeting template (Robert pipeline + DeAdria client health + one decision) — 1 hr
0 [CC] Weekly auto-report to DeAdria & Robert (scorecard + HQ snapshot, no manual assembly)
1 [DOC] SOP library home (every recurring task documented once, then automated or delegated)

## L. Authority & referral engine
1 [DOC/CC] Proof assets only (corrected 2026-11-01): case studies and results snapshots from real client data for the website/proposals. NO AKR social posting calendar — acquisition is outbound audit + referrals + partners. Client social content = parked add-on only.
1 [DOC] Referral ask system (built into pilot agreements + quarterly calls; tracked in CRM)
2 [DOC] Partner outreach kit (FSM consultants, trade coaches, peer groups; conference plan Year 2)

## M. Retention & support
1 [CC] Churn-risk alerts (ask-rate drop, owner disengagement, slow review month → save play)
1 [DOC] Save-play scripts; cancellation exit flow (client keeps assets — trust brand)
1 [CFG] Client comms channel + response SLA for client questions

## N. AI/build team operating rules
0 [DOC] Who builds what: Claude Code builds scrapers/generators/dashboards/automations; Claude drafts copy/scripts/reports and analyzes; GHL hosts client-facing systems; humans approve anything client- or prospect-facing before it sends
0 [DOC] Prompt/template library (audit narrative, response drafts, outreach copy, report insights — all in brand voice)
0 [CFG] Repo + backups for all CC-built tools; test checklist before any automation touches a client

## Deliberately NOT building (waste / traps)
- Custom review software (rent: GHL/NiceJob layer)
- Custom CRM (GHL)
- Client mobile app
- Ads management system (parked add-on)
- Website builder for clients (parked add-on, template only later)

## O. AI agent layer (added 2026-11-01 — DeAdria's requirement: agents help run it alongside her full-time job; she must NOT be the bottleneck)

### Design rule: agent-first, exception-only human review
- Every process is written first as an agent job spec: trigger → inputs → decision rules → output → escalation condition → success metric. If a task can't be specced, it stays a documented human SOP until it can.
- DeAdria's involvement is ONE batched exception queue, reviewed in a set window (target 20-30 min/day), never a stream of pings during her workday.
- Autonomy ladder per task AND per client: Draft mode (human approves everything) → Batch mode (human approves a daily batch) → Auto mode (agent acts, human audits a sample). Promotion is earned by metrics: draft edit rate and error rate below threshold for 30 days.
- Traffic-light authority: GREEN = agent acts alone (routine, reversible, templated). YELLOW = agent drafts, human batch-approves. RED = agent stops and escalates immediately (1-2 star review, angry client, payment failure, compliance risk, anything off-script).

### The agent roster
1. Scout Agent [CC] — scrapes/enriches prospects, applies ICP filter, detects FSM, scores fit. Output: qualified prospect list. GREEN.
2. Audit Agent [CC] — builds the one-page competitor audit per prospect; flags data it couldn't verify. GREEN for generation, YELLOW for first-send per batch.
3. Outreach Agent [CFG/CC] — runs sequences inside guardrails (caps, suppression, CAN-SPAM); pauses itself on bounce/reply anomalies. GREEN inside rules.
4. Triage Agent [CC] — classifies every reply (positive/neutral/OOO/hostile/not-a-fit), routes warm replies to Robert's queue with a summary + suggested opener, pings speed-to-lead alert. GREEN.
5. Robert's Briefing Agent [CC] — before every discovery call: one-page brief (audit highlights, competitor names, software state, likely objections, talk track). Output lands in his scorecard/queue. GREEN.
6. Onboarding Chaser Agent [CC] — owns the gate checklist after signature: sends access requests, generates QR assets, schedules kickoff, nudges the client (not DeAdria) until the gate clears. YELLOW on message copy, GREEN on chasing cadence.
7. Review Response Agent [CC] — drafts every review response in the client's voice from their client-brain file; 4-5 star = ladder per autonomy tier; 1-3 star = always YELLOW/RED with a suggested recovery action. Never auto-posts a negative response at any tier.
8. Client Ops Agent [CC] — monitors ask-rate vs jobs completed, response SLA, GBP changes, review velocity; opens exception tickets only when a threshold breaks. GREEN monitoring, tickets to DeAdria's queue.
9. Insight Agent [CC] — monthly theme mining per client (praise/complaint patterns, example quotes), drafts the scoreboard insight line and the quarterly process-fix recommendation for DeAdria to edit. YELLOW (she edits, never writes from scratch).
10. Reporting Agent [CC] — builds customer scoreboards, Robert's scorecard data, HQ dashboard, and the pre-meeting weekly pack. GREEN.
11. Client Comms Agent [CC] — answers routine client questions from the knowledge base (status, next steps, report explanations); anything emotional, financial, or off-base = RED escalate. YELLOW until proven.
12. Money Agent [CC] — watches Stripe: failed payments → retry + polite chase sequence; monthly money report; flags churn-risk payment behavior. GREEN on process, RED on any dispute/chargeback.
13. Proof Agent [CC] — PHASE 2 ONLY, re-scoped 2026-11-01 at DeAdria's correction: AKR's model has NO social content calendar. This agent only turns real client results into sales proof assets (case-study drafts, results snapshots for the website/proposals). Client social-media content exists ONLY if the parked client add-on is ever activated (after 10 retained clients); it is not part of the core model. YELLOW.
14. QA / Compliance Agent [CC] — pre-send checker on everything outbound: brand voice, compliance rails (no gating language, no incentive offers, no guarantees), names/numbers match source data. Can BLOCK a send. GREEN (blocking authority).
15. Chief-of-Staff Agent [CC] — the orchestrator: runs the daily rhythm, assembles DeAdria's single exception queue, chases Robert's and DeAdria's own overdue items, prepares the weekly operating pack, tracks gates and goals, and reports agent health (errors, edit rates, stuck queues). This agent is what makes "not the bottleneck" real.

### Foundations agents need (build BEFORE the agents)
- Structured data model: CRM fields, naming conventions, pipeline stages — agents fail on messy data, not on intelligence.
- Client brain file per client: voice examples, services, service area, competitors, access status, preferences, autonomy tier. One file, always current, every agent reads it.
- Single exception inbox (one queue UI across all agents) with audit log: every agent action logged (what, when, confidence, source data).
- Agent health metrics: edit rate, error rate, escalation rate per agent — reviewed in the weekly meeting; autonomy changes are data decisions.
- Failure design: agent monitors itself; broken automation alerts same day; every automated flow has a documented manual fallback; quarterly "DeAdria-offline drill" — business must run a week without her.
- Security: least-privilege access per tool, client data separated per sub-account, no client data in prompts beyond the client's own brain file.

### What stays human (deliberately)
- Robert's discovery calls and relationships; DeAdria's quarterly strategy calls and final say on process-fix recommendations; any negative-review recovery conversation; pricing/contract exceptions; the weekly decision meeting. Agents prepare, humans decide and relate.
