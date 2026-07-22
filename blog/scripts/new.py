#!/usr/bin/env python3
"""Create a new blog post with proper frontmatter."""

import sys
from datetime import date
from pathlib import Path
from textwrap import dedent

CONTENT_DIR = Path(__file__).parent.parent / "content"
CATEGORIES = sorted(
    d.name for d in CONTENT_DIR.iterdir() if d.is_dir() and d.name != "pages"
)


def main() -> None:
    print("Available categories:", ", ".join(CATEGORIES) if CATEGORIES else "(none yet)")
    category = input("Category (or new name): ").strip()
    if not category:
        print("Cancelled.")
        sys.exit(1)

    slug = input("Slug (URL-friendly name): ").strip()
    if not slug:
        print("Cancelled.")
        sys.exit(1)

    title = input("Title: ").strip() or slug.replace("-", " ").title()
    tags = input("Tags (comma-separated): ").strip()

    # Use a far-future date for drafts
    draft_date = "2099-12-31 00:00"

    cat_dir = CONTENT_DIR / category
    cat_dir.mkdir(parents=True, exist_ok=True)
    filepath = cat_dir / f"{date.today().isoformat()}-{slug}.md"

    content = dedent(f"""\
        ---
        title: {title}
        date: {draft_date}
        slug: {slug}
        tags: {tags}
        status: draft
        ---

        Write your post here.
    """)

    filepath.write_text(content, encoding="utf-8")
    print(f"Created: {filepath}")


if __name__ == "__main__":
    main()
