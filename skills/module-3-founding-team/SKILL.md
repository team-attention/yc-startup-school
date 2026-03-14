---
name: module-3-founding-team
description: |
  This skill should be used when the user asks about "공동창업자", "co-founder", "지분", "equity split", "공동창업자 찾기", "공동창업자 관계", "vesting", "창업팀 구성", "yc module 3", "/yc-m3", or any questions about co-founder selection, equity distribution, working together, or co-founder breakups. Teaches YC Startup School Module 3 from Harj Taggar and Michael Seibel's lectures.
---

# YC Startup School — Module 3: Founding Team

This module covers the most overlooked source of startup failure: co-founder relationships. The #1 reason startups fail at YC is co-founder breakups. Harj Taggar (finding co-founders) and Michael Seibel (equity mistakes) provide frameworks for selecting, compensating, and maintaining co-founding relationships.

## Instructions

1. Read ALL three transcript files from `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-3/` using the Read tool:
   - `keys-to-successful-co-founder-relationships.md` (note: no transcript available, use chapter titles for topics)
   - `co-founder-equity-mistakes-to-avoid.md`
   - `how-to-find-a-co-founder.md`
2. Present key frameworks from each lecture with speaker attribution
3. Analyze the user's co-founder situation:
   - Solo founder or existing co-founding team?
   - Equity split done yet? Vesting/cliff in place?
   - Stress test history: have they worked together under pressure?
4. Generate a workbook-style self-assessment with questions derived from the lectures
5. Save the completed assessment to `knowledge/yc-startup-school/module-3-assessment.md` in the user's project root

## Key Topics

### Finding a Co-Founder (Harj Taggar)
- **Why you need one**: More work done, emotional support, pattern matching (Facebook/Apple both had co-founders)
- **Solo founder exception**: Only if (1) high-conviction idea + domain expertise AND (2) you're technical — then start building and find co-founder in parallel
- **What to look for**: Stress tolerance first (most important), aligned high-level goals, complementary skills + trajectory over current skills
- **Where to find**: People you already know first (never assume they're unavailable — always ask), YC co-founder matching platform, hackathons/open source
- **Co-founder matching heuristic**: Look for people you would have met anyway; avoid pairs with nothing in common except the platform
- **3 common breakup causes**: Loss of mutual respect / both wanting CEO title / different work ethic expectations
- **Maintenance**: Regular scheduled 1-on-1s, don't avoid disagreements, small releases of pressure over time vs. one big confrontation

### Equity (Michael Seibel)
- **Core principle**: Be generous with co-founder equity — it's a motivation tool for future work, not a reward for past contribution
- **Default to near-equal splits**: The "midwit" tries to calculate perfect splits; the wise founder gives generously
- **Vesting + cliff are non-negotiable**: 4-year vesting, 1-year cliff — applies to ALL founders including CEO
- **Co-founders must be essential**: Smallest number of people who can build MVP + get it to customers + start learning
- **Equity is for future work**: 99% of the work is still ahead; 6 months head start is irrelevant over a 10-20 year journey
- **CEO firing rights**: CEO must retain ability to fire non-performing founders regardless of equity split
- **Pre-PMF breakup guidelines**: Before 1-year cliff → token equity (2-5%). After cliff but pre-PMF → no more than 5% retained
- **Bad reasons for unequal splits**: "They agreed" / "I had the idea" / "I started earlier" / "They need salary" / "I'm more experienced" / "I raised money first" / "I launched first"
- **Bad advice to reject**: Performance-based equity / part-time founders / dynamic equity agreements

## Output Format

### Part 1: Module Summary
- Why co-founder failure is the #1 startup killer
- The 3 qualities to look for in a co-founder (stress tolerance, aligned goals, complementary trajectory)
- Michael Seibel's equity framework: generosity as a strategic tool
- Vesting/cliff mechanics and why they protect everyone
- The pre-PMF breakup guidelines

### Part 2: Apply to Your Situation
Assess against the module's criteria:
- Co-founder status: solo, searching, or paired?
- If paired: equity split and vesting structure in place? Have you worked under stress together?
- Have you explicitly discussed goals, work expectations, and CEO authority?
- Are there unspoken resentments building? (test: when did you last have a frank 1-on-1?)

### Part 3: Self-Assessment Workbook
Generate 7-9 questions drawn directly from the lectures:

1. Can you name 3 people in your network you'd want as a co-founder — and have you actually asked them? (Not assumed they're unavailable)
2. Think of a stressful situation you've been in with your potential/current co-founder. How did they handle it?
3. Have you explicitly discussed: why you both want to start a company, what success looks like, and how hard you expect to work?
4. What's your current equity split — and could each co-founder still be highly motivated in year 3 when things are hard?
5. Do you have a 4-year vesting schedule with a 1-year cliff in place for ALL founders, including yourself?
6. Is your current co-founding team the minimum number of people who can build, ship, and learn? If you have 4+ co-founders, what conversation hasn't happened?
7. Michael Seibel's bad reasons list: "I had the idea / I started earlier / I raised money / I launched first" — which of these have you used to justify unequal equity?
8. When did you last have a frank 1-on-1 with your co-founder about how the relationship is going?
9. If your co-founder left tomorrow, what's the plan? (Harj's advice: have this conversation before you need it)

## References

- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-3/co-founder-equity-mistakes-to-avoid.md`
  - Author: Michael Seibel (YC Group Partner)
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-3/how-to-find-a-co-founder.md`
  - Author: Harj Taggar (YC Group Partner)
  - Key examples: Dropbox (Drew Houston + Arash), Facebook (Zuckerberg + Moskovitz), Apple (Jobs + Wozniak)
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-3/keys-to-successful-co-founder-relationships.md`
  - Authors: Catheryn Li, Divya Bhat (YC)
  - Note: No transcript available; use chapter titles for topic coverage
