---
name: module-2-startup-ideas
description: |
  This skill should be used when the user asks about "아이디어 검증", "스타트업 아이디어", "startup ideas", "tarpit", "아이디어 찾는 방법", "좋은 아이디어인지", "yc module 2", "/yc-m2", or any question about generating, evaluating, or pivoting startup ideas. Teaches YC Startup School Module 2 content from Jared Friedman's lecture.
---

# YC Startup School — Module 2: Startup Ideas

This module teaches how to find, evaluate, and generate startup ideas — including the dangerous traps (tarpit ideas, wrong filters) that cause most founders to either wait too long or pursue bad ideas. Jared Friedman (YC Partner) provides a systematic framework backed by patterns from thousands of YC companies.

## Instructions

1. Read the transcript from `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-2/how-to-get-startup-ideas.md` using the Read tool
2. Present the key frameworks and mental models from the lecture with speaker attribution (Jared Friedman, YC Partner)
3. If the user has an existing idea, evaluate it using the 4-criteria idea quality score formula
4. Analyze the user's situation:
   - Ask about their background, domain expertise, and current ideas if not known
   - Identify which of the 7 recipes is most applicable to their situation
   - Check for the 4 dangerous filters that may be blocking their best ideas
5. Generate a workbook-style self-assessment with questions derived from the lecture
6. Save the completed assessment to `knowledge/yc-startup-school/module-2-assessment.md` in the user's project root

## Key Topics

- **4 most common mistakes**: Waiting for amazing idea / jumping too fast / solution-in-search-of-a-problem (SISP) / believing ideas are hard to find
- **Idea quality score formula (4 criteria)**: Market size + Founder/market fit + Problem certainty + New insight — average the scores
- **Good idea signals**: Making something you personally want, only recently became possible, successful similar companies exist elsewhere
- **4 dangerous filters** (turn these off): Ideas that seem hard to start (schlep blindness) / boring spaces / too ambitious / existing competitors
- **Organic vs. explicit idea generation**: Organic ideas are more likely to be good; explicit generation is a backup
- **7 recipes ranked best to worst**:
  1. Start from your unfair advantage (best)
  2. Things you wish someone else would build
  3. Things you'd work on for 10 years even if they failed
  4. Recent changes in the world
  5. Successful companies with new variants (default skeptical)
  6. Crowdsource from domain experts
  7. Broken industries (worst unless you have domain expertise)
- **Tarpit ideas**: Problems that seem like good ideas but have hidden fatal flaws; many founders get stuck here

## Output Format

### Part 1: Module Summary
- The 4 mistakes and why each is deadly
- The idea quality score formula with real examples (Coinbase, Airbnb, Flexport)
- The 4 filters to disable — with the Stripe/schlep blindness story
- The 7 recipes with clear ranking and cautions

### Part 2: Apply to Your Situation (Idea Evaluation)
If the user has an idea, score it on all 4 criteria (1-10 scale):
- Market size: Are there existing large companies doing something similar?
- Founder/market fit: What's your unfair advantage here?
- Problem certainty: Do you have personal experience with this pain?
- New insight: What do you know that others don't or are wrong about?

Identify which of the 7 recipes this idea came from, and flag any dangerous filters that may be distorting evaluation.

### Part 3: Self-Assessment Workbook
Generate 6-8 questions drawn directly from the lecture:

1. What are 3 companies you've worked at? For each: what did you learn that others don't know / what seemed broken / what did they build in-house that others need?
2. What's a product or service you desperately wish existed for yourself?
3. What recent technological or regulatory change has created an opportunity that didn't exist 2 years ago?
4. Which of the 4 filters (hard to start / boring / too ambitious / competitors) do you notice yourself applying most often? Give a concrete example.
5. If you were to evaluate your current best idea on the 4-criteria formula, what score would each criterion get and why?
6. Can you name a successful company doing something similar in another geography or vertical — what's the variant you could build?
7. Who are the domain experts in your network you could spend 30 minutes with to crowdsource problem ideas?

## References

- Transcript: `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-2/how-to-get-startup-ideas.md`
  - Author: Jared Friedman (YC Partner)
  - Key examples: Google, Facebook (good execution > brilliant idea), Airbnb, Coinbase, Stripe (schlep blindness), Dropbox (competitors as validation), DoorDash, Rappi, Flexport, Mixpanel, Gusto, PlanGrid, Standard Cognition
