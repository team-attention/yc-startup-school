# YC Startup School for Claude Code

> Engineering is being conquered. What's left is taste and business.
> This plugin turns YC's entire startup curriculum into interactive AI-guided workbooks.

---

### Without this plugin

You watch YC lectures. You take notes. You forget them. You never apply the frameworks to *your* startup. The gap between knowing and doing stays wide.

### With this plugin

You type `/yc-4` and Claude reads the full transcript of "How to Talk to Users", analyzes *your* project, and asks you the hard questions — one at a time — that Gustaf Alstromer would ask. Then saves your answers as a structured assessment.

---

## What's Inside

**54 full transcripts** from YC's official library. Not summaries. Not notes. The actual words.

| Skill | What it does | Lectures |
|-------|-------------|----------|
| `/yc-1` | Deciding to start a startup | Harj Taggar + 2 PG essays |
| `/yc-2` | Getting and evaluating ideas | Jared Friedman + PG essay |
| `/yc-3` | Building your founding team | Co-founders, equity, working together |
| `/yc-4` | Planning an MVP | Talk to users, build MVP, technical founders |
| `/yc-5` | Launching | Launch strategy, first customers, PG essay |
| `/yc-6` | Growing and monetizing | KPIs, business models, metrics |
| `/yc-7` | Fundraising | How fundraising works, applying to YC |
| `/yc-8` | Stories from great founders | Zuckerberg, Wojcicki |
| `/yc-ai` | AI Startup School | Karpathy, Altman, Musk, Nadella + 11 more |
| `/pg` | Paul Graham Guru | 14 essays. Ask anything, get PG's voice. |

Each skill has its own `references/` folder with the full transcripts co-located. The skill **reads its references** → **presents frameworks** → **analyzes your project** → **interactive workbook with AskUserQuestion** → **saves assessment**.

---

## Install

Paste this into Claude Code:

```
Install the yc-startup-school plugin from /path/to/yc-startup-school
```

Or via marketplace:

```bash
claude plugin marketplace add https://github.com/team-attention/yc-startup-school
claude plugin install yc-startup-school
```

---

## How Each Skill Works

```
You: /yc-2

Claude: [reads full transcript of "How to Get Startup Ideas" by Jared Friedman]
        [reads PG's "How to Get Startup Ideas" essay]
        [reads your CLAUDE.md to understand your project]

        Part 1: Here are the 4 filters Jared teaches...
        Part 2: Applying to your project — you're strong on X, missing Y...
        Part 3: Let me ask you question 1 of 7...

        Q: "What problem are you solving, and did you discover it
            from personal experience or brainstorming?"
            a) Personal experience — I lived this problem
            b) Observed others struggling with it
            c) Brainstormed / market research
            d) Someone told me about it

You: a

Claude: Good — that matches Jared's "founder-market fit" pattern.
        Airbnb, Stripe, Dropbox all started this way.
        Next question...
```

After all questions, you get a synthesis with a readiness score, strengths, gaps, and one action item. Saved to `knowledge/yc-startup-school/`.

---

## The `/pg` Skill

Ask Paul Graham anything. Claude reads all 14 essays and channels PG's voice:

```
You: /pg 우리 비즈니스 모델이 좀 복잡한데 괜찮을까?

Claude: [reads all 14 PG essays]

        PG would say: "If you can't explain your business model
        in one sentence, you don't have one yet. The most valuable
        truths are the ones most people don't believe. Stop trying
        to be clever about revenue — make something people want,
        and the money follows. 100% of startups that make something
        popular manage to make money from it."

        Let me diagnose your situation...
```

---

## Project Structure

```
skills/
  yc-1-deciding-to-start-a-startup/
    SKILL.md              ← skill definition
    references/           ← co-located transcripts
  yc-2-getting-and-evaluating-startup-ideas/
    SKILL.md
    references/
  ...
  ai-startup-school/
    SKILL.md
    references/           ← 15 AI leader transcripts
  guru-paul-graham/
    SKILL.md
    references/           ← 14 PG essays
references/bonus/         ← extra lectures not in official curriculum
scripts/                  ← scraper
```

## Data Sources

All transcripts extracted from `ycombinator.com/library` server-rendered JSON. Paul Graham essays from `paulgraham.com`. Scraper included: `scripts/scrape_yc_library.py`.

```bash
# Re-scrape to update
python3 scripts/scrape_yc_library.py all
```

---

## Why I Built This

Engineering is getting solved. Cursor, Claude Code, Copilot — the gap between idea and code is collapsing. But the gap between idea and *good* idea? Between building and building *the right thing*? That's widening.

I wanted to vibe-code my business decisions the way I vibe-code my software. Not by asking ChatGPT generic questions, but by having the actual YC curriculum — the specific words of Harj Taggar, Jared Friedman, Gustaf Alstromer, Paul Graham — loaded into context and applied to my real situation.

This is v1. I'm experimenting. If you use it, break it, improve it — PRs welcome.

---

## Credits

- [Y Combinator](https://www.ycombinator.com/) — transcript content, used for educational purposes
- [Paul Graham](https://paulgraham.com/) — original essays
- Inspired by [ofou/graham-essays](https://github.com/ofou/graham-essays) and [garrytan/gstack](https://github.com/garrytan/gstack)

## License

MIT — Transcript content remains property of respective authors/Y Combinator.

---

*Built by [Team Attention](https://github.com/team-attention) — the guild that ships AI tools for builders.*
