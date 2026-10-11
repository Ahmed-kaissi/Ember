#!/bin/sh
cd "$(dirname "$0")" || exit 1
if ! command -v python3 >/dev/null 2>&1; then
  printf '%s\n' 'Python 3 is required to open Ember. Install it, then try again.'
  printf '%s' 'Press Return to close...'
  read -r _
  exit 1
fi
if [ ! -f "serve_ember.py" ] || [ ! -f "ember-ai.html" ]; then
  printf '%s\n' 'Ember files are missing. Re-extract the complete ember-ai-package.zip and keep its files together.'
  printf '%s' 'Press Return to close...'
  read -r _
  exit 1
fi
exec python3 "serve_ember.py"
