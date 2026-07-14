"""Simple business summarization agent."""

from __future__ import annotations

from agents.base_agent import AgentInput, AgentOutput, BaseAgent
from core.config import AppConfig


BUSINESS_TEXT = (
    "A small consulting studio wants to use AI agents to research business ideas, "
    "summarize market signals, and decide which experiments are worth testing first."
)


class TestAgent(BaseAgent):
    name = "test_agent"

    def build_prompt(self, agent_input: AgentInput) -> str:
        return (
            "Summarize the following business idea in one clear sentence. "
            "Do not add extra commentary.\n\n"
            f"Business idea:\n{agent_input.text}"
        )


def run_test_agent(config: AppConfig) -> AgentOutput:
    agent = TestAgent(config)
    return agent.run(AgentInput(text=BUSINESS_TEXT))
