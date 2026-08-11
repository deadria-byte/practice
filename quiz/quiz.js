// Restaurant Profit Leak Audit — quiz logic.
// Everything here runs in the visitor's browser. No data leaves the page yet;
// see the TODO in index.html about wiring the email step to Resend later.

const QUESTIONS = [
  {
    pillar: "labor",
    text: "How often do you find yourself covering a shift because someone didn't show up or you're short-staffed?",
    options: [
      { label: "Rarely", points: 0 },
      { label: "Sometimes", points: 1 },
      { label: "Weekly", points: 2 },
      { label: "Constantly", points: 3 },
    ],
  },
  {
    pillar: "labor",
    text: "Could a new hire run a shift correctly without you there in their first two weeks?",
    options: [
      { label: "Very confident — they'd have a real system to follow", points: 0 },
      { label: "Somewhat", points: 1 },
      { label: "Not very", points: 2 },
      { label: "Not at all — we don't really have a training system", points: 3 },
    ],
  },
  {
    pillar: "food",
    text: "When's the last time your food cost percentage surprised you, in a bad way?",
    options: [
      { label: "Never — it's dialed in and I track it closely", points: 0 },
      { label: "Once in a while", points: 1 },
      { label: "Almost every month", points: 2 },
      { label: "Honestly, I don't track it closely", points: 3 },
    ],
  },
  {
    pillar: "food",
    text: "How consistent is prep waste and portioning across your team?",
    options: [
      { label: "Tight — documented portions everyone follows", points: 0 },
      { label: "Mostly consistent", points: 1 },
      { label: "Depends who's on shift", points: 2 },
      { label: "No real system", points: 3 },
    ],
  },
  {
    pillar: "service",
    text: "When a customer complaint happens, how does your team handle it?",
    options: [
      { label: "Clear recovery process, staff empowered to fix it", points: 0 },
      { label: "Staff usually check with a manager first", points: 1 },
      { label: "Inconsistent, depends who's working", points: 2 },
      { label: "Complaints often turn into lost customers", points: 3 },
    ],
  },
  {
    pillar: "ops",
    text: "Do you have written opening/closing/mid-shift checklists your team actually uses?",
    options: [
      { label: "Yes, and they're followed", points: 0 },
      { label: "Yes, but they get skipped", points: 1 },
      { label: "Informal — it's in people's heads", points: 2 },
      { label: "No", points: 3 },
    ],
  },
  {
    pillar: "leadership",
    text: "If you took a full week off with no phone, what would happen to day-to-day operations?",
    options: [
      { label: "Runs the same", points: 0 },
      { label: "A few small hiccups", points: 1 },
      { label: "Noticeable problems", points: 2 },
      { label: "It would probably fall apart", points: 3 },
    ],
  },
  {
    pillar: "ai",
    text: "How much of your admin work (scheduling, ordering, reporting) is still done by hand?",
    options: [
      { label: "Mostly automated already", points: 0 },
      { label: "Some of it", points: 1 },
      { label: "Very little is automated", points: 2 },
      { label: "All of it, by hand", points: 3 },
    ],
  },
];

const PILLARS = {
  labor: {
    tag: "SOP-01",
    title: "Labor and Staffing",
    body: "Your biggest leak is likely turnover and coverage gaps — every last-minute scramble to cover a shift costs you money and consistency. A real staffing and training system closes this fast.",
  },
  food: {
    tag: "SOP-02",
    title: "Food Cost and Inventory",
    body: "Your biggest leak is likely prep waste and portioning drift — small inconsistencies that quietly eat 4-6% of margin before they ever show up on a report.",
  },
  service: {
    tag: "SOP-03",
    title: "Customer Service and Recovery",
    body: "Your biggest leak is likely inconsistent recovery — one bad table handled the wrong way costs you a repeat customer, and it's happening more than you see.",
  },
  ops: {
    tag: "SOP-04",
    title: "Daily Operations and Systems",
    body: "Your biggest leak is likely dependence on tribal knowledge — when checklists live in people's heads instead of on paper, quality swings shift to shift.",
  },
  leadership: {
    tag: "SOP-05",
    title: "Management and Leadership",
    body: "Your biggest leak is likely that the operation depends entirely on you — until a shift lead can run the floor the way you would, you can't step away without a drop in quality.",
  },
  ai: {
    tag: "SOP-06",
    title: "AI Business Operations",
    body: "Your biggest leak is likely hours lost to manual admin work — scheduling, ordering, and reporting that could run on autopilot are instead eating your week.",
  },
};

