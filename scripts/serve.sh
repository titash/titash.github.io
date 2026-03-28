#!/usr/bin/env bash
# kills any existing mkdocs serve process, then starts mkdocs server in watch mode
pkill -f "mkdocs serve" 2>/dev/null || true
echo "Starting MkDocs server..."
uv run mkdocs serve
