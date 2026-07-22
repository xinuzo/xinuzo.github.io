#!/usr/bin/env bash
# Dev server rendering only recent posts (last N days, default 365).
# Usage: ./scripts/recent.sh [N]
set -euo pipefail

DAYS="${1:-365}"
cd "$(dirname "$0")/.."
RECENT_DAYS="$DAYS" uv run pelican content -s recentconf.py --listen
