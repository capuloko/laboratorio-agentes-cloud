"""Minimal OpenAI Agents SDK smoke test for GitHub Actions."""

from __future__ import annotations

import asyncio
import os

from agents import Agent, Runner


DEFAULT_TEXT = (
    "A cloud agent lab lets you test small AI business ideas from GitHub Actions "
    "without running Python, Docker, or a server on your local machine."
)


def get_input_text() -> str:
    """Read workflow input from the environment, with a safe default."""
    return os.getenv("AGENT_INPUT_TEXT", "").strip() or DEFAULT_TEXT


async def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "Missing OPENAI_API_KEY. Add it in GitHub repo Settings -> "
            "Secrets and variables -> Actions."
        )

    input_text = get_input_text()
    agent = Agent(
        name="SummaryAgent",
        instructions=(
            "You summarize text clearly. Return exactly three concise bullet points. "
            "Use the same language as the input when possible."
        ),
    )

    result = await Runner.run(
        agent,
        input=f"Summarize this text:\n\n{input_text}",
    )

    print("=== Input ===")
    print(input_text)
    print("\n=== Agent output ===")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
