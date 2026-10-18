# AGENTS.md

Selenium bot that books desks/parking on deskbird.com. Flat Python project, no packages, no build system.

## Commands

- Setup: `python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt` (README targets Windows-bash venv activation; on Linux use `source venv/bin/activate`)
- Run: `python main.py` from the repo root (entrypoint `main.py` -> `bot.reservar()`)
- There are no tests, linters, formatters, or CI. Do not invent verification commands; the only check is a real run against deskbird.

## Setup requirements

- Copy `.env.example` to `.env`: `CHROMIUM_BINARY`, `CHROMEDRIVER_PATH` (must match browser version), `CHROME_USER_DATA_DIR` + `CHROME_PROFILE`. Without a persistent profile the Deskbird session is lost and every run requires manual login.
- `HEADLESS`, `TIMEOUT`, `LOGGING_LEVEL`, `RESERVAS`, `HOME`, `MESES` live in `settings.py`, not in `.env`.
- `settings.py` runs `load_dotenv()` at import time.

## Architecture

- `bot.py` — driver setup, date logic (weekend + `HOME` telework days are skipped), reservation loop.
- `reservas_page.py` — Page Object; **all** UI selectors (`data-testid`, XPath text matches) live here. When Deskbird changes its UI, fix only this file.
- `settings.py` — all config, including `RESERVAS` list of `ReservaConfig`.

## Conventions and gotchas

- Selector failures save a screenshot to `capturas/<step_name>.png` (gitignored). Read the screenshot to debug before touching selectors.
- `MESES` is English ("January"...) on purpose: the calendar month picker is matched by English text.
- `HOME = [1, 4]` uses `weekday()` indices (0=Monday), so Tuesday and Friday are skipped.
- Each step in `reservas_page.py` logs, screenshots, and re-raises; `bot.py` catches per-reservation errors, so one failed booking doesn't stop the rest.
- Code and log messages are in Spanish; keep new identifiers/comments consistent with the file you edit.
- Commit style is loose (`fix:`/`feature:` prefixes appear sometimes, Spanish descriptions common).

## README caveats

- README says selenium is the only dependency; `requirements.txt` also pins `python-dotenv==1.0.1`. Trust `requirements.txt`.

## IMPORTANT

- NEVER compile the code