const state = {
  index: 0,
  answers: [], // one entry per question: { pillar, points }
};

const els = {
  progressTrack: document.getElementById("progress-track"),
  progressFill: document.getElementById("progress-fill"),
  screenIntro: document.getElementById("screen-intro"),
  screenQuestion: document.getElementById("screen-question"),
  screenEmail: document.getElementById("screen-email"),
  screenResults: document.getElementById("screen-results"),
  questionCount: document.getElementById("question-count"),
  questionText: document.getElementById("question-text"),
  answerList: document.getElementById("answer-list"),
  emailForm: document.getElementById("email-form"),
  resultsHeadline: document.getElementById("results-headline"),
  resultsSummary: document.getElementById("results-summary"),
  leakTag: document.getElementById("leak-tag"),
  leakTitle: document.getElementById("leak-title"),
  leakBody: document.getElementById("leak-body"),
  btnStart: document.getElementById("btn-start"),
  btnRetake: document.getElementById("btn-retake"),
};

function showScreen(screen) {
  [els.screenIntro, els.screenQuestion, els.screenEmail, els.screenResults].forEach((s) => {
    s.hidden = s !== screen;
  });
}

function renderQuestion() {
  const q = QUESTIONS[state.index];
  els.progressTrack.hidden = false;
  els.progressFill.style.width = `${(state.index / QUESTIONS.length) * 100}%`;
  els.questionCount.textContent = `Question ${state.index + 1} of ${QUESTIONS.length}`;
  els.questionText.textContent = q.text;
  els.answerList.innerHTML = "";

  q.options.forEach((opt) => {
    const btn = document.createElement("button");
    btn.className = "answer-option";
    btn.type = "button";
    btn.textContent = opt.label;
    btn.addEventListener("click", () => selectAnswer(q.pillar, opt.points));
    els.answerList.appendChild(btn);
  });

  showScreen(els.screenQuestion);
}

function selectAnswer(pillar, points) {
  state.answers.push({ pillar, points });
  state.index += 1;

  if (state.index < QUESTIONS.length) {
    renderQuestion();
  } else {
    els.progressFill.style.width = "100%";
    showScreen(els.screenEmail);
  }
}

function scoreResults() {
  const totals = {};
  Object.keys(PILLARS).forEach((key) => (totals[key] = 0));
  state.answers.forEach(({ pillar, points }) => {
    totals[pillar] += points;
  });

  const maxPossible = { labor: 6, food: 6, service: 3, ops: 3, leadership: 3, ai: 3 };
  let topPillar = null;
  let topRatio = -1;
  Object.keys(totals).forEach((key) => {
    const ratio = totals[key] / maxPossible[key];
    if (ratio > topRatio) {
      topRatio = ratio;
      topPillar = key;
    }
  });

  const overallTotal = Object.values(totals).reduce((a, b) => a + b, 0);
  const overallMax = Object.values(maxPossible).reduce((a, b) => a + b, 0);
  const overallRatio = overallTotal / overallMax;

  let severity;
  if (overallRatio < 0.3) severity = "Tight Operation";
  else if (overallRatio < 0.6) severity = "Moderate Leak Risk";
  else severity = "High Leak Risk";

  return { topPillar, severity };
}

function renderResults() {
  const { topPillar, severity } = scoreResults();
  const pillar = PILLARS[topPillar];

  els.resultsHeadline.textContent = severity;
  els.resultsSummary.textContent =
    "Based on your answers, here's where your back of house is most likely losing money first:";
  els.leakTag.textContent = pillar.tag;
  els.leakTitle.textContent = pillar.title;
  els.leakBody.textContent = pillar.body;

  showScreen(els.screenResults);
}

els.btnStart.addEventListener("click", () => {
  state.index = 0;
  state.answers = [];
  renderQuestion();
});

els.emailForm.addEventListener("submit", (e) => {
  e.preventDefault();
  // TODO (Phase 1, Weeks 1-2): send this email to Resend / the nurture sequence
  // once domain warm-up and CAN-SPAM setup are done. Not wired yet — see index.html.
  renderResults();
});

els.btnRetake.addEventListener("click", (e) => {
  e.preventDefault();
  els.progressTrack.hidden = true;
  showScreen(els.screenIntro);
});
