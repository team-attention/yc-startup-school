---
name: module-4-planning-mvp
description: |
  This skill should be used when the user asks about "MVP", "유저 인터뷰", "talk to users", "사용자 대화", "제품 개발", "프로토타입", "MVP 만들기", "사용자 인터뷰 방법", "yc module 4", "/yc-m4", or any questions about user research, building an MVP, product-market fit iteration, or technical founder advice. Teaches YC Startup School Module 4 from Gustaf Alströmer, Michael Seibel, and Diana Hu's lectures.
---

# YC Startup School — Module 4: Planning MVP

This module is the most operationally dense in YC Startup School. Three lectures cover the full product development loop: talk to users (Gustaf Alströmer) → build MVP (Michael Seibel) → iterate as a technical founder (Diana Hu). The core insight: founders who deeply understand users build better products faster.

## Instructions

1. Read ALL transcript files from `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-4/` using the Read tool:
   - `how-to-talk-to-users.md` (has full transcript)
   - `how-to-build-an-mvp.md` (no transcript — use chapter titles and description)
   - `tips-for-technical-startup-founders.md` (has full transcript)
2. Present key frameworks from each lecture with speaker attribution
3. Analyze the user's current product development stage:
   - Have they done user interviews? With how many people?
   - Do they have a prototype or MVP built?
   - What stage: ideating / building MVP / post-launch iterating?
4. Generate a workbook-style self-assessment with questions derived from the lectures
5. Save the completed assessment to `knowledge/yc-startup-school/module-4-assessment.md` in the user's project root

## Key Topics

### Talking to Users (Gustaf Alströmer)
- **Who to talk to**: Network first (less honest but accessible), ex-colleagues, LinkedIn/Reddit/Slack communities
- **Interview format**: Video/phone/in-person only — 5-minute video call > 5,000 survey responses
- **Golden rule**: Do NOT introduce your idea until the end or not at all — your job is to listen
- **6 core questions**: "Tell me how you do X today" / "What's hardest about X?" / "Why is it hard?" / "How often?" / "Why important?" / "What do you do to solve it today?"
- **Follow-up techniques**: "What do you mean by that?" / "Tell me more about that" / "Why is that important to you?"
- **Questions to NOT ask**: "Will you use our product?" / "Which features?" / Yes/no questions / "How would a better product look?" / Two questions at once
- **Users have good problems, bad solutions**: Gmail users wanted split-screen (real problem: slowness). Airbnb guests wanted phone numbers (real problem: trust).
- **MVP prototype sessions**: Don't tell them what to do — give a goal and watch. Have them think aloud.
- **Keep users engaged**: Slack/WhatsApp group with early users, ship fast in response to feedback, give them exclusive access feeling

### Building MVP (Michael Seibel)
- **Pre-launch goals**: Get MVP built → get it in front of customers → start learning (chapters from video)
- **Solve "hair on fire" problems**: Find the problems users desperately need solved, not just nice-to-haves
- **Build quickly**: Use minimal features; every feature you don't build is time saved
- **Classic MVPs**: Airbnb (photos + listings only), Twitch (just Justin.tv streaming), Stripe (manual bank form processing behind clean API)
- **Fear of launching**: Most founders' biggest blocker — ship anyway

### Technical Founder Principles (Diana Hu)
- **3 stages**: Ideating (days) → Building MVP (weeks) → Launch/iterate (ongoing)
- **Prototype fast**: Clickable Figma / terminal script / 3D rendering — just enough to show and get feedback. Build in days, not weeks.
- **Do things that don't scale**: Manual onboarding, founders as customer support, DoorDash on plain HTML + Google Forms + Find My Friends
- **90/10 solution** (Paul Buchheit): First version will be rewritten. Restrict scope (geography, user type, data type) to ship now. This is your startup superpower.
- **Tech stack choice**: Choose for iteration speed, not prestige. Facebook shipped on PHP. DoorDash launched on static HTML. The code will be rewritten.
- **Don't hire too early**: At MVP stage, founders building = faster learning. Hiring slows you down and dilutes your product understanding.
- **Post-launch**: Hard data (analytics) + soft data (user interviews). Continuously launch. Balance building vs. fixing — tech debt is fine pre-PMF.
- **Role evolution**: 2-5 engineers: 70% coding. 5-10: <50%. 10+: transition to architecture or people leadership.

## Output Format

### Part 1: Module Summary
- The user interview loop: who → how to reach → what to ask → what NOT to ask → how to synthesize
- MVP philosophy: solve hair-on-fire problems, not feature wish lists
- Diana Hu's 3-stage framework with principles per stage
- The 90/10 solution and "do things that don't scale" as startup superpowers

### Part 2: Apply to Your Situation
Assess against the module's frameworks:
- Stage identification: ideating / building MVP / post-launch?
- User interview count: 0 / 1-5 / 5-20 / ongoing?
- Prototype/MVP status and time spent building so far
- Biggest current blocker: talking to users vs. building vs. fear of shipping?
- Tech stack choice: optimized for speed or for prestige/scale?

### Part 3: Self-Assessment Workbook
Generate 7-9 questions drawn directly from the lectures:

1. Name 5 people you could interview this week about the problem you're solving. What's stopping you from booking those calls today?
2. In your last user conversation, did you introduce your idea early? What did you learn vs. what did you pitch?
3. What's the "how do you do X today?" answer for your target user — and does your MVP actually make that better?
4. Is the problem you're solving "hair on fire" — would users pay to fix it or cobble together workarounds? What evidence do you have?
5. If you had to ship an MVP in 2 weeks using only what you can build today, what would you cut? (That cut version might be your real MVP.)
6. Which "do things that don't scale" hack could you use right now to get your first 10 users without writing any new code?
7. What tech choices have you made for prestige/scale vs. for shipping speed? What would the Jedi Master version of your stack look like?
8. When did you last ship something new and show it to a user? What did you learn?
9. What's one insight from a user interview that changed what you're building?

## References

- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-4/how-to-talk-to-users.md`
  - Author: Gustaf Alströmer (YC Group Partner, ex-Airbnb)
  - Key examples: Airbnb host/guest relationship, Brian Chesky's 50 Airbnb experiment, Gmail split-screen request
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-4/how-to-build-an-mvp.md`
  - Author: Michael Seibel (YC Group Partner)
  - Note: No transcript available; use video chapters (Airbnb, Twitch, Stripe examples)
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-4/tips-for-technical-startup-founders.md`
  - Author: Diana Hu (YC Group Partner, ex-CTO Escher Reality/Niantic)
  - Key examples: Optimizely prototype (days), DoorDash (static HTML + Google Forms), Stripe (manual bank forms), Segment (5 launches in a month), WayUp, Pokémon Go launch bugs
