#!/bin/bash

# Get the absolute path of the project root
PROJECT_ROOT=$(cd "$(dirname "$0")/.." && pwd)

# Run the Discord chat extractor with the correct Python path
cd "$PROJECT_ROOT" && PYTHONPATH="$PROJECT_ROOT" uv run scripts/extract_discord_chat.py 