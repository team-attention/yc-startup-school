#!/usr/bin/env python3
"""
YC Library Transcript Scraper

Extracts transcripts from ycombinator.com/library pages
by parsing the data-page JSON attribute in server-rendered HTML.
"""

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.request


def fetch_article(slug: str) -> dict | None:
    """Fetch article data from YC Library page."""
    url = f"https://www.ycombinator.com/library/{slug}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw_html = resp.read().decode("utf-8")
        match = re.search(r'data-page="([^"]*)"', raw_html)
        if not match:
            return None
        decoded = html.unescape(match.group(1))
        data = json.loads(decoded)
        return data["props"]["article"]
    except Exception as e:
        print(f"  ERROR fetching {slug}: {e}", file=sys.stderr)
        return None


def fetch_library_carousel(carousel_name: str) -> list[dict]:
    """Fetch all articles from a named carousel on the library page."""
    url = "https://www.ycombinator.com/library"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw_html = resp.read().decode("utf-8")
    match = re.search(r'data-page="([^"]*)"', raw_html)
    if not match:
        return []
    decoded = html.unescape(match.group(1))
    data = json.loads(decoded)
    for carousel in data["props"]["carousels"]:
        if carousel["name"] == carousel_name:
            return carousel["articles"]
    return []


def article_to_markdown(article: dict, series: str) -> str:
    """Convert article dict to markdown with YAML frontmatter."""
    title = article.get("title", "")
    author = article.get("author", "")
    slug = article.get("slug", "")
    description = article.get("description", "")
    youtube_id = article.get("youtube_id", "")
    categories = article.get("categories", [])
    duration = article.get("video_duration")
    transcript = article.get("transcript") or ""
    chapters = article.get("video_chapters") or []
    created_at = article.get("created_at", "")

    youtube_url = f"https://www.youtube.com/watch?v={youtube_id}" if youtube_id else ""
    source_url = f"https://www.ycombinator.com/library/{slug}"

    # Build frontmatter
    lines = ["---"]
    lines.append(f'title: "{title}"')
    lines.append(f'author: "{author}"')
    lines.append(f'slug: "{slug}"')
    lines.append(f'series: "{series}"')
    if youtube_id:
        lines.append(f'youtube_id: "{youtube_id}"')
        lines.append(f'youtube_url: "{youtube_url}"')
    lines.append(f'source_url: "{source_url}"')
    if description:
        lines.append(f'description: "{description}"')
    if categories:
        cats = ", ".join(f'"{c}"' for c in categories)
        lines.append(f"categories: [{cats}]")
    if duration:
        lines.append(f"duration_seconds: {duration}")
    if created_at:
        lines.append(f'created_at: "{created_at}"')
    if chapters:
        lines.append("chapters:")
        for ch in chapters:
            if isinstance(ch, list) and len(ch) >= 2:
                lines.append(f'  - time: {ch[0]}')
                lines.append(f'    title: "{ch[1]}"')
    has_transcript = len(transcript.strip()) > 0
    lines.append(f"has_transcript: {str(has_transcript).lower()}")
    lines.append("---")
    lines.append("")

    # Title
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"**{author}**")
    if youtube_url:
        lines.append(f"[YouTube]({youtube_url}) | [YC Library]({source_url})")
    else:
        lines.append(f"[YC Library]({source_url})")
    lines.append("")

    # Transcript
    if transcript.strip():
        lines.append("## Transcript")
        lines.append("")
        lines.append(transcript.strip())
    else:
        lines.append("## Transcript")
        lines.append("")
        lines.append("_Transcript not available. Watch the video above._")

    lines.append("")
    return "\n".join(lines)


def slugify(title: str) -> str:
    """Convert title to filesystem-safe name."""
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")[:80]


def scrape_carousel(carousel_name: str, output_dir: str, series: str):
    """Scrape all articles from a carousel and save to output_dir."""
    print(f"\n{'='*60}")
    print(f"Scraping: {carousel_name}")
    print(f"Output:   {output_dir}")
    print(f"{'='*60}")

    articles = fetch_library_carousel(carousel_name)
    print(f"Found {len(articles)} articles in carousel")

    os.makedirs(output_dir, exist_ok=True)

    stats = {"ok": 0, "no_transcript": 0, "error": 0}

    for i, brief in enumerate(articles):
        slug = brief["slug"]
        title = brief.get("title", slug)
        print(f"\n[{i+1}/{len(articles)}] {title}")

        article = fetch_article(slug)
        if not article:
            stats["error"] += 1
            continue

        md = article_to_markdown(article, series)
        filename = f"{slugify(title)}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md)

        transcript = article.get("transcript") or ""
        if transcript.strip():
            stats["ok"] += 1
            print(f"  OK  {len(transcript):>6} chars → {filename}")
        else:
            stats["no_transcript"] += 1
            print(f"  NO TRANSCRIPT → {filename}")

        time.sleep(0.5)  # polite delay

    print(f"\nDone: {stats['ok']} with transcript, {stats['no_transcript']} without, {stats['error']} errors")
    return stats


def scrape_pg_essays(output_dir: str):
    """Scrape Paul Graham essays from YC Library carousel."""
    return scrape_carousel("Essays by Paul Graham", output_dir, "Paul Graham Essays")


def main():
    parser = argparse.ArgumentParser(description="Scrape YC Library transcripts")
    parser.add_argument(
        "target",
        choices=["startup-school", "ai-startup-school", "pg-essays", "all"],
        help="Which content to scrape",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Base output directory (default: ./transcripts/)",
    )
    args = parser.parse_args()

    base = args.output_dir or os.path.join(os.path.dirname(os.path.dirname(__file__)), "transcripts")

    targets = {
        "startup-school": ("Startup School", os.path.join(base, "startup-school"), "Startup School"),
        "ai-startup-school": ("AI Startup School", os.path.join(base, "ai-startup-school"), "AI Startup School"),
        "pg-essays": ("Essays by Paul Graham", os.path.join(base, "pg-essays"), "Paul Graham Essays"),
    }

    if args.target == "all":
        for key in targets:
            carousel_name, out_dir, series = targets[key]
            scrape_carousel(carousel_name, out_dir, series)
    else:
        carousel_name, out_dir, series = targets[args.target]
        scrape_carousel(carousel_name, out_dir, series)


if __name__ == "__main__":
    main()
