"""Reusable base class for simple OpenAI-powered agents."""

from __future__ import annotations

from abc import ABC, abstractmethod

from openai import OpenAI
from pydantic import BaseModel, Field

from core.config import AppConfig


class AgentInput(BaseModel):
    text: str = Field(min_length=1)


class AgentOutput(BaseModel):
    agent_name: str
    result: str


class BaseAgent(ABC):
    name = "base_agent"

    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.client = OpenAI(api_key=config.openai_api_key)

    @abstractmethod
    def build_prompt(self, agent_input: AgentInput) -> str:
        """Build the prompt that will be sent to the model."""

    def run(self, agent_input: AgentInput) -> AgentOutput:
        response = self.client.responses.create(
            model=self.config.model,
            input=self.build_prompt(agent_input),
        )
        result = response.output_text.strip()
        return AgentOutput(agent_name=self.name, result=result)
