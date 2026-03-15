---
name: yc-6-growing-and-monetizing
description: |
  This skill should be used when the user asks about "성장", "수익화", "KPI", "비즈니스 모델", "PMF", "메트릭", "코호트", "retention", "pricing", "/yc-6", "지표 설정", "가격 책정", "리텐션", "product market fit 측정", "growth", "monetizing", "business model". YC Startup School Module 6: Growing and Monetizing — KPI setting, startup metrics, and business models from Divya Bhat, Tom Blomfield, and Aaron Epstein.
---

# YC Startup School — Module 6: Growing and Monetizing

## Official Curriculum

- 📺 **How to Set KPIs and Prioritize Your Time** — Divya Bhat (YC) ✅ transcript as `setting-kpis-and-goals.md`
- 📺 **Startup Business Models and Pricing** — Aaron Epstein (YC) ✅ transcript as `yc-guide-to-business-models.md`
- 📺 **Growth for Startups** — Gustaf Alströmer ❌ no direct transcript (but `key-startup-metrics.md` by Tom Blomfield covers growth metrics comprehensively)

## Instructions

1. Read ALL transcript files from `${CLAUDE_PLUGIN_ROOT}/skills/yc-6-growing-and-monetizing/references/`:
   - `setting-kpis-and-goals.md` — Divya Bhat (YC)
   - `key-startup-metrics.md` — Tom Blomfield (YC)
   - `yc-guide-to-business-models.md` — Aaron Epstein (YC)
2. Present key frameworks from each lecture with speaker attribution
3. Assess the user's current metrics, business model, and retention data
4. Generate a workbook-style self-assessment derived from the lectures
5. Save to `knowledge/yc-startup-school/module-6-assessment.md`
6. Run the interactive Self-Assessment Workbook:
   - Ask each question ONE AT A TIME using AskUserQuestion
   - Wait for the user's response before asking the next question
   - After each answer, provide brief feedback connecting their response to the module's frameworks
   - After all questions, synthesize their answers into a personalized assessment
7. Save the completed assessment (questions + answers + synthesis) to the appropriate knowledge path

## Key Frameworks

### Setting KPIs (Divya Bhat)
- **One metric that matters (OMTM)**: Choose the single metric that best represents whether you're solving the problem. Everything else is secondary.
- **Weekly growth rate**: 5-7% WoW is the YC benchmark for healthy early-stage growth
- **Leading vs. lagging indicators**: Track leading indicators (actions that predict growth) not just lagging (revenue)
- **Prioritization**: Work backwards from your primary metric to the highest-leverage activities this week

### Key Startup Metrics (Tom Blomfield)
- **Revenue metrics**: MRR, ARR, ACV — know which applies to your model
- **Growth metrics**: WoW, MoM — track consistently. YC looks at trajectory, not snapshot
- **Churn**: Annual churn > 5% is a problem for SaaS. Diagnose before it compounds.
- **Engagement by type**: DAU/MAU for consumer, seats/usage for B2B, GMV/take-rate for marketplace
- **PMF signal**: Users would be "very disappointed" if you shut down (40%+ threshold per Sean Ellis)

### Business Models and Pricing (Aaron Epstein)
- **The full spectrum**: SaaS, marketplace, transactional, advertising, hardware, usage-based
- **Unit economics**: LTV, CAC, payback period — LTV:CAC > 3x is the benchmark for sustainable growth
- **Revenue quality**: Recurring > one-time; predictable > lumpy
- **Pricing heuristic**: Start higher than feels comfortable. It is almost always easier to lower prices than to raise them.

## Output Format

### Part 1: Module Content
- OMTM selection framework with examples by business type
- Weekly growth rate benchmarks and how to calculate correctly
- Business model comparison table relevant to the user's category
- PMF signal checklist derived from the metrics lectures

### Part 2: Apply to Your Situation
- Current metrics assessment: what the user is tracking vs. what they should be
- Business model fit: which model matches their revenue pattern?
- Retention and pricing gaps identified
- PMF assessment: right signals visible?

### Part 3: Interactive Workbook (AskUserQuestion)
- Ask questions ONE AT A TIME — do not list all questions at once
- Use AskUserQuestion tool for each question
- After each answer, give 1-2 sentence feedback connecting to the module's framework
- Provide multiple choice options where appropriate to make it easier to answer
- After completing all questions, generate a synthesis:
  - Overall readiness score (1-10) for this module's topic
  - Top strength identified from answers
  - Top gap identified from answers
  - One specific action item
- Save completed workbook to `knowledge/yc-startup-school/module-6-workbook.md`

Questions to ask interactively:
1. What is your single most important metric right now? What is its current value?
2. What is your week-over-week growth rate for the past 4 weeks? Accelerating or decelerating?
3. Have you drawn your cohort retention curve? Does it flatten or go to zero?
4. What percentage of your users would be "very disappointed" if your product shut down?
5. What business model are you using — and is it the right one for your current stage?
6. What is your current pricing, and how did you arrive at it? Have you tried raising it?
7. What is your LTV:CAC ratio (if applicable)? Is it above 3x?
8. What is your primary metric's leading indicator — what action predicts next week's number?

## Bonus Content

The bonus folder contains additional growth and monetization lectures that extend this module:
- `${CLAUDE_PLUGIN_ROOT}/references/bonus/consumer-startup-metrics.md` — DAU/MAU, D1/D7/D30 retention benchmarks by category
- `${CLAUDE_PLUGIN_ROOT}/references/bonus/how-to-improve-cohort-retention.md` — Cohort analysis, aha moment, time-to-value
- `${CLAUDE_PLUGIN_ROOT}/references/bonus/how-to-price-for-b2b.md` — Value-based pricing, B2B pricing tiers, the pricing conversation
- `${CLAUDE_PLUGIN_ROOT}/references/bonus/how-to-get-the-most-out-of-vibe-coding.md` — AI-assisted development for faster iteration

## References

- `${CLAUDE_PLUGIN_ROOT}/skills/yc-6-growing-and-monetizing/references/setting-kpis-and-goals.md` — Divya Bhat (YC)
- `${CLAUDE_PLUGIN_ROOT}/skills/yc-6-growing-and-monetizing/references/key-startup-metrics.md` — Tom Blomfield (YC)
- `${CLAUDE_PLUGIN_ROOT}/skills/yc-6-growing-and-monetizing/references/yc-guide-to-business-models.md` — Aaron Epstein (YC)
