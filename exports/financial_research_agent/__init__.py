"""Financial Research Agent — Autonomous stock analysis and reporting."""

from .agent import (
    FinancialResearchAgent,
    default_agent,
    goal,
    nodes,
    edges,
    entry_node,
    entry_points,
    pause_nodes,
    terminal_nodes,
    conversation_mode,
    identity_prompt,
    loop_config,
)
from .config import default_config, metadata

__all__ = [
    "FinancialResearchAgent",
    "default_agent",
    "goal",
    "nodes",
    "edges",
    "entry_node",
    "entry_points",
    "pause_nodes",
    "terminal_nodes",
    "conversation_mode",
    "identity_prompt",
    "loop_config",
    "default_config",
    "metadata",
]
