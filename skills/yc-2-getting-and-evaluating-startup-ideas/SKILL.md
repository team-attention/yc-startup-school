---
name: yc-2-getting-and-evaluating-startup-ideas
description: |
  This skill should be used when the user asks about "아이디어 검증", "스타트업 아이디어", "startup ideas", "tarpit", "아이디어 찾는 방법", "좋은 아이디어인지", "/yc-2", "피벗", "아이디어 평가", "idea evaluation", or any question about generating, evaluating, or pivoting startup ideas. YC Startup School Module 2: Getting and Evaluating Startup Ideas — Jared Friedman's systematic framework backed by patterns from thousands of YC companies, plus PG's canonical essay.
---

# YC Startup School — Module 2: Getting and Evaluating Startup Ideas

## Official Curriculum

- 📺 **How to Get and Evaluate Startup Ideas** — Jared Friedman (YC Partner) ✅ transcript available
- 📖 **How to Get Startup Ideas** — Paul Graham ✅ transcript available as `pg-how-to-get-startup-ideas.md` (also via `/pg` skill)
- 📺 **All About Pivoting** — Dalton Caldwell ❌ no transcript (video only)
- 📺 **Where Do Great Startup Ideas Come From?** — Dalton Caldwell & Michael Seibel ❌ no transcript (video only)

## Instructions

1. Read ALL transcript files from `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-2/`:
   - `how-to-get-startup-ideas.md` — Jared Friedman (YC Partner)
   - `pg-how-to-get-startup-ideas.md` — Paul Graham
2. Present the key frameworks and mental models with speaker attribution
3. If the user has an idea, score it on the 4-criteria formula and identify which recipe it came from
4. Generate a workbook-style self-assessment derived from the lectures
5. Save to `knowledge/yc-startup-school/module-2-assessment.md`
6. Run the interactive Self-Assessment Workbook:
   - Ask each question ONE AT A TIME using AskUserQuestion
   - Wait for the user's response before asking the next question
   - After each answer, provide brief feedback connecting their response to the module's frameworks
   - After all questions, synthesize their answers into a personalized assessment
7. Save the completed assessment (questions + answers + synthesis) to the appropriate knowledge path

## Key Frameworks

- **4 most common mistakes**: Waiting for the perfect idea / jumping too fast / solution-in-search-of-a-problem (SISP) / believing good ideas are hard to find
- **Idea quality score (4 criteria)**: Market size + Founder/market fit + Problem certainty + New insight — score each 1-10 and average
- **Good idea signals**: Making something you personally want; recently became possible; similar companies succeed elsewhere
- **4 dangerous filters to turn OFF**: Schlep blindness (hard to start) / boring / too ambitious / existing competitors
- **Organic vs. explicit generation**: Organic ideas (noticed while living your life) are more reliable than brainstormed ones
- **7 recipes ranked best to worst**:
  1. Start from your unfair advantage (best)
  2. Things you wish someone else would build
  3. Things you'd work on for 10 years even if they failed
  4. Recent changes in the world
  5. Successful companies with new variants (default skeptical)
  6. Crowdsource from domain experts
  7. Broken industries (worst unless you have domain expertise)
- **Tarpit ideas**: Problems that seem good but have hidden fatal flaws — distinguish from genuinely hard problems
- **PG's organic method**: Work on things that interest you; be at the leading edge of a field; notice what's missing

## Output Format

### Part 1: Module Content
- The 4 mistakes and why each is deadly (examples: Google, Facebook, Airbnb, Stripe/schlep blindness)
- The idea quality score formula with scoring examples
- The 4 filters to disable and how to recognize when you're applying them
- The 7 recipes with clear ranking and cautions
- PG's organic idea-finding method alongside Friedman's systematic approach

### Part 2: Apply to Your Situation
If the user has an idea, score it on all 4 criteria (1-10):
- Market size: Large companies doing something similar?
- Founder/market fit: What is your unfair advantage?
- Problem certainty: Personal experience with this pain?
- New insight: What do you know that others don't or are wrong about?

Identify which recipe the idea came from. Flag any dangerous filters distorting evaluation. Check for tarpit warning signs.

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
- Save completed workbook to `knowledge/yc-startup-school/module-2-workbook.md`

Questions to ask interactively:
1. What are 3 companies you've worked at? For each: what did you learn that others don't know / what seemed broken / what did they build in-house that others need?
2. What product or service do you desperately wish existed for yourself?
3. What recent technological or regulatory change created an opportunity that didn't exist 2 years ago?
4. Which filter do you apply most often — hard / boring / ambitious / competitors? Give a concrete example.
5. Score your current best idea on the 4 criteria. What's the weakest score and why?
6. Can you name a successful company doing something similar in another geography or vertical?
7. Who are domain experts in your network you could spend 30 minutes with to crowdsource problem ideas?

## References

- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-2/how-to-get-startup-ideas.md` — Jared Friedman (YC Partner)
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-2/pg-how-to-get-startup-ideas.md` — Paul Graham (also via `/pg` skill)
