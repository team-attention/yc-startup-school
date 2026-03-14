---
name: ai-startup-school
description: |
  This skill should be used when the user mentions "AI 스타트업", "AI startup school", "AI 트렌드", "소프트웨어 3.0", "/yc-ai", "AI 창업", "AI 산업 트렌드", "AI 빌더", "Karpathy", "Sam Altman", "AGI", "vibe coding", or asks about insights from top AI leaders. Use this skill to synthesize knowledge from 15 AI Startup School transcripts (Karpathy, Altman, Musk, Nadella, Fei-Fei Li, Chollet, Ng, Srinivas, Jumper, Finn, Kaplan, Field, Truell, Masad, and panel) and apply them to the user's current AI work or startup context.
---

# AI Startup School — Synthesized Insights from the Top Minds

This skill reads all 15 AI Startup School transcripts and synthesizes the key cross-cutting insights from the world's top AI leaders. Apply these insights to the user's current AI-related work, startup strategy, or product decisions.

## Transcript Files

All transcripts are located at `${CLAUDE_PLUGIN_ROOT}/transcripts/ai-startup-school/`:

1. `andrej-karpathy-software-is-changing-again.md` — Software 3.0, LLMs as new compute layer
2. `andrew-ng-building-faster-with-ai.md` — AI-augmented workflows, iteration speed
3. `aravind-srinivas-the-race-to-build-the-ai-browser-of-the-future.md` — AI-native products, Perplexity story
4. `chelsea-finn-building-robots-that-can-do-anything.md` — Robotics, generalist AI agents
5. `elon-musk-digital-superintelligence-multiplanetary-life-how-to-be-useful.md` — First principles, civilizational scale
6. `every-ai-founder-should-be-asking-these-questions.md` — Panel: founder mindset, key questions
7. `fei-fei-li-spatial-intelligence-is-the-next-frontier-in-ai.md` — Spatial intelligence, embodied AI
8. `figma-ceo-dylan-field-how-ai-will-transform-design.md` — AI-native product design, incumbents vs. startups
9. `franois-chollet-the-arc-prize-how-we-get-to-agi.md` — ARC Prize, measuring true intelligence, AGI paths
10. `john-jumper-alphafold-and-the-future-of-science.md` — AI for science, AlphaFold, deep tech
11. `michael-truell-building-cursor-at-23-taking-on-github-copilot-and-advice-to-engi.md` — Vibe coding, Cursor story, AI-native dev tools
12. `sam-altman-the-future-of-openai-chatgpts-origins-and-building-ai-hardware.md` — OpenAI roadmap, AI hardware, AGI timeline
13. `satya-nadella-microsofts-ai-bets-hyperscaling-quantum-computing-breakthroughs.md` — Hyperscaling, enterprise AI, infra bets
14. `scaling-and-the-road-to-human-level-ai-anthropic-co-founder-jared-kaplan.md` — Scaling laws, human-level AI roadmap
15. `the-future-of-software-creation-with-replit-ceo-amjad-masad.md` — No-code/low-code future, AI-native creation

## Instructions

### Step 1: Read All Transcripts

Read ALL 15 transcript files from `${CLAUDE_PLUGIN_ROOT}/transcripts/ai-startup-school/` before generating any response. Do not skip files — cross-transcript synthesis is the core value of this skill.

### Step 2: Understand the User's Context

Before synthesizing, understand what the user is working on:
- Are they building an AI product? Which stage?
- Are they evaluating a technology bet (infra, model, agent, etc.)?
- Are they thinking about positioning, competition, or timing?
- Are they looking for inspiration or validation?

If context is unclear from the conversation, infer from recent files or ask one focused question.

### Step 3: Synthesize Across Themes

Organize insights around the major cross-cutting themes that emerge from the transcripts:

**Theme 1: Software 3.0 / The New Programming Paradigm**
- Karpathy's framing: LLMs are a new layer of compute; natural language is the new programming interface
- Truell (Cursor): "Vibe coding" as the emergent behavior — non-engineers shipping real software
- Masad (Replit): Software creation democratized; who builds software is changing

**Theme 2: AGI Paths and Timelines**
- Altman, Kaplan, Chollet disagree productively: scaling vs. architectural breakthroughs vs. general intelligence benchmarks
- Chollet's ARC Prize as the honest AGI test — current LLMs fail at systematic generalization
- Kaplan's scaling laws: predictable capability gains, but diminishing returns per compute dollar

**Theme 3: AI Hardware and Infrastructure**
- Altman: OpenAI building own chips; inference cost curves matter for product economics
- Nadella: Hyperscaling is real, but enterprise adoption is the next bottleneck
- Srinivas: Model costs collapsing → new product opportunities at the application layer

**Theme 4: Embodied AI and Physical World**
- Fei-Fei Li: Spatial intelligence as the missing frontier — AI that understands 3D physical space
- Finn: Generalist robots require the same paradigm shift as LLMs; data is the constraint
- Jumper: AlphaFold shows AI solving century-old science problems — the physical world is the next domain

**Theme 5: AI-Native Products vs. AI-Wrapped Products**
- Field (Figma): AI changes what products are possible, not just how they're built
- Srinivas: Being AI-native from day 1 is a durable advantage incumbents can't fully replicate
- Truell: Cursor succeeded by re-thinking the entire IDE, not adding AI to VS Code

**Theme 6: What AI Founders Should Prioritize**
- Ng: Build faster with AI; iteration speed is the new moat
- Panel ("Every AI founder should be asking"): distribution, defensibility, timing, data flywheels
- Musk: First-principles thinking; don't optimize existing systems — question the system itself

### Step 4: Apply to User's Situation

Map the most relevant 2–3 themes to the user's specific context. Be direct:
- "Given you're building X, Karpathy's Software 3.0 framing is directly applicable because..."
- "The tension Chollet raises between scaling and true generalization matters here because..."
- "Srinivas's point about AI-native products vs. AI-wrapped products is exactly the decision you're facing..."

### Step 5: Highlight Actionable Takeaways

Close with 3–5 concrete, prioritized actions for the user as an AI founder or builder:
- Specific product decisions to make or revisit
- Technology bets to consider or avoid
- Positioning or narrative shifts
- Questions to test their own assumptions

## Output Format

Structure the response as follows:

```
## AI Startup School — Insights for [User's Context]

### Most Relevant Themes

**[Theme Name]** — [2-3 sentences synthesizing 2+ speakers on this theme and why it applies]

**[Theme Name]** — [same]

**[Theme Name]** — [same]

### Applied to Your Situation

[Direct application paragraph — specific, not generic]

### Actionable Takeaways

1. [Action] — [Why, citing specific speaker/insight]
2. [Action] — [Why]
3. [Action] — [Why]
```

Always cite specific speakers by name. Avoid generic AI enthusiasm — these speakers often disagree, and the disagreements are informative.

## References

- Transcript directory: `${CLAUDE_PLUGIN_ROOT}/transcripts/ai-startup-school/`
- 15 files covering: Karpathy, Ng, Srinivas, Finn, Musk, panel, Fei-Fei Li, Field, Chollet, Jumper, Truell, Altman, Nadella, Kaplan, Masad
