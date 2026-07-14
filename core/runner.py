"""Cloud execution entry point for agent runs."""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agents.test_agent import run_test_agent
from core.config import load_config
from evals.simple_eval import evaluate_output, print_eval_result


AGENTS = {
    "test_agent": run_test_agent,
}


def write_result(agent_name: str, result: str) -> Path:
    results_dir = ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    result_path = results_dir / f"{agent_name}_result.txt"
    result_path.write_text(result + "\n", encoding="utf-8")
    return result_path


def main() -> None:
    config = load_config()
    agent_name = os.getenv("AGENT_NAME", "test_agent").strip() or "test_agent"

    if agent_name not in AGENTS:
        available = ", ".join(sorted(AGENTS))
        raise ValueError(f"Unknown agent '{agent_name}'. Available agents: {available}")

    output = AGENTS[agent_name](config)

    print("=====\nAGENT RESULT\n=====")
    print(output.result)

    result_path = write_result(agent_name, output.result)
    print(f"\nResult saved to: {result_path}")

    passed = evaluate_output(output.result)
    print_eval_result(passed)

    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
