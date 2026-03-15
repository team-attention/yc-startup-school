---
name: yc-4-planning-an-mvp
description: |
  This skill should be used when the user asks about "MVP", "유저 인터뷰", "talk to users", "사용자 대화", "제품 개발", "프로토타입", "MVP 만들기", "/yc-4", "product development", "user research", "사용자 인터뷰", or any questions about user research, building an MVP, or product-market fit iteration. YC Startup School Module 4: Planning an MVP — Gustaf Alströmer on talking to users, Michael Seibel on building MVP, and Diana Hu on technical founder principles.
---

# YC Startup School — Module 4: Planning an MVP

## Official Curriculum

- 📺 **How to Talk to Users** — Gustaf Alströmer (YC Group Partner, ex-Airbnb) ✅ transcript available
- 📺 **How to Build an MVP** — Michael Seibel (YC Group Partner) ✅ transcript available
- 📖 **Product Development Cycle Fundamentals** — Michael Seibel ✅ transcript available as `tips-for-technical-startup-founders.md` (Diana Hu, YC Group Partner)

## Instructions

1. Read ALL three transcript files from `${CLAUDE_PLUGIN_ROOT}/skills/yc-4-planning-an-mvp/references/`:
   - `how-to-talk-to-users.md` — Gustaf Alströmer (YC Group Partner, ex-Airbnb)
   - `how-to-build-an-mvp.md` — Michael Seibel (YC Group Partner)
   - `tips-for-technical-startup-founders.md` — Diana Hu (YC Group Partner, ex-CTO Escher Reality/Niantic)
2. Present key frameworks from each lecture with speaker attribution
3. Assess the user's stage: ideating / building MVP / post-launch iterating
4. Generate a workbook-style self-assessment derived from the lectures
5. Save to `knowledge/yc-startup-school/module-4-assessment.md`
6. Run the interactive Self-Assessment Workbook:
   - Ask each question ONE AT A TIME using AskUserQuestion
   - Wait for the user's response before asking the next question
   - After each answer, provide brief feedback connecting their response to the module's frameworks
   - After all questions, synthesize their answers into a personalized assessment
7. Save the completed assessment (questions + answers + synthesis) to the appropriate knowledge path

## Key Frameworks

### Talking to Users (Gustaf Alströmer)
- **Golden rule**: Do NOT introduce your idea until the end or not at all — your job is to listen
- **Who to talk to**: Network first (less honest but accessible), ex-colleagues, LinkedIn/Reddit/Slack communities
- **Format**: Video/phone/in-person only — 5-minute video call > 5,000 survey responses
- **6 core questions**: "Tell me how you do X today" / "What's hardest about X?" / "Why is it hard?" / "How often?" / "Why important?" / "What do you do to solve it today?"
- **Questions NOT to ask**: "Will you use our product?" / "Which features?" / "How would a better product look?"
- **Users have good problems, bad solutions**: Gmail users wanted split-screen (real problem: slowness). Airbnb guests wanted phone numbers (real problem: trust).
- **Keep users engaged**: Slack/WhatsApp group, ship fast in response to feedback, exclusive access feeling

### Building MVP (Michael Seibel)
- **Pre-launch goals**: Get MVP built → in front of customers → start learning
- **Solve "hair on fire" problems**: Problems users desperately need solved, not nice-to-haves
- **Classic MVPs**: Airbnb (photos + listings only), Twitch (just Justin.tv streaming), Stripe (manual bank form processing behind clean API)
- **Build quickly**: Every feature you don't build is time saved. Fear of launching is the biggest blocker — ship anyway

### Technical Founder Principles (Diana Hu)
- **3 stages**: Ideating (days) → Building MVP (weeks) → Launch/iterate (ongoing)
- **Prototype fast**: Clickable Figma / terminal script — build in days, not weeks
- **Do things that don't scale**: Manual onboarding, founders as support, DoorDash on plain HTML + Google Forms + Find My Friends
- **90/10 solution** (Paul Buchheit): First version will be rewritten. Restrict scope to ship now. This is your startup superpower.
- **Tech stack for iteration speed**: Facebook shipped on PHP. DoorDash launched on static HTML. Code will be rewritten.
- **Don't hire too early**: At MVP stage, founders building = faster learning

## Output Format

### Part 1: Module Content
- The user interview loop: who → how to reach → what to ask → what NOT to ask → synthesize
- MVP philosophy: hair-on-fire problems, not feature wish lists
- Diana Hu's 3-stage framework with principles per stage
- The 90/10 solution and "do things that don't scale" as startup superpowers

### Part 2: Apply to Your Situation
- Stage: ideating / building MVP / post-launch?
- User interview count: 0 / 1-5 / 5-20 / ongoing?
- Prototype/MVP status and time spent building so far
- Biggest blocker: talking to users vs. building vs. fear of shipping?
- Tech stack: optimized for speed or prestige?

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
- Save completed workbook to `knowledge/yc-startup-school/module-4-workbook.md`

Questions to ask interactively:
1. Name 5 people you could interview this week. What's stopping you from booking those calls today?
2. In your last user conversation, did you introduce your idea early? What happened?
3. What's the "how do you do X today?" answer — and does your MVP actually make that better?
4. Is the problem "hair on fire"? Would users pay to fix it or cobble together workarounds?
5. If you had to ship an MVP in 2 weeks using only what you can build today, what would you cut?
6. Which "do things that don't scale" hack could get you your first 10 users without new code?
7. What tech choices have you made for prestige/scale vs. shipping speed?
8. What's one insight from a user interview that changed what you're building?

## References

- `${CLAUDE_PLUGIN_ROOT}/skills/yc-4-planning-an-mvp/references/how-to-talk-to-users.md` — Gustaf Alströmer
- `${CLAUDE_PLUGIN_ROOT}/skills/yc-4-planning-an-mvp/references/how-to-build-an-mvp.md` — Michael Seibel
- `${CLAUDE_PLUGIN_ROOT}/skills/yc-4-planning-an-mvp/references/tips-for-technical-startup-founders.md` — Diana Hu
