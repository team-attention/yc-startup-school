---
name: yc-3-building-your-founding-team
description: |
  This skill should be used when the user asks about "공동창업자", "co-founder", "지분", "equity", "equity split", "vesting", "창업팀", "공동창업자 찾기", "공동창업자 관계", "/yc-3", "co-founder breakup", "지분 배분", or any questions about co-founder selection, equity distribution, or founding team dynamics. YC Startup School Module 3: Building Your Founding Team — the #1 reason startups fail at YC is co-founder breakups.
---

# YC Startup School — Module 3: Building Your Founding Team

## Official Curriculum

- 📺 **All About Co-Founders** — Catheryn Li & Divya Bhat (YC) ✅ transcript as `keys-to-successful-co-founder-relationships.md`
- 📺 **Co-Founder Mistakes That Kill Companies** — Dalton Caldwell & Michael Seibel ❌ no transcript (but `co-founder-equity-mistakes-to-avoid.md` by Michael Seibel covers the equity mistake patterns)
- 📺 **How to Split Equity Among Co-Founders** — Michael Seibel ✅ transcript as `co-founder-equity-mistakes-to-avoid.md`
- 📺 **How to Work Together** — Kevin Hale ❌ no transcript (but `how-to-find-a-co-founder.md` by Harj Taggar covers finding and working with co-founders)

## Instructions

1. Read ALL three transcript files from `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-3/`:
   - `keys-to-successful-co-founder-relationships.md` — Catheryn Li & Divya Bhat (YC)
   - `co-founder-equity-mistakes-to-avoid.md` — Michael Seibel (YC Group Partner)
   - `how-to-find-a-co-founder.md` — Harj Taggar (YC Group Partner)
2. Present key frameworks from each lecture with speaker attribution
3. Assess the user's co-founder situation: solo / searching / paired — and equity/vesting status
4. Generate a workbook-style self-assessment derived from the lectures
5. Save to `knowledge/yc-startup-school/module-3-assessment.md`
6. Run the interactive Self-Assessment Workbook:
   - Ask each question ONE AT A TIME using AskUserQuestion
   - Wait for the user's response before asking the next question
   - After each answer, provide brief feedback connecting their response to the module's frameworks
   - After all questions, synthesize their answers into a personalized assessment
7. Save the completed assessment (questions + answers + synthesis) to the appropriate knowledge path

## Key Frameworks

### Finding a Co-Founder (Harj Taggar)
- **Why you need one**: More work done, emotional support, pattern matching. Facebook, Apple — both had co-founders
- **Solo founder exception**: Only if (1) high-conviction domain expertise AND (2) technical — then build and find co-founder in parallel
- **What to look for**: Stress tolerance first (most important), aligned high-level goals, complementary trajectory over current skills
- **Where to find**: People you already know first — never assume they're unavailable; always ask. Also: YC co-founder matching, hackathons, open source
- **3 breakup causes**: Loss of mutual respect / both wanting CEO title / different work ethic expectations
- **Maintenance**: Regular 1-on-1s, small pressure releases vs. one big confrontation

### Keys to Successful Co-Founder Relationships (Catheryn Li & Divya Bhat)
- Explicit communication on roles, expectations, and decision-making authority from day one
- Regular check-ins — don't wait for problems to surface in product or investor meetings
- Alignment on the "why": personal goals, life circumstances, exit expectations

### Equity (Michael Seibel)
- **Core principle**: Be generous with co-founder equity — it motivates future work, not rewards past contribution
- **Default to near-equal splits**: Trying to calculate the "perfect" split is the wrong mental model
- **Vesting + cliff are non-negotiable**: 4-year vesting, 1-year cliff — applies to ALL founders including CEO
- **Smallest founding team**: Minimum people who can build MVP + get it to customers + start learning
- **CEO must retain firing rights** regardless of equity split
- **Pre-PMF breakup guidelines**: Before 1-year cliff → 2-5% token equity. After cliff but pre-PMF → no more than 5% retained
- **Bad reasons for unequal splits**: "I had the idea" / "I started earlier" / "I raised money" / "I launched first" / "I'm more experienced"

## Output Format

### Part 1: Module Content
- Why co-founder failure is the #1 startup killer at YC
- The 3 qualities to look for (stress tolerance, aligned goals, complementary trajectory)
- Michael Seibel's equity philosophy: generosity as strategic tool
- Vesting/cliff mechanics and why they protect everyone
- Pre-PMF breakup guidelines with specific percentages

### Part 2: Apply to Your Situation
- Co-founder status: solo / searching / paired?
- If paired: equity split and vesting structure in place? Worked under stress together?
- Have you explicitly discussed goals, work expectations, CEO authority?
- Any unspoken resentments building? When was the last frank 1-on-1?

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
- Save completed workbook to `knowledge/yc-startup-school/module-3-workbook.md`

Questions to ask interactively:
1. Name 3 people you'd want as co-founder — have you actually asked them? (Not assumed they're unavailable)
2. Describe a stressful situation with your potential co-founder. How did they handle it?
3. Have you explicitly discussed: why you both want to start, what success looks like, how hard you'll work?
4. What's your current equity split — could each co-founder stay motivated in year 3 when things are hard?
5. Do you have 4-year vesting with 1-year cliff in place for ALL founders including yourself?
6. Is your founding team the minimum number to build, ship, and learn?
7. Which bad reasons (idea / earlier / raised / launched) have you used to justify your split?
8. When did you last have a frank 1-on-1 with your co-founder about how the relationship is going?

## References

- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-3/keys-to-successful-co-founder-relationships.md` — Catheryn Li & Divya Bhat (YC)
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-3/co-founder-equity-mistakes-to-avoid.md` — Michael Seibel (YC Group Partner)
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-3/how-to-find-a-co-founder.md` — Harj Taggar (YC Group Partner)
