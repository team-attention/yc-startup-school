---
name: yc-1-deciding-to-start-a-startup
description: |
  This skill should be used when the user asks about "창업 시작", "스타트업 시작해야 할까", "should I start a startup", "should I start", "창업할 준비가 됐는지", "/yc-1", "창업 결정", "FAANG 그만둬야 하나", or questions about founder resilience, worst-case analysis, and when to make the leap. YC Startup School Module 1: Deciding to Start a Startup — Harj Taggar's decision framework and Paul Graham's foundational essays on why to start.
---

# YC Startup School — Module 1: Deciding to Start a Startup

## Official Curriculum

- 📺 **Should You Start A Startup?** — Harj Taggar (YC Group Partner) ✅ transcript available
- 📺 **Why You Should Leave Your FAANG Job** — Dalton Caldwell & Michael Seibel ❌ no transcript (video only)
- 📖 **Why to Not Not Start a Startup** — Paul Graham ✅ transcript available (also via `/pg` skill)
- 📖 **Before the Startup** — Paul Graham ✅ transcript available (also via `/pg` skill)

## Instructions

1. Read ALL transcript files from `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-1/`:
   - `should-you-start-a-startup.md` — Harj Taggar (YC Group Partner)
   - `why-to-not-not-start-a-startup.md` — Paul Graham
   - `before-the-startup.md` — Paul Graham
2. Present the key frameworks and mental models with speaker attribution
3. Apply the worst-case analysis and resilience frameworks to the user's specific context
4. Generate a workbook-style self-assessment derived from the lectures
5. Save to `knowledge/yc-startup-school/module-1-assessment.md`
6. Run the interactive Self-Assessment Workbook:
   - Ask each question ONE AT A TIME using AskUserQuestion
   - Wait for the user's response before asking the next question
   - After each answer, provide brief feedback connecting their response to the module's frameworks
   - After all questions, synthesize their answers into a personalized assessment
7. Save the completed assessment (questions + answers + synthesis) to the appropriate knowledge path

## Key Frameworks

- **Resilience over credentials**: Traditional success signals (school, big company) are weak predictors. Benchling case study — Sajith, a quiet engineer → $6B company CEO through sheer resilience
- **Worst-case analysis**: "What do I have to lose?" as a real calculation, not rhetoric. Typical worst case: 1 year, below-market salary, valuable learning
- **Learning as hidden asset**: Startup experience has career value even if the startup fails (Rippling hires 50+ former founders)
- **Initial motivations don't matter**: Money, curiosity, passion — all valid; what matters is enduring motivation under pressure
- **Energy differential**: The gap between draining day job and energizing side work is the key "when to leap" signal
- **"Few people really love" heuristic** (Paul Buchheit): 1 passionate user beats 1M indifferent signups
- **PG's counterintuitive truths** (Before the Startup): Work on things that matter, work with people you respect, do things that seem dumb to others

## Output Format

### Part 1: Module Content
- Key frameworks with speaker attribution and direct quotes
- The worst-case framework with real numbers
- PG's counterintuitive list from "Before the Startup" and "Why to Not Not Start"

### Part 2: Apply to Your Situation
- Worst-case scenario analysis for the user's specific context (age, job, obligations)
- Resilience signals the user has already demonstrated
- Current environment: potential co-founders nearby?
- Energy differential check: draining job vs. energizing side work?

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
- Save completed workbook to `knowledge/yc-startup-school/module-1-workbook.md`

Questions to ask interactively:
1. What is your worst-case scenario if you started today — and can you genuinely live with it?
2. When you work on side projects, what does that energy feel like compared to your day job?
3. Who are the 2-3 smartest people you enjoy talking about ideas with — and are you around them regularly?
4. Have you pushed through significant rejection or failure before? What did that reveal about you?
5. What objection to starting do you keep coming back to? (PG: most objections are rationalizations)
6. If you didn't start now, what would need to be true in 1 year for you to feel ready?
7. Do you have a problem you personally have — not brainstormed, but lived?

## References

- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-1/should-you-start-a-startup.md` — Harj Taggar (YC Group Partner)
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-1/why-to-not-not-start-a-startup.md` — Paul Graham (also via `/pg` skill)
- `${CLAUDE_PLUGIN_ROOT}/transcripts/startup-school/module-1/before-the-startup.md` — Paul Graham (also via `/pg` skill)
