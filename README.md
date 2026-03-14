# YC Startup School — Complete Transcript Archive

YC Startup School, AI Startup School, and Paul Graham Essays의 전체 transcript/essay를 구조화된 Markdown 파일로 보관합니다.

## Contents

| Directory | Series | Files | With Transcript |
|-----------|--------|-------|-----------------|
| `transcripts/startup-school/` | Startup School | 25 | 22 |
| `transcripts/ai-startup-school/` | AI Startup School | 15 | 15 |
| `transcripts/pg-essays/` | Paul Graham Essays | 14 | 14 |
| **Total** | | **54** | **51** |

## File Format

모든 파일은 YAML frontmatter + Markdown body:

```yaml
---
title: "How to get startup ideas"
author: "Jared Friedman"
slug: "8g-how-to-get-startup-ideas"
series: "Startup School"
youtube_id: "Th8JoIan4dg"
youtube_url: "https://www.youtube.com/watch?v=Th8JoIan4dg"
source_url: "https://www.ycombinator.com/library/8g-how-to-get-startup-ideas"
categories: ["Getting Ideas", "Idea Evaluation"]
duration_seconds: 1920
has_transcript: true
---
```

## Data Source

- **Transcripts**: `ycombinator.com/library` server-rendered `data-page` JSON에서 추출
- **PG Essays**: `paulgraham.com` 원문 HTML에서 추출
- **Scraper**: `scripts/scrape_yc_library.py`

## Credits

- Transcript content: [Y Combinator](https://www.ycombinator.com/) — used for educational purposes
- Paul Graham essays: [paulgraham.com](https://paulgraham.com/) — original essays by Paul Graham
- Scraper approach inspired by [ofou/graham-essays](https://github.com/ofou/graham-essays) (930+ stars, MIT License)

## Usage

```bash
# Scrape all content (re-run to update)
python3 scripts/scrape_yc_library.py all

# Scrape specific series
python3 scripts/scrape_yc_library.py startup-school
python3 scripts/scrape_yc_library.py ai-startup-school
python3 scripts/scrape_yc_library.py pg-essays
```

## License

MIT — Transcript content remains property of respective authors/Y Combinator.
