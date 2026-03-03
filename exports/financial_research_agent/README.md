# Financial Research Agent

Autonomous agent for stock news retrieval and sentiment analysis.

## Pipeline
1. **Intake**: Collects ticker symbol (e.g. `AAPL`) and analysis window (e.g. `7` days).
2. **Researcher**: Fetches news using `news_by_company`, checks sentiment, and summarizes.
3. **Analyst**: Generates a Markdown report and saves it for download.

## Usage
- Start the agent and provide input in JSON format:
  ```json
  { "ticker": "AAPL", "analysis_window_days": 7 }
  ```
- The agent will produce a `<TICKER>_report.md` in its data directory.

## Constraints

- Designed to run on **free-tier LLM APIs**, which may impose strict request and token limits.
- `max_tokens` is limited to **~1200 per step** to reduce rate-limit issues.
- External news retrieval depends on **NewsData.io API availability and quota limits**.
- The researcher node was validated successfully; extended runs may encounter LLM rate limits before the analyst node completes when using free-tier providers.
- The agent prioritizes **concise, structured outputs** over verbose reasoning to maintain reliability within constrained API quotas.
