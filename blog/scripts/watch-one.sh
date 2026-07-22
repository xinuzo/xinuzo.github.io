#!/usr/bin/env bash
# Dev server rendering only a single post by slug.
# Usage: ./scripts/watch-one.sh <slug>
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <slug>"
  exit 1
fi

SLUG="$1"
cd "$(dirname "$0")/.."

# Find the matching article file
FILE=$(find content -name "*-${SLUG}.md" -not -path "content/pages/*" | head -1)
if [ -z "$FILE" ]; then
  echo "Error: No article found matching slug '$SLUG'"
  exit 1
fi

# Use ARTICLE_PATHS to render only this one file
ARTICLE_PATHS="[\"$FILE\"]" uv run pelican content --listen \
  -e "ARTICLE_PATHS=$ARTICLE_PATHS"
