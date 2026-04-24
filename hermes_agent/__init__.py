"""Hermes Agent - A fork of NousResearch/hermes-agent.

An intelligent agent framework built around the Hermes model family,
supporting tool use, function calling, and multi-step reasoning.

Personal fork notes:
- Using this for experimenting with custom tool integrations
- Upstream: https://github.com/NousResearch/hermes-agent
"""

__version__ = "0.1.0"
__author__ = "Hermes Agent Contributors"
__license__ = "Apache-2.0"

from hermes_agent.agent import HermesAgent
from hermes_agent.config import AgentConfig

__all__ = [
    "HermesAgent",
    "AgentConfig",
    "__version__",
]
