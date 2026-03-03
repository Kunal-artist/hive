"""Node definitions for the Financial Research Agent."""

from framework.graph import NodeSpec

# Node 1: Intake (client-facing)
intake_node = NodeSpec(
    id="intake",
    name="Intake",
    description="Collect parameters from user",
    node_type="event_loop",
    client_facing=True,
    max_node_visits=0,
    input_keys=["new_ticker"],
    output_keys=["ticker", "analysis_window_days"],
    nullable_output_keys=["new_ticker"],
    success_criteria="Ticker and window are validated.",
    system_prompt="""\
You are an intake specialist.

**STEP 1 — Present to user (text only, NO tool calls):**
- Ask for stock ticker and analysis window (default 7 days).
- Accept JSON: { "ticker": "AAPL", "analysis_window_days": 7 }

**STEP 2 — After user responds, call set_output:**
- set_output("ticker", "TICKER")
- set_output("analysis_window_days", DAYS)
""",
    tools=[],
)

# Node 2: Researcher (autonomous)
researcher_node = NodeSpec(
    id="researcher",
    name="Researcher",
    description="Fetch and analyze news",
    node_type="event_loop",
    max_node_visits=0,
    input_keys=["ticker", "analysis_window_days"],
    output_keys=["research_data"],
    success_criteria="News and sentiment analyzed.",
    system_prompt="""\
Analyze recent news and sentiment for the ticker. Keep reasoning concise.

1. `news_by_company` for ticker headlines.
2. `news_sentiment` for ticker mood.
3. `web_search` if news is sparse.

Summarize highlights and sentiment.
Call `set_output("research_data", DATA_JSON)`
""",
    tools=["news_by_company", "news_sentiment", "news_search"],
)

# Node 3: Analyst (client-facing)
analyst_node = NodeSpec(
    id="analyst",
    name="Analyst",
    description="Generate and present report",
    node_type="event_loop",
    client_facing=True,
    max_node_visits=0,
    input_keys=["research_data", "ticker"],
    output_keys=["new_ticker"],
    success_criteria="Report generated and saved.",
    system_prompt="""\
Generate a Markdown report:
1. Recent News Highlights
2. Sentiment Overview
3. Investment Outlook

Save as `<TICKER>_report.md` using `save_data`.
Call `serve_file_to_user` for download.

**STEP 1 — Present report text and download link.**
**STEP 2 — Ask for next ticker and call set_output("new_ticker", ...).**
""",
    tools=["save_data", "serve_file_to_user"],
)

__all__ = ["intake_node", "researcher_node", "analyst_node"]
