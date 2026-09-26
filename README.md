# StoneSignal

A runnable prototype for a lab-grown engagement-ring quote audit. Buyers enter a ring profile and receive a transparent **fictional** comparison band, risk flags, and verification checklist.

## Run

```bash
npm ci
npm run dev
```

```bash
cd api
uv sync --frozen
uv run uvicorn main:app --reload
```

## Verify

```bash
npm run typecheck
npm run test:e2e
npm run build
npm run audit:prod
cd api && uv run pytest
```

The GitHub Pages deployment is frontend-only. The Python/FastAPI backend is runnable and tested source; it is not publicly deployed. No paid APIs or live appraisal data are used.

## Source and limitations

Inspired by Ideabrowser’s public idea page: https://www.ideabrowser.com/hub/ideas/a-24-hour-verdict-on-an-engagement-ring-ed6f38ca. This repo summarizes the concept and contains no private newsletter text, tracking links, or personal email metadata. See `research/notes.md` and `docs/`.
