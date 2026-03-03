# Financial Research Agent

Autonomous agent for stock news retrieval and sentiment analysis.

## Pipeline
1. **Intake**: Collects ticker symbol (e.g. `AAPL`) and analysis window (e.g. `7` days).
2. **Researcher**: Fetches news using `news_by_company`, checks sentiment, and summarizes.
3. **Analyst**: Generates a Markdown report and saves it for download.

## Usage
- Start the agent and provide input in JSON format:
  ```json
  { "ticker": "TSLA", "analysis_window_days": 7 }
  ```
- The agent will produce a `<TICKER>_report.md` in its data directory.

## Constraints
- Concise reasoning to avoid rate limits.
- `max_tokens` set to ~1200 per turn.
