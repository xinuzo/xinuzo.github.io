#!/usr/bin/env bash
# List all draft posts.
set -euo pipefail

cd "$(dirname "$0")/.."
grep -rl "^status: draft" content/ 2>/dev/null | sort || echo "No drafts found."
