"""Minimal evaluation helpers for agent outputs."""

from __future__ import annotations


MIN_OUTPUT_LENGTH = 20


def evaluate_output(output: str, min_length: int = MIN_OUTPUT_LENGTH) -> bool:
    clean_output = output.strip()
    return bool(clean_output) and len(clean_output) > min_length


def print_eval_result(passed: bool) -> None:
    print("\n=====\nEVAL\n=====")
    print("PASS" if passed else "FAIL")
