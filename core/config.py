"""Runtime configuration for the agent lab."""

from __future__ import annotations

import os

from pydantic import BaseModel, Field


DEFAULT_MODEL = "gpt-5.4-mini"


class AppConfig(BaseModel):
    openai_api_key: str = Field(min_length=1)
    model: str = DEFAULT_MODEL


def load_config() -> AppConfig:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "Missing OPENAI_API_KEY. Add it as a GitHub Actions repository secret."
        )

    model = os.getenv("OPENAI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    return AppConfig(openai_api_key=api_key, model=model)
