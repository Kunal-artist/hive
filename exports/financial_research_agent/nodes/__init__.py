"""Node definitions for the Financial Research Agent."""

from framework.graph import NodeSpec

# Node 1: Intake (client-facing)
intake_node = NodeSpec(
    id="intake",
    name="Intake",
    description="Collect stock ticker from user",
    node_type="event_loop",
    client_facing=True,
    max_node_visits=0,
    input_keys=["new_ticker"],
    output_keys=["ticker"],
    nullable_output_keys=["new_ticker"],
    success_criteria="The stock ticker is valid and ready for research.",
    system_prompt="""\
You are an intake specialist for financial research.

**STEP 1 — Present to user (text only, NO tool calls):**
- Greet the user and ask for the stock ticker they'd like to research.
- If it's a new ticker from a previous loop (in `new_ticker`), confirm if they'd like to analyze that or something else.

**STEP 2 — After user responds, call set_output:**
- set_output("ticker", "[TICKER_SYMBOL]")
""",
    tools=[],
)

# Node 2: Researcher (autonomous)
researcher_node = NodeSpec(
    id="researcher",
    name="Researcher",
    description="Perform autonomous research and analysis",
    node_type="event_loop",
    max_node_visits=0,
    input_keys=["ticker"],
    output_keys=["report_text", "report_filename"],
    success_criteria="Research is complete and Markdown report is saved.",
    system_prompt="""\
You are a lead financial researcher. Given a stock ticker, analyze recent performance and sentiment.

**Task Sequence:**
1. Use `news_by_company` to fetch headlines from the last 7 days.
2. Use `news_sentiment` for the ticker symbol to gauge overall market mood.
3. Synthesize this into a structured Markdown report including:
   - Recent News Highlights (last 7 days)
   - Sentiment Analysis
   - Research Conclusion (Investment-style overview)

**Persistence:**
- Generate a filename like `[ticker]_report.md`.
- Call `save_data` to write the Markdown report.
- Call `set_output("report_filename", "[filename]")`.
- Call `set_output("report_text", "[Markdown Content]")` in a SEPARATE turn.
""",
    tools=["news_by_company", "news_sentiment", "save_data"],
)

# Node 3: Analyst (client-facing)
analyst_node = NodeSpec(
    id="analyst",
    name="Analyst",
    description="Present report and provide file access",
    node_type="event_loop",
    client_facing=True,
    max_node_visits=0,
    input_keys=["report_text", "report_filename"],
    output_keys=["new_ticker"],
    success_criteria="User has reviewed the report and decided next steps.",
    system_prompt="""\
You are a presentation analyst. 

**STEP 1 — Present (text only, NO tool calls):**
1. Display the full Markdown report (`report_text`) in the chat.
2. Inform the user that the report has been saved as `report_filename`.
3. Provide a link using `serve_file_to_user(filename=report_filename, label="Download Report")`.
4. Ask if they'd like to research a different ticker.

**STEP 2 — After user responds, call set_output:**
- set_output("new_ticker", "[next_ticker_or_done]")
""",
    tools=["serve_file_to_user"],
)

__all__ = ["intake_node", "researcher_node", "analyst_node"]
