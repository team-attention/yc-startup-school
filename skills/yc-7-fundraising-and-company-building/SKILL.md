---
name: yc-7-fundraising-and-company-building
description: |
  This skill should be used when the user asks about "펀딩", "투자", "fundraising", "YC 지원", "YC 합격", "SAFE", "투자 용어", "엔젤 투자", "/yc-7", "어떻게 투자받나", "how fundraising works", "YC application", "startup legal terms", "cap table", "equity dilution". YC Startup School Module 7: Fundraising and Company Building — Brad Flora on how startup fundraising works and Dalton Caldwell on how to apply and succeed at YC.
---

# YC Startup School — Module 7: Fundraising and Company Building

## Official Curriculum

- 📺 **How Startup Fundraising Works in 2022** — Brad Flora (YC Partner) ✅ transcript available
- 📺 **How to Apply and Succeed at Y Combinator** — Dalton Caldwell (YC Managing Director) ✅ transcript available

## Instructions

1. Read ALL transcript files from `${CLAUDE_PLUGIN_ROOT}/skills/yc-7-fundraising-and-company-building/references/`:
   - `how-startup-fundraising-works.md` — Brad Flora (YC Partner)
   - `how-to-apply-and-succeed-at-yc.md` — Dalton Caldwell (YC Managing Director)
2. Present key frameworks from each lecture with speaker attribution
3. Assess the user's fundraising stage, YC interest, and legal/cap table hygiene
4. Generate a workbook-style self-assessment derived from the lectures
5. Save to `knowledge/yc-startup-school/module-7-assessment.md`
6. Run the interactive Self-Assessment Workbook:
   - Ask each question ONE AT A TIME using AskUserQuestion
   - Wait for the user's response before asking the next question
   - After each answer, provide brief feedback connecting their response to the module's frameworks
   - After all questions, synthesize their answers into a personalized assessment
7. Save the completed assessment (questions + answers + synthesis) to the appropriate knowledge path

## Key Frameworks

### How Startup Fundraising Works (Brad Flora)
- **The fundraising journey**: Bootstrapping → pre-seed (friends/angels) → seed (institutional) → Series A (VC)
- **SAFE mechanics**: Simple Agreement for Future Equity — valuation cap, discount, MFN clause. Post-money SAFE is the current standard.
- **Valuation cap**: The price ceiling at which your SAFE converts. Lower = better for investor. Higher = you believe more in your future value.
- **Priced rounds vs. convertible**: SAFEs and notes are faster/cheaper. Priced rounds set a definitive valuation with preferred stock.
- **Investor psychology**: Investors fund lines, not dots — show consistent trajectory. Warm intro > cold outreach by 10x.
- **Fundraising process**: Build the list → get intros → run parallel conversations → create urgency → close → wire transfer before celebrating
- **Common mistakes**: Raising too early (no traction), raising too much (dilution + distraction), taking bad money (misaligned investors)

### How to Apply and Succeed at YC (Dalton Caldwell)
- **What YC actually looks for**: Founder quality first, idea second. "Do these founders understand their users? Are they building something people want?"
- **Application questions that matter most**: "What are you building?" (one clear sentence), "Why now?", "What's your traction?"
- **Common application mistakes**: Vague descriptions / overselling the market / no traction or fake traction / unclear why these founders
- **The YC interview**: 10 minutes, fast-paced, about your business. Not a pitch — a conversation. Expect hard questions about your weakest assumptions.
- **When to apply**: Apply even before you feel ready. YC invests in people who can figure it out.
- **What YC provides**: $500K, access to alumni network, YC brand, Demo Day — the network compounds over decades

## Output Format

### Part 1: Module Content
- The fundraising journey stages and when to move between them
- SAFE mechanics explained with a concrete conversion example
- YC application success factors and the questions that matter most
- The fundraising process: managing parallel conversations

### Part 2: Apply to Your Situation
- Fundraising readiness: where are you in the journey and what's the next milestone?
- YC application fit: traction, one-sentence description, why these founders?
- Cap table and legal hygiene: IP assigned, incorporation clean, vesting in place?
- SAFE vs. priced round decision for current stage

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
- Save completed workbook to `knowledge/yc-startup-school/module-7-workbook.md`

Questions to ask interactively:
1. What is your one-sentence company description — would it make sense to a YC partner in 10 seconds?
2. What is your current growth rate, and what traction can you show to back it up?
3. Why now? What changed in the world that makes this the right moment?
4. What stage of funding are you at, and what milestone will you hit before your next raise?
5. Do you understand your cap table? Can you explain it simply?
6. Have you decided between SAFE and priced round? What drove that decision?
7. Who are your target investors and how will you get warm introductions?
8. Have you assigned IP to your company? Is your incorporation paperwork clean?
9. If applying to YC: what is the weakest part of your application right now?

## Bonus Content

The bonus folder contains a foundational legal vocabulary lecture relevant to this module:
- `${CLAUDE_PLUGIN_ROOT}/references/bonus/starting-a-company-the-key-terms-you-should-know.md` — Cap table, common vs. preferred stock, option pool, term sheet components, key documents

## References

- `${CLAUDE_PLUGIN_ROOT}/skills/yc-7-fundraising-and-company-building/references/how-startup-fundraising-works.md` — Brad Flora (YC Partner)
- `${CLAUDE_PLUGIN_ROOT}/skills/yc-7-fundraising-and-company-building/references/how-to-apply-and-succeed-at-yc.md` — Dalton Caldwell (YC Managing Director)
