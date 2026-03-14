---
name: yc-5-launching
description: |
  This skill should be used when the user asks about "론칭", "첫 고객", "launching", "first customers", "cold email", "콜드 이메일", "/yc-5", "스타트업 출시", "고객 확보", "do things that don't scale", "launch strategy", "how to launch". YC Startup School Module 5: Launching — Kat Mañalac on launching repeatedly, Gustaf Alströmer on first customer acquisition, and PG's "Do Things That Don't Scale" essay.
---

# YC Startup School — Module 5: Launching

## Official Curriculum

- 📺 **How to Launch (Again and Again)** — Kat Mañalac (YC Partner) ✅ transcript as `the-best-way-to-launch-your-startup.md`
- 📺 **How to Get Your First Customers** — Gustaf Alströmer (YC Group Partner) ✅ transcript available
- 📖 **Do Things That Don't Scale** — Paul Graham ✅ transcript available (also via `/pg` skill)

## Instructions

1. Read ALL transcript files from `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-5/`:
   - `the-best-way-to-launch-your-startup.md` — Kat Mañalac (YC Partner)
   - `how-to-get-your-first-customers.md` — Gustaf Alströmer (YC Group Partner)
   - `do-things-that-dont-scale.md` — Paul Graham (also via `/pg` skill)
2. Present key frameworks from each lecture with speaker attribution
3. Analyze the user's current launch and customer acquisition stage
4. Generate a workbook-style self-assessment derived from the lectures
5. Save to `knowledge/yc-startup-school/module-5-assessment.md`

## Key Frameworks

### How to Launch (Again and Again) (Kat Mañalac)
- **Launch early and often**: Don't wait for a "perfect" product — launching is a learnable, repeatable skill
- **5 launch types**: Personal network / Community (HN, Product Hunt, Reddit) / Press/media / Social posts / YC Launch (Show HN)
- **One-sentence pitch**: Must explain what you do in plain English. Test: does a stranger immediately understand the value?
- **Show HN structure**: What it is + who it's for + what makes it different — in the first sentence
- **Each launch teaches something different**: Network launch = warm signal, community launch = cold signal, press = brand

### How to Get Your First Customers (Gustaf Alströmer)
- **Your first 10 users come from manual effort**, not growth hacking — accept this
- **Where to find them**: Personal network, ex-colleagues, LinkedIn/Slack communities, conferences, cold email
- **Do things that don't scale first**: Airbnb's Gustaf personally helped hosts improve listings. Stripe's founders manually set up merchant accounts.
- **Convert early users to evangelists**: Give access before everyone else; respond to feedback immediately; make them feel part of building
- **Community seeding**: Post in Slack groups, subreddits, and forums where your users already gather

### Do Things That Don't Scale (Paul Graham)
- **Recruit users manually**: Go find them one by one. This is not embarrassing — it's essential
- **Build an exceptional experience for a small number of users**, not a mediocre one for many
- **Learn from manual work**: The understanding gained by doing things yourself cannot be gained any other way
- **The Stripe example**: Founders asked people at hackathons "wanna try our payment API?" and set up their account on the spot
- **Consult, then productize**: Doing things manually first tells you what to build

## Output Format

### Part 1: Module Content
- The "launch repeatedly" mindset vs. big-bang launch thinking
- The 5 launch types and when to use each
- Gustaf's manual first-customer playbook
- PG's "do things that don't scale" doctrine with specific examples

### Part 2: Apply to Your Situation
- Current launch status: launched 0 / 1 / many times?
- Which launch channels are most relevant (B2B vs. B2C, enterprise vs. SMB, developer vs. consumer)?
- First customer acquisition: what's working and what's missing?
- "Do things that don't scale" audit: what manual things should be happening right now?

### Part 3: Workbook
1. Can you describe your product in one sentence that makes sense to a stranger?
2. Have you launched at least once? What did you learn from that launch?
3. Who are the first 10 people you could personally reach out to today (not blast email — personally)?
4. What's the most manual, unscalable thing you could do right now to get 1 more paying user?
5. Where do your target customers spend time online (subreddits, Slack groups, forums)?
6. What communities could you post in this week? What would you say?
7. Are you responding to early users within hours? What's your feedback loop like?
8. If you haven't launched yet — what is the smallest thing you could ship and put in front of 3 real people this week?

## Bonus Content

The bonus folder contains a cold email tactics lecture relevant to first customer acquisition:
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/bonus/how-to-convert-customers-with-cold-emails.md` — Cold email funnel, subject lines, body structure, follow-up sequences

## References

- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-5/the-best-way-to-launch-your-startup.md` — Kat Mañalac
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-5/how-to-get-your-first-customers.md` — Gustaf Alströmer
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-5/do-things-that-dont-scale.md` — Paul Graham (also via `/pg` skill)
