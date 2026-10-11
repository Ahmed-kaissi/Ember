@echo off
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  echo Python 3 is required to open Ember. Install it, then try again.
  pause
  exit /b 1
)
if not exist "serve_ember.py" (
  echo Ember files are missing. Re-extract the complete ember-ai-package.zip and keep its files together.
  pause
  exit /b 1
)
if not exist "ember-ai.html" (
  echo Ember files are missing. Re-extract the complete ember-ai-package.zip and keep its files together.
  pause
  exit /b 1
)
py -3 serve_ember.py
if errorlevel 1 pause
