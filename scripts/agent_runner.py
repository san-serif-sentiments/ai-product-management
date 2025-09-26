"""Utility to preview agent prompts and guardrails."""

from __future__ import annotations

import argparse
from pathlib import Path


def load_prompt(agent_name: str) -> str:
    prompt_path = Path("agents/prompts") / f"{agent_name}.md"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found for agent '{agent_name}' at {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview AI Reading agent configuration")
    parser.add_argument("--agent", required=True, help="Agent name matching prompt filename (e.g., ingestion-agent)")
    parser.add_argument("--config", default="agents/configs/guardrails.example.yml", help="Guardrail config path")
    args = parser.parse_args()

    prompt = load_prompt(args.agent)
    print(f"Agent: {args.agent}\n")
    print("System Prompt Preview:\n----------------------")
    print(prompt.strip()[:1200] + ("\n..." if len(prompt) > 1200 else ""))
    print("\nGuardrail configuration located at:")
    print(Path(args.config).resolve())


if __name__ == "__main__":
    main()
