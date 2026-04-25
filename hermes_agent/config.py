"""Configuration management for Hermes Agent.

Loads and validates environment variables and application settings.
"""

from __future__ import annotations

import os
from typing import Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # --- LLM / Model ---
    model_name: str = Field(
        default="NousResearch/Hermes-3-Llama-3.1-8B",
        description="HuggingFace model identifier or local path.",
    )
    model_max_tokens: int = Field(
        default=4096,
        description="Maximum number of tokens for model context window.",
    )
    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0,
        description="Sampling temperature for generation.",
    )
    top_p: float = Field(
        default=0.9,
        ge=0.0,
        le=1.0,
        description="Top-p (nucleus) sampling parameter.",
    )

    # --- API Keys ---
    openai_api_key: Optional[str] = Field(
        default=None,
        description="OpenAI API key (used when routing to OpenAI-compatible endpoints).",
    )
    openai_api_base: Optional[str] = Field(
        default=None,
        description="Base URL for OpenAI-compatible API endpoint.",
    )
    anthropic_api_key: Optional[str] = Field(
        default=None,
        description="Anthropic API key for Claude models.",
    )

    # --- Agent Behaviour ---
    max_iterations: int = Field(
        default=10,
        ge=1,
        description="Maximum number of reasoning/tool-use iterations per run.",
    )
    verbose: bool = Field(
        default=False,
        description="Enable verbose logging of agent steps.",
    )
    streaming: bool = Field(
        default=True,
        description="Stream tokens to stdout during generation.",
    )

    # --- Tool Configuration ---
    enable_web_search: bool = Field(
        default=False,
        description="Enable the web-search tool.",
    )
    serpapi_api_key: Optional[str] = Field(
        default=None,
        description="SerpAPI key required when enable_web_search is True.",
    )
    enable_code_execution: bool = Field(
        default=False,
        description="Allow the agent to execute Python code locally.",
    )

    # --- Storage ---
    memory_backend: str = Field(
        default="in_memory",
        description="Backend for conversation memory: 'in_memory' or 'redis'.",
    )
    redis_url: Optional[str] = Field(
        default=None,
        description="Redis connection URL (required when memory_backend='redis').",
    )

    # --- Logging ---
    log_level: str = Field(
        default="INFO",
        description="Python logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).",
    )

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        allowed = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        upper = v.upper()
        if upper not in allowed:
            raise ValueError(f"log_level must be one of {allowed}, got '{v}'")
        return upper

    @field_validator("memory_backend")
    @classmethod
    def validate_memory_backend(cls, v: str) -> str:
        allowed = {"in_memory", "redis"}
        if v not in allowed:
            raise ValueError(f"memory_backend must be one of {allowed}, got '{v}'")
        return v

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
        "extra": "ignore",
    }


# Module-level singleton — import this throughout the project.
settings = Settings()
